# Paperpile Brief 2026-06-06 - Lessons from building Claude Code: How we use skills

## 基本情報

- **タイトル**: Lessons from building Claude Code: How we use skills
- **著者**: メタデータからは不明
- **年 / venue**: 2026 / Claude
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: Anthropic が Claude Code 内部で多数の skills を構築・運用・スケールさせた経験から得た知見をまとめた記事または技術メモ。
- **先行研究と比べてどこがすごい？**: PDF本文がなく、abstract相当のメタデータのみのため詳細は不明。ただし「hundreds of skills internally」とあるため、単発のプロンプト設計ではなく、多数の再利用可能な skill を組織内で運用した実践知に価値がありそう。
- **技術や手法の肝はどこ？**: メタデータからは不明。推測できる範囲では、Claude Code における skill の設計、管理、スケーリング、社内利用時のパターン化が中心と思われる。
- **どうやって有効だと検証した？**: メタデータからは不明。実験、評価指標、比較対象、ユーザー数、運用期間などは確認できない。
- **議論はある？**: PDF本文がないため限界や失敗例は不明。特に、skills の品質管理、バージョン管理、権限、安全性、過剰な抽象化、利用者教育が論点になりそう。
- **次に読む/試すなら**: 元記事を取得して、skills の設計原則とアンチパターンを確認する。自分の Codex/Claude Code 用 skill を1つ作り、再利用性と保守性を試す。多数の skills を運用する場合の命名・検索・更新フローを調べる。
- **キーワード**: `Claude Code`, `skills`, `Anthropic`, `agent workflow`, `tool use`, `prompt engineering`

## 気になったこと

- 「hundreds of skills」をどう分類・発見・更新しているのか。
- skill はプロンプト資産なのか、ツール連携込みの実行単位なのか。
- 社内運用で品質が落ちる skill や重複 skill をどう検出しているのか。
- Claude Code 固有の話と、一般的なエージェント設計に転用できる話の境界。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [noauthor-2026-hx-lessons-from-building-claude-code-how-we-use-skills-9d1d3139.md](../../chat/2026-06-06/noauthor-2026-hx-lessons-from-building-claude-code-how-we-use-skills-9d1d3139.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
