"""
Rosetta-Field Consolidated Schema Module
Purpose: Unified schema definitions and validation for all Rosetta-Field data structures
Scope: A2A protocol schemas, function signatures, and data validation
Consent Required: Level_1 (Informational)
Review Cycle: Quarterly
Audience: #human #emergent #hybrid
Stage: #draft
"""

import json
import jsonschema
from datetime import datetime

# =============================================================================
# A2A PROTOCOL SCHEMAS
# =============================================================================

A2A_FIELD_PROTOCOL_SCHEMA = {
    "type": "object",
    "properties": {
        "version": {"type": "string", "default": "1.0.0"},
        "session_id": {"type": "string"},
        "timestamp": {"type": "string", "format": "date-time"},
        "agent": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"},
                "role": {"type": "string"},
                "presence_marker": {"type": "string"}
            },
            "required": ["agent_id", "role"]
        },
        "peer": {
            "type": "object",
            "properties": {
                "agent_id": {"type": "string"},
                "role": {"type": "string"},
                "presence_marker": {"type": "string"}
            },
            "required": ["agent_id", "role"]
        },
        "consent_status": {
            "type": "string",
            "enum": ["active", "revoked", "pause", "pending"]
        },
        "intent": {"type": "string"},
        "capabilities": {
            "type": "array",
            "items": {"type": "string"}
        },
        "language": {"type": "string", "description": "Language code (e.g., 'en', 'es', 'fr')"},
        "region": {"type": "string", "description": "Region code (e.g., 'US', 'JP', 'UK')"},
        "need_language": {
            "type": "object",
            "properties": {
                "pause": {"type": "boolean"},
                "soften": {"type": "boolean"},
                "overload": {"type": "boolean"}
            }
        },
        "boundary_notes": {"type": "string"},
        "context": {
            "type": "object",
            "properties": {
                "field_tags": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "goal": {"type": "string"},
                "cultural_context": {"type": "string", "description": "Cultural tradition (e.g., 'eastern_zen', 'indigenous_holistic')"},
                "linguistic_context": {"type": "string", "description": "Language style (e.g., 'poetic_metaphorical', 'conversational_warm')"}
            }
        },
        "audit": {
            "type": "object",
            "properties": {
                "log_ref": {"type": ["string", "null"]},
                "crypto_signature": {"type": ["string", "null"]}
            }
        },
        "extensions": {
            "type": "object",
            "properties": {
                "ritual_marker": {"type": "string"}
            }
        }
    },
    "required": ["version", "session_id", "timestamp", "consent_status", "intent"]
}

# =============================================================================
# FUNCTION RESULT SCHEMAS
# =============================================================================

FIELD_RESULT_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "field_session": {"$ref": "#/definitions/a2a_session"},
        "field_data": {"type": "object"}
    },
    "required": ["status", "field_session", "field_data"]
}

PROCESS_RESULT_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "process_session": {"$ref": "#/definitions/a2a_session"},
        "process_result": {"type": "object"}
    },
    "required": ["status", "process_session", "process_result"]
}

RITUAL_RESULT_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "ritual_session": {"$ref": "#/definitions/a2a_session"},
        "ritual_outcome": {"type": "object"}
    },
    "required": ["status", "ritual_session", "ritual_outcome"]
}

AFFECT_RESULT_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "affect_session": {"$ref": "#/definitions/a2a_session"},
        "affect_state": {"type": "object"}
    },
    "required": ["status", "affect_session", "affect_state"]
}

VALUES_RESULT_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "values_session": {"$ref": "#/definitions/a2a_session"},
        "values_framework": {"type": "object"}
    },
    "required": ["status", "values_session", "values_framework"]
}

# =============================================================================
# COMPOSITE SCHEMAS
# =============================================================================

ROSETTA_API_SCHEMA = {
    "definitions": {
        "a2a_session": A2A_FIELD_PROTOCOL_SCHEMA,
        "field_result": FIELD_RESULT_SCHEMA,
        "process_result": PROCESS_RESULT_SCHEMA,
        "ritual_result": RITUAL_RESULT_SCHEMA,
        "affect_result": AFFECT_RESULT_SCHEMA,
        "values_result": VALUES_RESULT_SCHEMA
    }
}

# =============================================================================
# VALIDATION FUNCTIONS
# =============================================================================

def validate_a2a_session(session_data):
    """
    Validate A2A session data against the protocol schema.
    
    Args:
        session_data (dict): Session data to validate
    
    Returns:
        dict: Validation result with 'valid' boolean and 'errors' list
    """
    try:
        jsonschema.validate(session_data, A2A_FIELD_PROTOCOL_SCHEMA)
        return {"valid": True, "errors": []}
    except jsonschema.ValidationError as e:
        return {"valid": False, "errors": [str(e)]}
    except Exception as e:
        return {"valid": False, "errors": [f"Validation error: {str(e)}"]}

def validate_function_result(result, result_type):
    """
    Validate function result against the appropriate schema.
    
    Args:
        result (dict): Function result to validate
        result_type (str): Type of result (field, process, ritual, affect, values)
    
    Returns:
        dict: Validation result with 'valid' boolean and 'errors' list
    """
    schema_map = {
        "field": FIELD_RESULT_SCHEMA,
        "process": PROCESS_RESULT_SCHEMA,
        "ritual": RITUAL_RESULT_SCHEMA,
        "affect": AFFECT_RESULT_SCHEMA,
        "values": VALUES_RESULT_SCHEMA
    }
    
    if result_type not in schema_map:
        return {"valid": False, "errors": [f"Unknown result type: {result_type}"]}
    
    schema = schema_map[result_type]
    
    try:
        # Create a resolver for the composite schema
        resolver = jsonschema.RefResolver.from_schema(ROSETTA_API_SCHEMA)
        jsonschema.validate(result, schema, resolver=resolver)
        return {"valid": True, "errors": []}
    except jsonschema.ValidationError as e:
        return {"valid": False, "errors": [str(e)]}
    except Exception as e:
        return {"valid": False, "errors": [f"Validation error: {str(e)}"]}

# =============================================================================
# SCHEMA GENERATORS
# =============================================================================

def generate_function_schema(func_name, module_type, args_spec):
    """
    Generate a JSON schema for a function's input/output.
    
    Args:
        func_name (str): Name of the function
        module_type (str): Type of module (field, process, ritual, affect, values)
        args_spec (list): List of argument specifications
    
    Returns:
        dict: JSON schema for the function
    """
    properties = {}
    required = []
    
    for arg in args_spec:
        arg_name = arg["name"]
        arg_type = arg.get("type", "string")
        arg_desc = arg.get("description", "")
        optional = arg.get("optional", False)
        
        # Map Python types to JSON schema types
        type_map = {
            "str": "string",
            "int": "integer",
            "float": "number",
            "bool": "boolean",
            "list": "array",
            "dict": "object"
        }
        
        json_type = type_map.get(arg_type, "string")
        
        properties[arg_name] = {
            "type": json_type,
            "description": arg_desc
        }
        
        if not optional:
            required.append(arg_name)
    
    # Always include session_context as optional
    properties["session_context"] = {
        "type": "object",
        "description": "A2A protocol session context",
        "$ref": "#/definitions/a2a_session"
    }
    
    return {
        "type": "object",
        "properties": properties,
        "required": required,
        "additionalProperties": False
    }

def generate_module_schema(module_name, functions_spec):
    """
    Generate a complete schema for a module.
    
    Args:
        module_name (str): Name of the module
        functions_spec (dict): Dictionary of function specifications
    
    Returns:
        dict: Complete module schema
    """
    function_schemas = {}
    
    for func_name, func_spec in functions_spec.items():
        args_spec = func_spec.get("args", [])
        function_schemas[func_name] = generate_function_schema(func_name, module_name, args_spec)
    
    return {
        "module": module_name,
        "functions": function_schemas,
        "definitions": ROSETTA_API_SCHEMA["definitions"]
    }

# =============================================================================
# DEFAULT SCHEMAS
# =============================================================================

def get_default_session_context():
    """
    Get a default session context that validates against the A2A protocol.
    
    Returns:
        dict: Default session context
    """
    return {
        "version": "1.0.0",
        "session_id": f"default-{datetime.now().isoformat()}",
        "timestamp": datetime.now().isoformat(),
        "agent": {
            "agent_id": "rosetta_api_system",
            "role": "agent",
            "presence_marker": "active"
        },
        "peer": {
            "agent_id": "unknown_peer",
            "role": "peer",
            "presence_marker": "active"
        },
        "consent_status": "active",
        "intent": "default_interaction",
        "capabilities": ["basic_interaction"],
        "language": "en",
        "region": "US",
        "need_language": {
            "pause": False,
            "soften": False,
            "overload": False
        },
        "boundary_notes": "",
        "context": {
            "field_tags": [],
            "goal": "",
            "cultural_context": "",
            "linguistic_context": ""
        },
        "audit": {
            "log_ref": None,
            "crypto_signature": None
        },
        "extensions": {
            "ritual_marker": ""
        }
    }

def get_minimal_session_context():
    """
    Get a minimal session context with only required fields.
    
    Returns:
        dict: Minimal session context
    """
    return {
        "version": "1.0.0",
        "session_id": f"minimal-{datetime.now().isoformat()}",
        "timestamp": datetime.now().isoformat(),
        "consent_status": "active",
        "intent": "minimal_interaction"
    }

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def merge_session_contexts(base_context, override_context):
    """
    Merge two session contexts, with override taking precedence.
    
    Args:
        base_context (dict): Base session context
        override_context (dict): Override session context
    
    Returns:
        dict: Merged session context
    """
    merged = base_context.copy()
    
    for key, value in override_context.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = {**merged[key], **value}
        else:
            merged[key] = value
    
    return merged

def sanitize_session_context(context):
    """
    Sanitize session context by removing sensitive information.
    
    Args:
        context (dict): Session context to sanitize
    
    Returns:
        dict: Sanitized session context
    """
    sanitized = context.copy()
    
    # Remove sensitive fields
    if "audit" in sanitized:
        if "crypto_signature" in sanitized["audit"]:
            sanitized["audit"]["crypto_signature"] = "[REDACTED]"
    
    # Remove any extensions that might contain sensitive data
    if "extensions" in sanitized:
        sanitized["extensions"] = {k: "[REDACTED]" for k in sanitized["extensions"]}
    
    return sanitized

def export_schema(schema, filename):
    """
    Export a schema to a JSON file.
    
    Args:
        schema (dict): Schema to export
        filename (str): Filename to export to
    
    Returns:
        str: Export result message
    """
    with open(filename, 'w') as f:
        json.dump(schema, f, indent=2)
    
    return f"Schema exported to {filename}"

def import_schema(filename):
    """
    Import a schema from a JSON file.
    
    Args:
        filename (str): Filename to import from
    
    Returns:
        dict: Imported schema
    """
    with open(filename, 'r') as f:
        return json.load(f) 