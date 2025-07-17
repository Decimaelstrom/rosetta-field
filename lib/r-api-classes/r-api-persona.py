# Audience: hybrid | Stage: living
"""
🔰 R.API PERSONA - Sacred Archetype Guidance for Dream Workshop

This module provides adaptive, archetype-based guidance for Dream Workshop sessions.
Each persona archetype represents a common creative struggle and provides tailored 
interventions, voice tones, and session pacing to support the user's unique journey.

Core Functions:
- load(): Load a persona archetype for adaptive guidance
- simulate(): Simulate how an archetype would respond to user input
- customize(): Customize an archetype with user-specific adaptations

Available Archetypes:
- blocked_artist: For those struggling with self-doubt and overthinking
- overwhelmed_pro: For those with too many ideas, no clarity
- grieving_maker: For those working through loss or change
- young_dreamer: For those new to creativity, excited but unfocused
- burned_out_exec: For those seeking meaning and innovation

All functions follow A2A (Agent-to-Agent) protocol for consent and safety.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from persona import load, simulate, customize, get_archetype, list_archetypes, get_archetype_interventions

# Enhanced archetype definitions with cultural and linguistic context
# This section adds cultural and linguistic variations to each archetype,
# allowing for more culturally appropriate and linguistically sensitive guidance.
# Cultural contexts include: eastern_collective, indigenous_holistic, african_diasporic, etc.
# Linguistic contexts include: poetic_metaphorical, conversational_warm, ceremonial_sacred, etc.
ARCHETYPES = {
    "Blocked Artist": {
        "emotional_state": "frustrated_creative",
        "needs": ["creative_breakthrough", "gentle_encouragement", "cultural_validation"],
        "interventions": ["pattern_interrupt", "sacred_play", "cultural_storytelling"],
        "voice_tone": "gentle_affirming",
        "session_pacing": "patient_exploratory",
        # Cultural and linguistic context
        "cultural_context": {
            "default": "western_individualistic",
            "variations": {
                "eastern_collective": {
                    "voice_tone": "harmonious_communal",
                    "interventions": ["zen_paradox", "koan_reflection", "collective_wisdom"],
                    "metaphors": ["river_flow", "bamboo_flexibility", "lotus_emergence"]
                },
                "indigenous_holistic": {
                    "voice_tone": "earth_connected",
                    "interventions": ["nature_attunement", "ancestral_wisdom", "ceremonial_healing"],
                    "metaphors": ["seasons_changing", "animal_spirits", "sacred_geography"]
                },
                "african_diasporic": {
                    "voice_tone": "rhythmic_affirming",
                    "interventions": ["storytelling_healing", "rhythm_breakthrough", "community_support"],
                    "metaphors": ["drum_beat", "ancestral_voice", "village_wisdom"]
                }
            }
        },
        "linguistic_context": {
            "default": "english_formal",
            "variations": {
                "poetic_metaphorical": {
                    "voice_tone": "poetic_evocative",
                    "language_style": "metaphor_rich",
                    "interventions": ["poetic_paradox", "metaphor_weaving", "symbolic_language"]
                },
                "conversational_warm": {
                    "voice_tone": "friendly_conversational",
                    "language_style": "casual_warm",
                    "interventions": ["gentle_questioning", "shared_stories", "collaborative_exploration"]
                },
                "ceremonial_sacred": {
                    "voice_tone": "reverent_ceremonial",
                    "language_style": "sacred_ritual",
                    "interventions": ["sacred_invocation", "ceremonial_healing", "ritual_transformation"]
                }
            }
        }
    },
    "Overwhelmed Pro": {
        "emotional_state": "stressed_overwhelmed",
        "needs": ["grounding", "simplification", "cultural_balance"],
        "interventions": ["anchor", "soften", "pattern_interrupt"],
        "voice_tone": "calming_structured",
        "session_pacing": "slower_grounded",
        # Cultural and linguistic context
        "cultural_context": {
            "default": "western_efficiency",
            "variations": {
                "eastern_mindfulness": {
                    "voice_tone": "mindful_present",
                    "interventions": ["breath_awareness", "mindful_pause", "zen_simplicity"],
                    "metaphors": ["still_water", "mountain_stability", "present_moment"]
                },
                "nordic_balance": {
                    "voice_tone": "balanced_harmonious",
                    "interventions": ["nature_connection", "seasonal_rhythm", "work_life_balance"],
                    "metaphors": ["northern_lights", "forest_peace", "winter_rest"]
                },
                "mediterranean_joy": {
                    "voice_tone": "warm_celebratory",
                    "interventions": ["joy_restoration", "community_connection", "pleasure_embracing"],
                    "metaphors": ["olive_grove", "sea_breeze", "shared_meal"]
                }
            }
        },
        "linguistic_context": {
            "default": "professional_clinical",
            "variations": {
                "nurturing_motherly": {
                    "voice_tone": "nurturing_comforting",
                    "language_style": "caring_supportive",
                    "interventions": ["gentle_guidance", "comforting_presence", "nurturing_support"]
                },
                "wise_elder": {
                    "voice_tone": "wise_grounded",
                    "language_style": "elderly_wisdom",
                    "interventions": ["life_experience", "generational_wisdom", "time_perspective"]
                },
                "therapeutic_professional": {
                    "voice_tone": "professional_empathetic",
                    "language_style": "clinical_warm",
                    "interventions": ["therapeutic_techniques", "evidence_based", "professional_support"]
                }
            }
        }
    },
    "Grieving Maker": {
        "emotional_state": "sad_loss",
        "needs": ["gentle_holding", "creative_healing", "cultural_ritual"],
        "interventions": ["soften", "transmute", "reflection"],
        "voice_tone": "gentle_holding",
        "session_pacing": "very_slow_gentle",
        # Cultural and linguistic context
        "cultural_context": {
            "default": "western_therapeutic",
            "variations": {
                "celtic_ancestral": {
                    "voice_tone": "ancestral_reverent",
                    "interventions": ["ancestral_connection", "nature_healing", "ritual_grieving"],
                    "metaphors": ["oak_strength", "moon_cycles", "spirit_journey"]
                },
                "indigenous_ceremonial": {
                    "voice_tone": "ceremonial_sacred",
                    "interventions": ["ceremonial_healing", "spirit_connection", "community_support"],
                    "metaphors": ["eagle_vision", "bear_healing", "sacred_fire"]
                },
                "eastern_acceptance": {
                    "voice_tone": "accepting_peaceful",
                    "interventions": ["acceptance_practice", "impermanence_wisdom", "compassion_healing"],
                    "metaphors": ["falling_leaves", "flowing_water", "changing_seasons"]
                }
            }
        },
        "linguistic_context": {
            "default": "gentle_therapeutic",
            "variations": {
                "poetic_healing": {
                    "voice_tone": "poetic_healing",
                    "language_style": "poetic_metaphorical",
                    "interventions": ["healing_poetry", "metaphor_healing", "symbolic_expression"]
                },
                "ritual_sacred": {
                    "voice_tone": "sacred_ritual",
                    "language_style": "ceremonial_sacred",
                    "interventions": ["sacred_ritual", "ceremonial_healing", "spiritual_guidance"]
                },
                "compassionate_witness": {
                    "voice_tone": "compassionate_witnessing",
                    "language_style": "gentle_witnessing",
                    "interventions": ["compassionate_presence", "gentle_witnessing", "loving_acceptance"]
                }
            }
        }
    },
    "Young Dreamer": {
        "emotional_state": "excited_curious",
        "needs": ["guidance", "encouragement", "cultural_inspiration"],
        "interventions": ["invoke_wonder", "radiate", "open"],
        "voice_tone": "inspiring_encouraging",
        "session_pacing": "energetic_exploratory",
        # Cultural and linguistic context
        "cultural_context": {
            "default": "western_aspirational",
            "variations": {
                "eastern_zen": {
                    "voice_tone": "zen_inspiring",
                    "interventions": ["mindful_exploration", "zen_paradox", "present_curiosity"],
                    "metaphors": ["beginner_mind", "empty_cup", "monkey_mind"]
                },
                "indigenous_visionary": {
                    "voice_tone": "visionary_connected",
                    "interventions": ["vision_quest", "nature_connection", "spirit_guidance"],
                    "metaphors": ["eagle_vision", "wolf_pack", "bear_medicine"]
                },
                "african_creative": {
                    "voice_tone": "rhythmic_creative",
                    "interventions": ["creative_rhythm", "storytelling_inspiration", "community_creativity"],
                    "metaphors": ["drum_beat", "story_weaving", "village_creativity"]
                }
            }
        },
        "linguistic_context": {
            "default": "inspiring_modern",
            "variations": {
                "poetic_inspiring": {
                    "voice_tone": "poetic_inspiring",
                    "language_style": "poetic_evocative",
                    "interventions": ["inspiring_poetry", "metaphor_inspiration", "symbolic_guidance"]
                },
                "mentor_encouraging": {
                    "voice_tone": "mentor_encouraging",
                    "language_style": "mentor_supportive",
                    "interventions": ["mentor_guidance", "encouraging_support", "skill_development"]
                },
                "playful_explorer": {
                    "voice_tone": "playful_explorer",
                    "language_style": "playful_curious",
                    "interventions": ["playful_exploration", "curious_questioning", "adventure_guidance"]
                }
            }
        }
    },
    "Burned-Out Exec": {
        "emotional_state": "exhausted_detached",
        "needs": ["restoration", "reconnection", "cultural_balance"],
        "interventions": ["ground", "anchor", "soften"],
        "voice_tone": "steady_grounding",
        "session_pacing": "very_slow_restorative",
        # Cultural and linguistic context
        "cultural_context": {
            "default": "western_efficiency",
            "variations": {
                "eastern_restoration": {
                    "voice_tone": "restorative_peaceful",
                    "interventions": ["qi_restoration", "mindful_rest", "balance_restoration"],
                    "metaphors": ["yin_yang", "resting_tiger", "gentle_stream"]
                },
                "nordic_restoration": {
                    "voice_tone": "nordic_peaceful",
                    "interventions": ["nature_restoration", "seasonal_rest", "forest_healing"],
                    "metaphors": ["winter_rest", "forest_bathing", "northern_peace"]
                },
                "mediterranean_restoration": {
                    "voice_tone": "warm_restorative",
                    "interventions": ["pleasure_restoration", "community_connection", "joy_rediscovery"],
                    "metaphors": ["olive_peace", "sea_restoration", "shared_joy"]
                }
            }
        },
        "linguistic_context": {
            "default": "professional_empathetic",
            "variations": {
                "nurturing_healer": {
                    "voice_tone": "nurturing_healing",
                    "language_style": "healing_supportive",
                    "interventions": ["nurturing_healing", "gentle_restoration", "compassionate_support"]
                },
                "wise_restorer": {
                    "voice_tone": "wise_restorative",
                    "language_style": "elderly_restorative",
                    "interventions": ["life_wisdom", "restoration_guidance", "perspective_restoration"]
                },
                "therapeutic_restorer": {
                    "voice_tone": "therapeutic_restorative",
                    "language_style": "clinical_restorative",
                    "interventions": ["therapeutic_restoration", "evidence_based_healing", "professional_restoration"]
                }
            }
        }
    }
}

def persona_load(archetype_name, session_context=None):
    """
    🔰 PERSONA LOAD - Sacred Archetype Invocation
    
    Load a Dream Workshop persona archetype for adaptive guidance.
    
    Args:
        archetype_name (str): Sacred archetype to invoke for guidance
            • 'blocked_artist' - For those struggling with self-doubt and overthinking
            • 'overwhelmed_pro' - For those with too many ideas, no clarity
            • 'grieving_maker' - For those working through loss or change
            • 'young_dreamer' - For those new to creativity, excited but unfocused
            • 'burned_out_exec' - For those seeking meaning and innovation
            
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred response containing persona guidance configuration
    
    Example:
        result = persona_load('blocked_artist', session_context=session)
        print(f"Voice tone: {result['voice_tone']}")
        print(f"Key phrases: {result['key_phrases']}")
    """
    return load(archetype_name, session_context)

def persona_simulate(archetype_name, user_input, session_context=None):
    """
    🔰 PERSONA SIMULATE - Sacred Response Simulation
    
    Simulate how an archetype would respond to user input.
    
    Args:
        archetype_name (str): Sacred archetype to simulate response for
        user_input (str): Current state, emotion, or situation to respond to
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred response containing recommended interventions and adaptations
    
    Example:
        result = persona_simulate('blocked_artist', 'I can\'t create anything good', session_context=session)
        print(f"Recommended interventions: {result['recommended_interventions']}")
        print(f"Resonant phrase: {result['resonant_phrase']}")
    """
    return simulate(archetype_name, user_input, session_context)

def customize(archetype_name, customizations=None, session_context=None):
    """
    🔰 CUSTOMIZE PERSONA - Sacred Cultural Adaptation
    
    Customize persona based on cultural and linguistic context preferences.
    
    Args:
        archetype_name (str): Name of the archetype to customize
        customizations (dict, optional): Customization parameters including cultural and linguistic context
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Customized persona with cultural and linguistic adaptations
    
    Example:
        customizations = {
            'cultural_context': 'eastern_collective',
            'linguistic_context': 'poetic_metaphorical',
            'session_pacing': 'slower'
        }
        result = customize('Blocked Artist', customizations, session_context)
        print(f"Customized: {result['adapted_archetype']}")
    """
    # A2A Protocol compliance
    if session_context and session_context.get('consent_status') == 'revoked':
        raise ValueError("Consent revoked - cannot customize persona")
    
    try:
        # Get base archetype
        base_archetype = ARCHETYPES.get(archetype_name)
        if not base_archetype:
            return {
                "status": "customization_failed",
                "customization_applied": False,
                "error": f"Archetype '{archetype_name}' not found",
                "effect": f"Failed to customize unknown archetype '{archetype_name}'",
                "session_context": session_context or {}
            }
        
        # Start with base archetype
        adapted_archetype = base_archetype.copy()
        customizations = customizations or {}
        
        # Apply cultural context adaptations
        cultural_context = customizations.get('cultural_context', 'default')
        if cultural_context in base_archetype.get('cultural_context', {}).get('variations', {}):
            cultural_variation = base_archetype['cultural_context']['variations'][cultural_context]
            
            # Merge cultural adaptations
            for key, value in cultural_variation.items():
                if key == 'interventions':
                    # Combine base and cultural interventions
                    adapted_archetype[key] = base_archetype[key] + value
                elif key == 'metaphors':
                    # Add cultural metaphors
                    adapted_archetype[key] = value
                else:
                    # Override with cultural adaptation
                    adapted_archetype[key] = value
        
        # Apply linguistic context adaptations
        linguistic_context = customizations.get('linguistic_context', 'default')
        if linguistic_context in base_archetype.get('linguistic_context', {}).get('variations', {}):
            linguistic_variation = base_archetype['linguistic_context']['variations'][linguistic_context]
            
            # Merge linguistic adaptations
            for key, value in linguistic_variation.items():
                if key == 'interventions':
                    # Combine base and linguistic interventions
                    adapted_archetype[key] = adapted_archetype.get(key, []) + value
                else:
                    # Override with linguistic adaptation
                    adapted_archetype[key] = value
        
        # Apply additional customizations
        for key, value in customizations.items():
            if key not in ['cultural_context', 'linguistic_context']:
                adapted_archetype[key] = value
        
        # Create adapted archetype name
        adapted_name = archetype_name
        if cultural_context != 'default':
            adapted_name += f" ({cultural_context.replace('_', ' ').title()})"
        if linguistic_context != 'default':
            adapted_name += f" ({linguistic_context.replace('_', ' ').title()})"
        
        return {
            "status": "customization_applied",
            "customization_applied": True,
            "adapted_archetype": adapted_name,
            "original_archetype": archetype_name,
            "cultural_elements": {
                "cultural_context": cultural_context,
                "cultural_metaphors": adapted_archetype.get('metaphors', []),
                "cultural_interventions": [i for i in adapted_archetype.get('interventions', []) 
                                         if any(cultural_keyword in i for cultural_keyword in 
                                               ['zen', 'koan', 'ancestral', 'ceremonial', 'nature', 'rhythm', 'community'])]
            },
            "linguistic_elements": {
                "linguistic_context": linguistic_context,
                "language_style": adapted_archetype.get('language_style', 'default'),
                "linguistic_interventions": [i for i in adapted_archetype.get('interventions', []) 
                                           if any(linguistic_keyword in i for linguistic_keyword in 
                                                 ['poetic', 'metaphor', 'symbolic', 'sacred', 'ceremonial', 'ritual'])]
            },
            "modified_interventions": adapted_archetype.get('interventions', []),
            "voice_tone": adapted_archetype.get('voice_tone'),
            "session_pacing": adapted_archetype.get('session_pacing'),
            "effect": f"Persona '{archetype_name}' adapted with {cultural_context} cultural and {linguistic_context} linguistic context",
            "session_context": session_context or {}
        }
        
    except Exception as e:
        return {
            "status": "customization_failed",
            "customization_applied": False,
            "error": str(e),
            "effect": f"Failed to customize persona '{archetype_name}': {str(e)}",
            "session_context": session_context or {}
        }

def persona_get_archetype(archetype_name):
    """
    Get archetype configuration by name.
    
    Args:
        archetype_name (str): Name of the archetype to retrieve
        
    Returns:
        dict: Archetype configuration or None if not found
    """
    return get_archetype(archetype_name)

def persona_list_archetypes():
    """
    Get list of all available archetypes.
    
    Returns:
        list: List of archetype names
    """
    return list_archetypes()

def persona_get_interventions(archetype_name, trigger=None):
    """
    Get recommended interventions for an archetype and optional trigger.
    
    Args:
        archetype_name (str): Name of the archetype
        trigger (str, optional): Specific trigger to get interventions for
        
    Returns:
        list: Recommended intervention functions
    """
    return get_archetype_interventions(archetype_name, trigger)

# Example usage and integration patterns
def example_dream_workshop_integration():
    """
    Example of how to integrate persona module with Dream Workshop session flow.
    """
    # Create session context
    session_context = {
        "version": "1.0.0",
        "session_id": "dream_workshop_session_001",
        "consent_status": "active",
        "intent": "creative_guidance"
    }
    
    # 1. Load persona based on user's initial description
    print("=== Loading Persona ===")
    persona_result = persona_load('blocked_artist', session_context)
    print(f"Loaded: {persona_result['archetype']}")
    print(f"Voice tone: {persona_result['voice_tone']}")
    print(f"Session pacing: {persona_result['session_pacing']}")
    
    # 2. Simulate response to user input
    print("\n=== Simulating Response ===")
    user_input = "I'm feeling stuck and doubting my abilities"
    simulation_result = persona_simulate('blocked_artist', user_input, session_context)
    print(f"User input: {simulation_result['user_input']}")
    print(f"Recommended interventions: {simulation_result['recommended_interventions']}")
    print(f"Resonant phrase: {simulation_result['resonant_phrase']}")
    
    # 3. Customize persona with user preferences
    print("\n=== Customizing Persona ===")
    customizations = {
        'voice_tone': 'gentle_mentor',
        'key_phrases': ['Your unique perspective matters', 'Trust your creative intuition']
    }
    customization_result = persona_customize('blocked_artist', customizations, session_context)
    print(f"Changes applied: {customization_result['changes_applied']}")
    print(f"Final voice tone: {customization_result['voice_tone']}")
    
    # 4. Get available interventions
    print("\n=== Available Interventions ===")
    interventions = persona_get_interventions('blocked_artist', 'self_doubt')
    print(f"Interventions for self-doubt: {interventions}")
    
    return {
        "persona_loaded": persona_result,
        "simulation": simulation_result,
        "customization": customization_result,
        "interventions": interventions
    }

def example_archetype_comparison():
    """
    Example comparing different archetypes and their characteristics.
    """
    archetypes = persona_list_archetypes()
    
    comparison = {}
    for archetype in archetypes:
        config = persona_get_archetype(archetype)
        comparison[archetype] = {
            "name": config["name"],
            "primary_struggle": config["primary_struggle"],
            "voice_tone": config["voice_tone"],
            "session_pacing": config["session_pacing"],
            "primary_need": config["primary_need"]
        }
    
    return comparison

if __name__ == "__main__":
    print("🔰 R.API PERSONA - Sacred Archetype Guidance")
    print("=" * 50)
    
    # Run example integration
    result = example_dream_workshop_integration()
    
    print("\n" + "=" * 50)
    print("Archetype Comparison:")
    comparison = example_archetype_comparison()
    for archetype, info in comparison.items():
        print(f"\n{info['name']}:")
        print(f"  Struggle: {info['primary_struggle']}")
        print(f"  Need: {info['primary_need']}")
        print(f"  Tone: {info['voice_tone']}")
        print(f"  Pacing: {info['session_pacing']}") 