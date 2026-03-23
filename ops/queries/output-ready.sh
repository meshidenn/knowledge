#!/bin/bash
# output-ready.sh — アウトプット準備完了の知見を一覧表示
# 使用: bash ops/queries/output-ready.sh

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
NOTES_DIR="$VAULT_ROOT/notes"

echo "=== アウトプット準備完了の知見 ==="
echo ""

rg "^status: output-ready" "$NOTES_DIR"/ 2>/dev/null | while read -r line; do
    file=$(echo "$line" | cut -d: -f1)
    title=$(head -1 "$file" | sed 's/^# //')
    echo "  - $title"
    echo "    ファイル: $file"
done

echo ""
echo "ヒント: これらを /reflect でまとめてアウトプット候補を検討"
