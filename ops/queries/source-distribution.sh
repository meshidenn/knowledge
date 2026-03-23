#!/bin/bash
# source-distribution.sh — ソースタイプ別の知見分布を集計
# 使用: bash ops/queries/source-distribution.sh

VAULT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
NOTES_DIR="$VAULT_ROOT/notes"

echo "=== ソース別知見分布 ==="
echo ""

for source_type in paper blog x-post experiment book; do
    count=$(rg "^source_type: $source_type" "$NOTES_DIR"/ 2>/dev/null | wc -l | tr -d ' ')
    echo "  $source_type: $count件"
done

total=$(ls "$NOTES_DIR"/*.md 2>/dev/null | grep -v "map\|index" | wc -l | tr -d ' ')
echo ""
echo "  合計知見数: $total件"
