---
description: 利用可能なすべてのスキルのリファレンス
type: manual
generated_from: "arscontexta-0.8.0"
---

# Skills

## 処理スキル

| スキル | 用途 | 例 |
|-------|------|---|
| `/reduce` | ソース素材から知見を抽出 | `/reduce inbox/paper.md` |
| `/reflect` | 知見間の接続を発見 | `/reflect [知見名]` |
| `/reweave` | 新しい知見で古いノートを更新 | `/reweave [古い知見名]` |
| `/verify` | 知見の品質確認（description・スキーマ・リンク） | `/verify [知見名]` |
| `/validate` | バルト全体のスキーマ一括検証 | `/validate` |

## オーケストレーションスキル

| スキル | 用途 | 例 |
|-------|------|---|
| `/seed` | ソースのフルパイプライン処理（reduce→reflect→verify） | `/seed inbox/paper.md` |
| `/pipeline` | バッチ処理オーケストレーション | `/pipeline` |
| `/ralph` | 継続的バックグラウンド処理 | `/ralph` |
| `/tasks` | タスクスタック管理 | `/tasks` |

## ナビゲーションスキル

| スキル | 用途 | 例 |
|-------|------|---|
| `/next` | インテリジェントな次アクション推奨 | `/next` |
| `/stats` | バルトメトリクスと進捗 | `/stats` |
| `/graph` | グラフクエリ生成 | `/graph orphans` |

## 成長スキル

| スキル | 用途 | 例 |
|-------|------|---|
| `/learn` | トピックをリサーチしてグラフを拡張 | `/learn "LoRAの仕組み"` |
| `/remember` | フリクションと方法論学習をキャプチャ | `/remember` |

## 進化スキル

| スキル | 用途 | 例 |
|-------|------|---|
| `/arscontexta:rethink` | observations/tensionsをトリアージ | `/arscontexta:rethink` |
| `/refactor` | バルト構造の改善 | `/refactor` |

## プラグインコマンド（/arscontexta:）

| コマンド | 用途 |
|---------|------|
| `/arscontexta:help` | 利用可能なすべてのコマンドを表示 |
| `/arscontexta:health` | バルトヘルスチェック |
| `/arscontexta:next` | 次アクション推奨 |
| `/arscontexta:learn` | ディープリサーチ |
| `/arscontexta:rethink` | observationsのトリアージ |
| `/arscontexta:remember` | フリクションキャプチャ |
| `/arscontexta:architect` | 設定変更のアドバイス |
| `/arscontexta:ask` | 方法論への問い合わせ |
| `/arscontexta:tutorial` | インタラクティブチュートリアル |

---
Topics:
- [[manual]]
