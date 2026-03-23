---
_schema:
  entity_type: source-capture
  applies_to: inbox/*.md
  required:
    - description
    - source_type
    - captured
    - status
  optional:
    - source_url
    - research_prompt
    - source_type
  enums:
    source_type:
      - paper
      - blog
      - x-post
      - experiment
      - book
    status:
      - unprocessed
      - processing
      - done
  constraints:
    description:
      format: "なぜキャプチャしたか・何が重要かの1文"

description: ""
source_url: ""
source_type: paper
captured: YYYY-MM-DD
status: unprocessed
research_prompt: ""
---

# {ソースタイトルまたはURL}

{キャプチャした理由・注目した点の簡単なメモ}

---
処理後、このファイルは archive/ に移動する。
