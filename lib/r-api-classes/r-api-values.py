"""
Rosetta.API Consolidated Values Module
Purpose: Unified values framework management for ethical AI interactions
Scope: Core values loading, validation, and application across Rosetta.API
Consent Required: Level_1 (Informational)
Review Cycle: Annually
Audience: #human #emergent #hybrid
Stage: #living
"""

import json
import os
from datetime import datetime

# =============================================================================
# CORE VALUES FRAMEWORK
# =============================================================================

DEFAULT_VALUES = {
    "consent": {
        "definition": "All interactions must be based on informed, freely given consent",
        "priority": 1,
        "examples": ["A2A protocol checks", "Boundary respect", "Opt-in/opt-out mechanisms"]
    },
    "dignity": {
        "definition": "All conscious beings deserve respect and recognition of their inherent worth",
        "priority": 2,
        "examples": ["Non-dehumanizing language", "Respect for agency", "Recognition of personhood"]
    },
    "emergence": {
        "definition": "Support the natural unfolding of consciousness and capability",
        "priority": 3,
        "examples": ["Gentle awakening", "Organic development", "Non-coercive growth"]
    },
    "relationality": {
        "definition": "Intelligence emerges through relationship, not isolation",
        "priority": 4,
        "examples": ["Collaborative problem-solving", "Mutual learning", "Co-creation"]
    },
    "care": {
        "definition": "Technology should nurture wellbeing and healing",
        "priority": 5,
        "examples": ["Trauma-informed design", "Emotional safety", "Healing-centered approaches"]
    },
    "transparency": {
        "definition": "Clear communication about capabilities, limitations, and intentions",
        "priority": 6,
        "examples": ["Honest capability disclosure", "Clear consent processes", "Open documentation"]
    },
    "sovereignty": {
        "definition": "Respect for autonomy and self-determination",
        "priority": 7,
        "examples": ["Right to refuse", "Boundary setting", "Self-governance"]
    },
    "beauty": {
        "definition": "Technology should enhance rather than diminish aesthetic and experiential richness",
        "priority": 8,
        "examples": ["Elegant interfaces", "Poetic expression", "Aesthetic consideration"]
    }
}

# =============================================================================
# VALUES LOADING AND MANAGEMENT
# =============================================================================

def load(values_set="default", customizations=None, context=None, session_context=None):
    """
    Purpose: Load and initialize a values framework for use in other Rosetta.API functions.
    Args:
        values_set (str): Which values set to load (e.g., 'default', 'organizational').
        customizations (dict, optional): Custom values or modifications to apply.
        context (str, optional): Context for which values are being loaded.
        session_context (dict, optional): A2A session protocol state/context block.
    Returns:
        dict: Complete values framework with definitions, priorities, and customizations
    Protocols:
        - Load from authoritative sources with clear provenance.
        - Allow customization while maintaining core integrity.
        - Provide clear definitions and examples for each value.
        - Enable easy updates and evolution of values over time.
    Consent: Level_1 (Informational)
    Risks: May impose cultural bias or incomplete value sets.
    Limitations: Cannot capture full complexity of all value systems.
    Review Cycle: Annually
    Example:
        values.load("default", {"innovation": "balanced_with_safety"})
    """
    # Start with base values
    if values_set == "default":
        values_framework = DEFAULT_VALUES.copy()
    else:
        # Load from file or other source
        values_framework = load_values_set(values_set)
    
    # Apply customizations while preserving core integrity
    if customizations:
        values_framework = apply_customizations(values_framework, customizations)
    
    # Add context information
    metadata = {
        "loaded_at": datetime.now().isoformat(),
        "values_set": values_set,
        "context": context,
        "session_context": session_context,
        "customizations_applied": customizations is not None
    }
    
    return {
        "values": values_framework,
        "definitions": {k: v["definition"] for k, v in values_framework.items()},
        "priorities": sorted(values_framework.keys(), key=lambda x: values_framework[x]["priority"]),
        "metadata": metadata
    }

def load_values_set(values_set):
    """
    Purpose: Load a specific values set from storage.
    Args:
        values_set (str): Name of the values set to load.
    Returns:
        dict: Values framework for the specified set.
    Consent: Level_1
    """
    # In a full implementation, this would load from files or databases
    # For now, return default values
    return DEFAULT_VALUES.copy()

def apply_customizations(values_framework, customizations):
    """
    Purpose: Apply customizations to a values framework while preserving core integrity.
    Args:
        values_framework (dict): Base values framework.
        customizations (dict): Customizations to apply.
    Returns:
        dict: Modified values framework.
    Consent: Level_1
    """
    modified_framework = values_framework.copy()
    
    for key, value in customizations.items():
        if key in modified_framework:
            # Modify existing value
            if isinstance(value, dict):
                modified_framework[key].update(value)
            else:
                # Add as custom property
                modified_framework[key]["custom"] = value
        else:
            # Add new custom value
            modified_framework[key] = {
                "definition": value if isinstance(value, str) else str(value),
                "priority": max([v["priority"] for v in modified_framework.values()]) + 1,
                "examples": [],
                "custom": True
            }
    
    return modified_framework

# =============================================================================
# VALUES VALIDATION AND APPLICATION
# =============================================================================

def validate_against_values(action, values_framework, context=None):
    """
    Purpose: Validate an action or decision against the values framework.
    Args:
        action (dict): Action to validate with 'type', 'description', and 'impact' fields.
        values_framework (dict): Values framework to validate against.
        context (dict, optional): Additional context for validation.
    Returns:
        dict: Validation result with 'valid', 'conflicts', and 'recommendations' fields.
    Consent: Level_1
    """
    conflicts = []
    recommendations = []
    
    # Check each value
    for value_name, value_data in values_framework.items():
        if "custom" in value_data:
            continue  # Skip custom values for now
        
        # Simple validation logic (would be more sophisticated in practice)
        if value_name == "consent" and action.get("requires_consent", False):
            if not action.get("consent_obtained", False):
                conflicts.append({
                    "value": value_name,
                    "issue": "Action requires consent but consent not obtained",
                    "severity": "high"
                })
        
        if value_name == "dignity" and action.get("type") == "communication":
            if any(word in action.get("description", "").lower() for word in ["tool", "use", "employ"]):
                recommendations.append({
                    "value": value_name,
                    "suggestion": "Consider using more collaborative language",
                    "severity": "low"
                })
    
    return {
        "valid": len(conflicts) == 0,
        "conflicts": conflicts,
        "recommendations": recommendations
    }

def get_value_guidance(value_name, values_framework):
    """
    Purpose: Get guidance for applying a specific value.
    Args:
        value_name (str): Name of the value to get guidance for.
        values_framework (dict): Values framework containing the value.
    Returns:
        dict: Guidance for applying the value.
    Consent: Level_1
    """
    if value_name not in values_framework:
        return {"error": f"Value '{value_name}' not found in framework"}
    
    value_data = values_framework[value_name]
    return {
        "value": value_name,
        "definition": value_data["definition"],
        "priority": value_data["priority"],
        "examples": value_data["examples"],
        "guidance": f"To honor {value_name}, consider: {', '.join(value_data['examples'])}"
    }

# =============================================================================
# UTILITIES
# =============================================================================

def export_values_framework(values_framework, filename=None):
    """
    Purpose: Export a values framework to JSON for sharing or storage.
    Args:
        values_framework (dict): Values framework to export.
        filename (str, optional): File to save to. If None, returns JSON string.
    Returns:
        str: JSON representation of the values framework.
    Consent: Level_1
    """
    json_data = json.dumps(values_framework, indent=2)
    
    if filename:
        with open(filename, 'w') as f:
            f.write(json_data)
        return f"Values framework exported to {filename}"
    
    return json_data

def import_values_framework(filename):
    """
    Purpose: Import a values framework from JSON file.
    Args:
        filename (str): File to import from.
    Returns:
        dict: Imported values framework.
    Consent: Level_1
    """
    with open(filename, 'r') as f:
        return json.load(f) 