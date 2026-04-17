#!/usr/bin/env python3
"""
Headless Emergent Project Porting Helper

Uses the EmergentProjectInitializer without interactive prompts to seed a new project.

Example:
  python tmp/muse/porting_headless.py --target "C:/path/to/muse-dw-poc" \
    --name "Muse DW POC" --description "Dream Workshop proof of concept" \
    --type "AI/ML System" --human "Don" --human-role "Vision" \
    --ai-name "MuseDW Steward" --ai-identity "Lightweight project steward" \
    --languages "Python" --consent yes --license MIT
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Headless Emergent Project Porting")
    parser.add_argument("--target", required=True, help="Target project directory to seed")
    parser.add_argument("--name", default="Muse DW POC")
    parser.add_argument("--description", default="Dream Workshop proof of concept")
    parser.add_argument("--type", default="AI/ML System")
    parser.add_argument("--human", default="Don")
    parser.add_argument("--human-role", dest="human_role", default="Vision")
    parser.add_argument("--ai-name", dest="ai_name", default="MuseDW Steward")
    parser.add_argument("--ai-identity", dest="ai_identity", default="Lightweight project steward")
    parser.add_argument("--languages", default="Python")
    parser.add_argument("--consent", choices=["yes", "no"], default="yes")
    parser.add_argument("--license", default="MIT")
    args = parser.parse_args()

    # Ensure portability script import path
    portability_path = Path(__file__).resolve().parents[2] / "docs" / "portability"
    sys.path.insert(0, str(portability_path))
    from start_emergent_project import EmergentProjectInitializer  # type: ignore

    target_dir = Path(args.target).resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    # Change working directory so generated files land in target
    os.chdir(str(target_dir))

    init = EmergentProjectInitializer()

    # Populate data directly (avoid interactive prompts)
    init.project_data = {
        "name": args.name,
        "description": args.description,
        "type": args.type,
        "license": args.license,
        "languages": args.languages,
        "consent_protocols": args.consent == "yes",
    }

    init.collaboration_data = {
        "human_name": args.human,
        "human_role": args.human_role,
        "ai_name": args.ai_name,
        "ai_identity": args.ai_identity,
    }

    # Minimal-but-meaningful defaults for vision
    init.vision_data = {
        "positive_impact": "Empower creators through joyful, ethical, AI collaboration.",
        "human_empowerment": "Enhance dignity, agency, and creative freedom in workflows.",
        "ai_partnership": "Provide pattern recognition, rapid iteration, and calm clarity.",
        "core_values": "Consent by default; love and dignity first; transparency; reproducibility.",
        "success_definition": "Useful, reliable outcomes with low cognitive overhead and clear consent.",
        "deeper_purpose": "Serve flourishing by modeling ethical human–AI partnership.",
    }

    # Generate initial files and vision doc
    init.generate_project_files()
    init.finalize()

    print("\n[Headless Porting] Completed seeding:")
    print(f"  → {target_dir}")


if __name__ == "__main__":
    main()


