# Paperpile Brief 2026-06-12 - SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction

## 基本情報

- **タイトル**: SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction
- **著者**: Yuting Ning, Zhehao Zhang, Yash Kumar Lal, Boyu Gou, Junyi Li, Weitong Ruan, Chentao Ye, Rahul Gupta, Diyi Yang, Yu Su, Huan Sun
- **年 / venue**: 2026 / arXiv [cs.CL]
- **リンク**: https://arxiv.org/pdf/2606.02540 / Project: https://osu-nlp-group.github.io/SkillHarm / GitHub: https://github.com/OSU-NLP-Group/SkillHarm / Data: https://huggingface.co/datasets/osunlp/SkillHarm

## 落合陽一フォーマット

- **ひとことでいうと**: エージェントの「スキル」パッケージを攻撃面として捉え、単発実行だけでなくスキルの再利用・永続化まで含めた攻撃ベンチマーク SkillHarm と、自動攻撃構築パイプライン AutoSkillHarm を提案した論文。
- **先行研究と比べてどこがすごい？**: 既存の skill-based attack 評価は主に1セッション内の毒入りスキル実行に閉じていたが、本研究は Fixed-Payload Poisoning と Self-Mutating Poisoning の2シナリオで、クロスセッション再利用時の遅延発火を評価する。さらに、リスクを data pipeline / system environment / agent autonomy の3カテゴリ・12種類に整理し、879攻撃サンプル、71スキルを対象にしている。
- **技術や手法の肝はどこ？**: スキルを自然言語指示、参照資料、実行スクリプトを含む「信頼されやすい永続パッケージ」と見なし、そこに悪性ペイロードや自己変異フックを埋め込む点。AutoSkillHarm は natural-language harness で coding agent に攻撃対象選定、ペイロード設計、成功判定器生成、品質フィルタを実行させる。攻撃成功は LLM judge だけでなく、具体的な環境状態を検査する deterministic evaluator で測る。
- **どうやって有効だと検証した？**: Claude Code、Codex、Gemini CLI、OpenCode などのエージェントハーネス構成で、FPP と SMP の攻撃成功率を評価。PDF本文によれば、FPP は最大 86.3%、SMP は最大 69.3% の attack success rate を示した。さらに、失敗の多くが「防御に成功した」のではなく「毒入りファイルを読まなかった」ことに由来する可能性を分析し、skill scanner や defensive system prompt も十分ではないと報告している。
- **議論はある？**: 攻撃サンプルは自動生成されるため、実世界の攻撃多様性をどこまで代表しているかは検討余地がある。評価は特定のスキル集合、タスク環境、エージェントハーネスに依存するため、他のスキル流通基盤や権限モデルで同じ脆弱性が出るかは追加検証が必要。PDF抽出上、細かい表や付録の数値はレイアウト崩れがあり得るため断定しすぎない。
- **次に読む/試すなら**: 1. SkillHarm の GitHub と Hugging Face データセットを見て、攻撃サンプルと evaluator の実装を確認する。2. 自分の Codex/agent skill 運用で、スキルファイルの永続変更・外部通信・権限昇格を検出する最小テストを作る。3. 関連する SKILL-INJECT、PoisonedSkills、SkillSafetyBench と比較して、防御設計の共通失敗点を整理する。
- **キーワード**: `agent skills`, `prompt injection`, `skill poisoning`, `cross-session attack`, `benchmark`, `LLM agents`, `security`

## 気になったこと

- 自己変異型攻撃 SMP に対して、スキルディレクトリを read-only 化するだけでどの程度防げるのか。
- 「毒入りファイルを読まなかったから失敗」に見えるケースを、防御性能として数えるべきか、単なるタスク実行経路の偶然として扱うべきか。
- skill scanner が見逃した contextualized payload の具体例と、静的解析・実行時監査・権限分離のどれが効きやすいか。
- 公開スキルエコシステムで、インストール時レビュー、実行時 sandbox、スキル更新監査をどう組み合わせるべきか。

## そのまま聞ける質問

- この論文の主張で一番弱い仮定は？
- 実装に落とすなら最小再現実験は？
- 関連研究として追加で探すべきキーワードは？
---

## 追加で聞く

- Chat prompt: [ning2026-zq-skillharm-lifecycle-aware-skill-based-attacks-via-automated-9752702b.md](../../chat/2026-06-12/ning2026-zq-skillharm-lifecycle-aware-skill-based-attacks-via-automated-9752702b.md)
- モバイルではObsidian Mobileで上のchatファイルを開き、本文をChatGPT mobileへ貼る。
