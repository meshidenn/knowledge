#!/bin/bash
# session-capture.sh — セッション終了時の状態保存
# Stopフックで実行される

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# arscontextaバルトのマーカーチェック
if [ ! -f "$VAULT_ROOT/.arscontexta" ]; then
    exit 0
fi

SESSION_FILE="$VAULT_ROOT/ops/sessions/current.json"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# current.jsonをアーカイブ
if [ -f "$SESSION_FILE" ]; then
    cp "$SESSION_FILE" "$VAULT_ROOT/ops/sessions/$TIMESTAMP.json"
fi

# セッション終了を記録
echo "セッション終了: $TIMESTAMP" >> "$VAULT_ROOT/ops/sessions/session-log.txt"

exit 0
