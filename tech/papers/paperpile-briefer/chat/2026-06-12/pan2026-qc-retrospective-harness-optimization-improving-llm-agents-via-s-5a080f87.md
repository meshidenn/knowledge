# Chat Prompt 2026-06-12

以下のPaperpile Daily Briefについて、追加で質問したいです。

## 対象論文

- Retrospective Harness Optimization: Improving {LLM} agents via self-preference over trajectory rollouts

## 質問したいこと

- 最初に読むべき論文を1本選んで、理由を教えて。
- 実装・検証に落とすなら、最小の再現実験は何？
- 関連研究を探すためのキーワードを5個出して。

## Brief

# Paperpile Brief 2026-06-12 - Retrospective Harness Optimization: Improving LLM agents via self-preference over trajectory rollouts

## 基本情報

- **タイトル**: Retrospective Harness Optimization: Improving LLM agents via self-preference over trajectory rollouts
- **著者**: Wenbo Pan, Shujie Liu, Chin-Yew Lin, Jingying Zeng, Xianfeng Tang, Xiangyang Zhou, Yan Lu, Xiaohua Jia
- **年 / venue**: 2026 / arXiv [cs.AI]
- **リンク**: https://arxiv.org/pdf/2606.05922 / arXiv:2606.05922v2 / code: https://github.com/wbopan/retro-harness / project: https://paper-rho.wenbo.io

## 落合陽一フォーマット

- **ひとことでいうと**: LLMエージェントの過去の実行軌跡だけを使い、検証ラベルなしでスキル・ツール・指示からなる「harness」を自己改善する RHO を提案した論文。
- **先行研究と比べてどこがすごい？**: OPRO、DSPy、TextGrad、ADAS、Meta-Harness などは基本的に検証セットやスコアを使うが、RHO はラベルなしの過去軌跡だけで単発の retrospective pass を行う。Dynamic Cheatsheet や ReasoningBank のような経験ベース手法が主にメモリやスキル文面を扱うのに対し、RHO はツール・スキル・指示を含むフル harness を更新する点が差分。SWE-Bench Pro では Vanilla Codex の pass rate 0.59 から RHO で 0.78 へ改善したと報告している。
- **技術や手法の肝はどこ？**: 3段階のパイプライン。まず過去軌跡から難しく多様なタスクを DPP で coreset 選択する。次に各タスクを複数回解き直し、各軌跡内の失敗をみる self-validation と、軌跡間の不一致をみる self-consistency で改善指示を抽出する。最後に複数の候補 harness を生成し、元 harness との軌跡比較を自己選好でペアワイズ評価して、正の改善がある候補だけを採用する。
- **どうやって有効だと検証した？**: Codex エージェントをベースに、ソフトウェア工学、技術作業、知識作業の3領域で評価。本文の表では SWE-Bench Pro が 0.59→0.78、Terminal-Bench 2 が 0.71→0.76、GAIA-2 が 0.29→0.37 とされ、Dynamic Cheatsheet、ReasoningBank、Sleep-time Compute より大きい改善を示した。PDF本文にはアブレーションや長期セッションでの行動変化分析も含まれるが、抽出テキスト由来なので細かい数値は断定しすぎない。
- **議論はある？**: 最大の仮定は、モデルの自己評価・自己選好が実際のタスク成功率と十分相関すること。ラベルなしで改善できるのは強いが、自己選好が同じモデルの盲点を増幅する可能性がある。また、過去軌跡の分布が将来タスクを代表しない場合、coreset 選択や harness 更新が局所最適化になる。実行コストも、coreset の複数ロールアウトと候補 harness の再解決が必要で軽くはない。
- **次に読む/試すなら**: 自分の Codex/エージェント運用ログで、失敗軌跡を3本ずつ再実行して self-validation / self-consistency の診断プロンプトだけ試す。RHO の GitHub 実装を読み、harness が実際にどのファイル単位で更新されるか確認する。比較対象として Meta-Harness、Dynamic Cheatsheet、ReasoningBank を読む。
- **キーワード**: `LLM agents`, `harness optimization`, `self-preference`, `self-supervised optimization`, `trajectory rollouts`, `DPP coreset`, `self-validation`, `self-consistency`, `SWE-Bench`

## 気になったこと

- 自己選好の ranker が失敗を見抜けないタスク、たとえば仕様理解や外部事実確認でどれくらい破綻するか。
- harness 更新が「汎用的な改善」ではなく、coreset に含まれたタスクへの過適合になっていないかをどう検出するか。
- 実装上は、軌跡ログから chain-of-thought 相当をどこまで扱う前提なのか、また商用環境で保存・再利用できるログ粒度はどの程度か。
- DPP による difficulty/diversity 選択と、単純な失敗率上位サンプリングの差が実運用でどれくらい効くか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
