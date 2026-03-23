#!/bin/bash
# session-orient.sh — セッション開始時のオリエンテーション
# ops/derivation.mdが存在する場合のみ実行（arscontextaバルトのみ）

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# アーズコンテクスタバルトのマーカーチェック
if [ ! -f "$VAULT_ROOT/.arscontexta" ]; then
    exit 0
fi

# セッションIDを設定
SESSION_ID="${CLAUDE_CONVERSATION_ID:-$(date +%Y%m%d-%H%M%S)}"
SESSION_FILE="$VAULT_ROOT/ops/sessions/current.json"

# セッション状態を初期化/更新
mkdir -p "$VAULT_ROOT/ops/sessions"
cat > "$SESSION_FILE" << EOF
{
  "session_id": "$SESSION_ID",
  "start_time": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "notes_created": [],
  "notes_modified": [],
  "discoveries": [],
  "last_activity": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF

# バルト構造を出力（ツリーインジェクション）
echo ""
echo "=== 知見システム オリエント ==="
echo ""
echo "## バルト構造"
ls -la "$VAULT_ROOT/notes/" 2>/dev/null | head -20 || echo "(notes/ 空)"
echo ""

# inboxのアイテム数をチェック
INBOX_COUNT=$(ls "$VAULT_ROOT/inbox/"*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$INBOX_COUNT" -gt "0" ]; then
    echo "⚠ inbox: $INBOX_COUNT 件の未処理アイテム"
fi

# observationsとtensionsの件数をチェック
OBS_COUNT=$(ls "$VAULT_ROOT/ops/observations/"*.md 2>/dev/null | wc -l | tr -d ' ')
TEN_COUNT=$(ls "$VAULT_ROOT/ops/tensions/"*.md 2>/dev/null | wc -l | tr -d ' ')

if [ "$OBS_COUNT" -ge "10" ]; then
    echo "⚠ observations: $OBS_COUNT 件のpending → /arscontexta:rethink を実行推奨"
fi
if [ "$TEN_COUNT" -ge "5" ]; then
    echo "⚠ tensions: $TEN_COUNT 件のpending → /arscontexta:rethink を実行推奨"
fi

echo ""
echo "## ops/goals.md"
cat "$VAULT_ROOT/ops/goals.md" 2>/dev/null || echo "(goals.md 未作成)"

echo ""
echo "## ops/reminders.md"
TODAY=$(date +%Y-%m-%d)
if [ -f "$VAULT_ROOT/ops/reminders.md" ]; then
    # 今日以前の未チェックリマインダーを表示
    grep "^\- \[ \]" "$VAULT_ROOT/ops/reminders.md" | while read -r line; do
        DATE=$(echo "$line" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
        if [ -n "$DATE" ] && [ "$DATE" \<= "$TODAY" ]; then
            echo "  期限: $line"
        fi
    done
fi

echo ""
echo "==========================="
