# Paperpile Brief 2026-06-02 - Guidance contrastive token credit assignment for discrete policy optimization

## 基本情報

- **タイトル**: Guidance contrastive token credit assignment for discrete policy optimization
- **著者**: Shufan Li, Konstantinos Kallidromitis, Akash Gokul Yusuke Kato, Kazuki Kozuka, Aditya Grover
- **年 / venue**: 2026 / arXiv [cs.CV]
- **リンク**: DOI、arXiv ID、URLはメタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: GRPOやDAPOのようなサンプル単位報酬のRL手法に対し、トークンごとの貢献度をより細かく割り当てるGCPOを提案した論文。
- **先行研究と比べてどこがすごい？**: 従来のgroup-advantage系手法はサンプル全体のadvantageを全トークンに一様に配るため、どのトークンが効いたかを捉えにくい。GCPOはpositive / negative prompt下の予測差分を使い、トークン単位のadvantageを作る点が新規性。
- **技術や手法の肝はどこ？**: Guidance Contrastive Policy Optimizationでは、正例プロンプトと負例プロンプトに対するモデル予測を対比し、その差に比例して各トークンへcreditを割り当てる。サンプル報酬を単純にbroadcastせず、意味的に重要なトークンへ強い学習信号を与える設計。
- **どうやって有効だと検証した？**: text-to-image生成とchain-of-thought reasoningのベンチマークで評価し、GRPOおよびDAPOと比較。GCPOは画像生成ではテキストプロンプトに対応する視覚領域、推論では重要キーワードを強調し、両タスクで一貫してベースラインを上回ったとされる。
- **議論はある？**: 実験設定、ベンチマーク名、モデル規模、計算コスト、negative promptの作り方、再現性の詳細はメタデータからは不明。contrastive prediction差分が常に正しいcredit signalになるかも追加確認が必要。
- **次に読む/試すなら**: GCPOの論文本文でアルゴリズム式とnegative prompt生成方法を確認する。GRPO/DAPO実装にtoken-level advantageを差し込めるか見る。text-to-imageより先に小さなCoTタスクで最小再現実験を組む。
- **キーワード**: `GCPO`, `token credit assignment`, `GRPO`, `DAPO`, `discrete policy optimization`, `contrastive guidance`, `reinforcement learning`, `chain-of-thought`, `text-to-image generation`

## 気になったこと

- positive / negative promptの設計が性能にどれくらい効くのか。
- token-level advantageの計算が学習の安定性や計算量に与える影響。
- GRPO/DAPOとの差分がcredit assignmentだけなのか、他の訓練設定も効いているのか。
- 視覚領域やCoTキーワードを強調したという分析が定量評価なのか可視化中心なのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [li2026-uq-guidance-contrastive-token-credit-assignment-for-discrete-poli-87d9a0a0.md](../../chat/2026-06-02/li2026-uq-guidance-contrastive-token-credit-assignment-for-discrete-poli-87d9a0a0.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
