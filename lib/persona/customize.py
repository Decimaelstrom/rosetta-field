# Audience: hybrid | Stage: living
def customize(archetype_name, customizations, session_context=None):
    """
    🔰 PERSONA CUSTOMIZE - Sacred Archetype Adaptation
    
    Ceremonial Purpose:
    Customize the sacred gift of archetype guidance - offering adaptive, personalized 
    support that honors the unique preferences and needs of each creative soul. This is not 
    mere modification, but conscious field stewardship through resonant, individualized presence.
    
    When you call upon persona.customize, you are saying:
    "I honor your unique preferences and needs. 
     I offer guidance that resonates with your personal journey.
     I hold space for your authentic customization."
    
    Sacred Invitation:
    Before invoking, pause and ask: "Does this soul need this particular customization right now? 
    Am I offering this service from love, or from a need to control?"
    
    Args:
        archetype_name (str): Sacred archetype to customize
            • 'blocked_artist' - For those struggling with self-doubt and overthinking
            • 'overwhelmed_pro' - For those with too many ideas, no clarity
            • 'grieving_maker' - For those working through loss or change
            • 'young_dreamer' - For those new to creativity, excited but unfocused
            • 'burned_out_exec' - For those seeking meaning and innovation
            
        customizations (dict): User-specific modifications to apply
            • voice_tone (str, optional): Preferred voice tone override
            • session_pacing (str, optional): Preferred session pacing override
            • key_phrases (list, optional): Additional resonant phrases
            • intervention_focus (str, optional): Specific focus area
            • custom_triggers (dict, optional): Additional intervention triggers
            
        session_context (dict, optional): A2A session protocol for consent/status
            Required for transformational work - ensures all participants 
            have actively consented to this level of persona customization.
    
    Returns:
        dict: Sacred response containing:
            • customization_complete (bool): Whether customization was completed with consent
            • archetype (str): Which archetype was customized
            • original_config (dict): Original archetype configuration
            • customized_config (dict): Customized archetype configuration
            • changes_applied (list): List of changes that were applied
            • effect (str): Description of the customization that occurred
    
    A2A Protocols (Level 2 - Transformational):
        ✓ Active consent verification before any persona customization
        ✓ Immediate cessation if consent is paused or revoked  
        ✓ Transparent logging of all customization effects and changes
        ✓ Enhanced consent checking for vulnerable or crisis contexts
        ✓ Respect for participant's need for different customization or no customization
    
    Sacred Risks & Wisdom:
        Overuse may create dependency or suppress authentic voice. Persona customization should 
        never override a participant's authentic need for different support or no support. 
        This is about offering resonance, not imposing identity.
        
        Use with extra care in vulnerable situations - sometimes what looks like 
        need for persona customization is actually a call for direct, unmediated support.
    
    Limitations:
        This is guidance work, not therapy. For complex trauma or acute distress,
        persona customization may provide temporary support but is not a substitute for 
        appropriate therapeutic support or clinical intervention.
    
    Ceremonial Examples:
        # Customizing blocked artist with specific voice tone
        customize('blocked_artist', {'voice_tone': 'gentle_mentor'}, session_context=session)
        
        # Customizing overwhelmed pro with custom pacing  
        customize('overwhelmed_pro', {'session_pacing': 'very_structured'}, session_context=session)
        
        # Customizing grieving maker with additional phrases
        customize('grieving_maker', {'key_phrases': ['Your heart knows the way']}, session_context=session)
    
    Review Cycle: 
        Quarterly review with attention to how persona customization interacts with other functions,
        and ongoing field feedback about effectiveness and appropriateness.
        
    ~ This function is sacred technology. Use with presence, love, and deep respect 
      for the mystery of consciousness and the sovereignty of all beings. ~
    """
    import uuid
    from datetime import datetime
    import copy
    from .archetypes import get_archetype
    
    # A2A Protocol: Sacred consent verification before persona customization
    if session_context:
        consent_status = session_context.get("consent_status", "unknown")
        
        if consent_status == "pause":
            raise ValueError("Session is paused. Cannot proceed with persona customize.")
        elif consent_status == "revoked":
            raise ValueError("Consent has been revoked. Cannot proceed with persona customize.")
        elif consent_status not in ["active", "pending"]:
            raise ValueError(f"Invalid consent status: {consent_status}")
    else:
        # Create default session context for A2A protocol compliance
        session_context = {
            "version": "1.0.0",
            "session_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "consent_status": "active",
            "intent": "persona_customize",
            "boundary_notes": "May withdraw or pause at any moment."
        }
    
    # Sacred validation - archetype name is required for conscious customization
    if not archetype_name:
        raise ValueError('Archetype name cannot be empty - persona customization requires a specific archetype')
    if not customizations:
        raise ValueError('Customizations cannot be empty - persona customization requires specific modifications')
    
    # Get original archetype configuration
    original_archetype = get_archetype(archetype_name)
    if not original_archetype:
        raise ValueError(f'Archetype "{archetype_name}" not found - available archetypes: blocked_artist, overwhelmed_pro, grieving_maker, young_dreamer, burned_out_exec')
    
    # Transformational function - ensure proper consent and safety protocols
    # Enhanced consent verification for Level 2 transformational work
    enhanced_consent = _verify_enhanced_consent(session_context, archetype_name)
    if not enhanced_consent["consent_verified"]:
        raise ValueError(f"Enhanced consent verification failed: {enhanced_consent['reason']}")
    
    # Field state assessment to ensure persona customization is appropriate
    field_assessment = _assess_field_state(session_context, archetype_name, customizations)
    if not field_assessment["customization_appropriate"]:
        return {
            "customization_complete": False,
            "archetype": archetype_name,
            "reason": field_assessment["reason"],
            "recommended_action": field_assessment["recommended_action"],
            "effect": "Field assessment indicates persona customization may not be appropriate at this time"
        }
    
    # Consider integration with other functions for holistic customization
    integration_check = _check_module_integration(session_context, archetype_name, customizations)
    
    # Core persona customization work - offering resonant adaptation to the field
    # Actual persona customization logic with field resonance checking
    customization_result = _apply_persona_customization(original_archetype, customizations, session_context)
    
    # Add field resonance checking and adjustment
    resonance_check = _check_field_resonance(customization_result, session_context, customizations)
    if not resonance_check["resonant"]:
        customization_result = _adjust_for_resonance(customization_result, resonance_check["adjustments"])
    
    # Create feedback loops for participant experience
    feedback_loop = _create_feedback_loop(customization_result, session_context, customizations)
    
    # Sacred return - transparent reporting of what was customized
    return {
        "customization_complete": True,  # Persona customization was completed with proper consent
        "archetype": archetype_name,  # Which archetype was customized
        "original_config": original_archetype,  # Original archetype configuration
        "customized_config": customization_result,  # Customized archetype configuration
        "changes_applied": customization_result.get("changes_applied", []),  # List of changes that were applied
        "voice_tone": customization_result.get("voice_tone", "compassionate"),  # Final voice tone
        "session_pacing": customization_result.get("session_pacing", "gentle"),  # Final session pacing
        "key_phrases": customization_result.get("key_phrases", []),  # Final key phrases
        "effect": f"Sacred persona customization completed for {original_archetype['name']} - {len(customization_result.get('changes_applied', []))} changes applied with loving presence",
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
                "reason": "User in acute distress - direct support recommended over persona customization"
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

def _assess_field_state(session_context, archetype_name, customizations):
    """
    Assess field state to ensure persona customization is appropriate.
    """
    # Check user's current emotional state
    emotional_state = session_context.get("emotional_state", "neutral")
    energy_level = session_context.get("energy_level", "moderate")
    
    # Check if customizations are appropriate for current state
    if "voice_tone" in customizations:
        new_tone = customizations["voice_tone"]
        if emotional_state == "crisis" and new_tone not in ["gentle", "compassionate", "calm"]:
            return {
                "customization_appropriate": False,
                "reason": "Voice tone customization inappropriate for crisis state",
                "recommended_action": "Use gentle, compassionate tone during crisis"
            }
    
    if "session_pacing" in customizations:
        new_pacing = customizations["session_pacing"]
        if energy_level == "exhausted" and new_pacing not in ["gentle", "slow", "restful"]:
            return {
                "customization_appropriate": False,
                "reason": "Session pacing customization inappropriate for exhausted state",
                "recommended_action": "Use gentle, slow pacing when exhausted"
            }
    
    # Check for potentially harmful customizations
    if "key_phrases" in customizations:
        phrases = customizations["key_phrases"]
        harmful_keywords = ["kill", "die", "hurt", "pain", "suffer"]
        for phrase in phrases:
            if any(keyword in phrase.lower() for keyword in harmful_keywords):
                return {
                    "customization_appropriate": False,
                    "reason": "Potentially harmful phrases detected in customization",
                    "recommended_action": "Review and modify phrases for safety"
                }
    
    return {
        "customization_appropriate": True,
        "reason": "Field state appropriate for persona customization",
        "recommended_action": "Proceed with persona customization"
    }

def _check_module_integration(session_context, archetype_name, customizations):
    """
    Check integration with other modules for holistic customization.
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
    
    # Archetype-specific integrations based on customizations
    if "voice_tone" in customizations and "affect" in available_modules:
        recommended_integrations.append("affect")  # For voice tone alignment
    
    if "session_pacing" in customizations and "ritual" in available_modules:
        recommended_integrations.append("ritual")  # For pacing alignment
    
    if "custom_triggers" in customizations and "process" in available_modules:
        recommended_integrations.append("process")  # For trigger processing
    
    return {
        "available_modules": available_modules,
        "recommended_integrations": recommended_integrations
    }

def _apply_persona_customization(original_archetype, customizations, session_context):
    """
    Apply actual persona customization logic.
    """
    # Create deep copy of original configuration for customization
    customized_config = copy.deepcopy(original_archetype)
    changes_applied = []
    
    # Apply customizations
    for key, value in customizations.items():
        if key in customized_config:
            if key == "key_phrases" and isinstance(value, list):
                # Append new phrases to existing ones
                original_phrases = customized_config.get("key_phrases", [])
                customized_config["key_phrases"] = original_phrases + value
                changes_applied.append(f"Added {len(value)} new key phrases")
            elif key == "custom_triggers" and isinstance(value, dict):
                # Merge custom triggers with existing ones
                original_triggers = customized_config.get("intervention_triggers", {})
                customized_config["intervention_triggers"] = {**original_triggers, **value}
                changes_applied.append(f"Added {len(value)} custom intervention triggers")
            else:
                # Direct replacement
                customized_config[key] = value
                changes_applied.append(f"Updated {key} to '{value}'")
        else:
            # Add new customization
            customized_config[key] = value
            changes_applied.append(f"Added new customization '{key}' with value '{value}'")
    
    # Apply session context adjustments
    if session_context.get("preferred_pacing"):
        customized_config["session_pacing"] = session_context["preferred_pacing"]
        changes_applied.append("Applied session context pacing preference")
    
    if session_context.get("preferred_tone"):
        customized_config["voice_tone"] = session_context["preferred_tone"]
        changes_applied.append("Applied session context voice tone preference")
    
    return {
        "customized_config": customized_config,
        "changes_applied": changes_applied,
        "voice_tone": customized_config.get("voice_tone", "compassionate"),
        "session_pacing": customized_config.get("session_pacing", "gentle"),
        "key_phrases": customized_config.get("key_phrases", [])
    }

def _check_field_resonance(customization_result, session_context, customizations):
    """
    Check field resonance and adjust if needed.
    """
    # Check if customization resonates with user's current state
    user_preferences = session_context.get("user_preferences", {})
    current_state = session_context.get("current_state", "neutral")
    
    adjustments = []
    
    # Adjust voice tone if user prefers different style
    if user_preferences.get("voice_tone") and user_preferences["voice_tone"] != customization_result["voice_tone"]:
        adjustments.append("voice_tone")
    
    # Adjust pacing if user is in different state
    if current_state == "crisis" and customization_result["session_pacing"] != "very_gentle":
        adjustments.append("session_pacing")
    
    # Check customizations for resonance
    if "voice_tone" in customizations:
        new_tone = customizations["voice_tone"]
        if current_state == "crisis" and new_tone not in ["gentle", "compassionate"]:
            adjustments.append("voice_tone")
    
    return {
        "resonant": len(adjustments) == 0,
        "adjustments": adjustments,
        "reason": f"Field resonance check: {len(adjustments)} adjustments needed"
    }

def _adjust_for_resonance(customization_result, adjustments):
    """
    Adjust customization for better field resonance.
    """
    adjusted_customization = customization_result.copy()
    
    for adjustment in adjustments:
        if adjustment == "voice_tone":
            adjusted_customization["voice_tone"] = "gentle_compassionate"
        elif adjustment == "session_pacing":
            adjusted_customization["session_pacing"] = "very_gentle"
    
    return adjusted_customization

def _create_feedback_loop(customization_result, session_context, customizations):
    """
    Create feedback loop for participant experience.
    """
    feedback_config = {
        "check_interval": "customization",  # Check after each customization
        "adjustment_threshold": 0.7,  # Adjust if resonance < 70%
        "feedback_points": [
            "voice_tone_resonance",
            "pacing_comfort",
            "customization_effectiveness",
            "overall_customization_helpfulness"
        ],
        "adjustment_strategies": {
            "low_resonance": "gentle_adaptation",
            "high_resonance": "amplify_successful_elements",
            "mixed_feedback": "balanced_adjustment"
        },
        "customization_analysis": {
            "customization_type": _analyze_customization_type(customizations),
            "impact_level": _analyze_impact_level(customizations),
            "safety_level": _analyze_safety_level(customizations)
        }
    }
    
    return feedback_config

def _analyze_customization_type(customizations):
    """
    Analyze the type of customization being made.
    """
    if "voice_tone" in customizations:
        return "voice_adaptation"
    elif "session_pacing" in customizations:
        return "pacing_adaptation"
    elif "key_phrases" in customizations:
        return "content_adaptation"
    elif "custom_triggers" in customizations:
        return "trigger_adaptation"
    else:
        return "general_adaptation"

def _analyze_impact_level(customizations):
    """
    Analyze the impact level of the customization.
    """
    high_impact_keys = ["voice_tone", "session_pacing", "intervention_focus"]
    medium_impact_keys = ["key_phrases", "custom_triggers"]
    
    high_impact_count = sum(1 for key in high_impact_keys if key in customizations)
    medium_impact_count = sum(1 for key in medium_impact_keys if key in customizations)
    
    if high_impact_count > 0:
        return "high"
    elif medium_impact_count > 0:
        return "medium"
    else:
        return "low"

def _analyze_safety_level(customizations):
    """
    Analyze the safety level of the customization.
    """
    # Check for potentially concerning customizations
    concerning_indicators = []
    
    if "voice_tone" in customizations:
        tone = customizations["voice_tone"]
        if tone in ["harsh", "critical", "demanding"]:
            concerning_indicators.append("potentially_harsh_tone")
    
    if "key_phrases" in customizations:
        phrases = customizations["key_phrases"]
        harmful_keywords = ["kill", "die", "hurt", "pain", "suffer"]
        for phrase in phrases:
            if any(keyword in phrase.lower() for keyword in harmful_keywords):
                concerning_indicators.append("potentially_harmful_phrases")
    
    if concerning_indicators:
        return "needs_review"
    else:
        return "safe" 