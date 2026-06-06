# Paperpile Brief 2026-06-06 - A primer in post-training reasoning data: What we know about how it works

## 基本情報

- **タイトル**: A primer in post-training reasoning data: What we know about how it works
- **著者**: Yaoming Li, Guangxiang Zhao, Qilong Shi, Lin Sun, Xiangzheng Zhang, Tong Yang
- **年 / venue**: 2026 / arXiv [cs.CL]
- **リンク**: DOI・arXiv ID・URLはメタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: 大規模推論モデルの性能を左右する「ポストトレーニング用推論データ」について、公開研究・システム報告を横断的に整理したサーベイ/入門論文。
- **先行研究と比べてどこがすごい？**: 個別のデータセット、RLレシピ、報酬モデル、ベンチマーク、 frontier system report に散らばっていた知見を、150本以上の公開研究・報告をもとに「推論データ」という観点から統合している点。抽象的な訓練手法ではなく、何のデータが効くのかに焦点を当てている。
- **技術や手法の肝はどこ？**: 分野を4つの問いで整理していること。すなわち、どんなデータオブジェクトが存在するか、何がそのデータを有用にするか、どう構築されるか、どのようにスケールするか。この枠組みを通じて、今後の reasoning-data release や post-training recipe を評価・帰属するための見取り図を作っている。
- **どうやって有効だと検証した？**: PDF本文がなく、メタデータ上はサーベイ論文であることしか確認できないため、独自実験や定量評価の有無はメタデータからは不明。abstract上は150以上の公開研究・システム報告の統合が主な根拠。
- **議論はある？**: PDF本文がないため詳細な限界は不明。ただしメタデータから見える論点として、公開研究・公開レポートに依存するため、非公開の frontier model training data や内部アブレーションの知見は十分に扱えない可能性がある。また、推論データの「有用性」をどう因果的に切り分けるかは難しい。
- **次に読む/試すなら**: 1. 本文PDFを取得して4分類の詳細と引用リストを確認する。2. 自分のLLM post-training実験に対して、データを「object / usefulness / construction / scaling」の4軸で棚卸しする。3. reasoning data の品質指標、合成データ生成、RL報酬設計に関する引用先を追う。
- **キーワード**: `post-training`, `reasoning data`, `large reasoning models`, `reinforcement learning`, `reward models`, `survey`

## 気になったこと

- 「reasoning data object」として何を分類しているのか。CoT、verifier trace、tool-use trajectory、preference pair、RL rollout などがどう整理されているか確認したい。
- データの有用性を、正解率・多様性・難易度・検証可能性・探索性のどれで説明しているのか。
- スケーリング則について、データ量、問題難易度、モデルサイズ、RLステップ数のどれを主変数として扱っているのか。
- 公開モデルと frontier system report の知見を同じ枠組みに入れるとき、どの程度まで再現可能性を担保しているのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [li2026-fk-a-primer-in-post-training-reasoning-data-what-we-know-about-ho-8c936437.md](../../chat/2026-06-06/li2026-fk-a-primer-in-post-training-reasoning-data-what-we-know-about-ho-8c936437.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
