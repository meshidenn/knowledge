---
description: このシステムがどのように導出されたか — architectコマンドとreseedコマンドを支える記録
created: 2026-03-24
engine_version: "0.8.0"
---

# システム導出記録

## 設定ディメンション

| ディメンション | 位置 | 会話シグナル | 確信度 |
|--------------|------|------------|--------|
| 粒度 (Granularity) | atomic | 「本質的な情報を抽出したい」「論文・ブログ・Xと複数ソース横断」 | High |
| 整理 (Organization) | flat | Researchプリセットデフォルト、反対シグナルなし | Inferred |
| リンク (Linking) | explicit | ML/技術ドメインでの横断的接続、明示的依存関係 | Medium |
| 処理 (Processing) | heavy | 「本質的な情報を抽出」「深堀」「アウトプットしたい」 | High |
| ナビゲーション (Navigation) | 3-tier | 年間100〜200件の知見 × 原子的粒度 | Inferred |
| メンテナンス (Maintenance) | condition-based | Researchプリセット標準 | Inferred |
| スキーマ (Schema) | moderate | 複数ソースタイプ、アウトプットステータス管理が必要 | Medium |
| 自動化 (Automation) | full | Claude Codeプラットフォーム、フルサポート | High |

## パーソナリティディメンション

| ディメンション | 位置 | シグナル |
|--------------|------|--------|
| 温かさ (Warmth) | clinical | 技術・研究ドメイン、シグナルなし → デフォルト |
| 主張度 (Opinionatedness) | neutral | 研究コンテキスト、結論はユーザーが判断 → デフォルト |
| フォーマリティ (Formality) | professional | 技術ドメイン → デフォルト |
| 感情認識 (Emotional Awareness) | task-focused | 知識処理・技術検証 → デフォルト |

## ボキャブラリーマッピング

| 汎用語 | ドメイン語 | カテゴリ |
|--------|-----------|---------|
| notes | notes | フォルダ |
| inbox | inbox | フォルダ |
| archive | archive | フォルダ |
| note (type) | 知見 | ノートタイプ |
| reduce | 抽出 (reduce) | 処理フェーズ |
| reflect | 接続 (reflect) | 処理フェーズ |
| reweave | 更新 (reweave) | 処理フェーズ |
| verify | 確認 (verify) | 処理フェーズ |
| rethink | 振り返り (rethink) | メタスキル |
| MOC | テーママップ | ナビゲーション |
| description | description | スキーマフィールド |
| topics | topics | スキーマフィールド |
| relevant_notes | relevant_notes | スキーマフィールド |

## プラットフォーム

- Tier: Claude Code
- 自動化レベル: full (フルオートメーション)
- 自動化: full — すべての機能がデイワンから有効

## アクティブ機能ブロック

- [x] wiki-links — always included (kernel)
- [x] atomic-notes — granularity = atomic
- [x] mocs — 3-tier navigation
- [x] processing-pipeline — heavy processing
- [x] schema — always included
- [x] maintenance — always included
- [x] self-evolution — always included
- [x] methodology-knowledge — always included
- [x] session-rhythm — always included
- [x] templates — always included
- [x] ethical-guardrails — always included
- [x] helper-functions — always included
- [x] graph-analysis — always included
- [ ] semantic-search — 任意（qmdインストール後に有効化可能）
- [ ] personality — シグナルなし、ニュートラル・ヘルプフルデフォルト
- [ ] self-space — Researchプリセットデフォルト OFF、ops/に統合
- [ ] multi-domain — 単一ドメイン（tech/ML）

## 一貫性検証結果

- ハード制約確認: 3項目。違反: なし
- ソフト制約確認: 7項目。自動調整: なし。ユーザー確認: なし
- 補償メカニズム: atomic + explicit linking → semantic search optional (明示的リンクで当面十分)

## 失敗モードリスク

1. **コレクターの誤謬** (HIGH) — Xやブログを溜め込むだけで抽出しない
2. **言葉通りのコピー** (HIGH) — 要約を知見と間違える
3. **孤立ノート** (HIGH) — 接続なしの知見が蓄積する
4. **生産性ポルノ** (HIGH) — システム改善が知識蓄積より優先される

## 生成パラメータ

- フォルダ名: notes/, inbox/, archive/
- スキル: 16スキル（ボキャブラリー変換済み）
- フック: session-orient, session-capture, validate-note, auto-commit
- テンプレート: knowledge-note.md, topic-map.md, source-capture.md, observation-note.md
- トポロジー: skills（フレッシュコンテキスト/フェーズ）
- セルフスペース: 無効（ops/goals.mdにルーティング）
