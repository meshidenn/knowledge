# Paperpile Brief 2026-06-06 - Lessons from building Claude Code: How we use skills

## 基本情報

- **タイトル**: Lessons from building Claude Code: How we use skills
- **著者**: メタデータからは不明
- **年 / venue**: 2026 / Claude
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: Anthropic が Claude Code で多数の「skills」を社内構築・運用して得た知見をまとめた記事。
- **先行研究と比べてどこがすごい？**: メタデータとabstractのみでは詳細不明。ただし、単発のプロンプト設計ではなく、数百規模のskillsを実運用・スケールさせた経験知に焦点がある点が特徴と思われる。
- **技術や手法の肝はどこ？**: メタデータからは不明。タイトルからは、Claude Codeにおけるskill設計、再利用可能な手順化、内部ナレッジのツール化、運用時の品質管理が中心と推測される。
- **どうやって有効だと検証した？**: メタデータからは不明。PDF本文がなく、実験・評価・比較対象は確認できない。
- **議論はある？**: メタデータからは不明。skillsの粒度、保守コスト、過剰な手順化、モデル更新時の劣化、社内ユースケースへの依存などは確認すべき論点。
- **次に読む/試すなら**: 元記事本文を取得して、skillの設計原則・失敗例・評価方法を確認する。Claude Codeで自分の反復作業を1つskill化して、効果と保守負荷を試す。既存のCodex/Claude向けskill設計パターンと比較する。
- **キーワード**: `Claude Code`, `skills`, `agent workflows`, `Anthropic`, `developer tools`

## 気になったこと

- PDF本文がなく、abstractも短いため、具体的な設計原則や実例は未確認。
- 「hundreds of skills」をどう分類・発見・更新・評価しているのか。
- skillはプロンプト、ツール呼び出し、ドキュメント、コード生成規約のどこまでを含む概念なのか。
- 社内利用で得た知見が、個人開発や小規模チームにもそのまま適用できるのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [noauthor-2026-hx-lessons-from-building-claude-code-how-we-use-skills-9d1d3139.md](../../chat/2026-06-06/noauthor-2026-hx-lessons-from-building-claude-code-how-we-use-skills-9d1d3139.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
