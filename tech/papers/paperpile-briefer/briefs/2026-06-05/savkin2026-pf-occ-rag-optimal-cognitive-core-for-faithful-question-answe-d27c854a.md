# Paperpile Brief 2026-06-05 - {OCC}-{RAG}: Optimal Cognitive Core for faithful question answering

## 基本情報

- **タイトル**: {OCC}-{RAG}: Optimal Cognitive Core for faithful question answering
- **著者**: Maksim Savkin, Mikhail Goncharov, Alexander Gambashidze, Alla Chepurova, Dmitrii Tarasov, Nikita Andriianov, Daria Pugacheva, Vasily Konovalov, Andrey Galichin, Ivan Oseledets
- **年 / venue**: 2026 / arXiv [cs.CL]
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: 大規模な汎用LLMではなく、与えられた文脈に忠実に多段推論して回答する小型言語モデルOCC-RAGを作った論文。
- **先行研究と比べてどこがすごい？**: パラメトリック知識の多さよりも、提供文脈に基づく推論・引用・棄却判断に特化した設計を取っている点。0.6B / 1.7Bの小型モデルで、2〜6倍サイズの汎用モデルに対して、HotpotQA、MuSiQue、TAT-QA、ConFiQA、MuSiQue-Unで同等以上と主張している。
- **技術や手法の肝はどこ？**: multi-context / multi-hop QAを大量合成する学習パイプラインを作り、300万件超のデータで中間学習した点。回答時には構造化された reasoning trace と、文脈中のリテラルな引用に基づく source citation を出す設計らしい。
- **どうやって有効だと検証した？**: abstract上では、multi-hop reasoning系のHotpotQA、MuSiQue、TAT-QA、faithfulness評価のConFiQA、拒否性能のMuSiQue-Unで比較したとされる。ただしPDF本文がないため、比較モデル、正確なスコア、評価プロンプト、統計的有意性はメタデータからは不明。
- **議論はある？**: PDF未取得のため詳細な限界は不明。気になる点は、合成データの分布に過適合していないか、引用が「見かけ上の根拠」になっていないか、RAG文脈にノイズや矛盾がある場合の挙動、ドメイン外QAでのfaithfulness維持。
- **次に読む/試すなら**: OCC-RAG-0.6B / 1.7Bのモデル公開先を探す。ConFiQAやMuSiQue-Unでの拒否条件を確認する。自分のRAGデータで「引用必須・根拠なしなら棄却」の最小評価セットを作る。
- **キーワード**: `RAG`, `faithful QA`, `small language model`, `multi-hop reasoning`, `abstention`, `source citation`

## 気になったこと

- PDF本文がないため、OCCの「Optimal Cognitive Core」が具体的にモデル構造なのか、学習方針なのか、データ設計思想なのかを確認したい。
- reasoning traceが教師ありで学習されたものか、推論時フォーマット制御だけなのかが重要。
- 「literal quotes from the context」による citation が、回答生成の検証にも使われているのか、単なる出力形式なのかを確認したい。
- 合成QAデータ300万件超の生成元、品質管理、リーク対策、ベンチマーク汚染対策を読むべき。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [savkin2026-pf-occ-rag-optimal-cognitive-core-for-faithful-question-answe-d27c854a.md](../../chat/2026-06-05/savkin2026-pf-occ-rag-optimal-cognitive-core-for-faithful-question-answe-d27c854a.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
