# Chat Prompt 2026-06-05

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- Domain-specific data synthesis for {LLMs} via minimal sufficient representation learning

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-05 - Domain-specific data synthesis for LLMs via minimal sufficient representation learning

## 基本情報

- **タイトル**: Domain-specific data synthesis for LLMs via minimal sufficient representation learning
- **著者**: Tong Ye, Hang Yu, Tengfei Ma, Xuhong Zhang, Jianguo Li, Peng Di, Peiyu Liu, Jianwei Yin, Wenhai Wang
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: メタデータからは不明

## 落合陽一フォーマット

- **ひとことでいうと**: 明示的なドメイン説明やプロンプト設計に頼らず、少数の参照例からドメイン固有の合成データを作るためのDOMINOという手法を提案した論文。
- **先行研究と比べてどこがすごい？**: 従来のデータ合成は、自然言語で書かれたドメイン定義や手作業のプロンプトに強く依存する「演繹的」アプローチだった。本論文は、参照サンプルだけからドメイン性を抽出する「帰納的」アプローチに切り替え、言語化しづらいドメインにも適用できる点が新しい。
- **技術や手法の肝はどこ？**: DOMINOは、参照例から「最小十分なドメイン表現」を学習し、それを合成データ生成のガイドに使う。具体的には、prompt tuningとcontrastive disentanglement objectiveを組み合わせ、ドメインレベルのパターンとサンプル固有のノイズを分離することで、過学習を抑えつつドメインらしさを保つ。
- **どうやって有効だと検証した？**: PDF本文は未取得のため、abstractベース。暗黙的なドメイン定義が必要なコーディング系ベンチマークで評価し、DOMINOで合成したデータによるfine-tuningが、強力なinstruction-tuned backboneに対してPass@1を最大4.63%改善したとされる。
- **議論はある？**: PDF本文がないため詳細な限界はメタデータからは不明。気になる点は、参照例の数や品質にどれだけ依存するか、ドメイン表現が本当に「最小十分」かをどう検証したか、coding以外のドメインにどこまで一般化するか。細かい実験設定、比較対象、アブレーション、再現性情報は本文確認が必要。
- **次に読む/試すなら**: DOMINOの目的関数とprompt tuningの実装詳細を確認する。参照例数を変えたアブレーションを見る。自分の関心ドメインで、既存LLMに参照例だけを与えて合成データを作る最小実験を設計する。
- **キーワード**: `domain-specific data synthesis`, `LLM fine-tuning`, `minimal sufficient representation`, `prompt tuning`, `contrastive learning`, `synthetic data`, `domain adaptation`

## 気になったこと

- 「最小十分なドメイン表現」を理論的にどう定義し、実装上はどのパラメータや埋め込みとして保持しているのか。
- support expansionの理論保証が、実際のLLM生成分布に対してどの程度意味を持つのか。
- 参照例にノイズや外れ値が混ざった場合、ドメイン表現が崩れないか。
- coding benchmark以外、たとえば医療、法務、科学論文要約のような専門ドメインでも有効か。
- DOMINOで生成したデータの品質評価を、人手評価・自動評価・下流性能のどれに依存しているのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
