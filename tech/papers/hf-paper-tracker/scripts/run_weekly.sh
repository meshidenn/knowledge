#!/bin/bash
set -euo pipefail

# ============================================
# HF Paper Tracker - 週次トレンド分析
# cron から呼び出されるエントリポイント
# ============================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_DIR"

WEEK_LABEL=$(date +%Y-W%V)
OUTPUT_FILE="papers/weekly/${WEEK_LABEL}.md"
LOG_FILE="logs/weekly-${WEEK_LABEL}.log"

mkdir -p papers/weekly logs

exec > >(tee -a "$LOG_FILE") 2>&1
echo "=== Weekly Analysis: $WEEK_LABEL $(date +%H:%M:%S) ==="

# --- 既に実行済みならスキップ ---
if [ -f "$OUTPUT_FILE" ]; then
    echo "[SKIP] $OUTPUT_FILE already exists"
    exit 0
fi

# --- 今週の日次ファイルがあるか確認 ---
DAILY_FILES=$(find papers/daily -maxdepth 1 -name "*.md" -newer papers/weekly/.gitkeep 2>/dev/null | sort || true)

if [ -z "$DAILY_FILES" ]; then
    # .gitkeep より新しいファイルがない場合、今週の日付で探す
    MONDAY=$(date -d "last monday" +%Y-%m-%d 2>/dev/null || date -v-monday +%Y-%m-%d 2>/dev/null || date +%Y-%m-%d)
    echo "[INFO] Looking for files from $MONDAY onwards..."
    DAILY_FILES=$(ls papers/daily/2*.md 2>/dev/null | sort || true)
fi

if [ -z "$DAILY_FILES" ]; then
    echo "[WARN] No daily intake files found"
    echo "# 📊 $WEEK_LABEL 週次トレンド分析\n\n今週の日次インテークが見つかりませんでした。" > "$OUTPUT_FILE"
    exit 0
fi

FILE_COUNT=$(echo "$DAILY_FILES" | wc -l | tr -d ' ')
echo "[INFO] Found $FILE_COUNT daily files"

# --- Claude Code で週次分析 ---
echo "[1/3] Running weekly analysis..."

claude -p "
papers/daily/ ディレクトリにある .md ファイル（日次インテーク結果）を全て読んで、
週次トレンド分析を実行してください。
結果を $OUTPUT_FILE に保存してください。
CLAUDE.md の「週次トレンド分析」セクションのフォーマットに従ってください。
" --allowedTools "Bash(read_file:*)" "Bash(write_file:*)" "Bash(ls:*)" > /dev/null 2>&1

# フォールバック
if [ ! -f "$OUTPUT_FILE" ] || [ ! -s "$OUTPUT_FILE" ]; then
    echo "[WARN] Retrying with direct content..."
    DAILY_CONTENT=$(cat $DAILY_FILES)
    claude -p "
以下は今週の日次インテーク結果です。週次トレンド分析を実行してください。
CLAUDE.md のフォーマットに従ってMarkdownだけを出力してください。

${DAILY_CONTENT}
" --print > "$OUTPUT_FILE"
fi

echo "[OK] Saved to $OUTPUT_FILE"

# --- メール送信 ---
echo "[2/3] Sending email..."
python3 scripts/send_email.py "$OUTPUT_FILE"

# --- Git コミット & プッシュ ---
echo "[3/3] Committing..."
git add papers/ logs/
if ! git diff --staged --quiet; then
    git commit -m "📊 $WEEK_LABEL weekly analysis"
    git push
    echo "[OK] Pushed to remote"
else
    echo "[SKIP] Nothing to commit"
fi

echo "=== Done: $(date +%H:%M:%S) ==="
