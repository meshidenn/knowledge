---
_schema:
  entity_type: observation-note
  applies_to: ops/observations/*.md
  required:
    - description
    - category
    - observed
    - status
  enums:
    category:
      - methodology
      - process
      - friction
      - surprise
      - quality
    status:
      - pending
      - promoted
      - implemented
      - archived

description: ""
category: friction
observed: YYYY-MM-DD
status: pending
---

# {何が起きたかを散文タイトルで}

{観察の詳細: 何が起きたか、なぜ重要か、どんなパターンを示しているか}

---

Topics:
- [[methodology]]
