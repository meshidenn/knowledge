---
description: よくある問題とその解決方法
type: manual
generated_from: "arscontexta-0.8.0"
---

# Troubleshooting

## よくある問題

### 孤立した知見（接続なし）

**症状:** notes/に知見はあるが、テーママップからリンクされていない

**解決策:**
```bash
bash ops/queries/orphan-notes.sh  # 孤立知見を検出
/reflect [知見名]                  # 接続を探索
```

### ぶら下がりリンク（存在しないファイルへのリンク）

**症状:** `[[知見名]]` リンクが存在しないファイルを指している

**解決策:** 知見を削除・リネームした場合は、すべてのリンクを更新する。
```bash
grep -r "[[削除した知見名]]" notes/  # 影響を受けるファイルを特定
```

### inboxの溢れ（コレクターの誤謬）

**症状:** inbox/に10件以上のアイテムが溜まっている

**解決策:** キャプチャを止めて処理を優先する
```bash
/reduce inbox/[最も重要なソース]
/pipeline  # キューをバッチ処理
```

### 方法論ドリフト

**症状:** システムの動作が期待から外れてきた

**解決策:**
```bash
/arscontexta:rethink drift  # ドリフト検出を実行
```

### スキルが利用できない

**症状:** `/reduce` などのスキルが「見つからない」

**解決策:** Claude Codeを再起動する（スキルはセッション開始時にロードされる）

### パイプラインのストール

**症状:** ops/queue/queue.jsonにタスクが残っているが進捗がない

**解決策:**
```bash
cat ops/queue/queue.json  # ストールしているタスクを確認
/next                      # 次のアクションを評価
```

## よくある間違いとその修正

| 間違い | 正しい方法 |
|-------|----------|
| notes/に直接ファイルを作成 | inbox/にキャプチャ → /reduceで処理 |
| タイトルがトピックラベル（「Transformer」） | 命題を使う（「Transformerは...できる」） |
| descriptionがタイトルの言い換え | スコープ・メカニズム・含意を追加 |
| 接続なしに知見を作成 | /reflectで必ず接続を探索 |
| テーマなしにMOCを作成 | 20件以上の知見が溜まってから作成 |

---

関連:
- [[meta-skills]] — /rethinkと/rememberの詳細
- [[configuration]] — 設定調整

Topics:
- [[manual]]
