import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("fetch_new_papers", ROOT / "scripts" / "fetch_new_papers.py")
fetch_new_papers = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(fetch_new_papers)

INDEX_SPEC = importlib.util.spec_from_file_location("update_index", ROOT / "scripts" / "update_index.py")
update_index = importlib.util.module_from_spec(INDEX_SPEC)
assert INDEX_SPEC.loader is not None
INDEX_SPEC.loader.exec_module(update_index)

BOOTSTRAP_SPEC = importlib.util.spec_from_file_location("bootstrap_seen", ROOT / "scripts" / "bootstrap_seen.py")
bootstrap_seen = importlib.util.module_from_spec(BOOTSTRAP_SPEC)
assert BOOTSTRAP_SPEC.loader is not None
BOOTSTRAP_SPEC.loader.exec_module(bootstrap_seen)


class FetchNewPapersTest(unittest.TestCase):
    def test_extracts_new_references_from_json_export(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            export = tmp_path / "paperpile.json"
            state = tmp_path / "seen.json"
            output = tmp_path / "raw.json"
            export.write_text(
                json.dumps(
                    {
                        "references": [
                            {"id": "a", "title": "A Paper", "authors": [{"first": "Ada", "last": "Lovelace"}], "doi": "10.1/a"},
                            {"id": "b", "title": "B Paper", "author": "Grace Hopper and Alan Kay", "arxiv": "2401.00001"},
                        ]
                    }
                )
            )
            state.write_text(json.dumps({"seen_ids": ["a"]}))

            refs = fetch_new_papers.load_export(export)
            seen = fetch_new_papers.load_seen(state)
            new_refs = [ref for ref in refs if ref["id"] not in seen]
            output.write_text(json.dumps({"count": len(new_refs), "papers": new_refs}))

            data = json.loads(output.read_text())
            self.assertEqual(data["count"], 1)
            self.assertEqual(data["papers"][0]["title"], "B Paper")
            self.assertEqual(data["papers"][0]["authors"], ["Grace Hopper", "Alan Kay"])
            self.assertEqual(data["papers"][0]["url"], "https://arxiv.org/abs/2401.00001")

    def test_parses_basic_bibtex_export(self):
        with tempfile.TemporaryDirectory() as tmp:
            export = Path(tmp) / "paperpile.bib"
            export.write_text(
                """@article{smith2024,
  title={Interesting Paper},
  author={Smith, Jane and Doe, John},
  year={2024},
  doi={10.1234/example}
}
"""
            )

            refs = fetch_new_papers.load_export(export)

            self.assertEqual(len(refs), 1)
            self.assertEqual(refs[0]["title"], "Interesting Paper")
            self.assertEqual(refs[0]["url"], "https://doi.org/10.1234/example")

    def test_collects_pdf_paths_from_export_attachments(self):
        ref = fetch_new_papers.normalize_reference(
            {
                "id": "a",
                "title": "PDF Paper",
                "attachments": [
                    {"path": "/papers/a.pdf"},
                    {"filePath": "/papers/supplement.txt"},
                    {"localPath": "~/Paperpile/b.pdf"},
                ],
            }
        )

        self.assertEqual(ref["pdf_paths"], ["/papers/a.pdf", "~/Paperpile/b.pdf"])

    def test_updates_readable_index_and_latest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            briefs = root / "briefs"
            chat = root / "chat"
            briefs.mkdir()
            chat.mkdir()
            (briefs / "2026-05-27.md").write_text("# Paperpile Daily Brief 2026-05-27\n")
            (briefs / "2026-05-28.md").write_text("# Paperpile Daily Brief 2026-05-28\n")
            (chat / "2026-05-28.md").write_text("# Chat Prompt\n")

            index = update_index.build_index(briefs, chat, 30)

            self.assertIn("[Paperpile Daily Brief 2026-05-28](2026-05-28.md)", index)
            self.assertIn("[chat](../chat/2026-05-28.md)", index)

    def test_bootstrap_seen_writes_existing_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            export = root / "paperpile.json"
            state = root / "state" / "seen.json"
            export.write_text(json.dumps({"references": [{"id": "a", "title": "A"}, {"id": "b", "title": "B"}]}))

            refs = bootstrap_seen.fetch_new_papers.load_export(export)
            state.parent.mkdir(parents=True)
            state.write_text(json.dumps({"seen_ids": sorted(ref["id"] for ref in refs)}))

            data = json.loads(state.read_text())
            self.assertEqual(data["seen_ids"], ["a", "b"])


if __name__ == "__main__":
    unittest.main()
