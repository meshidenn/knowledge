#!/bin/bash
# stale-notes.sh — 30日以上更新されていない知見を検出
# 使用: bash ops/queries/stale-notes.sh

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
NOTES_DIR="$VAULT_ROOT/notes"

echo "=== 古い知見（30日以上未更新）==="
echo ""

find "$NOTES_DIR" -name "*.md" -mtime +30 | while read -r note; do
    basename_note=$(basename "$note" .md)
    [[ "$basename_note" == *"map"* ]] && continue
    [[ "$basename_note" == "index" ]] && continue

    days=$(( ($(date +%s) - $(date -r "$note" +%s)) / 86400 ))
    echo "  $basename_note ($days日前)"
done

echo ""
echo "ヒント: /reweave で古い知見を更新"
