# Paperpile Brief 2026-06-02 - Trust-region behavior Blending for on-policy distillation

## 基本情報

- **タイトル**: Trust-region behavior Blending for on-policy distillation
- **著者**: Daniil Plyusov, Alexey Gorbatovski, Alexey Malakhov, Nikita Balagansky, Boris Shaposhnikov, Daria Korotyshova, Daniil Gavrilov
- **年 / venue**: 2026 / arXiv [cs.LG]
- **リンク**: DOI・arXiv ID・URLはメタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: on-policy distillationで、学習初期の弱いstudent rolloutをteacherに近い行動方策で補助するwarmup手法TRBを提案した論文。
- **先行研究と比べてどこがすごい？**: offline distillationのprefix mismatchを避けるOPDでも、初期studentが生成するprefix品質が低い問題が残る。TRBはstudent中心のKL trust region内でteacherに最も近いbehavior policyを使い、初期rolloutを改善する点が新しい。
- **技術や手法の肝はどこ？**: per-prefixのreverse-KL OPD lossは変えず、rollout policyだけをwarmup中に置き換える。KL budgetを徐々に0へannealし、最終的には純粋なstudent rolloutへ戻す設計が肝。
- **どうやって有効だと検証した？**: 2つの数学推論distillation設定で比較実験を行い、比較手法の中で最も強い平均性能を達成したとされる。具体的なモデル、データセット、指標、ベースライン名はメタデータからは不明。
- **議論はある？**: KL budgetの設定・annealing scheduleへの感度、teacherに近いbehavior policyの計算コスト、数学推論以外への一般化はメタデータからは不明。warmup後にstudent rolloutへ戻るため、初期改善がどれだけ最終性能に残るかも確認したい。
- **次に読む/試すなら**: TRBのbehavior policy導出式を確認する。KL budgetとannealing scheduleのablationを見る。小さな数学推論タスクでOPD baselineとの差を再現する。
- **キーワード**: `on-policy distillation`, `trust region`, `KL divergence`, `behavior policy`, `math reasoning`, `teacher-student learning`

## 気になったこと

- 「closest-to-teacher behavior policy inside a student-centered KL trust region」が閉形式で解けるのか、サンプリング近似なのか。
- reverse-KL OPD lossを固定したままrollout policyだけ変えることで、分布シフトやimportance correctionは問題にならないのか。
- 数学推論以外、たとえばコード生成や対話モデル蒸留でも同じwarmup効果が出るのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [plyusov2026-zz-trust-region-behavior-blending-for-on-policy-distillation-cac2debd.md](../../chat/2026-06-02/plyusov2026-zz-trust-region-behavior-blending-for-on-policy-distillation-cac2debd.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
