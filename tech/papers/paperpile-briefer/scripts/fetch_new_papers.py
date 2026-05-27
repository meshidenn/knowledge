# /// script
# requires-python = ">=3.11"
# ///
"""
Paperpile export(JSON/BibTeX)から未処理の論文を抽出してraw JSONへ保存する。

状態ファイルはこのスクリプトでは更新しない。要約生成とpushが成功した後に
mark_processed.pyで確定することで、失敗時に論文を取り逃がさない。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from typing import Any


REFERENCE_LIST_KEYS = (
    "references",
    "items",
    "papers",
    "entries",
    "publications",
    "library",
)


def first_string(*values: Any) -> str:
    for value in values:
        if value is None:
            continue
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, (int, float)):
            return str(value)
    return ""


def normalize_authors(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, str):
        return [part.strip() for part in re.split(r"\s+and\s+|;", value) if part.strip()]
    if isinstance(value, list):
        authors: list[str] = []
        for author in value:
            if isinstance(author, str):
                if author.strip():
                    authors.append(author.strip())
            elif isinstance(author, dict):
                name = first_string(
                    author.get("name"),
                    author.get("fullName"),
                    " ".join(
                        part
                        for part in [
                            first_string(author.get("first"), author.get("given")),
                            first_string(author.get("last"), author.get("family")),
                        ]
                        if part
                    ),
                )
                if name:
                    authors.append(name)
        return authors
    return []


def flatten_reference_lists(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if not isinstance(data, dict):
        return []

    for key in REFERENCE_LIST_KEYS:
        value = data.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]

    candidates: list[dict[str, Any]] = []
    stack = [data]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            if first_string(current.get("title"), current.get("name")):
                candidates.append(current)
            stack.extend(current.values())
        elif isinstance(current, list):
            stack.extend(current)
    return candidates


def stable_id(ref: dict[str, Any]) -> str:
    explicit = first_string(
        ref.get("paperpileId"),
        ref.get("paperpile_id"),
        ref.get("id"),
        ref.get("key"),
        ref.get("citationKey"),
        ref.get("doi"),
        ref.get("DOI"),
        ref.get("arxivId"),
        ref.get("arxiv"),
    )
    if explicit:
        return explicit.lower()
    title = first_string(ref.get("title"), ref.get("name"))
    authors = "|".join(normalize_authors(ref.get("authors") or ref.get("author")))
    year = first_string(ref.get("year"), ref.get("published"), ref.get("date"))
    digest = hashlib.sha256(f"{title}|{authors}|{year}".encode()).hexdigest()[:16]
    return f"generated:{digest}"


def normalize_reference(ref: dict[str, Any]) -> dict[str, Any]:
    nested = ref.get("metadata") if isinstance(ref.get("metadata"), dict) else {}
    merged = {**nested, **ref}
    title = first_string(merged.get("title"), merged.get("name"))
    doi = first_string(merged.get("doi"), merged.get("DOI"))
    arxiv_id = first_string(merged.get("arxivId"), merged.get("arxiv"), merged.get("eprint"))
    url = first_string(merged.get("url"), merged.get("URL"), merged.get("link"))
    if not url and doi:
        url = f"https://doi.org/{doi}"
    if not url and arxiv_id:
        url = f"https://arxiv.org/abs/{arxiv_id}"

    return {
        "id": stable_id(merged),
        "title": title,
        "authors": normalize_authors(merged.get("authors") or merged.get("author")),
        "year": first_string(merged.get("year"), merged.get("publishedYear"), merged.get("date")),
        "venue": first_string(merged.get("journal"), merged.get("booktitle"), merged.get("venue"), merged.get("publisher")),
        "abstract": first_string(merged.get("abstract"), merged.get("summary")),
        "doi": doi,
        "arxiv_id": arxiv_id,
        "url": url,
        "added": first_string(merged.get("added"), merged.get("created"), merged.get("dateAdded"), merged.get("createdAt")),
        "source": "paperpile-export",
    }


def parse_json_export(path: Path) -> list[dict[str, Any]]:
    return [normalize_reference(ref) for ref in flatten_reference_lists(json.loads(path.read_text()))]


def parse_bibtex_export(path: Path) -> list[dict[str, Any]]:
    text = path.read_text()
    refs: list[dict[str, Any]] = []
    for match in re.finditer(r"@(?P<type>\w+)\s*\{\s*(?P<key>[^,]+),(?P<body>.*?)(?=\n@|\Z)", text, flags=re.S):
        fields: dict[str, str] = {"key": match.group("key").strip(), "entry_type": match.group("type")}
        for field in re.finditer(r"(?P<name>\w+)\s*=\s*(?P<value>\{(?:[^{}]|\{[^{}]*\})*\}|\"[^\"]*\"|[^,\n]+)", match.group("body"), flags=re.S):
            value = field.group("value").strip().rstrip(",").strip()
            if (value.startswith("{") and value.endswith("}")) or (value.startswith('"') and value.endswith('"')):
                value = value[1:-1]
            fields[field.group("name")] = re.sub(r"\s+", " ", value).strip()
        refs.append(normalize_reference(fields))
    return refs


def load_seen(path: Path) -> set[str]:
    if not path.exists():
        return set()
    data = json.loads(path.read_text())
    return set(data.get("seen_ids", []))


def load_export(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        refs = parse_json_export(path)
    elif suffix in {".bib", ".bibtex"}:
        refs = parse_bibtex_export(path)
    else:
        raise ValueError(f"Unsupported Paperpile export format: {path.suffix}")
    return [ref for ref in refs if ref["title"]]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", required=True, help="Paperpile JSON/BibTeX export path")
    parser.add_argument("--state", required=True, help="Seen-state JSON path")
    parser.add_argument("--output", required=True, help="Raw output JSON path")
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    export_path = Path(args.export).expanduser()
    state_path = Path(args.state).expanduser()
    output_path = Path(args.output).expanduser()

    if not export_path.exists():
        raise FileNotFoundError(f"PAPERPILE_EXPORT_PATH does not exist: {export_path}")

    refs = load_export(export_path)
    seen = load_seen(state_path)
    new_refs = [ref for ref in refs if ref["id"] not in seen]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            {
                "date": args.date,
                "source_export": str(export_path),
                "count": len(new_refs),
                "paper_ids": [ref["id"] for ref in new_refs],
                "papers": new_refs,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    print(f"[OK] Found {len(new_refs)} new papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
