# Paperpile Brief 2026-06-12 - Kwai Keye-VL-2.0 Technical Report

## 基本情報

- **タイトル**: Kwai Keye-VL-2.0 Technical Report
- **著者**: Kwai Keye Team, Bin Wen, Changyi Liu, Chengru Song, Chongling Rao, Guowang Zhang, Han Li, Haonan Fan, Hengrui Ju, Jiankang Chen ほか
- **年 / venue**: 2026 / arXiv [cs.CV]
- **リンク**: https://arxiv.org/abs/2606.10651v1 / arXiv:2606.10651v1

## 落合陽一フォーマット

- **ひとことでいうと**: 256K文脈の長尺動画理解とCode/Tool/Search系のエージェント能力を狙った、30B MoE・3B activeのオープンソース視覚言語モデル Keye-VL-2.0-30B-A3B の技術報告。
- **先行研究と比べてどこがすごい？**: GQAベースのマルチモーダルモデルにDeepSeek Sparse Attentionを適用し、長尺動画で問題になるKV cache肥大と計算コストを抑えながら256K contextを扱う点が主張の核。さらに、複数タスクを混ぜると基礎推論能力が落ちる問題に対して、13種類のRL済み教師を使うCross-Modal Multi-Teacher On-Policy Distillationで能力統合を狙う。
- **技術や手法の肝はどこ？**: Native-resolution ViT、画像/動画の統一エンコード、GQA互換DSA、MoE backbone、Context-RL/Video-RL、Agentic RL、MOPDを組み合わせている。特にMOPDでは、学生モデルのon-policy rolloutに対してタスク別教師がtoken-level feedbackを与え、top-k overlap、SPRR、token-category-aware scaling、反復崩壊ペナルティで蒸留を安定化する。
- **どうやって有効だと検証した？**: PDF抽出範囲では、TimeLens系の時間定位、LongVideoBench、Video-MME-v2などの長尺動画理解ベンチマークで、Qwen3.5-35B-A3B、Qwen3-VL-235B-A22B、Gemini-3-Flashなどと比較している。図1ではActivityNet/QVHighlights/Charades-TimeLens、LongVideoBench、Video-MME-v2で強い性能を示すとされる。ただし詳細な評価節は今回のPDF抽出が17ページまでのため、表全体・全条件・統計的検証は本文抽出範囲では不明。
- **議論はある？**: 技術報告としてシステム・学習パイプラインの説明は厚いが、抽出範囲内ではデータの内部比率、decontaminationの厳密性、教師モデル依存、長尺動画での失敗例、商用APIモデルとの評価条件差の影響は十分には検証できない。PDF抽出テキスト上では、細かい数値・表・式にはレイアウト崩れがあるため断定は避けるべき。
- **次に読む/試すなら**: Hugging Faceのcheckpointを確認し、実際に256K級動画入力の推論コストとメモリを測る。TimeLens/LongVideoBenchで小規模再現を回し、フレームサンプリング条件を比較する。MOPDとVideo-RLのアブレーションが本文後半にあるか確認する。
- **キーワード**: `multimodal foundation model`, `long-video understanding`, `DeepSeek Sparse Attention`, `Mixture-of-Experts`, `on-policy distillation`, `agentic RL`

## 気になったこと

- GQA+DSAで「lossless 256K context」と呼ぶとき、視覚トークンの削減・索引化・top-k選択がどこまで情報を落としていない扱いなのか。
- MOPDの13教師はどの程度公開・再現可能なのか。教師が非公開なら、モデルcheckpointは出ても学習再現性は限定される。
- Video-RLは約31K video samplesとあるが、長尺動画能力の伸びがデータ由来かDSA由来かを切り分けるアブレーションを見たい。
- Agentic RLのCode/Tool/Search能力が、マルチモーダル入力を伴う実環境タスクでどれだけ効くのか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [kwai-keye-team2026-ga-kwai-keye-vl-2-0-technical-report-2691244c.md](../../chat/2026-06-12/kwai-keye-team2026-ga-kwai-keye-vl-2-0-technical-report-2691244c.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
