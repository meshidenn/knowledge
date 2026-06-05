# Chat Prompt 2026-06-05

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- {OCC}-{RAG}: Optimal Cognitive Core for faithful question answering

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-05 - OCC-RAG: Optimal Cognitive Core for faithful question answering

## 基本情報

- **タイトル**: OCC-RAG: Optimal Cognitive Core for faithful question answering
- **著者**: Maksim Savkin, Mikhail Goncharov, Alexander Gambashidze, Alla Chepurova, Dmitrii Tarasov, Nikita Andriianov, Daria Pugacheva, Vasily Konovalov, Andrey Galichin, Ivan Oseledets
- **年 / venue**: 2026 / arXiv [cs.CL]
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: 大規模な汎用LLMではなく、与えられた文脈に忠実に多段推論・回答・拒否を行う小型言語モデルOCC-RAGを提案した論文。
- **先行研究と比べてどこがすごい？**: パラメトリック知識の多さよりも、提供コンテキストに基づく忠実なQA能力に特化している点が差分。0.6B/1.7B規模のSLMで、2〜6倍大きい汎用モデルに匹敵または上回ると主張している。ただしPDF本文がなく、比較条件や統計的な詳細はメタデータからは不明。
- **技術や手法の肝はどこ？**: OCCという「タスク特化小型モデル」の設計思想に基づき、OCC-RAGでは複数文脈・複数ホップQAデータを大規模合成する学習パイプラインを作っている。300万件超の例で、多段推論、文脈忠実性、答えられない場合の棄権を狙ってmid-trainingしている点がコア。
- **どうやって有効だと検証した？**: abstract上ではHotpotQA、MuSiQue、TAT-QAで多段推論、ConFiQAでfaithfulness、MuSiQue-Unでrefusalを評価したとされる。比較対象は「2〜6倍大きい汎用モデル」とあるが、具体的なモデル名・スコア・評価プロンプトはメタデータからは不明。
- **議論はある？**: PDF本文がないため、限界や失敗例はメタデータからは不明。気になる点は、合成データの分布偏り、引用が本当に根拠として機能しているか、構造化reasoning traceがfaithfulnessを保証するのか、ベンチマーク外のRAG用途にどこまで一般化するか。
- **次に読む/試すなら**: OCC-RAG-0.6B/1.7Bのモデル公開先を探す。HotpotQA/MuSiQueで手元RAGタスクに近い最小評価を組む。合成QA生成パイプラインの詳細とデータライセンスを確認する。
- **キーワード**: `RAG`, `faithful QA`, `small language model`, `multi-hop reasoning`, `abstention`, `context grounding`

## 気になったこと

- 引用つきreasoning traceが、単なる生成フォーマットではなく実際の根拠選択能力を改善しているのか。
- 「literal quotes from the context」によるcitationは、長文・表・数式・ノイズ混じりPDFでも安定するのか。
- 300万件超の合成データの生成元、フィルタリング、品質評価、汚染対策。
- 小型モデルが大きい汎用モデルを上回る条件は、コンテキストが十分与えられる場合に限定されるのか。
- 実運用では、検索器の失敗時にOCC-RAGがどれくらい適切に拒否できるのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
