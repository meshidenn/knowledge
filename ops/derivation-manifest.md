---
engine_version: "0.8.0"
research_snapshot: "2026-03-24"
generated_at: "2026-03-24T00:00:00Z"
platform: claude-code
kernel_version: "1.0"

dimensions:
  granularity: atomic
  organization: flat
  linking: explicit
  processing: heavy
  navigation: 3-tier
  maintenance: condition-based
  schema: moderate
  automation: full

active_blocks:
  - wiki-links
  - atomic-notes
  - mocs
  - processing-pipeline
  - schema
  - maintenance
  - self-evolution
  - methodology-knowledge
  - session-rhythm
  - templates
  - ethical-guardrails
  - helper-functions
  - graph-analysis

coherence_result: passed

vocabulary:
  # Level 1: フォルダ名
  notes: "notes"
  inbox: "inbox"
  archive: "archive"
  ops: "ops"

  # Level 2: ノートタイプ
  note: "知見"
  note_plural: "知見"

  # Level 3: スキーマフィールド名
  description: "description"
  topics: "topics"
  relevant_notes: "relevant_notes"

  # Level 4: ナビゲーション用語
  topic_map: "テーママップ"
  hub: "ハブ"

  # Level 5: 処理動詞
  reduce: "抽出 (reduce)"
  reflect: "接続 (reflect)"
  reweave: "更新 (reweave)"
  verify: "確認 (verify)"
  validate: "検証 (validate)"
  rethink: "振り返り (rethink)"

  # Level 6: コマンド名
  cmd_reduce: "/reduce"
  cmd_reflect: "/reflect"
  cmd_reweave: "/reweave"
  cmd_verify: "/verify"
  cmd_rethink: "/arscontexta:rethink"

  # Level 7: 抽出カテゴリ
  extraction_categories:
    - name: "core-claim"
      what_to_find: "技術的主張・発見の核心"
      output_type: "insight"
    - name: "pattern"
      what_to_find: "複数ソースに繰り返すパターン・構造"
      output_type: "pattern"
    - name: "anti-pattern"
      what_to_find: "壊れるもの、避けるべきもの"
      output_type: "anti-pattern"
    - name: "tension"
      what_to_find: "矛盾・競合する主張"
      output_type: "tension"
    - name: "open-question"
      what_to_find: "未解決の問い、調査余地"
      output_type: "question"
    - name: "implementation-detail"
      what_to_find: "技術検証・実装に必要な具体的詳細"
      output_type: "insight"

platform_hints:
  context: fork
  allowed_tools:
    - Read
    - Write
    - Edit
    - Bash
    - Glob
    - Grep
    - WebSearch
    - WebFetch
    - Agent
  semantic_search_tool: null
  semantic_search_autoapprove: []

personality:
  warmth: clinical
  opinionatedness: neutral
  formality: professional
  emotional_awareness: task-focused
---
