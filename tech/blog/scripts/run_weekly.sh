#!/bin/bash
set -euo pipefail

# ============================================
# tech/blog - 週次技術記事まとめ生成
# ============================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_DIR"

WEEK_LABEL=$(date +%Y-W%V)
RAW_FILE="raw/${WEEK_LABEL}.json"
WEEKLY_FILE="weekly/${WEEK_LABEL}.md"
SUMMARY_FILE="summary.md"

mkdir -p raw weekly

echo "=== 週次まとめ生成: $WEEK_LABEL $(date +%H:%M:%S) ==="

# --- 既に実行済みならスキップ ---
if [ -f "$WEEKLY_FILE" ]; then
    echo "[SKIP] $WEEKLY_FILE は既に存在します"
    exit 0
fi

# --- 記事取得 ---
echo "[1/3] Zenn/Qiita から記事を取得..."
uv run scripts/fetch_articles.py

if [ ! -f "$RAW_FILE" ]; then
    echo "[ERROR] $RAW_FILE が存在しません"
    exit 1
fi

ARTICLE_COUNT=$(python3 -c "import json; d=json.load(open('$RAW_FILE')); print(d['count'])")
echo "[INFO] 取得件数: $ARTICLE_COUNT 件"

if [ "$ARTICLE_COUNT" -eq 0 ]; then
    echo "[WARN] 記事が0件のため終了"
    exit 0
fi

# --- 週次まとめ生成 ---
echo "[2/3] 週次まとめを生成中..."

RAW_CONTENT=$(cat "$RAW_FILE")

claude --print <<PROMPT > "$WEEKLY_FILE"
以下は今週（$WEEK_LABEL）いいね・ストックした技術記事の一覧（JSON）です。
これをもとに週次まとめMarkdownを作成してください。

## 出力形式

\`\`\`markdown
# 週次技術記事まとめ $WEEK_LABEL

## 記事一覧

### {トピック名}

- **[{タイトル}]({URL})**（{ソース: Zenn/Qiita}）
  {記事の要点を1〜2文で要約}

...

## 今週のハイライト

{特に注目すべき記事や傾向を3〜5点で箇条書き}
\`\`\`

## ルール
- 記事はトピック（例: LLM, インフラ, フロントエンド, TypeScript, etc.）でグループ化
- 要約はタイトルを繰り返さず、内容の本質を1〜2文で
- ソースのZenn/Qiitaを明記
- Markdownのみ出力（説明文は不要）

## 記事データ
${RAW_CONTENT}
PROMPT > "$WEEKLY_FILE"

echo "[OK] $WEEKLY_FILE を生成しました"

# --- 全体まとめ更新 ---
echo "[3/3] 全体まとめを更新中..."

# 既存のsummary.mdがあれば読み込む
EXISTING_SUMMARY=""
if [ -f "$SUMMARY_FILE" ]; then
    EXISTING_SUMMARY=$(cat "$SUMMARY_FILE")
fi

WEEKLY_CONTENT=$(cat "$WEEKLY_FILE")

claude --print <<PROMPT
以下の情報をもとに全体まとめ（summary.md）を更新してください。

## 指示
- トピック別に「現状・動向・注目点」をまとめる
- 今週の内容を反映して既存まとめを更新（新トピックがあれば追加）
- 各トピックに最終更新週を記載
- Markdownのみ出力

## 出力形式
\`\`\`markdown
# 技術トレンド全体まとめ

最終更新: $WEEK_LABEL

## {トピック名}（最終更新: YYYY-WXX）

{動向・現状を3〜5文で。具体的な記事名や技術名を含める}

...
\`\`\`

## 既存の全体まとめ
${EXISTING_SUMMARY:-（初回のため既存まとめなし）}

## 今週の週次まとめ
${WEEKLY_CONTENT}
PROMPT > "$SUMMARY_FILE"

echo "[OK] $SUMMARY_FILE を更新しました"

# --- Git コミット ---
git add raw/ weekly/ summary.md
if ! git diff --staged --quiet; then
    git commit -m "add:${WEEK_LABEL} 週次技術記事まとめ"
    echo "[OK] コミット完了"
else
    echo "[SKIP] コミット対象なし"
fi

echo "=== 完了: $(date +%H:%M:%S) ==="
