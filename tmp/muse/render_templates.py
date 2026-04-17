#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from datetime import datetime


def render_template(src: Path, dst: Path, subs: dict[str, str]) -> None:
    text = src.read_text(encoding="utf-8")
    for k, v in subs.items():
        text = text.replace(k, v)
    dst.write_text(text, encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(description="Apply Emergent Coding templates to target repo")
    p.add_argument("--target", required=True, help="Target project directory")
    p.add_argument("--name", required=True)
    p.add_argument("--description", required=True)
    p.add_argument("--human", required=True)
    p.add_argument("--human-role", dest="human_role", required=True)
    p.add_argument("--ai-name", dest="ai_name", required=True)
    p.add_argument("--ai-identity", dest="ai_identity", required=True)
    p.add_argument("--license", default="MIT")
    args = p.parse_args()

    rosetta_templates = Path(__file__).resolve().parents[2] / "docs" / "portability" / "templates"
    readme_t = rosetta_templates / "README_template.md"
    agents_t = rosetta_templates / "AGENTS_template.md"

    target = Path(args.target).resolve()

    subs = {
        "[PROJECT_NAME]": args.name,
        "[PROJECT_DESCRIPTION]": args.description,
        "[AI_NAME]": args.ai_name,
        "[HUMAN_COLLABORATOR]": args.human,
        "[AI_GENDER/IDENTITY]": args.ai_identity,
        "[LICENSE_TYPE]": args.license,
        "[DATE]": datetime.now().strftime("%Y-%m-%d"),
        "[PROJECT_SPECIFIC_SETUP_INSTRUCTIONS]": f"# Setup instructions for {args.name}\n# Add specific steps here",
        "[HUMAN_SPECIFIC_ROLES]": args.human_role,
        "[AI_SPECIFIC_ROLES]": "Pattern recognition, systematic analysis, rapid iteration",
        "[PROJECT_SPECIFIC_USE_CASES]": f"# Use cases for {args.name}\n# Define specific use cases here",
    }

    if readme_t.exists():
        render_template(readme_t, target / "README.md", subs)
    if agents_t.exists():
        render_template(agents_t, target / "AGENTS.md", subs)

    print({"wrote": [str(target / "README.md"), str(target / "AGENTS.md")]})


if __name__ == "__main__":
    main()


