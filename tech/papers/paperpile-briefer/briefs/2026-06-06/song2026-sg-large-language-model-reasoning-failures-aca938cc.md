# Paperpile Brief 2026-06-06 - Large language model reasoning failures

## 基本情報

- **タイトル**: Large language model reasoning failures
- **著者**: Song, Peiyang; Han, Pengrui; Goodman, Noah
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: GitHub repository: https://github.com/Peiyang-Song/Awesome-LLM-Reasoning-Failures

## 落合陽一フォーマット

- **ひとことでいうと**: LLMの推論失敗を体系的に整理し、失敗の種類・原因・緩和策を分類するサーベイ論文。
- **先行研究と比べてどこがすごい？**: メタデータ上の主張では、LLMの推論失敗に特化した初の包括的サーベイ。推論を「身体性を伴う推論」と「非身体的推論」に分け、さらに非身体的推論を直感的・非形式的推論と論理的・形式的推論に分ける枠組みを提示している点が差分。
- **技術や手法の肝はどこ？**: 推論能力そのものの分類軸と、推論失敗の分類軸を分けて整理すること。失敗は、LLMアーキテクチャに内在する根本的失敗、特定応用領域で現れる制約、入力の小さな変化に対する頑健性問題の3種類に分類される。
- **どうやって有効だと検証した？**: PDF本文がなく、abstractベースのため詳細は不明。各失敗について定義、既存研究の分析、根本原因、緩和策を整理したサーベイとして有効性を示していると読めるが、実験ベンチマークや定量評価の有無はメタデータからは不明。
- **議論はある？**: サーベイであるため、分類枠組みの網羅性や境界の曖昧さが論点になりそう。個別失敗の原因がモデル構造由来なのか、データ・評価設計・プロンプト依存なのかをどこまで切り分けられているかはメタデータからは不明。
- **次に読む/試すなら**: GitHubリポジトリの分類一覧を確認する。自分の対象タスクが「fundamental」「application-specific」「robustness」のどれに当たるか対応づける。代表的な失敗例を1つ選び、手元のLLMで最小再現プロンプトを作る。
- **キーワード**: `LLM reasoning`, `reasoning failure`, `survey`, `robustness`, `formal reasoning`, `embodied reasoning`

## 気になったこと

- 「embodied reasoning」と「non-embodied reasoning」の境界は、マルチモーダルLLMやロボティクスではどのように扱われているのか。
- 根本的失敗と頑健性問題は独立分類なのか、それとも同じ現象を別角度から見ているのか。
- 緩和策として、プロンプト工夫、外部ツール、検証器、探索、学習時の改善のどれが中心に整理されているのか。
- 公開GitHubリポジトリがどの粒度で論文を分類しているか確認したい。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [song2026-sg-large-language-model-reasoning-failures-aca938cc.md](../../chat/2026-06-06/song2026-sg-large-language-model-reasoning-failures-aca938cc.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
