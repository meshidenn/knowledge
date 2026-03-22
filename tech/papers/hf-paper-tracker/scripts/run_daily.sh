#!/bin/bash
set -euo pipefail

# ============================================
# HF Paper Tracker - 日次インテーク
# cron から呼び出されるエントリポイント
# ============================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_DIR"

DATE=$(date +%Y-%m-%d)
RAW_FILE="papers/daily/raw/${DATE}.json"
OUTPUT_FILE="papers/daily/${DATE}.md"
LOG_FILE="logs/${DATE}.log"

mkdir -p papers/daily/raw papers/weekly logs

exec > >(tee -a "$LOG_FILE") 2>&1
echo "=== Daily Intake: $DATE $(date +%H:%M:%S) ==="

# --- Step 1: 既に実行済みならスキップ ---
if [ -f "$OUTPUT_FILE" ]; then
    echo "[SKIP] $OUTPUT_FILE already exists"
    exit 0
fi

# --- Step 2: HF API からデータ取得 ---
echo "[1/4] Fetching papers..."
python3 scripts/fetch_papers.py

if [ ! -f "$RAW_FILE" ]; then
    echo "[ERROR] Failed to fetch papers"
    exit 1
fi

PAPER_COUNT=$(python3 -c "import json; print(json.load(open('$RAW_FILE'))['count'])")
echo "[OK] Fetched $PAPER_COUNT papers"

# --- Step 3: Claude Code で分析 ---
echo "[2/4] Analyzing with Claude Code..."

claude -p "
$RAW_FILE を読んで、日次インテークを実行してください。
結果を $OUTPUT_FILE に保存してください。
CLAUDE.md の「日次インテーク」セクションのフォーマットに従ってください。
" --allowedTools "Bash(read_file:*)" "Bash(write_file:*)" > /dev/null 2>&1

# フォールバック: ファイル書き出しに失敗した場合は stdout から取得
if [ ! -f "$OUTPUT_FILE" ]; then
    echo "[WARN] Retrying with direct output..."
    claude -p "
以下のJSONを読んで日次インテークを実行してください。
CLAUDE.md のフォーマットに厳密に従ってMarkdownだけを出力してください。
余計な説明は不要です。

$(cat "$RAW_FILE")
" --print > "$OUTPUT_FILE"
fi

if [ ! -f "$OUTPUT_FILE" ] || [ ! -s "$OUTPUT_FILE" ]; then
    echo "[ERROR] Analysis failed"
    exit 1
fi

echo "[OK] Saved to $OUTPUT_FILE"

# --- Step 4: メール送信 ---
echo "[3/4] Sending email..."
python3 scripts/send_email.py "$OUTPUT_FILE"

# --- Step 5: Git コミット & プッシュ ---
echo "[4/4] Committing..."
git add papers/ logs/
if ! git diff --staged --quiet; then
    git commit -m "📄 ${DATE} daily intake"
    git push
    echo "[OK] Pushed to remote"
else
    echo "[SKIP] Nothing to commit"
fi

echo "=== Done: $(date +%H:%M:%S) ==="
