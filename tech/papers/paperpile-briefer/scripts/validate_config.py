# /// script
# requires-python = ">=3.11"
# ///
"""運用前に必要なローカル設定を検査する。"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    errors: list[str] = []
    export_path = os.environ.get("PAPERPILE_EXPORT_PATH", "")
    if not export_path:
        errors.append("PAPERPILE_EXPORT_PATH is not set")
    elif not Path(export_path).expanduser().exists():
        errors.append(f"PAPERPILE_EXPORT_PATH does not exist: {export_path}")

    sync_script = os.environ.get("PAPERPILE_SYNC_SCRIPT", "")
    if sync_script:
        sync_path = Path(sync_script).expanduser()
        if not sync_path.exists():
            errors.append(f"PAPERPILE_SYNC_SCRIPT does not exist: {sync_script}")
        elif not os.access(sync_path, os.X_OK):
            errors.append(f"PAPERPILE_SYNC_SCRIPT is not executable: {sync_script}")

    if shutil.which("uv") is None:
        errors.append("uv command is not found")
    if shutil.which("codex") is None:
        errors.append("codex command is not found")

    if os.environ.get("EXPORT_TO_OBSIDIAN", "false") == "true":
        obsidian_dir = os.environ.get("OBSIDIAN_EXPORT_DIR", "")
        if not obsidian_dir:
            errors.append("EXPORT_TO_OBSIDIAN=true but OBSIDIAN_EXPORT_DIR is not set")
        else:
            try:
                Path(obsidian_dir).expanduser().mkdir(parents=True, exist_ok=True)
            except OSError as exc:
                errors.append(f"Cannot create OBSIDIAN_EXPORT_DIR: {obsidian_dir} ({exc})")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        return 1

    print("[OK] Configuration looks usable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
