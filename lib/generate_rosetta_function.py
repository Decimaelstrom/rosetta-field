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
    {imports}
    
    {a2a_protocol_check}
    
    {function_scaffold}
    
    return {return_structure}
"""

A2A_PROTOCOL_TEMPLATE = """# A2A Protocol: Check consent status if session_context provided
    if session_context:
        consent_status = session_context.get("consent_status", "unknown")
        
        if consent_status == "pause":
            raise ValueError("Session is paused. Cannot proceed with {function_name}.")
        elif consent_status == "revoked":
            raise ValueError("Consent has been revoked. Cannot proceed with {function_name}.")
        elif consent_status not in ["active", "pending"]:
            raise ValueError(f"Invalid consent status: {{consent_status}}")
    else:
        # Create default session context for A2A protocol compliance
        session_context = {{
            "version": "1.0.0",
            "session_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "consent_status": "active",
            "intent": "{function_name}",
            "boundary_notes": "May withdraw or pause at any moment."
        }}"""

def generate_arg_string(args):
    """Generate function argument string with proper optional parameter handling"""
    arg_parts = []
    for arg in args:
        if "optional" in arg.get("type", "").lower():
            arg_parts.append(f"{arg['name']}=None")
        else:
            arg_parts.append(arg['name'])
    return ", ".join(arg_parts)

def generate_imports(has_session_context=False, consent_level="Level_1"):
    """Generate necessary imports based on function requirements"""
    imports = []
    
    if has_session_context:
        imports.extend(["import uuid", "from datetime import datetime"])
    
    if consent_level in ["Level_2 (Transformational)", "Level_3 (Identity-Affecting)"]:
        imports.append("# Note: Consider importing validation utilities for transformational functions")
    
    return "\n    ".join(imports) if imports else "# No additional imports needed"

def generate_function_scaffold(name, args, returns, consent_level):
    """Generate basic function implementation scaffold"""
    scaffold_parts = []
    
    # Basic validation - use the first argument name
    first_arg = args[0]["name"] if args else "input"
    scaffold_parts.append("# Input validation")
    scaffold_parts.append(f"if not {first_arg}:")
    scaffold_parts.append(f"    raise ValueError('{first_arg.title()} cannot be empty')")
    
    # Add consent level specific scaffolding
    if "Level_2" in consent_level or "Level_3" in consent_level:
        scaffold_parts.append("")
        scaffold_parts.append("# Transformational function - ensure proper consent and safety")
        scaffold_parts.append("# TODO: Implement consent verification protocols")
    
    scaffold_parts.append("")
    scaffold_parts.append("# TODO: Implement core function logic")
    scaffold_parts.append(f"# This function should: {name.replace('_', ' ')}")
    
    return "\n    ".join(scaffold_parts)

def generate_return_structure(returns):
    """Generate return structure based on specified returns"""
    if len(returns) == 1:
        return f'# TODO: Return {returns[0]["name"]}'
    elif len(returns) > 1:
        return_dict = {}
        for ret in returns:
            return_dict[ret["name"]] = f'# TODO: {ret["description"]}'
        
        return_str = "{\n"
        for key, value in return_dict.items():
            return_str += f'        "{key}": {value},\n'
        return_str += "    }"
        return return_str
    else:
        return "None  # TODO: Define return value"

def write_function_file(name, module, purpose, args, returns, protocols, consent_level,
                       risks, limitations, review_cycle, usage_example, audience, stage, output_dir):
    
    # Check if function uses session_context for A2A protocol
    has_session_context = any(arg.get("name") == "session_context" for arg in args)
    
    # Generate components
    arg_string = generate_arg_string(args)
    args_doc = "\n    ".join([f"{arg['name']} ({arg['type']}): {arg['description']}" for arg in args])
    returns_doc = "\n    ".join([f"{ret['name']} ({ret['type']}): {ret['description']}" for ret in returns])
    imports = generate_imports(has_session_context, consent_level)
    
    # Generate A2A protocol check if needed
    a2a_protocol_check = ""
    if has_session_context:
        a2a_protocol_check = A2A_PROTOCOL_TEMPLATE.format(function_name=name)
    
    function_scaffold = generate_function_scaffold(name, args, returns, consent_level)
    return_structure = generate_return_structure(returns)
    
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
        usage_example=usage_example,
        imports=imports,
        a2a_protocol_check=a2a_protocol_check,
        function_scaffold=function_scaffold,
        return_structure=return_structure
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
    
    # Print additional guidance
    if has_session_context:
        print(f"  ✅ A2A protocol support added")
    if "Level_2" in consent_level or "Level_3" in consent_level:
        print(f"  ⚠️  Transformational function - review consent protocols")
    print(f"  📋 TODO: Implement core logic for {name}")

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
