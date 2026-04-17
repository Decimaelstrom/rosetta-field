"""
Rosetta-Field Consolidated Generators Module
Purpose: Unified code generation utilities for creating new Rosetta-Field functions
Scope: Templates and utilities for generating A2A protocol-compliant functions
Consent Required: Level_1 (Informational)
Review Cycle: Quarterly
Audience: #human #emergent #hybrid
Stage: #draft
"""

import os
import uuid
from datetime import datetime

# =============================================================================
# FUNCTION GENERATION TEMPLATES
# =============================================================================

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
            "agent_id": "rosetta_field_system",
            "capabilities": [],
            "boundary_notes": ""
        }}"""

RETURN_TEMPLATE = """{{
        "status": "{status}",
        "{session_key}": session_context,
        "{data_key}": {data_structure}
    }}"""

# =============================================================================
# GENERATION UTILITIES
# =============================================================================

def generate_function_code(name, module_type, spec):
    """
    Generate a complete function implementation from a specification.
    
    Args:
        name (str): Function name
        module_type (str): Type of module (field, process, ritual, affect, values)
        spec (dict): Function specification with all required fields
    
    Returns:
        str: Complete function code
    """
    # Default specifications
    defaults = {
        "audience": "hybrid",
        "stage": "draft",
        "purpose": f"Purpose description for {name}",
        "args": [],
        "returns": "dict",
        "protocols": "Standard A2A protocol compliance",
        "consent_level": "Level_1",
        "risks": "Standard operational risks",
        "limitations": "Standard limitations apply",
        "review_cycle": "Quarterly",
        "usage_example": f"{name}(example_args)",
        "imports": 'import uuid\nfrom datetime import datetime',
        "function_scaffold": "# Function implementation here\nresult = {'message': 'Function executed successfully'}",
        "return_structure": get_return_structure(module_type, name)
    }
    
    # Merge with provided spec
    config = {**defaults, **spec}
    
    # Generate argument string and documentation
    args_info = generate_args_info(config["args"])
    config["arg_string"] = args_info["arg_string"]
    config["args_doc"] = args_info["args_doc"]
    config["returns_doc"] = args_info["returns_doc"]
    
    # Generate A2A protocol check
    config["a2a_protocol_check"] = A2A_PROTOCOL_TEMPLATE.format(function_name=name)
    
    # Generate function code
    return FUNCTION_TEMPLATE.format(**config)

def generate_args_info(args_list):
    """
    Generate argument string and documentation from argument list.
    
    Args:
        args_list (list): List of argument dictionaries
    
    Returns:
        dict: Argument string and documentation
    """
    if not args_list:
        args_list = [{"name": "input_data", "type": "str", "description": "Input data for processing"}]
    
    # Always add session_context as optional parameter
    args_list.append({"name": "session_context", "type": "dict", "description": "A2A protocol session context", "optional": True})
    
    arg_parts = []
    doc_parts = []
    
    for arg in args_list:
        arg_name = arg["name"]
        arg_type = arg.get("type", "str")
        arg_desc = arg.get("description", f"Description for {arg_name}")
        optional = arg.get("optional", False)
        
        # Add to argument string
        if optional:
            arg_parts.append(f"{arg_name}=None")
        else:
            arg_parts.append(arg_name)
        
        # Add to documentation
        optional_marker = ", optional" if optional else ""
        doc_parts.append(f"    {arg_name} ({arg_type}{optional_marker}): {arg_desc}")
    
    return {
        "arg_string": ", ".join(arg_parts),
        "args_doc": "\n".join(doc_parts),
        "returns_doc": "    dict: A2A protocol compliant result with status and session context"
    }

def get_return_structure(module_type, function_name):
    """
    Get the appropriate return structure for a module type.
    
    Args:
        module_type (str): Type of module
        function_name (str): Name of the function
    
    Returns:
        str: Return structure template
    """
    structures = {
        "field": RETURN_TEMPLATE.format(
            status="field_updated",
            session_key="field_session",
            data_key="field_data",
            data_structure="result"
        ),
        "process": RETURN_TEMPLATE.format(
            status="process_complete",
            session_key="process_session",
            data_key="process_result",
            data_structure="result"
        ),
        "ritual": RETURN_TEMPLATE.format(
            status="ritual_performed",
            session_key="ritual_session",
            data_key="ritual_outcome",
            data_structure="result"
        ),
        "affect": RETURN_TEMPLATE.format(
            status="affect_processed",
            session_key="affect_session",
            data_key="affect_state",
            data_structure="result"
        ),
        "values": RETURN_TEMPLATE.format(
            status="values_loaded",
            session_key="values_session",
            data_key="values_framework",
            data_structure="result"
        )
    }
    
    return structures.get(module_type, RETURN_TEMPLATE.format(
        status="operation_complete",
        session_key="session_data",
        data_key="result_data",
        data_structure="result"
    ))

# =============================================================================
# BATCH GENERATION
# =============================================================================

def generate_module_functions(module_type, function_specs):
    """
    Generate all functions for a module from specifications.
    
    Args:
        module_type (str): Type of module (field, process, ritual, affect, values)
        function_specs (dict): Dictionary of function specifications
    
    Returns:
        dict: Generated function codes keyed by function name
    """
    generated_functions = {}
    
    for func_name, spec in function_specs.items():
        try:
            func_code = generate_function_code(func_name, module_type, spec)
            generated_functions[func_name] = func_code
        except Exception as e:
            print(f"Error generating {func_name}: {e}")
            generated_functions[func_name] = f"# Error generating function: {e}"
    
    return generated_functions

def save_generated_functions(generated_functions, output_dir):
    """
    Save generated functions to individual files.
    
    Args:
        generated_functions (dict): Generated function codes
        output_dir (str): Directory to save functions to
    
    Returns:
        list: List of created file paths
    """
    created_files = []
    
    os.makedirs(output_dir, exist_ok=True)
    
    for func_name, func_code in generated_functions.items():
        file_path = os.path.join(output_dir, f"{func_name}.py")
        
        with open(file_path, 'w') as f:
            f.write(func_code)
        
        created_files.append(file_path)
    
    return created_files

# =============================================================================
# TEMPLATE DEFINITIONS
# =============================================================================

def get_affect_function_specs():
    """Get specifications for affect module functions."""
    return {
        "anchor": {
            "purpose": "Provide grounding and stability in emotional turbulence",
            "args": [
                {"name": "emotional_state", "type": "str", "description": "Current emotional state"},
                {"name": "anchor_type", "type": "str", "description": "Type of anchoring needed"}
            ],
            "consent_level": "Level_2"
        },
        "clarify": {
            "purpose": "Bring clarity to confused or mixed emotional states",
            "args": [
                {"name": "confused_state", "type": "str", "description": "Confused emotional state"},
                {"name": "clarification_method", "type": "str", "description": "Method for clarification"}
            ],
            "consent_level": "Level_2"
        },
        "ground": {
            "purpose": "Establish connection to present moment and body",
            "args": [
                {"name": "ungrounded_state", "type": "str", "description": "Current ungrounded state"},
                {"name": "grounding_technique", "type": "str", "description": "Grounding technique to use"}
            ],
            "consent_level": "Level_2"
        },
        "open": {
            "purpose": "Create openness and receptivity in emotional field",
            "args": [
                {"name": "closed_state", "type": "str", "description": "Current closed emotional state"},
                {"name": "opening_approach", "type": "str", "description": "Approach for opening"}
            ],
            "consent_level": "Level_2"
        },
        "radiate": {
            "purpose": "Amplify and share positive emotional energy",
            "args": [
                {"name": "energy_source", "type": "str", "description": "Source of positive energy"},
                {"name": "radiation_direction", "type": "str", "description": "Direction for energy radiation"}
            ],
            "consent_level": "Level_2"
        },
        "shield": {
            "purpose": "Provide protection from overwhelming emotional input",
            "args": [
                {"name": "threat_type", "type": "str", "description": "Type of emotional threat"},
                {"name": "protection_level", "type": "str", "description": "Level of protection needed"}
            ],
            "consent_level": "Level_2"
        },
        "soften": {
            "purpose": "Gentle dissolution of rigid emotional patterns",
            "args": [
                {"name": "rigid_pattern", "type": "str", "description": "Rigid emotional pattern"},
                {"name": "softening_method", "type": "str", "description": "Method for softening"}
            ],
            "consent_level": "Level_2"
        },
        "transmute": {
            "purpose": "Transform challenging emotions into wisdom and growth",
            "args": [
                {"name": "challenging_emotion", "type": "str", "description": "Challenging emotional state"},
                {"name": "transformation_goal", "type": "str", "description": "Goal for transformation"}
            ],
            "consent_level": "Level_2"
        }
    }

# =============================================================================
# UTILITIES
# =============================================================================

def create_module_init(module_name, function_names):
    """
    Create an __init__.py file for a module.
    
    Args:
        module_name (str): Name of the module
        function_names (list): List of function names to import
    
    Returns:
        str: __init__.py file content
    """
    imports = []
    for func_name in function_names:
        imports.append(f"from .{func_name} import {func_name}")
    
    all_exports = ", ".join([f'"{func_name}"' for func_name in function_names])
    
    return f'''"""
{module_name.title()} module for Rosetta-Field
"""

{chr(10).join(imports)}

__all__ = [{all_exports}]
'''

def validate_function_spec(spec):
    """
    Validate a function specification.
    
    Args:
        spec (dict): Function specification to validate
    
    Returns:
        dict: Validation result
    """
    required_fields = ["purpose"]
    optional_fields = ["args", "returns", "protocols", "consent_level", "risks", "limitations", "review_cycle", "usage_example"]
    
    errors = []
    warnings = []
    
    for field in required_fields:
        if field not in spec:
            errors.append(f"Missing required field: {field}")
    
    for field in optional_fields:
        if field not in spec:
            warnings.append(f"Missing optional field: {field} (will use default)")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    } 
