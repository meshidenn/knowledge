---
description: 最初のセッションガイド — 最初の知見を作成して接続を構築する
type: manual
generated_from: "arscontexta-0.8.0"
---

# Getting Started

## 最初のセッションで期待すること

Claude Codeを再起動すると、`session-orient.sh`フックがバルト構造を注入します。これにより：
- 現在のinboxアイテム数
- ops/goals.mdの現在のスレッド
- 期限切れのリマインダー

が表示されます。

## 最初の知見を作る

### ステップ1: inboxにキャプチャ

論文や記事をinboxにキャプチャします：

```
inbox/に新しいファイルを作成してください。
タイトル: "Attention Is All You Need - 2017"
ソースURL: https://arxiv.org/abs/1706.03762
なぜキャプチャしたか: Transformerアーキテクチャの元論文、LLMの基盤
```

### ステップ2: /reduceで抽出

```
/reduce inbox/attention-is-all-you-need.md
```

このスキルが：
- 論文を読み、複数の原子的知見を抽出
- 各知見を `notes/` に個別ファイルとして作成
- `description`、`source_type`、`topics` フィールドを設定

### ステップ3: /reflectで接続

```
/reflect [作成された知見ファイル名]
```

このスキルが：
- 既存の知見グラフを探索
- 関連する知見とのWikiリンクを追加
- テーママップを更新

### ステップ4: /verifyで確認

```
/verify [知見ファイル名]
```

品質チェック（description、スキーマ、リンク）を実行。

## 接続の仕組み

Wikiリンク `[[知見タイトル]]` がグラフのエッジを作ります。タイトルは命題として機能します：

```markdown
Since [[self-attention enables parallelism that RNNs cannot achieve]],
大規模モデルの並列訓練が実用的になった。
```

## 次のステップ

- [[workflows]] — 処理パイプラインの詳細
- [[skills]] — 利用可能なすべてのスキル

---
Topics:
- [[manual]]
