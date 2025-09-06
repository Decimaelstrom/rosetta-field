#!/usr/bin/env python3
"""
MuseDW Steward Continuity (optional)
Reads IDE/workspace continuity if present (Cursor/VSCode state), writes a compact snapshot.
Safe to run even if no IDE state is present.
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict


def try_read_cursor_state() -> Dict[str, Any]:
    root = Path.home() / "AppData" / "Roaming" / "Cursor" / "User" / "workspaceStorage"
    if not root.exists():
        return {"found": False}
    # Heuristic: pick newest workspace/state.vscdb.backup or workspace.json if present
    candidates = sorted(root.glob("**/workspace.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        return {"found": False}
    latest = candidates[0]
    try:
        data = json.loads(latest.read_text(encoding="utf-8"))
        return {"found": True, "workspace_json": str(latest), "sample": list(data.keys())[:10]}
    except Exception as e:
        return {"found": False, "error": str(e)}


def main() -> None:
    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "cursor": try_read_cursor_state(),
    }
    out_dir = Path("meta")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "steward_continuity.json"
    out_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
    print(json.dumps({"saved": str(out_path)}, indent=2))


if __name__ == "__main__":
    main()


