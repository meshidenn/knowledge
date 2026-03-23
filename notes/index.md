---
description: 知見グラフへのエントリーポイント — ここからナビゲーションを開始する
type: moc
---

# index

技術知見システムへようこそ。このハブMOCはすべての技術的知見の入口です。

## 主要テーマ領域

| テーマ | 説明 |
|-------|------|
| [[machine-learning-map]] | ML・深層学習の基礎と応用 |
| [[llm-map]] | 大規模言語モデル・LLMアーキテクチャ |
| [[systems-map]] | 分散システム・インフラ・エンジニアリング |

*テーマは知見が20件以上蓄積してから作成する（今は空のMOCより少数の充実したMOCを優先）*

## ナビゲーション

- ハブ（ここ）→ ドメインMOC → トピックMOC → 知見ノート
- すべての知見ノートは `topics:` フィールドでここに繋がる
- 知見が見つからないときは `rg "description" notes/` でスキャン

## クイックスタット

```bash
echo "知見数:" && ls notes/*.md | grep -v "map\|index" | wc -l
echo "テーママップ数:" && ls notes/*map*.md 2>/dev/null | wc -l
echo "inbox待機:" && ls inbox/*.md 2>/dev/null | wc -l
```

## 最初の知見を作る

1. `inbox/` にソースをキャプチャ（論文URL、記事リンク、メモ）
2. `/reduce` で知見を抽出
3. `/reflect` で既存知見と接続
4. `/verify` で品質確認
