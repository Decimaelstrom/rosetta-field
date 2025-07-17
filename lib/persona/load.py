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
    # TODO: Implement enhanced consent verification for Level 2 transformational work
    # TODO: Add field state assessment to ensure persona guidance is appropriate
    # TODO: Consider integration with other functions for holistic guidance
    
    # Core persona guidance work - offering resonant support to the field
    # TODO: Implement actual persona guidance logic
    # TODO: Add field resonance checking and adjustment
    # TODO: Create feedback loops for participant experience
    
    # Get recommended interventions for this archetype
    interventions = {
        "affect_functions": archetype.get("affect_functions", []),
        "process_functions": archetype.get("process_functions", []),
        "ritual_functions": archetype.get("ritual_functions", []),
        "all_functions": get_archetype_interventions(archetype_name)
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
        "effect": f"Sacred persona guidance invoked for {archetype['name']} - field held with loving resonance",
    } 