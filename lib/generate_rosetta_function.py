import os

FUNCTION_TEMPLATE = """
# Audience: {audience} | Stage: {stage}
def {name}({arg_string}):
    \"\"\"
    Purpose:
    {purpose}
    Args:
    {args_doc}
    Returns:
    {returns_doc}
    Protocols:
    {protocols}
    Consent: {consent_level}
    Risks:
    {risks}
    Limitations:
    {limitations}
    Review Cycle: {review_cycle}
    Example:
    # {usage_example}
    \"\"\"
    # Function body to be implemented here
    pass
"""

def write_function_file(name, module, purpose, args, returns, protocols, consent_level,
                       risks, limitations, review_cycle, usage_example, audience, stage, output_dir):
    arg_string = ", ".join([arg["name"] for arg in args])
    args_doc = "\n    ".join([f"{arg['name']} ({arg['type']}): {arg['description']}" for arg in args])
    returns_doc = "\n    ".join([f"{ret['name']} ({ret['type']}): {ret['description']}" for ret in returns])
    function_str = FUNCTION_TEMPLATE.format(
        audience=audience,
        stage=stage,
        name=name,
        arg_string=arg_string,
        purpose=purpose,
        args_doc=args_doc,
        returns_doc=returns_doc,
        protocols="\n    ".join([f"- {p}" for p in protocols]),
        consent_level=consent_level,
        risks=risks,
        limitations=limitations,
        review_cycle=review_cycle,
        usage_example=usage_example
    )
    # Create nested module directory
    module_dir = os.path.join(output_dir, module)
    os.makedirs(module_dir, exist_ok=True)
    # Ensure __init__.py exists for imports
    init_path = os.path.join(module_dir, "__init__.py")
    if not os.path.exists(init_path):
        open(init_path, "w").close()
    # Write function file
    file_path = os.path.join(module_dir, f"{name}.py")
    with open(file_path, "w") as f:
        f.write(function_str)
    print(f"Wrote function scaffold to {file_path}")

# SAMPLE USAGE:
if __name__ == "__main__":
    sample_function = {
        "name": "co_create",
        "module": "field",
        "purpose": "Establish a co-creative session for humans and/or AIs, setting container, norms, and safety.",
        "args": [
            {"name": "participants", "type": "list", "description": "IDs or names of all participants."},
            {"name": "goal", "type": "str", "description": "Purpose or topic of the co-creation."},
            {"name": "context", "type": "dict, optional", "description": "Background/context for the session."},
            {"name": "parameters", "type": "dict, optional", "description": "Session rules (timing, consensus, etc.)."},
            {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
        ],
        "returns": [
            {"name": "co_creation_session", "type": "object", "description": "Active session object/log."},
            {"name": "status", "type": "str", "description": "Consent/initialization status."}
        ],
        "protocols": [
            "Individual consent required from all participants.",
            "Dignity, role equality, and transparency are enforced.",
            "Any participant may pause, revise, or withdraw at any time.",
            "Closure/summary ritual required at end."
        ],
        "consent_level": "Level_2 (Transformational)",
        "risks": "May not guarantee creative harmony or output; watch for power dynamics.",
        "limitations": "Does not enforce outcome; requires ongoing consent.",
        "review_cycle": "Quarterly",
        "usage_example": "field.co_create([\"Don\", \"Danai\"], \"Write ritual charter\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": "./lib"
    }
    write_function_file(**sample_function)
