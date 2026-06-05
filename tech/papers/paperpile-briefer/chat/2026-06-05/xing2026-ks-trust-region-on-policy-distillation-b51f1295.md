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

- **ひとことでいうと**: LLMのオンポリシー蒸留で、教師と学生モデルの分布がずれたときに不安定化する問題を、信頼できる領域だけで蒸留する Trust Region On-Policy Distillation, TrOPD で改善する論文。
- **先行研究と比べてどこがすごい？**: 既存の OPD, EOPD, REOPOLD などは、学生が生成したトークンに対して教師が常に信頼できる監督を与える前提が強い。TrOPD は教師の監督が信頼できる領域と外れ領域を分け、分布ミスマッチ下の逆KL推定の不安定性を抑える設計になっている点が差分。
- **技術や手法の肝はどこ？**: コアは、オンポリシー蒸留を「教師が信頼できるトークン領域」に限定する trust-region 的な学習。外れ領域では gradient clipping、masking、forward-KL 推定を使って悪影響を減らし、さらに教師 prefix から学生に生成を続けさせる off-policy guidance によって、学生の探索を信頼可能な領域へ寄せる。
- **どうやって有効だと検証した？**: abstract ベースでは、数学推論、コード生成、一般ドメインのベンチマークで OPD, EOPD, REOPOLD などのSoTA OPDベースラインと比較し、TrOPD が一貫して上回ったとされている。具体的なモデルサイズ、データセット名、数値差、アブレーションの詳細はメタデータからは不明。
- **議論はある？**: PDF本文がないため詳細な限界は不明。想定される論点は、信頼領域の判定基準がどれだけ頑健か、外れ領域処理の選択がタスクやモデルに依存しないか、教師 prefix による off-policy guidance が探索多様性を狭めないか、という点。
- **次に読む/試すなら**: TrOPD の trust-region 判定式と閾値設計を確認する。OPD/EOPD/REOPOLD との差分を実装レベルで比較する。小さな数学推論またはコード生成タスクで masking / clipping / forward-KL のアブレーションを再現する。
- **キーワード**: `on-policy distillation`, `LLM post-training`, `trust region`, `policy distillation`, `reverse KL`, `forward KL`, `distribution mismatch`

## 気になったこと

- 「教師が信頼できる領域」を何で測るのか。確率比、KL、教師尤度、学生尤度、あるいは別の信用スコアなのか。
- K1 reverse-KL estimator の最適化失敗が、どの条件で顕著に起きるのか。
- off-policy guidance がオンポリシー探索の改善なのか、実質的には教師軌道への回帰なのか。
- 数学推論・コード生成・一般ベンチマークで、どのタスクに一番効いているのか。
- REOPOLD との違いを、損失関数とサンプリング手順の観点で確認したい。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
