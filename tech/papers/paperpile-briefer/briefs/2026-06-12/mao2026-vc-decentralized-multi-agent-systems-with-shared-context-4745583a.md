# Paperpile Brief 2026-06-12 - Decentralized Multi-agent systems with shared context

## 基本情報

- **タイトル**: Decentralized Multi-agent systems with shared context
- **著者**: Yuzhen Mao, Azalia Mirhoseini
- **年 / venue**: 2026 / arXiv [cs.MA]
- **リンク**: https://arxiv.org/abs/2606.10662v1 / arXiv:2606.10662v1

## 落合陽一フォーマット

- **ひとことでいうと**: 中央司令役に依存するマルチエージェントシステムのボトルネックを、共有コンテキストとタスクキューで分散化する DeLM を提案した論文。
- **先行研究と比べてどこがすごい？**: Claude Code Subagents、AOrchestra、Kimi Agent Swarm などの中央集権的な scatter-gather 型調整では、主エージェントがタスク分解・結果統合・再配布を担うため、エージェント数が増えるほど通信と統合が詰まる。DeLM は「検証済み共有状態」を全エージェントが読む設計にして、進捗・失敗・制約を中央統合なしに再利用可能にした点が新しい。
- **技術や手法の肝はどこ？**: コアは、並列エージェント、共有コンテキスト、タスクキューの3点。各エージェントは非同期にタスクを取得し、共有コンテキストを読んで局所推論を行い、結果をコンパクトな gist に圧縮する。その gist は根拠に照らして検証されたものだけ共有状態に追加される。長い情報は gist、詳細要約、原文証拠へ段階的に unfold できる階層構造にしている。
- **どうやって有効だと検証した？**: SWE-bench Verified、LongBench-v2 Multi-Doc QA、OOLONG で評価。SWE-bench Verified では Avg.@1、Pass@2、Pass@4 で強い性能を示し、最強ベースライン比で最大10.5ポイント改善、コストもおよそ半分と報告。LongBench-v2 では複数の frontier model family に対して平均精度が最大5.7ポイント改善。OOLONG では DeLM 単体は RLM に劣るが、DELM+RLM のハイブリッドが精度・コストで最良になり、自然言語共有状態とコード実行型推論の補完性を示している。
- **議論はある？**: 共有状態に入れる前の検証は信頼性を上げる一方でオーバーヘッドがある。性能はタスク分解の質に依存し、粗すぎる分解や細かすぎる分解で効率が落ちる。構造化データの正確な集計では、自然言語の共有コンテキストだけでは弱く、RLM のようなコード実行型手法が必要になる。モデルごとにプロンプト最適化が必要という限界も述べられている。
- **次に読む/試すなら**: DeLM の共有コンテキスト設計を、自分の論文読解・コード修正エージェントに入れられるか試す。SWE-bench 系タスクで「失敗仮説を共有する」だけの最小実装を作る。RLM や ReadAgent との比較を読み、長文QAで gist/unfold の設計差を見る。
- **キーワード**: `multi-agent systems`, `decentralized coordination`, `shared context`, `task queue`, `test-time scaling`, `long-context reasoning`, `SWE-bench`, `LongBench-v2`, `RLM`

## 気になったこと

- admission-time verification の実装コストと、実際にどの程度の誤情報を防げているかを詳細に見たい。
- 共有コンテキストが大きくなったとき、gist の検索・優先順位付け・削除はどう制御するのか。
- 中央エージェントをなくしても、最終回答生成や追加タスク生成のタイミングで暗黙の中央化が起きていないか確認したい。
- ソフトウェア修正では「失敗した修正案」「通ったテスト」「未確認の仮説」をどうスキーマ化すると再利用しやすいか試したい。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [mao2026-vc-decentralized-multi-agent-systems-with-shared-context-4745583a.md](../../chat/2026-06-12/mao2026-vc-decentralized-multi-agent-systems-with-shared-context-4745583a.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
