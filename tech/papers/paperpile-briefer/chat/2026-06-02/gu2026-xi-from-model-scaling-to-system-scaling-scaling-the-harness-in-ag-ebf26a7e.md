# Chat Prompt 2026-06-02

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- From model scaling to system scaling: Scaling the harness in agentic {AI}

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-02 - From model scaling to system scaling: Scaling the harness in agentic AI

## 基本情報

- **タイトル**: From model scaling to system scaling: Scaling the harness in agentic AI
- **著者**: Gu, Shangding
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: https://github.com/SafeRL-Lab/cheetahclaws

## 落合陽一フォーマット

- **ひとことでいうと**: エージェントAIの次のボトルネックはモデル単体のスケーリングではなく、モデルを囲む実行・記憶・検証・統治レイヤー、つまり「harness」のスケーリングだと主張する論文。
- **先行研究と比べてどこがすごい？**: 従来の評価が最終タスク成功率に偏り、memory、retrieval、tool use、orchestration、verification、governanceを実装詳細として扱ってきた点を批判し、それらを第一級の設計・評価・最適化対象として定式化している。
- **技術や手法の肝はどこ？**: foundation model、memory substrate、context constructor、skill-routing layer、orchestration loop、verification-and-governance layerの相互作用を「agent harness」として捉え、context governance、trustworthy memory、dynamic skill routingを中心的ボトルネックとして整理する点。
- **どうやって有効だと検証した？**: Python-nativeな参照harnessとしてCheetahClawsを開発し、Claude CodeおよびOpenClawと比較したとある。ただし、具体的な評価指標、実験設定、定量結果はメタデータからは不明。
- **議論はある？**: 主張は設計思想・研究 agenda の色が強く、harness-level benchmarkの具体的実装や標準化可能性、既存エージェント基盤との差分の実証度はメタデータからは不明。CheetahClawsの再現性、保守性、実運用での安全性評価も追加確認が必要。
- **次に読む/試すなら**: CheetahClawsのGitHubを確認する。Claude Code/OpenClawとの比較軸を読む。harness-level benchmarkとして提案されるtrajectory quality、memory hygiene、context efficiency、verification costの定義を確認する。
- **キーワード**: `agentic AI`, `system scaling`, `agent harness`, `memory`, `skill routing`, `context governance`, `verification`, `governance`

## 気になったこと

- 「harnessをスケールする」とき、設計対象はアーキテクチャなのか、評価基盤なのか、運用プロセスなのか。
- CheetahClawsがClaude CodeやOpenClawに対して何を改善しているのか。
- memory hygieneやcommunication fidelityをどう測定するのか。
- モデル性能が上がった場合にもharness側のボトルネックは同じ形で残るのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
