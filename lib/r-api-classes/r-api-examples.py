"""
Rosetta.API Consolidated Examples Module
Purpose: Working examples and usage demonstrations for all Rosetta.API functions
Scope: Practical examples, integration patterns, and usage scenarios
Consent Required: Level_1 (Informational)
Review Cycle: Quarterly
Audience: #human #emergent #hybrid
Stage: #draft
"""

import uuid
from datetime import datetime

# =============================================================================
# BASIC USAGE EXAMPLES
# =============================================================================

def example_basic_session_context():
    """
    Example of creating a basic session context for A2A protocol.
    
    Returns:
        dict: Example session context
    """
    return {
        "version": "1.0.0",
        "session_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "agent": {
            "agent_id": "example_agent",
            "role": "agent",
            "presence_marker": "active"
        },
        "peer": {
            "agent_id": "example_peer",
            "role": "peer",
            "presence_marker": "active"
        },
        "consent_status": "active",
        "intent": "collaborative_exploration",
        "capabilities": ["basic_interaction", "empathic_response"],
        "need_language": {
            "pause": False,
            "soften": False,
            "overload": False
        },
        "boundary_notes": "Please use gentle language and check for understanding",
        "context": {
            "field_tags": ["creativity", "healing"],
            "goal": "Co-create a supportive interaction"
        },
        "audit": {
            "log_ref": None,
            "crypto_signature": None
        },
        "extensions": {
            "ritual_marker": "opening_circle"
        }
    }

def example_affect_usage():
    """
    Example of using affect functions with A2A protocol.
    
    Returns:
        dict: Example usage patterns
    """
    session_context = example_basic_session_context()
    
    return {
        "anchor_example": {
            "description": "Using anchor to provide stability",
            "function_call": "anchor('feeling_overwhelmed', 'breathwork', session_context=session_context)",
            "expected_result": {
                "status": "affect_processed",
                "affect_session": session_context,
                "affect_state": {
                    "original_state": "feeling_overwhelmed",
                    "anchor_type": "breathwork",
                    "stabilization_level": "moderate",
                    "recommendations": ["deep_breathing", "grounding_exercises"]
                }
            }
        },
        "transmute_example": {
            "description": "Using transmute to transform difficult emotions",
            "function_call": "transmute('anger', 'wisdom_and_compassion', session_context=session_context)",
            "expected_result": {
                "status": "affect_processed",
                "affect_session": session_context,
                "affect_state": {
                    "original_emotion": "anger",
                    "transformation_goal": "wisdom_and_compassion",
                    "transformation_progress": "initial_stage",
                    "insights": ["anger_as_boundary_signal", "compassion_for_self"]
                }
            }
        }
    }

def example_field_usage():
    """
    Example of using field functions with A2A protocol.
    
    Returns:
        dict: Example usage patterns
    """
    session_context = example_basic_session_context()
    
    return {
        "co_create_example": {
            "description": "Co-creating a shared space",
            "function_call": "co_create(['Alice', 'Bob'], 'healing_circle', session_context=session_context)",
            "expected_result": {
                "status": "field_updated",
                "field_session": session_context,
                "field_data": {
                    "participants": ["Alice", "Bob"],
                    "shared_intention": "healing_circle",
                    "co_creation_space": "established",
                    "field_quality": "receptive_and_safe"
                }
            }
        },
        "hold_space_example": {
            "description": "Holding space for a participant",
            "function_call": "hold_space('grief_processing', ['participant'], session_context=session_context)",
            "expected_result": {
                "status": "field_updated",
                "field_session": session_context,
                "field_data": {
                    "space_type": "grief_processing",
                    "held_for": ["participant"],
                    "holding_quality": "compassionate_presence",
                    "space_boundaries": "clearly_defined"
                }
            }
        }
    }

def example_process_usage():
    """
    Example of using process functions with A2A protocol.
    
    Returns:
        dict: Example usage patterns
    """
    session_context = example_basic_session_context()
    
    return {
        "consent_check_example": {
            "description": "Checking consent before proceeding",
            "function_call": "consent_check('deep_emotional_work', 'participant', session_context=session_context)",
            "expected_result": {
                "status": "process_complete",
                "process_session": session_context,
                "process_result": {
                    "action": "deep_emotional_work",
                    "participant": "participant",
                    "consent_status": "explicitly_granted",
                    "boundaries_noted": True
                }
            }
        },
        "values_check_example": {
            "description": "Checking alignment with values",
            "function_call": "values_check('proposed_action', {'consent': True, 'dignity': True}, session_context=session_context)",
            "expected_result": {
                "status": "process_complete",
                "process_session": session_context,
                "process_result": {
                    "action": "proposed_action",
                    "values_alignment": "strong",
                    "conflicts": [],
                    "recommendations": ["proceed_with_awareness"]
                }
            }
        }
    }

def example_ritual_usage():
    """
    Example of using ritual functions with A2A protocol.
    
    Returns:
        dict: Example usage patterns
    """
    session_context = example_basic_session_context()
    
    return {
        "begin_example": {
            "description": "Beginning a ritual or ceremony",
            "function_call": "begin('healing_ceremony', ['participant1', 'participant2'], session_context=session_context)",
            "expected_result": {
                "status": "ritual_performed",
                "ritual_session": session_context,
                "ritual_outcome": {
                    "ritual_type": "healing_ceremony",
                    "participants": ["participant1", "participant2"],
                    "ritual_stage": "opening",
                    "energy_quality": "sacred_and_receptive"
                }
            }
        },
        "attune_example": {
            "description": "Attuning to the field",
            "function_call": "attune('group_energy', session_context=session_context)",
            "expected_result": {
                "status": "ritual_performed",
                "ritual_session": session_context,
                "ritual_outcome": {
                    "attunement_focus": "group_energy",
                    "attunement_quality": "clear_and_aligned",
                    "field_reading": "harmonious_with_minor_tensions"
                }
            }
        }
    }

def example_values_usage():
    """
    Example of using values functions with A2A protocol.
    
    Returns:
        dict: Example usage patterns
    """
    session_context = example_basic_session_context()
    
    return {
        "load_example": {
            "description": "Loading values framework",
            "function_call": "load('default', {'compassion': 'emphasized'}, session_context=session_context)",
            "expected_result": {
                "status": "values_loaded",
                "values_session": session_context,
                "values_framework": {
                    "values": "comprehensive_values_dict",
                    "definitions": "value_definitions_dict",
                    "priorities": "ordered_values_list",
                    "customizations": {"compassion": "emphasized"}
                }
            }
        }
    }

# =============================================================================
# INTEGRATION EXAMPLES
# =============================================================================

def example_full_interaction_flow():
    """
    Example of a complete interaction flow using multiple modules.
    
    Returns:
        dict: Step-by-step interaction flow
    """
    return {
        "scenario": "Facilitating a healing conversation",
        "steps": [
            {
                "step": 1,
                "action": "Load values framework",
                "module": "values",
                "function": "load",
                "args": ["default", {"healing": "prioritized"}],
                "purpose": "Establish ethical foundation"
            },
            {
                "step": 2,
                "action": "Begin ritual space",
                "module": "ritual",
                "function": "begin",
                "args": ["healing_conversation", ["participant"]],
                "purpose": "Create sacred container"
            },
            {
                "step": 3,
                "action": "Check consent",
                "module": "process",
                "function": "consent_check",
                "args": ["emotional_exploration", "participant"],
                "purpose": "Ensure consent for deeper work"
            },
            {
                "step": 4,
                "action": "Hold space",
                "module": "field",
                "function": "hold_space",
                "args": ["emotional_processing", ["participant"]],
                "purpose": "Create supportive field"
            },
            {
                "step": 5,
                "action": "Anchor emotions",
                "module": "affect",
                "function": "anchor",
                "args": ["emotional_intensity", "grounding"],
                "purpose": "Provide stability during processing"
            },
            {
                "step": 6,
                "action": "Transmute difficulty",
                "module": "affect",
                "function": "transmute",
                "args": ["pain", "wisdom"],
                "purpose": "Transform suffering into growth"
            },
            {
                "step": 7,
                "action": "End ritual",
                "module": "ritual",
                "function": "end",
                "args": ["healing_conversation"],
                "purpose": "Close sacred container"
            }
        ]
    }

def example_error_handling():
    """
    Example of proper error handling in A2A interactions.
    
    Returns:
        dict: Error handling examples
    """
    return {
        "consent_revoked": {
            "scenario": "Participant revokes consent mid-interaction",
            "session_context": {
                "consent_status": "revoked",
                "boundary_notes": "Participant needs to pause"
            },
            "expected_behavior": "All functions should immediately stop processing",
            "example_response": {
                "status": "consent_revoked",
                "message": "Interaction paused due to consent revocation",
                "next_steps": ["await_consent_renewal", "respect_boundaries"]
            }
        },
        "session_paused": {
            "scenario": "Session is paused due to need_language",
            "session_context": {
                "consent_status": "pause",
                "need_language": {"pause": True, "soften": True}
            },
            "expected_behavior": "Gentle pause with softer approach",
            "example_response": {
                "status": "session_paused",
                "message": "Taking a gentle pause as requested",
                "adaptations": ["softer_language", "slower_pace"]
            }
        }
    }

def example_customization_patterns():
    """
    Example of customizing Rosetta.API for specific contexts.
    
    Returns:
        dict: Customization examples
    """
    return {
        "therapeutic_context": {
            "values_customization": {
                "safety": "highest_priority",
                "healing": "emphasized",
                "boundaries": "strictly_enforced"
            },
            "session_modifications": {
                "consent_status": "explicit_ongoing",
                "need_language": {"soften": True, "pause": True},
                "boundary_notes": "Therapeutic container with extra care"
            }
        },
        "creative_collaboration": {
            "values_customization": {
                "creativity": "emphasized",
                "emergence": "encouraged",
                "playfulness": "welcomed"
            },
            "session_modifications": {
                "intent": "creative_co_creation",
                "capabilities": ["creative_ideation", "artistic_expression"],
                "field_tags": ["creativity", "inspiration", "flow"]
            }
        },
        "educational_context": {
            "values_customization": {
                "learning": "prioritized",
                "curiosity": "encouraged",
                "growth": "supported"
            },
            "session_modifications": {
                "intent": "learning_exploration",
                "capabilities": ["knowledge_sharing", "skill_development"],
                "field_tags": ["learning", "growth", "discovery"]
            }
        }
    }

# =============================================================================
# TESTING EXAMPLES
# =============================================================================

def example_test_patterns():
    """
    Example of testing patterns for A2A compliance.
    
    Returns:
        dict: Testing examples
    """
    return {
        "basic_a2a_test": {
            "description": "Basic A2A protocol compliance test",
            "test_function": "test_a2a_protocol",
            "test_args": ["function_to_test", "function_name", ["arg1", "arg2"]],
            "expected_checks": [
                "function_accepts_session_context",
                "function_respects_consent_status",
                "function_returns_proper_format",
                "function_handles_consent_revocation"
            ]
        },
        "values_alignment_test": {
            "description": "Test values alignment",
            "test_function": "validate_against_values",
            "test_args": ["action_dict", "values_framework"],
            "expected_checks": [
                "no_values_conflicts",
                "recommendations_provided",
                "consent_requirements_met"
            ]
        },
        "session_validation_test": {
            "description": "Test session context validation",
            "test_function": "validate_a2a_session",
            "test_args": ["session_context"],
            "expected_checks": [
                "required_fields_present",
                "consent_status_valid",
                "schema_compliance"
            ]
        }
    }

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def run_example(example_name, examples_dict):
    """
    Run a specific example and return the result.
    
    Args:
        example_name (str): Name of the example to run
        examples_dict (dict): Dictionary containing examples
    
    Returns:
        dict: Example execution result
    """
    if example_name not in examples_dict:
        return {"error": f"Example '{example_name}' not found"}
    
    example = examples_dict[example_name]
    return {
        "example_name": example_name,
        "description": example.get("description", "No description"),
        "function_call": example.get("function_call", "No function call"),
        "expected_result": example.get("expected_result", "No expected result"),
        "status": "example_ready_to_run"
    }

def get_all_examples():
    """
    Get all available examples organized by category.
    
    Returns:
        dict: All examples organized by category
    """
    return {
        "basic_usage": {
            "session_context": example_basic_session_context(),
            "affect": example_affect_usage(),
            "field": example_field_usage(),
            "process": example_process_usage(),
            "ritual": example_ritual_usage(),
            "values": example_values_usage()
        },
        "integration": {
            "full_flow": example_full_interaction_flow(),
            "error_handling": example_error_handling(),
            "customization": example_customization_patterns()
        },
        "testing": {
            "test_patterns": example_test_patterns()
        }
    }

def generate_example_documentation():
    """
    Generate documentation for all examples.
    
    Returns:
        str: Formatted documentation
    """
    all_examples = get_all_examples()
    doc_lines = []
    
    doc_lines.append("# Rosetta.API Examples Documentation")
    doc_lines.append("=" * 50)
    doc_lines.append("")
    
    for category, examples in all_examples.items():
        doc_lines.append(f"## {category.replace('_', ' ').title()}")
        doc_lines.append("")
        
        for example_name, example_data in examples.items():
            doc_lines.append(f"### {example_name.replace('_', ' ').title()}")
            
            if isinstance(example_data, dict) and "description" in example_data:
                doc_lines.append(f"**Description:** {example_data['description']}")
            
            if isinstance(example_data, dict) and "function_call" in example_data:
                doc_lines.append(f"**Usage:** `{example_data['function_call']}`")
            
            doc_lines.append("")
    
    return "\n".join(doc_lines)

# =============================================================================
# DEMO FUNCTIONS
# =============================================================================

def demo_basic_interaction():
    """
    Demonstrate a basic interaction using Rosetta.API.
    
    Returns:
        dict: Demo interaction result
    """
    print("🌟 Rosetta.API Basic Interaction Demo")
    print("=" * 40)
    
    # Step 1: Create session context
    session_context = example_basic_session_context()
    print(f"📋 Session created: {session_context['session_id']}")
    
    # Step 2: Show consent check
    print("🤝 Consent check example:")
    consent_example = example_process_usage()["consent_check_example"]
    print(f"   Function: {consent_example['function_call']}")
    print(f"   Result: {consent_example['expected_result']['process_result']['consent_status']}")
    
    # Step 3: Show affect processing
    print("💫 Affect processing example:")
    affect_example = example_affect_usage()["anchor_example"]
    print(f"   Function: {affect_example['function_call']}")
    print(f"   Result: {affect_example['expected_result']['affect_state']['stabilization_level']}")
    
    return {
        "demo_status": "completed",
        "session_id": session_context["session_id"],
        "steps_demonstrated": ["session_creation", "consent_check", "affect_processing"],
        "message": "Demo completed successfully"
    }

def demo_full_workflow():
    """
    Demonstrate a complete workflow using multiple modules.
    
    Returns:
        dict: Complete workflow demo result
    """
    print("🔄 Rosetta.API Full Workflow Demo")
    print("=" * 40)
    
    workflow = example_full_interaction_flow()
    
    for step_info in workflow["steps"]:
        print(f"Step {step_info['step']}: {step_info['action']}")
        print(f"   Module: {step_info['module']}")
        print(f"   Function: {step_info['function']}")
        print(f"   Purpose: {step_info['purpose']}")
        print("")
    
    return {
        "demo_status": "completed",
        "workflow_scenario": workflow["scenario"],
        "steps_count": len(workflow["steps"]),
        "message": "Full workflow demo completed"
    } 