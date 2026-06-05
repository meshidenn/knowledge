# Paperpile Brief 2026-06-05 - Adaptive Auto-harness: Sustained self-improvement for agentic system deployment on open-ended task streams

## 基本情報

- **タイトル**: Adaptive Auto-harness: Sustained self-improvement for agentic system deployment on open-ended task streams
- **著者**: Zewen Liu, Zhan Shi, Yisi Sang, Bing He, Minhua Lin, Tianxin Wei, Dakuo Wang, Benoit Dumoulin, Wei Jin, Hanqing Lu
- **年 / venue**: 2026 / arXiv [cs.LG]
- **リンク**: https://github.com/A-EVO-Lab/AdaptiveHarness

## 落合陽一フォーマット

- **ひとことでいうと**: 固定ベンチマークではなく、分布が変化し続けるオープンエンドなタスク列に対して、LLMエージェントのプロンプト・ツール・記憶・スキルなどの「harness」を継続的に自己改善する枠組みを提案した論文。
- **先行研究と比べてどこがすごい？**: A-Evolve、GEPA、Meta-Harnessのような既存のauto-harness系は主に固定されたオフラインベンチマークで評価されるが、この論文は実運用に近い「履歴が増え続ける」「タスクが異質」「分布が時間変化する」状況を問題化している。単一harnessを高頻度に更新し続けると、初期に精度がピークを迎えた後に劣化するという脆さに対して、タスク単位の適応とルーティングを導入している点が新規性。
- **技術や手法の肝はどこ？**: oracle harnessとの差を「evolution loss」と「adaptation loss」に分解し、それぞれに対して、状態を持つmulti-agent evolver、solve-time routing付きのharness tree、人間が必要箇所に介入できるsteering hooksを組み合わせる。単一の万能harnessを更新し続けるのではなく、タスク特性に応じて複数のharnessを構築・選択する設計が中心。
- **どうやって有効だと検証した？**: abstractベースでは、prediction market、security competition、event forecastingのタスクストリームで評価し、5つの既存auto-harnessベースラインおよびablationと比較したとされる。各構成要素の寄与として、construction、routing、targeted human steeringが性能向上に効いたと説明されている。PDF本文がないため、具体的なデータセット規模、指標、数値差、統計的検定はメタデータからは不明。
- **議論はある？**: PDF本文がないため詳細な限界は不明。ただしabstractから見る限り、人間のsteering hooksにどの程度依存するか、harness treeの肥大化や運用コスト、分布変化検知の失敗時の挙動、既存ベースラインとの計算資源差が論点になりそう。細かな再現性や実装条件もメタデータからは不明。
- **次に読む/試すなら**: GitHubの実装を確認してharness treeとroutingの実装粒度を見る。A-Evolve、GEPA、Meta-Harnessとの違いを表にする。自分のエージェント評価環境で、固定ベンチではなく時系列タスク列を作って劣化曲線を再現する。
- **キーワード**: `auto-harness`, `LLM agents`, `self-improvement`, `open-ended task streams`, `harness routing`, `human steering`

## 気になったこと

- evolution lossとadaptation lossがどのように定義・推定されているのか。
- harness treeのノード分岐基準とsolve-time routingは、学習器なのかヒューリスティックなのか。
- 「accuracy peaks early and then declines」という現象が、どのベースライン・どのタスクでどれくらい強く出るのか。
- human-steering hooksが性能を上げるとして、その介入量・タイミング・コストはどう測られているのか。
- オープンエンドなタスクストリーム評価をどう標準化できるか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [liu2026-ca-adaptive-auto-harness-sustained-self-improvement-for-agentic-b6beed5f.md](../../chat/2026-06-05/liu2026-ca-adaptive-auto-harness-sustained-self-improvement-for-agentic-b6beed5f.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
