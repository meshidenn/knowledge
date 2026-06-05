# Chat Prompt 2026-06-05

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- Trust Region On-Policy Distillation

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-05 - Trust Region On-Policy Distillation

## 基本情報

- **タイトル**: Trust Region On-Policy Distillation
- **著者**: Xingrun Xing, Haoqing Wang, Boyan Gao, Ziheng Li, Yehui Tang
- **年 / venue**: 2026 / arXiv [cs.LG]
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: LLMのOn-Policy Distillationで、教師と生徒の分布がずれたときに不安定になる問題を、信頼できる領域だけで蒸留するTrust Region型の手法で改善する論文。
- **先行研究と比べてどこがすごい？**: 通常のOPDやEOPD、REOPOLDでは、学生モデルが生成したトークンに対する教師の監督が分布ミスマッチ下で信頼できず、勾配推定が壊れやすい。この論文は、教師の監督が信頼できる領域と外れ値領域を分け、信頼領域ではon-policy学習、外れ値領域ではクリッピング・マスキング・forward KL推定などを使う設計にしている点が新規性。
- **技術や手法の肝はどこ？**: コアはTrOPD、すなわちTrust Region On-Policy Distillation。学生が生成したトークンに対して、教師のtoken-level supervisionが信頼できる範囲だけでOPDを行い、分布ミスマッチ下でK1 reverse-KL estimatorが難しくなる問題を緩和する。さらに、教師prefixから学生に生成を継続させるoff-policy guidanceを使い、forward KLで信頼可能な領域へ探索を寄せる。
- **どうやって有効だと検証した？**: abstractベースでは、数学推論、コード生成、一般ドメインのベンチマークで、OPD、EOPD、REOPOLDなどのSoTA OPDベースラインと比較し、一貫して上回ったとされる。PDF本文がないため、具体的なモデルサイズ、データセット名、数値差、アブレーションの詳細はメタデータからは不明。
- **議論はある？**: PDF本文がないため詳細な限界は不明。想定される論点は、信頼領域の判定基準がどの程度頑健か、外れ値処理のハイパーパラメータ依存性、forward KLによるoff-policy guidanceが探索多様性を狭めないか、数学・コード以外の長期タスクやエージェント学習で同じように効くか。
- **次に読む/試すなら**: TrOPDのtrust region判定式とK1 reverse-KL estimatorの扱いを本文で確認する。OPD/EOPD/REOPOLDとの差分を実装単位で整理する。小さなLLM蒸留実験で、分布ミスマッチが大きい設定を作って再現する。
- **キーワード**: `on-policy distillation`, `trust region`, `LLM post-training`, `reverse KL`, `forward KL`, `policy distillation`

## 気になったこと

- trust regionを何で定義しているのか。教師と学生の確率比、KL、logprob差、あるいは別の信頼度指標か。
- 外れ値領域でのgradient clipping、masking、forward-KL estimationの使い分けは固定ルールか、実験的に選ぶものか。
- 「一貫して上回る」が、平均性能なのか、安定性・失敗率の改善なのか、compute効率も含むのかを確認したい。
- REOPOLDとの違いを、目的関数・サンプリング・credit assignmentの観点で比較したい。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
