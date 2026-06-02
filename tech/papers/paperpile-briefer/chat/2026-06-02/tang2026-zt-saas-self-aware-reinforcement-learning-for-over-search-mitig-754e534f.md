# Chat Prompt 2026-06-02

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- {SAAS}: Self-aware reinforcement learning for over-search mitigation in agentic search

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-02 - {SAAS}: Self-aware reinforcement learning for over-search mitigation in agentic search

## 基本情報

- **タイトル**: {SAAS}: Self-aware reinforcement learning for over-search mitigation in agentic search
- **著者**: Tang, Yunbo; Yang, Chengyi; Liu, Shiyu; Xiang, Zhishang; Chen, Zerui; Zhang, Qinggang; Su, Jinsong
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: DOI・arXiv ID・URLはメタデータからは不明。コード: https://github.com/XMUDeepLIT/SAAS

## 落合陽一フォーマット

- **ひとことでいうと**: LLMエージェントの検索しすぎ問題を、自己認識を育てる強化学習フレームワーク SAAS で抑える論文。
- **先行研究と比べてどこがすごい？**: エージェント検索は多段推論に有効だが、内部知識で足りる場面でも検索したり、十分な証拠が集まっても終了できない「over-search」が起きる。SAAS は精度を落とさず検索回数・推論遅延・計算コストを減らすことを狙う点が新規性。
- **技術や手法の肝はどこ？**: 検索なしロールアウトと検索ありロールアウトを対比して「検索境界」をモデル化し、その境界を報酬に反映して不要・冗長な検索を軌道レベルで罰する。さらに段階的最適化で、まず推論能力を優先し、その後に検索正則化を効かせて reward hacking を避ける。
- **どうやって有効だと検証した？**: extensive experiments により、精度を維持しつつ over-search を大幅に削減したとされる。ただし具体的なベンチマーク、比較対象、削減率、精度差はメタデータからは不明。
- **議論はある？**: 検索境界をどう安定に推定するか、内部知識で十分かどうかの判定がドメインやモデルサイズに依存しないかが論点。報酬設計が検索抑制に偏りすぎる可能性、未見タスクでの汎化、実運用でのコスト削減量はメタデータからは不明。
- **次に読む/試すなら**: コードを確認して報酬関数と stage-wise optimization の実装を見る。使われたベンチマークと検索回数削減率を確認する。既存の agentic RAG / tool-use agent に検索停止判定だけ移植できるか試す。
- **キーワード**: `agentic search`, `reinforcement learning`, `over-search mitigation`, `self-awareness`, `search boundary`, `LLM agents`

## 気になったこと

- 「検索境界」は教師なしで安定に見つかるのか、それともロールアウト品質に強く依存するのか。
- 精度維持と検索削減のトレードオフ曲線がどうなっているか。
- 検索コスト削減が、単純な search budget や early stopping baseline より本当に優れているのか。
- reward hacking を避ける stage-wise optimization の具体的なスケジュールと失敗例。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
