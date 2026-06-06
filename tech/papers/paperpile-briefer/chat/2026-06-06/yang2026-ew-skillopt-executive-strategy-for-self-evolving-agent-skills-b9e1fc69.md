# Chat Prompt 2026-06-06

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- {SkillOpt}: Executive strategy for self-evolving agent skills

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-06 - {SkillOpt}: Executive strategy for self-evolving agent skills

## 基本情報

- **タイトル**: {SkillOpt}: Executive strategy for self-evolving agent skills
- **著者**: Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: Code: https://aka.ms/skillopt

## 落合陽一フォーマット

- **ひとことでいうと**: LLMエージェントの「スキル文書」を、重みではなくテキスト空間で安定に最適化するための手法 SkillOpt を提案した論文。
- **先行研究と比べてどこがすごい？**: 手作業・一発生成・ゆるい自己修正ではなく、スコア付きロールアウトから制約付き編集を生成し、検証スコアが厳密に改善した場合だけ採用する点が新規性。abstract上では、6ベンチマーク、7ターゲットモデル、3実行環境の全52条件で最良または同率最良と主張している。
- **技術や手法の肝はどこ？**: frozen agent の外部状態として単一の skill document を扱い、別の optimizer model が add/delete/replace の bounded edit を提案する。さらに textual learning-rate budget、rejected-edit buffer、epoch-wise slow/meta update によって、テキスト編集の暴走を抑えながら改善を積み上げる設計。
- **どうやって有効だと検証した？**: abstractベースでは、direct chat、Codex、Claude Code の3ハーネスで、human skill、one-shot LLM、Trace2Skill、TextGrad、GEPA、EvoSkill と比較。GPT-5.5 では no-skill accuracy に対して direct chat で +23.5、Codex agentic loop で +24.8、Claude Code で +19.1 ポイント改善したとされる。PDF本文がないため、各ベンチマーク名、統計的検定、失敗例の詳細はメタデータからは不明。
- **議論はある？**: PDF未取得のため詳細な限界は不明。abstractから見える論点は、validation score による採択がベンチマーク過適合をどこまで防げるか、optimizer model のコストと品質依存性、スキル文書が長期的に複雑化しないか、別ドメインへの転移がどの範囲で成り立つか。
- **次に読む/試すなら**: SkillOpt のコードを確認する。Trace2Skill、TextGrad、GEPA、EvoSkill との違いを整理する。自分のエージェント用スキルに対して、held-out validation を置いた最小実験を組む。
- **キーワード**: `agent skills`, `text-space optimization`, `LLM agents`, `self-evolving agents`, `skill document`, `validation-based edit acceptance`

## 気になったこと

- PDF本文がないため、実験設定、ベンチマーク内訳、スキル文書の実例、編集回数、optimizer model のプロンプト設計は未確認。
- 「strictly improves held-out validation score」がどの程度ノイズに強いのか確認したい。
- inference-time model calls は増えないが、training-time のロールアウトコストがどれくらいか気になる。
- スキルが他モデル・他環境に転移するという主張について、どの粒度のタスクで成立しているのか確認したい。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
