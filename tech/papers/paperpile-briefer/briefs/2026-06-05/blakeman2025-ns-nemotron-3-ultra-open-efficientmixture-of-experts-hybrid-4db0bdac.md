# Paperpile Brief 2026-06-05 - Nemotron 3 Ultra / Nemotron 3 Nano

## 基本情報

- **タイトル**: Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning / Nemotron 3 Nano: Open, efficient Mixture-of-Experts hybrid Mamba-Transformer model for agentic reasoning
- **著者**: Aaron Blakeman, Aaron Grattafiori, Aarti Basant, Abhibha Gupta, Abhinav Khattar, Adi Renduchintala ほか多数
- **年 / venue**: 2025 / arXiv [cs.CL]
- **リンク**: DOI・arXiv ID・URLはメタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: NVIDIA系の大規模チームによる、Mixture-of-ExpertsとMamba-Transformerを組み合わせたオープンな推論・エージェント向けLLM「Nemotron 3 Nano 30B-A3B」を提示する論文。PDF本文は取得できていないため、以下はabstractベース。
- **先行研究と比べてどこがすごい？**: Nemotron 2 Nanoより精度を上げつつ、forward passあたりの活性化パラメータを半分未満にしたと主張している。さらにGPT-OSS-20BやQwen3-30B-A3B-Thinking-2507のような同規模オープンモデルに対して、最大3.3倍の推論スループットと、主要ベンチマークでの高精度を主張している。
- **技術や手法の肝はどこ？**: 30B規模だが各推論で約3B相当を活性化するMoE設計と、Mamba系の系列処理能力とTransformerを組み合わせたハイブリッド構成が中核。25兆text tokensで事前学習し、その後SFTと大規模RLを多様な環境で行う、という訓練パイプラインも重要。
- **どうやって有効だと検証した？**: abstract上では、Nemotron 2 Nano、GPT-OSS-20B、Qwen3-30B-A3B-Thinking-2507との比較、人気ベンチマーク、推論スループット、agentic・reasoning・chat能力、最大1M tokensのコンテキスト対応を評価したとされる。ただしPDF本文がないため、具体的なベンチマーク名、表の数値、評価条件、ハードウェア条件はメタデータからは不明。
- **議論はある？**: タイトルのメタデータが「Nemotron 3 Ultra」と「Nemotron 3 Nano」を連結したように見え、対象モデル名に不整合がある。性能主張はabstractでは強いが、比較条件、推論最適化、MoEルーティング、RL環境、1M context時の実効性能は本文なしでは検証できない。
- **次に読む/試すなら**: Hugging Face上のBase/Post-trainedチェックポイントを確認する。技術報告本文でベンチマーク表と推論条件を読む。ローカルまたはクラウドGPUで長文推論・ツール利用・reasoning系タスクの最小評価を回す。
- **キーワード**: `Mixture-of-Experts`, `Mamba-Transformer`, `Nemotron`, `agentic reasoning`, `long context`, `open language model`

## 気になったこと

- タイトルメタデータの「Ultra」と「Nano」の混在が、Paperpile取り込み時のタイトル結合ミスなのか、論文本体の命名なのか確認したい。
- 「最大3.3倍」の推論スループットが、どのGPU、batch size、sequence length、precision、serving stackで測られたものか確認したい。
- 1M tokens context対応が、単に入力可能という意味か、長距離検索・推論ベンチマークで有効性を示しているのか見たい。
- MoE + Mamba-Transformerの組み合わせが、長文効率・推論能力・エージェント実行のどこに効いているのか、ablationを探したい。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [blakeman2025-ns-nemotron-3-ultra-open-efficientmixture-of-experts-hybrid-4db0bdac.md](../../chat/2026-06-05/blakeman2025-ns-nemotron-3-ultra-open-efficientmixture-of-experts-hybrid-4db0bdac.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
