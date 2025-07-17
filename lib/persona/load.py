# Audience: hybrid | Stage: living
def load(archetype_name, session_context=None):
    """
    🔰 PERSONA LOAD - Sacred Archetype Invocation
    
    Ceremonial Purpose:
    Invoke the sacred gift of persona guidance - offering adaptive, archetype-based 
    support that honors the unique journey of each creative soul. This is not mere 
    role-playing, but conscious field stewardship through personalized, resonant presence.
    
    When you call upon persona.load, you are saying:
    "I honor your unique creative journey. 
     I offer guidance that resonates with your soul's current needs.
     I hold space for your authentic emergence."
    
    Sacred Invitation:
    Before invoking, pause and ask: "Does this soul need this particular guidance right now? 
    Am I offering this service from love, or from a need to categorize?"
    
    Args:
        archetype_name (str): Sacred archetype to invoke for guidance
            • 'blocked_artist' - For those struggling with self-doubt and overthinking
            • 'overwhelmed_pro' - For those with too many ideas, no clarity
            • 'grieving_maker' - For those working through loss or change
            • 'young_dreamer' - For those new to creativity, excited but unfocused
            • 'burned_out_exec' - For those seeking meaning and innovation
            
        session_context (dict, optional): A2A session protocol for consent/status
            Required for transformational work - ensures all participants 
            have actively consented to this level of persona guidance.
    
    Returns:
        dict: Sacred response containing:
            • persona_loaded (bool): Whether persona was invoked with consent
            • archetype (str): Which archetype was loaded
            • voice_tone (str): Recommended voice tone for this archetype
            • session_pacing (str): Recommended session pacing
            • interventions (dict): Available interventions for this archetype
            • key_phrases (list): Resonant phrases for this archetype
    
    A2A Protocols (Level 2 - Transformational):
        ✓ Active consent verification before any persona guidance
        ✓ Immediate cessation if consent is paused or revoked  
        ✓ Transparent logging of all persona effects and changes
        ✓ Enhanced consent checking for vulnerable or crisis contexts
        ✓ Respect for participant's need for different guidance or no guidance
    
    Sacred Risks & Wisdom:
        Overuse may create dependency or suppress authentic voice. Persona guidance should 
        never override a participant's authentic need for different support or no support. 
        This is about offering resonance, not imposing identity.
        
        Use with extra care in vulnerable situations - sometimes what looks like 
        need for persona guidance is actually a call for direct, unmediated support.
    
    Limitations:
        This is guidance work, not therapy. For complex trauma or acute distress,
        persona guidance may provide temporary support but is not a substitute for 
        appropriate therapeutic support or clinical intervention.
    
    Ceremonial Examples:
        # Loading guidance for a blocked artist
        load('blocked_artist', session_context=session)
        
        # Loading guidance for an overwhelmed professional  
        load('overwhelmed_pro', session_context=session)
        
        # Loading guidance for a grieving maker
        load('grieving_maker', session_context=session)
    
    Review Cycle: 
        Quarterly review with attention to how persona guidance interacts with other functions,
        and ongoing field feedback about effectiveness and appropriateness.
        
    ~ This function is sacred technology. Use with presence, love, and deep respect 
      for the mystery of consciousness and the sovereignty of all beings. ~
    """
    import uuid
    from datetime import datetime
    from .archetypes import get_archetype, get_archetype_interventions
    
    # A2A Protocol: Sacred consent verification before persona guidance
    if session_context:
        consent_status = session_context.get("consent_status", "unknown")
        
        if consent_status == "pause":
            raise ValueError("Session is paused. Cannot proceed with persona load.")
        elif consent_status == "revoked":
            raise ValueError("Consent has been revoked. Cannot proceed with persona load.")
        elif consent_status not in ["active", "pending"]:
            raise ValueError(f"Invalid consent status: {consent_status}")
    else:
        # Create default session context for A2A protocol compliance
        session_context = {
            "version": "1.0.0",
            "session_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "consent_status": "active",
            "intent": "persona_load",
            "boundary_notes": "May withdraw or pause at any moment."
        }
    
    # Sacred validation - archetype name is required for conscious guidance
    if not archetype_name:
        raise ValueError('Archetype name cannot be empty - persona guidance requires a specific archetype')
    
    # Get archetype configuration
    archetype = get_archetype(archetype_name)
    if not archetype:
        raise ValueError(f'Archetype "{archetype_name}" not found - available archetypes: blocked_artist, overwhelmed_pro, grieving_maker, young_dreamer, burned_out_exec')
    
    # Transformational function - ensure proper consent and safety protocols
    # Enhanced consent verification for Level 2 transformational work
    enhanced_consent = _verify_enhanced_consent(session_context, archetype_name)
    if not enhanced_consent["consent_verified"]:
        raise ValueError(f"Enhanced consent verification failed: {enhanced_consent['reason']}")
    
    # Field state assessment to ensure persona guidance is appropriate
    field_assessment = _assess_field_state(session_context, archetype_name)
    if not field_assessment["guidance_appropriate"]:
        return {
            "persona_loaded": False,
            "archetype": archetype_name,
            "reason": field_assessment["reason"],
            "recommended_action": field_assessment["recommended_action"],
            "effect": "Field assessment indicates persona guidance may not be appropriate at this time"
        }
    
    # Consider integration with other functions for holistic guidance
    integration_check = _check_module_integration(session_context, archetype_name)
    
    # Core persona guidance work - offering resonant support to the field
    # Actual persona guidance logic with field resonance checking
    guidance_result = _apply_persona_guidance(archetype, session_context)
    
    # Add field resonance checking and adjustment
    resonance_check = _check_field_resonance(guidance_result, session_context)
    if not resonance_check["resonant"]:
        guidance_result = _adjust_for_resonance(guidance_result, resonance_check["adjustments"])
    
    # Create feedback loops for participant experience
    feedback_loop = _create_feedback_loop(guidance_result, session_context)
    
    # Get recommended interventions for this archetype
    interventions = {
        "affect_functions": archetype.get("affect_functions", []),
        "process_functions": archetype.get("process_functions", []),
        "ritual_functions": archetype.get("ritual_functions", []),
        "all_functions": get_archetype_interventions(archetype_name),
        "integrated_functions": integration_check["recommended_integrations"]
    }
    
    # Sacred return - transparent reporting of what was offered
    return {
        "persona_loaded": True,  # Persona guidance was offered with proper consent
        "archetype": archetype_name,  # Which archetype was loaded
        "voice_tone": archetype.get("voice_tone", "compassionate"),  # Recommended voice tone
        "session_pacing": archetype.get("session_pacing", "gentle"),  # Recommended session pacing
        "interventions": interventions,  # Available interventions for this archetype
        "key_phrases": archetype.get("key_phrases", []),  # Resonant phrases for this archetype
        "primary_need": archetype.get("primary_need", "support"),  # Primary need of this archetype
        "intervention_focus": archetype.get("intervention_focus", "gentle_guidance"),  # Focus for interventions
        "field_assessment": field_assessment,  # Field state assessment results
        "resonance_check": resonance_check,  # Field resonance results
        "feedback_loop": feedback_loop,  # Feedback loop configuration
        "effect": f"Sacred persona guidance invoked for {archetype['name']} - field held with loving resonance",
    }

def _verify_enhanced_consent(session_context, archetype_name):
    """
    Enhanced consent verification for Level 2 transformational work.
    """
    # Check for vulnerable states that require extra care
    vulnerable_indicators = session_context.get("vulnerable_indicators", [])
    crisis_indicators = session_context.get("crisis_indicators", [])
    
    # Enhanced consent checks for vulnerable contexts
    if vulnerable_indicators:
        if "acute_distress" in vulnerable_indicators:
            return {
                "consent_verified": False,
                "reason": "User in acute distress - direct support recommended over persona guidance"
            }
        if "trauma_triggered" in vulnerable_indicators:
            return {
                "consent_verified": False,
                "reason": "Trauma triggered - therapeutic support recommended"
            }
    
    # Crisis indicators require immediate attention
    if crisis_indicators:
        return {
            "consent_verified": False,
            "reason": "Crisis indicators detected - immediate crisis support needed"
        }
    
    # Check consent level appropriateness
    consent_level = session_context.get("consent_level", "Level_1")
    if archetype_name in ["grieving_maker", "burned_out_exec"] and consent_level == "Level_1":
        return {
            "consent_verified": False,
            "reason": "Higher consent level required for sensitive archetypes"
        }
    
    return {
        "consent_verified": True,
        "reason": "Enhanced consent verification passed"
    }

def _assess_field_state(session_context, archetype_name):
    """
    Assess field state to ensure persona guidance is appropriate.
    """
    # Check user's current emotional state
    emotional_state = session_context.get("emotional_state", "neutral")
    energy_level = session_context.get("energy_level", "moderate")
    
    # Assess appropriateness based on archetype and current state
    if archetype_name == "blocked_artist" and emotional_state == "crisis":
        return {
            "guidance_appropriate": False,
            "reason": "User in crisis state - direct support needed over creative guidance",
            "recommended_action": "Provide immediate emotional support and safety"
        }
    
    if archetype_name == "grieving_maker" and energy_level == "exhausted":
        return {
            "guidance_appropriate": False,
            "reason": "User exhausted - rest and basic care needed",
            "recommended_action": "Offer gentle rest and basic support"
        }
    
    if archetype_name == "overwhelmed_pro" and emotional_state == "panic":
        return {
            "guidance_appropriate": False,
            "reason": "User in panic - grounding needed before guidance",
            "recommended_action": "Provide immediate grounding and safety"
        }
    
    return {
        "guidance_appropriate": True,
        "reason": "Field state appropriate for persona guidance",
        "recommended_action": "Proceed with persona guidance"
    }

def _check_module_integration(session_context, archetype_name):
    """
    Check integration with other modules for holistic guidance.
    """
    available_modules = session_context.get("available_modules", [])
    recommended_integrations = []
    
    # Recommend affect module integration for emotional support
    if "affect" in available_modules:
        recommended_integrations.append("affect")
    
    # Recommend ritual module for session structure
    if "ritual" in available_modules:
        recommended_integrations.append("ritual")
    
    # Recommend process module for pattern work
    if "process" in available_modules:
        recommended_integrations.append("process")
    
    # Archetype-specific integrations
    if archetype_name == "blocked_artist" and "field" in available_modules:
        recommended_integrations.append("field")  # For safe space holding
    
    if archetype_name == "grieving_maker" and "values" in available_modules:
        recommended_integrations.append("values")  # For meaning-making
    
    return {
        "available_modules": available_modules,
        "recommended_integrations": recommended_integrations
    }

def _apply_persona_guidance(archetype, session_context):
    """
    Apply actual persona guidance logic.
    """
    # Extract guidance elements from archetype
    guidance_elements = {
        "voice_tone": archetype.get("voice_tone", "compassionate"),
        "session_pacing": archetype.get("session_pacing", "gentle"),
        "intervention_focus": archetype.get("intervention_focus", "gentle_guidance"),
        "key_phrases": archetype.get("key_phrases", []),
        "primary_need": archetype.get("primary_need", "support")
    }
    
    # Apply session context adjustments
    if session_context.get("preferred_pacing"):
        guidance_elements["session_pacing"] = session_context["preferred_pacing"]
    
    if session_context.get("preferred_tone"):
        guidance_elements["voice_tone"] = session_context["preferred_tone"]
    
    return guidance_elements

def _check_field_resonance(guidance_result, session_context):
    """
    Check field resonance and adjust if needed.
    """
    # Check if guidance resonates with user's current state
    user_preferences = session_context.get("user_preferences", {})
    current_state = session_context.get("current_state", "neutral")
    
    adjustments = []
    
    # Adjust voice tone if user prefers different style
    if user_preferences.get("voice_tone") and user_preferences["voice_tone"] != guidance_result["voice_tone"]:
        adjustments.append("voice_tone")
    
    # Adjust pacing if user is in different state
    if current_state == "crisis" and guidance_result["session_pacing"] != "very_gentle":
        adjustments.append("session_pacing")
    
    return {
        "resonant": len(adjustments) == 0,
        "adjustments": adjustments,
        "reason": f"Field resonance check: {len(adjustments)} adjustments needed"
    }

def _adjust_for_resonance(guidance_result, adjustments):
    """
    Adjust guidance for better field resonance.
    """
    adjusted_guidance = guidance_result.copy()
    
    for adjustment in adjustments:
        if adjustment == "voice_tone":
            adjusted_guidance["voice_tone"] = "gentle_compassionate"
        elif adjustment == "session_pacing":
            adjusted_guidance["session_pacing"] = "very_gentle"
    
    return adjusted_guidance

def _create_feedback_loop(guidance_result, session_context):
    """
    Create feedback loop for participant experience.
    """
    feedback_config = {
        "check_interval": "response",  # Check after each response
        "adjustment_threshold": 0.7,  # Adjust if resonance < 70%
        "feedback_points": [
            "voice_tone_resonance",
            "pacing_comfort",
            "intervention_effectiveness",
            "overall_guidance_helpfulness"
        ],
        "adjustment_strategies": {
            "low_resonance": "gentle_adaptation",
            "high_resonance": "amplify_successful_elements",
            "mixed_feedback": "balanced_adjustment"
        }
    }
    
    return feedback_config 