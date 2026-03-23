---
_schema:
  entity_type: knowledge-note
  applies_to: notes/*.md
  required:
    - description
    - topics
  optional:
    - source
    - source_type
    - status
    - type
    - created
  enums:
    source_type:
      - paper
      - blog
      - x-post
      - experiment
      - book
    status:
      - processed
      - output-ready
      - archived
    type:
      - insight
      - pattern
      - tension
      - anti-pattern
      - question
  constraints:
    description:
      max_length: 200
      format: "タイトルを超えた情報を追加する1文（スコープ・メカニズム・含意）"
    topics:
      format: "Wikiリンクの配列（少なくとも1つ）"

description: ""
source: ""
source_type: paper
status: processed
topics: []
---

# {タイトルを散文命題として記述}

{本文: この知見が主張することとその根拠を書く。タイトルが命題、本文が論拠。}

---

Relevant Notes:
- [[関連知見]] — 関係のコンテキスト

Topics:
- [[テーママップへのリンク]]
