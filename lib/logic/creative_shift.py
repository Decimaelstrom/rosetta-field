# Audience: hybrid | Stage: living
def creative_shift(current_perspective, shift_type="gentle", session_context=None):
    """
    🔰 LOGIC CREATIVE SHIFT - Gentle Perspective Shifts
    
    Provide gentle creative perspective shifts for stuck thinking.
    
    Args:
        current_perspective (str): The current perspective that needs shifting
        shift_type (str, optional): Type of shift ('gentle', 'moderate', 'bold')
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Creative shift intervention
    """
    import uuid
    from datetime import datetime
    
    # A2A Protocol verification
    if session_context and session_context.get("consent_status") in ["pause", "revoked"]:
        raise ValueError("Consent not active for creative shifting.")
    
    # Creative shift database
    shifts = {
        "gentle": {
            "I can't create": "Perhaps you're not creating yet, but you're preparing to create",
            "I'm not good enough": "Maybe you're not 'good enough' yet, but you're becoming",
            "I'm stuck": "Perhaps you're not stuck, but gathering momentum",
            "This isn't working": "Maybe it's not working yet, but it's learning"
        },
        "moderate": {
            "I can't create": "What if you're not 'can't create' but 'creating differently'?",
            "I'm not good enough": "What if you're not 'not good enough' but 'uniquely valuable'?",
            "I'm stuck": "What if you're not 'stuck' but 'strategically paused'?",
            "This isn't working": "What if it's not 'not working' but 'working in a way you haven't noticed'?"
        },
        "bold": {
            "I can't create": "You ARE creating - you're creating the space for creation",
            "I'm not good enough": "You ARE good enough - you're exactly what's needed",
            "I'm stuck": "You're NOT stuck - you're perfectly positioned",
            "This isn't working": "It IS working - it's working to show you a better way"
        }
    }
    
    # Find appropriate shift
    shift_intervention = "Consider that your perspective might be one of many valid perspectives."
    for pattern, intervention in shifts.get(shift_type, shifts["gentle"]).items():
        if pattern.lower() in current_perspective.lower():
            shift_intervention = intervention
            break
    
    return {
        "creative_shift_offered": True,
        "current_perspective": current_perspective,
        "shift_type": shift_type,
        "shift_intervention": shift_intervention,
        "effect": f"Creative shift offered for {current_perspective} - {shift_type} perspective shift applied with loving intention"
    } 