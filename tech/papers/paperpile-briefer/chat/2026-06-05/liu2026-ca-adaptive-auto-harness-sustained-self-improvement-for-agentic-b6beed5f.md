# Chat Prompt 2026-06-05

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- Adaptive Auto-harness: Sustained self-improvement for agentic system deployment on open-ended task streams

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-05 - Adaptive Auto-harness: Sustained self-improvement for agentic system deployment on open-ended task streams

## 基本情報

- **タイトル**: Adaptive Auto-harness: Sustained self-improvement for agentic system deployment on open-ended task streams
- **著者**: Zewen Liu, Zhan Shi, Yisi Sang, Bing He, Minhua Lin, Tianxin Wei, Dakuo Wang, Benoit Dumoulin, Wei Jin, Hanqing Lu
- **年 / venue**: 2026 / arXiv [cs.LG]
- **リンク**: Code: https://github.com/A-EVO-Lab/AdaptiveHarness

## 落合陽一フォーマット

- **ひとことでいうと**: LLMエージェントのプロンプト、スキル、ツール、メモリなどの「harness」を、固定ベンチマークではなく変化し続けるタスク列に対して継続的に改善するための Adaptive Auto-Harness を提案した論文。
- **先行研究と比べてどこがすごい？**: A-Evolve、GEPA、Meta-Harness など既存の auto-harness は固定されたオフライン評価を主対象にしているのに対し、本研究は履歴が増え続け、タスク種別が混在し、分布が時間変化する実運用的な設定を扱う。単一harnessを高頻度に更新し続けると早期にピークを迎えて劣化する、という問題設定が新しい。
- **技術や手法の肝はどこ？**: オラクルharnessとの差を **evolution loss** と **adaptation loss** に分解し、それぞれに対して stateful multi-agent evolver、harness tree、solve-time routing、人間による steering hook を組み合わせる点。単一の万能harnessを育てるのではなく、タスクごとに適応・経路選択する設計が中心。
- **どうやって有効だと検証した？**: prediction-market、security-competition、event-forecasting のタスクストリームで評価し、5つの既存 auto-harness ベースラインおよび ablation と比較したとされる。PDF本文がないため、具体的なデータセット規模、指標、数値差、統計的有意性はメタデータからは不明。
- **議論はある？**: PDF本文がないため詳細な限界議論は不明。abstractから見る限り、履歴に十分な信号がない場合は human-steering hooks に依存するため、人間介入のコスト、再現性、介入基準の標準化が論点になりそう。harness tree と routing の失敗時にどの程度性能劣化するかも要確認。
- **次に読む/試すなら**: GitHub実装を確認して harness tree と routing の実装単位を見る。既存の A-Evolve / GEPA / Meta-Harness との比較条件を確認する。小さな時系列タスク列を作り、単一harness更新と task-wise routing の差を再現する。
- **キーワード**: `LLM agents`, `auto-harness`, `self-improvement`, `open-ended task streams`, `harness routing`, `human steering`

## 気になったこと

- harness tree のノードは何を単位に分岐するのか。タスククラスタ、性能履歴、プロンプト差分、ツール構成のどれが主軸か。
- solve-time routing は教師あり分類なのか、LLM判断なのか、過去性能ベースの検索なのか。
- human-steering hooks はどの頻度で必要になり、完全自動化との差はどの程度か。
- 「単一harnessは早期ピーク後に劣化する」という主張の実験条件と再現性を確認したい。
- prediction market / security competition / event forecasting 以外の、よりソフトウェア開発寄りのストリームにも効くか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
