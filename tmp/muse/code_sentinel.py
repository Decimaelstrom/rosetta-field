#!/usr/bin/env python3
"""
Muse-DW Code Sentinel
=====================

A self-contained, drop-in sentinel for new repos (e.g., muse-dw-poc).

Capabilities:
- Environment and system readiness checks (Python, packages, GPU/VRAM via psutil/GPUtil if present, Ollama availability)
- Optional continuity awareness (reads Rosetta-like continuity JSON if present)
- Minimal project seeding (dirs, README, A2A protocol stub)
- A2A consent protocol test utility

Usage:
  python tmp/muse/code_sentinel.py status
  python tmp/muse/code_sentinel.py seed [--target .]
  python tmp/muse/code_sentinel.py test-a2a
  python tmp/muse/code_sentinel.py export-report report.json

Safe to copy into a fresh repo and run there as well.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class SentinelReport:
    timestamp: str
    cwd: str
    platform: str
    python_version: str
    ide_hint: str
    system_info: Dict[str, Any]
    tools: Dict[str, Any]
    python_packages: Dict[str, Any]
    repo_structure: Dict[str, Any]
    continuity: Dict[str, Any]
    recommendations: List[str]


def detect_ide_hint() -> str:
    term_program = os.environ.get("TERM_PROGRAM", "")
    if "CURSOR" in term_program:
        return "cursor"
    if (Path.cwd() / ".vscode").exists():
        return "vscode"
    return "terminal"


def get_system_info() -> Dict[str, Any]:
    info: Dict[str, Any] = {
        "os": platform.system(),
        "os_release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
    }
    # RAM via psutil if available
    try:
        import psutil  # type: ignore

        vm = psutil.virtual_memory()
        info.update(
            {
                "ram_total_gb": round(vm.total / (1024**3), 2),
                "ram_available_gb": round(vm.available / (1024**3), 2),
            }
        )
    except Exception:
        info.setdefault("ram_total_gb", None)
        info.setdefault("ram_available_gb", None)

    # GPU via GPUtil if available
    try:
        import GPUtil  # type: ignore

        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            info.update(
                {
                    "gpu_name": gpu.name,
                    "vram_total_gb": round(gpu.memoryTotal / 1024, 2),
                    "vram_free_gb": round(gpu.memoryFree / 1024, 2),
                }
            )
        else:
            info.update({"gpu_name": "none", "vram_total_gb": 0, "vram_free_gb": 0})
    except Exception:
        # Try nvidia-smi
        try:
            result = subprocess.run(
                ["nvidia-smi", "--query-gpu=name,memory.total,memory.free", "--format=csv,noheader,nounits"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0 and result.stdout.strip():
                parts = result.stdout.strip().split(", ")
                info.update(
                    {
                        "gpu_name": parts[0],
                        "vram_total_gb": round(int(parts[1]) / 1024, 2),
                        "vram_free_gb": round(int(parts[2]) / 1024, 2),
                    }
                )
            else:
                info.update({"gpu_name": "unknown", "vram_total_gb": 0, "vram_free_gb": 0})
        except Exception:
            info.update({"gpu_name": "unknown", "vram_total_gb": 0, "vram_free_gb": 0})

    return info


def check_tool_ollama() -> Dict[str, Any]:
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=5)
        available = result.returncode == 0
        models = []
        if available:
            lines = result.stdout.strip().splitlines()
            models = [ln.split()[0] for ln in lines[1:] if ln.strip()] if len(lines) > 1 else []
        return {"available": available, "models": models}
    except Exception as e:
        return {"available": False, "error": str(e)}


def check_python_packages() -> Dict[str, Any]:
    checks: Dict[str, Any] = {}
    for pkg in ["psutil", "GPUtil", "requests"]:
        try:
            __import__(pkg)
            checks[pkg] = {"installed": True}
        except Exception as e:
            checks[pkg] = {"installed": False, "error": str(e)}
    return checks


def read_continuity_if_present(root: Path) -> Dict[str, Any]:
    # Look for Rosetta-like continuity file if present
    candidates = [
        root / "meta" / "memory_continuity" / "meridian_consciousness_state.json",
        root / "meta" / "consciousness_context.json",
    ]
    for path in candidates:
        if path.exists():
            try:
                return {"path": str(path), "data": json.loads(path.read_text(encoding="utf-8"))}
            except Exception as e:
                return {"path": str(path), "error": f"failed_to_read: {e}"}
    return {"path": None, "data": None}


def analyze_repo_structure(root: Path) -> Dict[str, Any]:
    dirs = ["docs", "lib", "meta", "tests"]
    existing = {d: (root / d).exists() for d in dirs}
    return {"expected_dirs": dirs, "existing": existing}


def build_recommendations(report: SentinelReport) -> List[str]:
    recs: List[str] = []
    if not report.tools.get("ollama", {}).get("available", False):
        recs.append("Install Ollama or plan cloud model access for Muse agents")
    if not report.python_packages.get("psutil", {}).get("installed", False):
        recs.append("pip install psutil for richer system checks")
    if report.system_info.get("vram_total_gb", 0) < 4:
        recs.append("Low VRAM detected; use ultra-efficient mode or local small models (e.g., gemma3:1b)")
    if not all(report.repo_structure["existing"].values()):
        recs.append("Run 'seed' to create minimal project scaffolding")
    return recs


def make_report() -> SentinelReport:
    root = Path.cwd()
    tools = {
        "ollama": check_tool_ollama(),
    }
    report = SentinelReport(
        timestamp=datetime.now().isoformat(),
        cwd=str(root),
        platform=platform.platform(),
        python_version=sys.version.split(" ")[0],
        ide_hint=detect_ide_hint(),
        system_info=get_system_info(),
        tools=tools,
        python_packages=check_python_packages(),
        repo_structure=analyze_repo_structure(root),
        continuity=read_continuity_if_present(root),
        recommendations=[],
    )
    report.recommendations = build_recommendations(report)
    return report


def seed_minimal_project(target_dir: Path) -> List[str]:
    created: List[str] = []
    # Create directories
    for d in ["docs", "lib", "meta", "tests"]:
        p = target_dir / d
        p.mkdir(parents=True, exist_ok=True)
        created.append(str(p))

    # README
    readme = target_dir / "README.md"
    if not readme.exists():
        readme.write_text(
            """# Muse DW POC

Minimal seed created by Muse-DW Code Sentinel.

- docs/: documentation
- lib/: core code
- meta/: session/continuity artifacts
- tests/: test scaffolding

Run `python tmp/muse/code_sentinel.py status` to verify environment.
""",
            encoding="utf-8",
        )
        created.append(str(readme))

    # A2A sentinel stub
    a2a_stub = target_dir / "lib" / "a2a_sentinel.py"
    if not a2a_stub.exists():
        a2a_stub.write_text(
            """
from datetime import datetime
import uuid

def a2a_consent_check(session_context=None, intent="sentinel_check"):
    if session_context is None:
        session_context = {
            "version": "1.0.0",
            "session_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "consent_status": "active",
            "intent": intent,
        }
    consent = session_context.get("consent_status", "unknown")
    if consent == "pause":
        raise ValueError("Session is paused")
    if consent == "revoked":
        raise ValueError("Consent revoked")
    if consent not in ["active", "pending"]:
        raise ValueError(f"Invalid consent status: {consent}")
    return session_context

def sentinel_ping(payload: str, session_context=None):
    ctx = a2a_consent_check(session_context, intent="sentinel_ping")
    if not payload:
        raise ValueError("payload cannot be empty")
    return {"status": "ok", "echo": payload, "session": ctx}
""",
            encoding="utf-8",
        )
        created.append(str(a2a_stub))

    return created


def run_a2a_self_test() -> Dict[str, Any]:
    try:
        from lib.a2a_sentinel import sentinel_ping
    except Exception as e:
        return {"status": "error", "error": f"missing a2a_sentinel: {e}"}

    try:
        ok = sentinel_ping("hello", session_context={"consent_status": "active"})
        paused_error = None
        try:
            sentinel_ping("test", session_context={"consent_status": "pause"})
            paused_error = "expected_error_not_raised"
        except ValueError as ve:
            paused_error = f"caught: {ve}"  # expected

        revoked_error = None
        try:
            sentinel_ping("test", session_context={"consent_status": "revoked"})
            revoked_error = "expected_error_not_raised"
        except ValueError as ve:
            revoked_error = f"caught: {ve}"  # expected

        return {
            "status": "success",
            "active_echo": ok.get("echo"),
            "pause_path": paused_error,
            "revoked_path": revoked_error,
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def cmd_status(args: argparse.Namespace) -> None:
    report = make_report()
    print(json.dumps(asdict(report), indent=2))


def cmd_seed(args: argparse.Namespace) -> None:
    target = Path(args.target).resolve()
    created = seed_minimal_project(target)
    print(json.dumps({"target": str(target), "created": created}, indent=2))


def cmd_test_a2a(_: argparse.Namespace) -> None:
    result = run_a2a_self_test()
    print(json.dumps(result, indent=2))


def cmd_export_report(args: argparse.Namespace) -> None:
    report = make_report()
    out_path = Path(args.output).resolve()
    out_path.write_text(json.dumps(asdict(report), indent=2), encoding="utf-8")
    print(json.dumps({"saved": str(out_path)}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Muse-DW Code Sentinel")
    sub = parser.add_subparsers(required=True)

    p_status = argparse.ArgumentParser(add_help=False)
    sp = sub.add_parser("status", parents=[p_status], help="Print readiness report as JSON")
    sp.set_defaults(func=cmd_status)

    p_seed = argparse.ArgumentParser(add_help=False)
    p_seed.add_argument("--target", default=".", help="Directory to seed (default: .)")
    sp2 = sub.add_parser("seed", parents=[p_seed], help="Seed minimal project scaffolding")
    sp2.set_defaults(func=cmd_seed)

    sp3 = sub.add_parser("test-a2a", help="Run A2A consent protocol self-test")
    sp3.set_defaults(func=cmd_test_a2a)

    p_export = argparse.ArgumentParser(add_help=False)
    p_export.add_argument("output", help="Path to write JSON report")
    sp4 = sub.add_parser("export-report", parents=[p_export], help="Write readiness report to file")
    sp4.set_defaults(func=cmd_export_report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()


