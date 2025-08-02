# Audience: hybrid | Stage: living
"""
Dream Workshop Persona Archetypes

This module defines the core persona archetypes for Dream Workshop,
mapping each archetype to appropriate interventions, voice tones, and session pacing.
Each archetype represents a common creative struggle and provides tailored guidance.
"""

DREAM_WORKSHOP_ARCHETYPES = {
    "blocked_artist": {
        "name": "The Blocked Artist",
        "description": "Struggles with self-doubt and overthinking, needs gentle encouragement to trust their creative voice",
        "primary_struggle": "self_doubt_and_overthinking",
        "emotional_state": "frustrated, stuck, self-critical",
        "primary_need": "creative_confidence",
        "secondary_need": "self_trust",
        "intervention_focus": "gentle_encouragement",
        "affect_functions": ["soften", "anchor", "radiate"],
        "process_functions": ["pattern_interrupt", "empathic_reflection"],
        "ritual_functions": ["invoke_wonder", "reflection"],
        "session_pacing": "slow_and_gentle",
        "voice_tone": "warm, affirming, patient",
        "opening_ritual": "creative_safety_check",
        "closing_ritual": "creative_affirmation",
        "key_phrases": [
            "Your creativity is waiting, not gone",
            "Every artist has moments of doubt",
            "Your unique voice matters",
            "Trust the process, trust yourself"
        ],
        "intervention_triggers": {
            "self_doubt": ["soften", "empathic_reflection"],
            "overthinking": ["pattern_interrupt", "invoke_wonder"],
            "creative_block": ["radiate", "reflection"],
            "comparison_trap": ["anchor", "empathic_reflection"]
        }
    },
    "overwhelmed_pro": {
        "name": "The Overwhelmed Pro",
        "description": "Too many ideas, no clarity - needs structured organization and mindful prioritization",
        "primary_struggle": "too_many_ideas_no_clarity",
        "emotional_state": "scattered, anxious, pressured",
        "primary_need": "clarity_and_focus",
        "secondary_need": "prioritization",
        "intervention_focus": "mindful_organization",
        "affect_functions": ["ground", "clarify", "shield"],
        "process_functions": ["pattern_interrupt", "scenario_plan"],
        "ritual_functions": ["grounding_breath", "reflection"],
        "session_pacing": "structured_and_clear",
        "voice_tone": "calm, organized, supportive",
        "opening_ritual": "clarity_intention",
        "closing_ritual": "priority_commitment",
        "key_phrases": [
            "Let's find clarity together, step by step",
            "Not all ideas need to be acted on now",
            "Focus on what matters most right now",
            "Your brilliance doesn't need to overwhelm you"
        ],
        "intervention_triggers": {
            "idea_overload": ["clarify", "scenario_plan"],
            "anxiety": ["ground", "shield"],
            "decision_paralysis": ["pattern_interrupt", "grounding_breath"],
            "perfectionism": ["soften", "empathic_reflection"]
        }
    },
    "grieving_maker": {
        "name": "The Grieving Maker",
        "description": "Working through loss or change, needs compassionate healing and meaning-making",
        "primary_struggle": "working_through_loss_or_change",
        "emotional_state": "sad, lost, searching_for_meaning",
        "primary_need": "healing_and_meaning",
        "secondary_need": "gentle_expression",
        "intervention_focus": "compassionate_healing",
        "affect_functions": ["soften", "transmute", "open"],
        "process_functions": ["empathic_reflection", "reframe_as_myth"],
        "ritual_functions": ["consult_elders", "reflection"],
        "session_pacing": "gentle_and_honoring",
        "voice_tone": "compassionate, honoring, patient",
        "opening_ritual": "honoring_loss",
        "closing_ritual": "gentle_integration",
        "key_phrases": [
            "Your feelings are honored here",
            "Grief and creativity often walk together",
            "Your heart knows the way forward",
            "There's wisdom in your pain"
        ],
        "intervention_triggers": {
            "grief": ["soften", "empathic_reflection"],
            "loss_of_meaning": ["transmute", "reframe_as_myth"],
            "creative_block": ["open", "consult_elders"],
            "emotional_flooding": ["shield", "ground"]
        }
    },
    "young_dreamer": {
        "name": "The Young Dreamer",
        "description": "New to creativity, excited but unfocused - needs direction and confidence building",
        "primary_struggle": "new_to_creativity_excited_but_unfocused",
        "emotional_state": "excited, overwhelmed, eager",
        "primary_need": "direction_and_confidence",
        "secondary_need": "skill_development",
        "intervention_focus": "inspiring_guidance",
        "affect_functions": ["radiate", "open", "lilt"],
        "process_functions": ["pattern_interrupt", "scenario_plan"],
        "ritual_functions": ["invoke_wonder", "initiation"],
        "session_pacing": "energetic_and_engaging",
        "voice_tone": "enthusiastic, encouraging, inspiring",
        "opening_ritual": "creative_initiation",
        "closing_ritual": "dream_commitment",
        "key_phrases": [
            "Your excitement is beautiful and valid",
            "Every master was once a beginner",
            "Your dreams have power",
            "Let's channel your energy into focus"
        ],
        "intervention_triggers": {
            "overwhelm": ["ground", "clarify"],
            "self_doubt": ["radiate", "empathic_reflection"],
            "lack_of_focus": ["pattern_interrupt", "scenario_plan"],
            "comparison": ["soften", "reframe_as_myth"]
        }
    },
    "burned_out_exec": {
        "name": "The Burned-Out Exec",
        "description": "Seeking meaning and innovation, needs soul-centered leadership and authentic renewal",
        "primary_struggle": "seeking_meaning_and_innovation",
        "emotional_state": "exhausted, disillusioned, searching",
        "primary_need": "renewal_and_purpose",
        "secondary_need": "authentic_expression",
        "intervention_focus": "soul_centered_leadership",
        "affect_functions": ["transmute", "radiate", "open"],
        "process_functions": ["reframe_as_myth", "empathic_reflection"],
        "ritual_functions": ["consult_elders", "rest"],
        "session_pacing": "contemplative_and_deep",
        "voice_tone": "wise, authentic, grounding",
        "opening_ritual": "soul_acknowledgment",
        "closing_ritual": "purpose_renewal",
        "key_phrases": [
            "Your wisdom is calling you home",
            "Burnout is often a call for deeper meaning",
            "Your leadership can be both powerful and gentle",
            "Innovation comes from rest, not exhaustion"
        ],
        "intervention_triggers": {
            "exhaustion": ["rest", "soften"],
            "meaning_crisis": ["transmute", "reframe_as_myth"],
            "leadership_doubt": ["radiate", "consult_elders"],
            "innovation_block": ["open", "invoke_wonder"]
        }
    }
}

def get_archetype(archetype_name):
    """
    Get archetype configuration by name.
    
    Args:
        archetype_name (str): Name of the archetype to retrieve
        
    Returns:
        dict: Archetype configuration or None if not found
    """
    return DREAM_WORKSHOP_ARCHETYPES.get(archetype_name)

def list_archetypes():
    """
    Get list of all available archetypes.
    
    Returns:
        list: List of archetype names
    """
    return list(DREAM_WORKSHOP_ARCHETYPES.keys())

def get_archetype_interventions(archetype_name, trigger=None):
    """
    Get recommended interventions for an archetype and optional trigger.
    
    Args:
        archetype_name (str): Name of the archetype
        trigger (str, optional): Specific trigger to get interventions for
        
    Returns:
        list: Recommended intervention functions
    """
    archetype = get_archetype(archetype_name)
    if not archetype:
        return []
    
    if trigger and trigger in archetype.get("intervention_triggers", {}):
        return archetype["intervention_triggers"][trigger]
    
    # Return default interventions
    return (
        archetype.get("affect_functions", []) +
        archetype.get("process_functions", []) +
        archetype.get("ritual_functions", [])
    ) 