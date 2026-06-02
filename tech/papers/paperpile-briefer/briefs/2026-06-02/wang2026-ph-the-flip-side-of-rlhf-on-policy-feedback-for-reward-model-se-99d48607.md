# Paperpile Brief 2026-06-02 - The flip side of {RLHF}: On-policy feedback for reward model self-supervised improvement

## 基本情報

- **タイトル**: The flip side of {RLHF}: On-policy feedback for reward model self-supervised improvement
- **著者**: Wang, Xiaobo; Wu, Tong; Tang, Min; Li, Jiaqi; Liu, Qi; Zheng, Zilong
- **年 / venue**: 2026 / arXiv [cs.CL]
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: RLHFにおける報酬モデルを、on-policy feedbackを使って自己教師あり的に改善する方法を扱う論文。
- **先行研究と比べてどこがすごい？**: タイトルからは、通常のRLHFで使われる人間フィードバックや固定的な報酬モデルに対し、方策が生成するデータに基づくon-policy feedbackで報酬モデルを継続的に改善する点が新規性と思われる。ただし性能差や具体的な比較対象はメタデータからは不明。
- **技術や手法の肝はどこ？**: 「reward model self-supervised improvement」とあるため、報酬モデル自身または方策から得られる信号を使って追加ラベルなしに報酬モデルを更新する設計が肝と考えられる。具体的な損失関数、データ生成手順、フィードバックの定義はメタデータからは不明。
- **どうやって有効だと検証した？**: 実験、評価データ、ベースライン、指標はメタデータからは不明。
- **議論はある？**: on-policy feedbackは分布シフトを減らせる可能性がある一方、報酬モデルの自己強化によるバイアス増幅、誤報酬の固定化、方策との共適応が懸念される。論文内での扱いはメタデータからは不明。
- **次に読む/試すなら**: 本文で手法の擬似コードと損失関数を確認する / RLHF・DPO・RLAIFとの比較実験を確認する / 報酬モデルの自己改善が破綻しないための正則化や検証手順を探す
- **キーワード**: `RLHF`, `reward model`, `on-policy feedback`, `self-supervised learning`, `alignment`

## 気になったこと

- on-policy feedbackは誰が、または何が生成するフィードバックなのか。
- 報酬モデルの自己教師あり改善で、誤った報酬信号の自己増幅をどう防ぐのか。
- DPO、IPO、RLAIF、online RLHF系の研究と何が本質的に違うのか。
- arXiv ID、URL、abstractがメタデータにないため、本文確認が必要。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [wang2026-ph-the-flip-side-of-rlhf-on-policy-feedback-for-reward-model-se-99d48607.md](../../chat/2026-06-02/wang2026-ph-the-flip-side-of-rlhf-on-policy-feedback-for-reward-model-se-99d48607.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
