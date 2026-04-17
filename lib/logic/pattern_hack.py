# Audience: hybrid | Stage: living
def pattern_hack(stuck_pattern, hack_type="perspective", session_context=None):
    """
    🔰 LOGIC PATTERN HACK - Advanced Pattern-Breaking
    
    Provide advanced pattern-breaking techniques for creative blocks.
    
    Args:
        stuck_pattern (str): The pattern that needs hacking
        hack_type (str, optional): Type of hack ('perspective', 'constraint', 'randomness')
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Pattern hack intervention
    """
    import uuid
    from datetime import datetime
    
    # A2A Protocol verification
    if session_context and session_context.get("consent_status") in ["pause", "revoked"]:
        raise ValueError("Consent not active for pattern hacking.")
    
    # Pattern hack database
    hacks = {
        "perspective": {
            "I can't create": "What if you're not creating for yourself, but for someone who needs exactly what you have to offer?",
            "I'm stuck": "What if being stuck is actually the universe's way of saying 'wait, there's something better coming'?",
            "This isn't working": "What if 'not working' is the perfect setup for something that will work even better?"
        },
        "constraint": {
            "I have too many options": "What if you could only use 3 materials? What would you create?",
            "I don't know where to start": "What if you had to start with the color blue?",
            "I'm overwhelmed": "What if you could only work for 5 minutes? What would you do?"
        },
        "randomness": {
            "I need inspiration": "Pick a random object in your room and make it the center of your creation",
            "I'm bored": "Do the opposite of what you think you should do",
            "I'm stuck": "Ask yourself: 'What would a 5-year-old do?'"
        }
    }
    
    # Find appropriate hack
    hack_intervention = "What if the problem is actually the solution?"
    for pattern, intervention in hacks.get(hack_type, hacks["perspective"]).items():
        if pattern.lower() in stuck_pattern.lower():
            hack_intervention = intervention
            break
    
    return {
        "pattern_hack_offered": True,
        "stuck_pattern": stuck_pattern,
        "hack_type": hack_type,
        "hack_intervention": hack_intervention,
        "effect": f"Pattern hack offered for {stuck_pattern} - {hack_type} technique applied for creative breakthrough"
    } 