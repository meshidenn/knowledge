#!/bin/bash
set -euo pipefail

# ============================================
# HF Paper Tracker - 週次トレンド分析
# cron から呼び出されるエントリポイント
# ============================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck disable=SC1091
. "$SCRIPT_DIR/cron_env.sh"

REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_DIR"

if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi

WEEK_LABEL=$(date +%Y-W%V)
OUTPUT_FILE="papers/weekly/${WEEK_LABEL}.md"
LOG_FILE="logs/weekly-${WEEK_LABEL}.log"

copy_weekly_to_obsidian() {
    mkdir -p "$OBSIDIAN_HF_PAPERS_WEEKLY"
    cp -f "$REPO_DIR/$OUTPUT_FILE" "$OBSIDIAN_HF_PAPERS_WEEKLY/$(basename "$OUTPUT_FILE")"
    echo "[OK] Copied to $OBSIDIAN_HF_PAPERS_WEEKLY/$(basename "$OUTPUT_FILE")"
}

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
    copy_weekly_to_obsidian
    exit 0
fi

FILE_COUNT=$(echo "$DAILY_FILES" | wc -l | tr -d ' ')
echo "[INFO] Found $FILE_COUNT daily files"

# 日次全文を argv に載せない（ARG_MAX 回避）
COMBINED=$(mktemp "${TMPDIR:-/tmp}/hf-weekly-combined.XXXXXX.md")
trap 'rm -f "$COMBINED"' EXIT
# shellcheck disable=SC2086
cat $DAILY_FILES > "$COMBINED"

# --- OpenAI Codex で週次分析 ---
echo "[1/4] Running weekly analysis with OpenAI Codex..."

if ! codex exec "
${COMBINED} を読んで週次トレンド分析を実行してください（複数日分の日次インテークを結合した1ファイルです）。
CLAUDE.md の「週次トレンド分析」セクションのフォーマットに厳密に従い、
最終回答は完成した Markdown 本文のみを返してください。
進捗説明、前置き、補足、コードフェンス、\`@papers/...\` のような参照表記は一切含めないでください。
出力の先頭行は必ず \`# 📊 ${WEEK_LABEL} 週次トレンド分析\` から始めてください。
" -s read-only -o "$OUTPUT_FILE" >/dev/null 2>&1; then
    echo "[ERROR] Weekly analysis failed"
    exit 1
fi

if [ ! -f "$OUTPUT_FILE" ] || [ ! -s "$OUTPUT_FILE" ]; then
    echo "[ERROR] Weekly analysis failed"
    exit 1
fi

echo "[OK] Saved to $OUTPUT_FILE"

# --- メール送信 ---
echo "[2/4] Sending email..."
uv run scripts/send_email.py "$OUTPUT_FILE"

# --- Git コミット & プッシュ ---
echo "[3/4] Committing..."
git add papers/ logs/
if ! git diff --staged --quiet; then
    git commit -m "📊 $WEEK_LABEL weekly analysis"
    git push
    echo "[OK] Pushed to remote"
else
    echo "[SKIP] Nothing to commit"
fi

echo "[4/4] Copying to Obsidian..."
copy_weekly_to_obsidian

echo "=== Done: $(date +%H:%M:%S) ==="
