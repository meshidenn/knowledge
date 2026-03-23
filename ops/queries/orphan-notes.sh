#!/bin/bash
# orphan-notes.sh — 接続のない孤立知見を検出
# 使用: bash ops/queries/orphan-notes.sh

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
NOTES_DIR="$VAULT_ROOT/notes"

echo "=== 孤立知見の検出 ==="
echo ""

orphan_count=0

for note in "$NOTES_DIR"/*.md; do
    [ -f "$note" ] || continue
    basename_note=$(basename "$note" .md)

    # MOCファイルは除外
    [[ "$basename_note" == *"map"* ]] && continue
    [[ "$basename_note" == "index" ]] && continue

    # この知見へのincoming linkを検索
    link_count=$(grep -r "\[\[${basename_note}\]\]" "$NOTES_DIR"/ 2>/dev/null | wc -l | tr -d ' ')

    if [ "$link_count" -eq 0 ]; then
        echo "  孤立: $basename_note"
        orphan_count=$((orphan_count + 1))
    fi
done

echo ""
echo "孤立知見数: $orphan_count"
