# Paperpile Brief 2026-06-02 - OpenSkillEval: Automatically auditing the open skill ecosystem for LLM agents

## 基本情報

- **タイトル**: OpenSkillEval: Automatically auditing the open skill ecosystem for LLM agents
- **著者**: Jiahao Ying, Boxian Ai, Wei Tang, Siyuan Liu, Yixin Cao
- **年 / venue**: 2026 / arXiv [cs.CL]
- **リンク**: https://yingjiahao14.github.io/OpenSkillEval-Web/

## 落合陽一フォーマット

- **ひとことでいうと**: LLMエージェント向けの「スキル」が本当に役に立つかを、現実的なタスクから自動生成したベンチマークで評価するフレームワークを提案した論文。
- **先行研究と比べてどこがすごい？**: 静的ベンチマークではなく、進化する実世界の成果物からタスクを自動構築し、モデル・エージェントフレームワーク・スキルの組み合わせを統一条件で比較する点。600以上の動的タスクと30のオープンソーススキルを使い、スキルの有無だけでなく「使いこなせるか」を評価している。
- **技術や手法の肝はどこ？**: プレゼン生成、フロントエンドWebデザイン、ポスター生成、データ可視化、レポート生成の5カテゴリで現実的タスクインスタンスを自動生成し、コミュニティ由来のスキルを収集・整理して、同一タスク設定で比較できるようにした点。
- **どうやって有効だと検証した？**: 600件超の動的生成タスク、30個のオープンソーススキル、複数の最先端モデルとエージェントフレームワークを対象に体系的評価を実施。結果として、スキルがあるだけでは性能向上せず、効果は基盤モデルとエージェントフレームワークに強く依存し、人気のある公開スキルでもベースエージェントを安定して上回るとは限らないことを示した。
- **議論はある？**: 評価指標の具体、対象モデル、フレームワーク名、スキル選定基準、コスト計測方法、評価者や自動採点の信頼性はメタデータからは不明。5カテゴリ以外の実務タスクへ一般化できるかも追加確認が必要。
- **次に読む/試すなら**: プロジェクトサイトでベンチマーク資源と追加ケースを確認する。自分の使っているエージェント環境でスキル有無のA/Bテストを再現する。公開スキルの人気指標と実性能のズレを調べる。
- **キーワード**: `LLM agents`, `skills`, `agent evaluation`, `dynamic benchmark`, `OpenSkillEval`, `cost-performance trade-off`

## 気になったこと

- スキルの「品質」をどう定義し、タスク成功率・コスト・安定性・生成物品質のどれを重視しているのか。
- 動的に生成されたタスクの正解や評価基準はどの程度自動化されているのか。
- 人気スキルが効かない原因は、スキル自体の問題なのか、モデルの読解・計画能力の問題なのか、エージェントフレームワーク側の呼び出し設計なのか。
- CodexやClaude Codeのような実コーディングエージェント環境で同様の評価を再現できるか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [ying2026-pf-openskilleval-automatically-auditing-the-open-skill-ecosyste-ad1d453a.md](../../chat/2026-06-02/ying2026-pf-openskilleval-automatically-auditing-the-open-skill-ecosyste-ad1d453a.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
