# Paperpile Brief 2026-06-12 - The role of feedback alignment in self-distillation

## 基本情報

- **タイトル**: The role of feedback alignment in self-distillation
- **著者**: Semih Kara, Oğuzhan Ersoy
- **年 / venue**: 2026 / arXiv [cs.AI]、ICML 2026 Workshop on RL from World Feedback (RLxF) accepted
- **リンク**: https://arxiv.org/abs/2606.11173v1 / arXiv:2606.11173v1

## 落合陽一フォーマット

- **ひとことでいうと**: 自己蒸留で使う「教師側コンテキスト」の形が学習効果を大きく左右し、解答全体や二値報酬よりも、モデル自身の推論ステップに沿った批評が効くことを示した論文。
- **先行研究と比べてどこがすごい？**: 従来の自己蒸留は、実行トレース、正解解法、外部フィードバックなどをコンテキストとして使うが、その「設計」は固定扱いだった。本論文はコンテキストの構造そのものを比較し、StepAlignFB が GRPO より Avg@12 で 16.11 ポイント、RefSol より 5.27 ポイント高いと報告している。
- **技術や手法の肝はどこ？**: 同じモデルを、質問のみを見る student と、質問+フィードバックを見る self-teacher に分け、両者のトークン分布差を自己蒸留する。肝は critic が solver の推論トレースをステップ単位で見て、正しい箇所はなるべくコピーし、誤ったステップだけを同じ記法・粒度で修正すること。これにより、分布シフトが「間違った近傍のトークン」に局在する。
- **どうやって有効だと検証した？**: Qwen3-1.7B を solver、Qwen/QwQ-32B を frozen critic とし、OpenMathReasoning の難しめの数学問題サブセットで評価。比較対象は GRPO、参照解法を与える RefSol、ステップ整合批評を与える StepAlignFB。30問の held-out test split に対して 12サンプル集約の Pass@12、Maj@12、Avg@12、平均回答長を測った。最良値では StepAlignFB が Pass@12 90.00、Maj@12 56.67、Avg@12 35.83 で最大。
- **議論はある？**: 評価セットは30問と小さく、OpenMathReasoning の特定条件でフィルタされた数学推論に限定される。critic が強い QwQ-32B で、フィードバック生成プロンプトもかなり作り込まれているため、一般タスク・弱い critic・低品質フィードバックでも同じ効果が出るかは未検証。最良チェックポイントをメトリクスごとに選ぶため、実運用では validation 選択の設計が重要。
- **次に読む/試すなら**: 1. 自分の推論タスクで「正解全文」ではなく「モデル出力に沿った差分批評」を作る最小実験を試す。 2. RefSol と StepAlignFB の per-token advantage を可視化し、信号が局在するか確認する。 3. critic を弱くした場合や、非数学タスクで同じ設計が効くか調べる。
- **キーワード**: `self-distillation`, `feedback alignment`, `step-aligned critique`, `GRPO`, `RLVR`, `process supervision`, `Qwen3`, `OpenMathReasoning`

## 気になったこと

- StepAlignFB の勝因が「ステップ整合」そのものなのか、「正しい部分をコピーする」ことによる in-context copying の効果なのかを分離した ablation がもっと欲しい。
- 評価が30問なので、統計的なばらつきや seed 依存性をどの程度見ているか追加確認したい。
- critic のフィードバック生成コストを含めた総計算量で、GRPO や RefSol とどこまで公平に比較できるかが気になる。
- 実装するなら、まず既存の解答ログに対して「正しいステップを保持し、誤りだけ修正する critic prompt」を作り、teacher context として差し込むのが最小再現になりそう。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [kara2026-qy-the-role-of-feedback-alignment-in-self-distillation-dea73a09.md](../../chat/2026-06-12/kara2026-qy-the-role-of-feedback-alignment-in-self-distillation-dea73a09.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
