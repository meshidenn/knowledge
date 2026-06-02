# Chat Prompt 2026-06-02

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- Not all disagreement is learnable: Token teachability in on-policy distillation

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-02 - Not all disagreement is learnable: Token teachability in on-policy distillation

## 基本情報

- **タイトル**: Not all disagreement is learnable: Token teachability in on-policy distillation
- **著者**: Wang, Yuanyi; Lu, Su; Gu, Yanggan; Wang, Pengkai; Yang, Yifan; Yan, Zhaoyi; Xie, Congkai; Wu, Jianmin; Yang, Hongxia
- **年 / venue**: 2026 / arXiv [cs.LG]
- **リンク**: DOI、arXiv ID、URLはメタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: On-policy distillationにおいて、教師と学生のトークン単位の不一致がすべて学習可能とは限らないことを示し、「教えやすい」トークンだけを選んで蒸留するTA-OPDを提案した論文。
- **先行研究と比べてどこがすごい？**: 従来のselective OPDが高エントロピーや高KL不一致のトークンを重視していたのに対し、この論文は「不一致の大きさ」ではなく「その不一致が学生にとって学習可能か」を見る。特に、教師分布が学生のtop-K候補内に補正的な確率質量を置くかどうかをlocal compatibility / token teachabilityとして定式化している。
- **技術や手法の肝はどこ？**: 固定コンテキスト診断で、同じ文脈におけるteacher-student KLの減少を測り、raw KL disagreementが学習価値の粗い代理変数にすぎないことを示す。そこから、学生の現在の支持集合に近い範囲で教師が有用な補正信号を出しているトークンを高teachabilityとして選び、OPD lossをその位置にだけ適用するTA-OPDを設計している。
- **どうやって有効だと検証した？**: Qwen2.5およびQwen 3のteacher-student設定で評価し、TA-OPDがfull-token OPDをしばしば上回り、保持トークン5%でも有効だったとされる。また、entropyベースおよびdivergenceベースの選択手法と比較して改善したとメタデータに記載されている。具体的なタスク、データセット、スコア、統計的有意性はメタデータからは不明。
- **議論はある？**: teachabilityの定義がtop-K候補や固定コンテキスト診断に依存する可能性がある。Qwen系以外のモデル、異なるサイズ差、長期的なrollout品質、推論能力タスクでの一般化はメタデータからは不明。5%トークン保持で良いという主張の安定性や、どの種類のトークンが選ばれるかの分析も追加確認したい。
- **次に読む/試すなら**: TA-OPDのteachability計算式とtop-K設定を確認する。既存のentropy/KL選択OPDと同一条件で小規模再現する。選択されたトークンの品詞・位置・難易度分布を可視化する。
- **キーワード**: `on-policy distillation`, `token teachability`, `selective OPD`, `KL divergence`, `teacher-student learning`, `Qwen`

## 気になったこと

- teachabilityは学生のtop-K候補に依存するため、学生が未熟すぎる段階では有用な教師信号を捨てすぎないか。
- 「incompatible disagreement」を本当に学習不能とみなしてよいのか、それともカリキュラムや温度調整で学習可能になるのか。
- 5% retained tokensでfull-token OPDを上回る場合、計算効率だけでなく過学習・ノイズ抑制の効果もあるのか。
- 報酬モデルやverifierなしで使える点は実装上強いが、タスク品質評価の詳細は確認が必要。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
