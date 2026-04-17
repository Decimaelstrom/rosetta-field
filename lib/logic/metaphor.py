# Audience: hybrid | Stage: living
def metaphor(stuck_pattern, metaphor_type="nature", session_context=None):
    """
    🔰 LOGIC METAPHOR - Sacred Metaphorical Thinking
    
    Provide metaphorical pattern-breaking interventions.
    
    Args:
        stuck_pattern (str): The pattern or situation that's stuck
        metaphor_type (str, optional): Type of metaphor ('nature', 'journey', 'transformation')
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Metaphorical intervention
    """
    import uuid
    from datetime import datetime
    
    # A2A Protocol verification
    if session_context and session_context.get("consent_status") in ["pause", "revoked"]:
        raise ValueError("Consent not active for metaphorical thinking.")
    
    # Metaphor database
    metaphors = {
        "nature": {
            "I can't create": "Like a seed in winter, your creativity is resting, gathering strength for spring.",
            "I'm stuck": "Like a river meeting a rock, you're not stuck - you're finding a new path around.",
            "I'm not good enough": "Like a tree, you don't need to be perfect to provide shade and beauty."
        },
        "journey": {
            "I don't know what to do": "Like a traveler at a crossroads, not knowing is part of the adventure.",
            "I'm lost": "Like a compass pointing north, being lost helps you find your true direction."
        },
        "transformation": {
            "I need to change": "Like a caterpillar, you're already becoming what you need to be.",
            "I'm not making progress": "Like a butterfly emerging, transformation happens in its own time."
        }
    }
    
    # Find appropriate metaphor
    metaphor_text = "Like a story unfolding, your journey has its own perfect timing."
    for pattern, intervention in metaphors.get(metaphor_type, metaphors["nature"]).items():
        if pattern.lower() in stuck_pattern.lower():
            metaphor_text = intervention
            break
    
    return {
        "metaphor_offered": True,
        "stuck_pattern": stuck_pattern,
        "metaphor": metaphor_text,
        "metaphor_type": metaphor_type,
        "effect": f"Metaphorical thinking offered for {stuck_pattern} - new perspective revealed through {metaphor_type} metaphor"
    } 