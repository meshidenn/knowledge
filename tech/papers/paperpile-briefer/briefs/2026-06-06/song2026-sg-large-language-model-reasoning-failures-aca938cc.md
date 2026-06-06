# Paperpile Brief 2026-06-06 - Large language model reasoning failures

## 基本情報

- **タイトル**: Large language model reasoning failures
- **著者**: Peiyang Song, Pengrui Han, Noah Goodman
- **年 / venue**: 2026 / Transactions on Machine Learning Research, arXiv [cs.AI]
- **リンク**: https://arxiv.org/abs/2602.06176 / PDF: https://arxiv.org/pdf/2602.06176.pdf / GitHub: https://github.com/Peiyang-Song/Awesome-LLM-Reasoning-Failures

## 落合陽一フォーマット

- **ひとことでいうと**: LLMの「推論ができない瞬間」を、非身体的推論と身体的推論、さらに基本的失敗・応用上の限界・ロバスト性問題という2軸で整理したサーベイ論文。
- **先行研究と比べてどこがすごい？**: 個別の失敗事例ではなく、LLM reasoning failures そのものを主題にした包括的サーベイとして、認知バイアス、論理、数学、コード、物理常識、視覚空間、ロボット計画までを同じ分類枠で接続している点が新しい。失敗を「性能が低い」だけでなく「小さな摂動で出力が揺れる」問題として扱う設計も重要。
- **技術や手法の肝はどこ？**: 推論を embodied / non-embodied に分け、non-embodied を informal / formal に細分化する。その上で、失敗を fundamental failures、application-specific limitations、robustness issues に分類する。各失敗について定義、既存研究、原因仮説、緩和策を並べ、LLMの弱点を横断的に見える形にしている。
- **どうやって有効だと検証した？**: 新しい実験ベンチマークを主に提案する論文ではなく、既存研究の体系的整理が主眼。PDF本文では、ワーキングメモリ、抑制制御、認知バイアス、reversal curse、構成的推論、数え上げ、算術、数学文章題、物理常識、2D/3D空間推論、ロボット計画などの既存評価研究を整理している。
- **議論はある？**: 根本原因分析が未完成な失敗が多い。特に構成的推論、高次Theory of Mind、2D/3D物理常識、マルチエージェント計画では、観察された失敗と内部機構の対応がまだ弱い。また、既存文献に依存するため、研究されやすい失敗領域に偏りがある。マルチターン・インタラクティブな現実的状況はまだ不足している。
- **次に読む/試すなら**: 1. GitHubリポジトリで失敗事例リストを確認する。 2. 自分のLLM評価に、言い換え・順序変更・変数名変更などの摂動テストを入れる。 3. 自分の用途を fundamental / limitation / robustness のどれに弱いか分類して評価項目を作る。
- **キーワード**: `LLM reasoning`, `reasoning failures`, `robustness`, `embodied reasoning`, `formal reasoning`, `cognitive bias`, `benchmarking`

## 気になったこと

- 「失敗分類」は実務評価にかなり使えそうだが、各カテゴリをどの粒度でテストケース化すれば十分か。
- reasoning-specialized models に対して、古い失敗事例がどれだけ残存しているかを継続測定するベンチマークが必要。
- 物理・ロボット・マルチエージェント系の失敗は、単純なプロンプト改善よりも world model、シミュレータ、フィードバック制御との統合が本筋に見える。
- 「推論失敗」を性能ランキングではなく、事故分析・故障分類として扱う視点は、AIエージェント評価にも転用できそう。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [song2026-sg-large-language-model-reasoning-failures-aca938cc.md](../../chat/2026-06-06/song2026-sg-large-language-model-reasoning-failures-aca938cc.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
