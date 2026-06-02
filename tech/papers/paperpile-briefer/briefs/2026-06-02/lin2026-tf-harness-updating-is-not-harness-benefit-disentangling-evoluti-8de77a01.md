# Paperpile Brief 2026-06-02 - Harness updating is not harness benefit: Disentangling evolution capabilities in self-evolving {LLM} agents

## 基本情報

- **タイトル**: Harness updating is not harness benefit: Disentangling evolution capabilities in self-evolving {LLM} agents
- **著者**: Lin, Minhua; Wu, Juncheng; Wang, Zijun; Shi, Zhan; Sang, Yisi; He, Bing; Liu, Zewen; Wei, Tianxin; Wu, Zongyu; Zhang, Zhiwei; Wang, Dakuo; Zhang, Xiang; Dumoulin, Benoit; Xie, Cihang; Zhou, Yuyin; Wang, Suhang; Lu, Hanqing
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: 自己進化型LLMエージェントにおける「ハーネス更新」と、実際に得られる「ハーネス由来の性能向上」を切り分けて評価しようとする論文。
- **先行研究と比べてどこがすごい？**: タイトルから見る限り、単にエージェントが自分の実行環境・評価手順・ツール利用枠組みを更新できることを能力向上とみなすのではなく、その更新が本当に有益かを分解して問う点が新規性。具体的な先行研究との差分、性能、比較結果はメタデータからは不明。
- **技術や手法の肝はどこ？**: 「harness updating」と「harness benefit」を別概念として扱い、自己進化LLMエージェントの進化能力を分解評価する設計が肝だと思われる。評価軸、ベンチマーク、エージェント構成、更新対象の詳細はメタデータからは不明。
- **どうやって有効だと検証した？**: メタデータからは不明。実験、データセット、比較対象、評価指標は確認が必要。
- **議論はある？**: メタデータからは不明。ただし論点としては、ハーネス更新がタスク性能を本当に改善するのか、評価環境への過適合ではないのか、自己進化エージェントの能力評価が再現可能かが重要になりそう。
- **次に読む/試すなら**: 論文本文またはarXiv IDを探す / 「harness updating」と「harness benefit」の定義を確認する / 実験設定が評価ハックや環境過適合をどう防いでいるかを見る
- **キーワード**: `self-evolving LLM agents`, `harness updating`, `agent evaluation`, `LLM agents`, `evolution capabilities`

## 気になったこと

- 「harness」とは具体的に何を指すのか。プロンプト、ツール、評価コード、実行環境、探索戦略のどれか。
- ハーネス更新による見かけの改善と、汎化する能力向上をどう分離しているのか。
- 自己進化エージェントが評価系に過適合するリスクをどう扱っているのか。
- 関連研究として、LLM agent self-improvement、automated prompt optimization、tool-use agent evaluation、benchmark contamination を探したい。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [lin2026-tf-harness-updating-is-not-harness-benefit-disentangling-evoluti-8de77a01.md](../../chat/2026-06-02/lin2026-tf-harness-updating-is-not-harness-benefit-disentangling-evoluti-8de77a01.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
