---
description: 処理パイプライン、メンテナンスサイクル、セッションリズム
type: manual
generated_from: "arscontexta-0.8.0"
---

# Workflows

## 処理パイプライン

ソースから知見への標準的なフロー：

```
inbox/ → /reduce → /reflect → /reweave → /verify → notes/
```

### ソースタイプ別の処理方針

| ソース | /reduceの深さ | 期待される出力 |
|-------|------------|-------------|
| 論文 | deep | 複数の原子的知見 + output-readyフラグ候補 |
| ブログ記事 | standard | 1〜3の主要知見 |
| Xのpost（単独） | quick | 1知見または無視 |
| Xのpost（スレッド） | standard | 主要洞察の抽出 |
| 技術深堀り（自分の検証） | deep | 知見 + `status: output-ready` |

### バッチ処理

inboxに複数アイテムがある場合：

```
/pipeline  — キュー内のすべてのアイテムを順次処理
/seed inbox/paper.md  — 1つのソースをフルパイプラインで処理
```

## セッションリズム

**Orient → Work → Persist**

### Orient（開始時）
```bash
cat ops/goals.md          # 現在のスレッドを確認
cat ops/reminders.md       # 期限切れアイテムを確認
ls inbox/                  # 処理待ちを確認
```

### Work（作業中）
- inboxにキャプチャ → /reduceで抽出 → /reflectで接続
- 発見したことは即座にキャプチャ（次のセッションまで覚えていない）

### Persist（終了前）
```bash
# ops/goals.mdを更新
# 新しい知見をテーママップに追加したか確認
# フリクションがあれば /arscontexta:remember でキャプチャ
```

## メンテナンスサイクル

条件ベースのトリガー（/nextが自動評価）：

| 条件 | 閾値 | アクション |
|-----|-----|----------|
| Observationのpending件数 | 10件以上 | /arscontexta:rethink |
| Tensionのpending件数 | 5件以上 | /arscontexta:rethink |
| テーママップサイズ | 40件以上 | 分割を検討 |
| inboxの放置 | 3日以上 | /reduce |
| ヘルスチェックの古さ | 7日以上 | /arscontexta:health |

## 既存スクリプトとの統合

```bash
# HF Daily Papersトラッカーの出力をinboxへ
tech/papers/hf-paper-tracker/の出力 → inbox/paper-YYYY-MM-DD.md

# Zenn/Qiitaブログまとめをinboxへ
tech/blog/の出力 → inbox/blog-summary-YYYY-MM-DD.md
```

---
Topics:
- [[manual]]
