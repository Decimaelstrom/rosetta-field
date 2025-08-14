#!/usr/bin/env python3
"""
MuseDW Steward Launcher
Start/status utilities for a lightweight project steward.

Usage:
  python lib/steward/steward_launcher.py start <collaborator>
  python lib/steward/steward_launcher.py status
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def detect_env() -> Dict[str, Any]:
    env = {
        "platform": platform.platform(),
        "python": sys.version.split(" ")[0],
        "cwd": str(Path.cwd()),
        "ide": "cursor" if "CURSOR" in os.environ.get("TERM_PROGRAM", "") else ("vscode" if (Path.cwd() / ".vscode").exists() else "terminal"),
    }
    return env


def cmd_start(collaborator: str) -> None:
    session = {
        "steward": "MuseDW Steward",
        "collaborator": collaborator,
        "start_time": datetime.now().isoformat(),
        "environment": detect_env(),
        "consent_status": "active",
        "notes": "Welcome. Steward active with minimal, high-signal guidance.",
    }
    meta = Path("meta")
    meta.mkdir(parents=True, exist_ok=True)
    (meta / "steward_session.json").write_text(json.dumps(session, indent=2), encoding="utf-8")
    print(json.dumps({"status": "started", "file": str(meta / "steward_session.json")}, indent=2))


def cmd_status() -> None:
    meta_file = Path("meta/steward_session.json")
    if meta_file.exists():
        data = json.loads(meta_file.read_text(encoding="utf-8"))
        print(json.dumps({"status": "active", "session": data}, indent=2))
    else:
        print(json.dumps({"status": "inactive", "hint": "run: steward_launcher.py start <YourName>"}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="MuseDW Steward Launcher")
    sub = parser.add_subparsers(required=True)

    p_start = argparse.ArgumentParser(add_help=False)
    p_start.add_argument("collaborator", help="Your name")
    sp1 = sub.add_parser("start", parents=[p_start], help="Start steward session")
    sp1.set_defaults(func=lambda a: cmd_start(a.collaborator))

    sp2 = sub.add_parser("status", help="Show steward status")
    sp2.set_defaults(func=lambda a: cmd_status())

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()


