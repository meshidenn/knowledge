#!/bin/bash
set -euo pipefail

# ============================================
# HF Paper Tracker - 日次インテーク
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

DATE=$(date +%Y-%m-%d)
RAW_FILE="papers/daily/raw/${DATE}.json"
OUTPUT_FILE="papers/daily/${DATE}.md"
LOG_FILE="logs/${DATE}.log"

copy_daily_to_obsidian() {
    mkdir -p "$OBSIDIAN_HF_PAPERS_DAILY"
    cp -f "$REPO_DIR/$OUTPUT_FILE" "$OBSIDIAN_HF_PAPERS_DAILY/$(basename "$OUTPUT_FILE")"
    echo "[OK] Copied to $OBSIDIAN_HF_PAPERS_DAILY/$(basename "$OUTPUT_FILE")"
}

mkdir -p papers/daily/raw papers/weekly logs

exec > >(tee -a "$LOG_FILE") 2>&1
echo "=== Daily Intake: $DATE $(date +%H:%M:%S) ==="

# --- Step 1: 既に実行済みならスキップ ---
if [ -f "$OUTPUT_FILE" ]; then
    echo "[SKIP] $OUTPUT_FILE already exists"
    exit 0
fi

# --- Step 2: HF API からデータ取得 ---
echo "[1/6] Fetching papers..."
if ! uv run scripts/fetch_papers.py; then
    echo "[INFO] No papers today — sending notification email"
    echo "# 📭 ${DATE} — 今日のHF Daily Papersはありませんでした" > "$OUTPUT_FILE"
    uv run scripts/send_email.py "$OUTPUT_FILE"
    copy_daily_to_obsidian
    exit 0
fi

if [ ! -f "$RAW_FILE" ]; then
    echo "[ERROR] Failed to fetch papers"
    exit 1
fi

PAPER_COUNT=$(uv run python -c "import json; print(json.load(open('$RAW_FILE'))['count'])")
echo "[OK] Fetched $PAPER_COUNT papers"

# --- Step 3: OpenAI Codex で分析 ---
echo "[2/6] Analyzing with OpenAI Codex..."

if ! codex exec "
${RAW_FILE} を読んで日次インテークを実行してください。
CLAUDE.md の「日次インテーク」セクションのフォーマットに厳密に従い、
最終回答は完成した Markdown 本文のみを返してください。
進捗説明、前置き、補足、コードフェンス、\`@papers/...\` のような参照表記は一切含めないでください。
出力の先頭行は必ず \`# 📅 ${DATE} Daily Papers インテーク\` から始めてください。
" -s read-only -o "$OUTPUT_FILE" >/dev/null 2>&1; then
    echo "[ERROR] Analysis failed"
    exit 1
fi

if [ ! -f "$OUTPUT_FILE" ] || [ ! -s "$OUTPUT_FILE" ]; then
    echo "[ERROR] Analysis failed"
    exit 1
fi

echo "[OK] Saved to $OUTPUT_FILE"

# --- Step 3b: スキップ論文に arXiv リンクを付与（raw JSON と突き合わせ・本文 URL 済みは除外） ---
echo "[3/6] Enriching skip section with arXiv links..."
uv run scripts/enrich_skip_links.py "$OUTPUT_FILE" "$RAW_FILE"

# --- Step 4: メール送信 ---
echo "[4/6] Sending email..."
uv run scripts/send_email.py "$OUTPUT_FILE"

# --- Step 5: Git コミット & プッシュ ---
echo "[5/6] Committing..."
git add papers/
if ! git diff --staged --quiet; then
    git commit -m "📄 ${DATE} daily intake"
    git push
    echo "[OK] Pushed to remote"
else
    echo "[SKIP] Nothing to commit"
fi

echo "[6/6] Copying to Obsidian..."
copy_daily_to_obsidian

echo "=== Done: $(date +%H:%M:%S) ==="
