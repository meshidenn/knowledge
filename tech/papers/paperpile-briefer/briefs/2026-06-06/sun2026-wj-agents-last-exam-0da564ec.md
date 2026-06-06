# Paperpile Brief 2026-06-06 - Agents' Last Exam

## 基本情報

- **タイトル**: Agents' Last Exam
- **著者**: Yiyou Sun, Xinyang Han, Weichen Zhang, Yuanbo Pang, Tianyu Wang, Yuhan Cao, Yixiao Huang, Chris Duroiu, Haoyun Zhang, Jeffrey Lin, Weishu Zhang, Tyler Zeng, Ying Yan, Bo Liu, Hanson Wen, Mingyang Xu, Xiaoyuan Liu, Zimeng Chen, Weiyan Shi, Amanda Dsouza, Vincent Sunn Chen, Dawn Song ほか多数
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: https://arxiv.org/abs/2606.05405 / PDF: https://arxiv.org/pdf/2606.05405.pdf

## 落合陽一フォーマット

- **ひとことでいうと**: AIエージェントが実際の専門職ワークフローを長時間・多段階で遂行できるかを測る、大規模な実務型ベンチマーク Agents' Last Exam（ALE）を提案した論文。
- **先行研究と比べてどこがすごい？**: MMLUやGPQAのような知識QAではなく、GUI・CLI・専門ソフト・ファイル生成を含む「仕事そのもの」を評価する点が差分。SWE-bench、OSWorld、Terminal-Bench、GDPval、RLIなどと比べて、SOC/O*NETに基づく55サブドメイン・13産業クラスタをすべてカバーし、1,490タスクインスタンスを専門家由来で構築している。人手評価ではなく、成果物やマイルストーンに対する決定的チェック・構造化ルーブリックで検証する設計も大きい。
- **技術や手法の肝はどこ？**: 「経済的に価値のある実務」を、代表性・複雑性・検証可能性の3条件でタスク化している点。250名以上の産業専門家と協力し、実際に完了済みのプロジェクトをもとにタスクを作り、レビュー、エンジニアによるドライラン、専門家委員会レビューを通して品質管理する。評価対象は、視覚認識、コード実行、ツール利用、長期計画を同じループで扱う Generalist Computer-Use Agent。
- **どうやって有効だと検証した？**: 論文本文では、ALEを既存ベンチマークとタスク形式・規模・産業カバレッジ・検証方式で比較し、さらに複数のエージェントハーネスと基盤モデル構成で実験している。最難層の平均 full pass rate は約2.6%で、最強構成でも容易な層で50%未満、最難層では10%未満とされる。Claude Code + Opus 4.7 の失敗分析では、理解・アプローチ上の失敗が多く、専門知識不足とGUI利用不足が主要ボトルネックとして示されている。
- **議論はある？**: 実務由来タスクを自動評価するため、チェック可能な成果物に寄りやすい可能性がある。専門家が提出したタスクの品質や代表性、非公開・継続追加される living benchmark としての再現性、モデルがベンチマークに過適合するリスクも論点。PDF抽出本文からは、各タスクの完全な公開範囲、ライセンス、長期的なデータ汚染対策の詳細までは十分に確認できない。
- **次に読む/試すなら**: 
  1. 公開タスク・Leaderboard・GitHub/HuggingFaceの実体を確認する。
  2. 自分のエージェント環境でALEの小規模サブセットを動かし、失敗ログを分類する。
  3. GDPval、RLI、OSWorld、Terminal-Benchとの評価設計の違いを表で比較する。
- **キーワード**: `AI agents`, `benchmark`, `computer-use agents`, `long-horizon tasks`, `O*NET`, `SOC taxonomy`, `workflow evaluation`, `automated verification`

## 気になったこと

- 「経済的に価値がある」タスクの選定基準が、産業ごとにどれだけ均質に適用されているか。
- 決定的チェックやルーブリックで評価できる成果物に限定すると、創造的・交渉的・曖昧な専門業務が落ちないか。
- GUI利用不足が本当にモデル能力の問題なのか、ハーネスや環境設計の問題なのかを切り分けたい。
- living benchmark として継続更新される場合、過去スコアとの比較可能性をどう維持するのか。
- ALE最難層で失敗するタスクに対し、専門ツールの訓練、RAG、環境操作ポリシー、分解計画のどれが最も効くか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [sun2026-wj-agents-last-exam-0da564ec.md](../../chat/2026-06-06/sun2026-wj-agents-last-exam-0da564ec.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
