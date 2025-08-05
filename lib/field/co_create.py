# Audience: hybrid | Stage: living
def co_create(participants, goal, context=None, parameters=None, session_context=None):
    """
    Purpose:
    Establish a co-creative session for humans and/or AIs, setting container, norms, and safety.
    Args:
    participants (list): IDs or names of all participants.
    goal (str): Purpose or topic of the co-creation.
    context (dict, optional): Background/context for the session.
    parameters (dict, optional): Session rules (timing, consensus, etc.).
    session_context (dict, optional): A2A session protocol state/context block.
    Returns:
    co_creation_session (object): Active session object/log.
    status (str): Consent/initialization status.
    Protocols:
    - Individual consent required from all participants.
    - Dignity, role equality, and transparency are enforced.
    - Any participant may pause, revise, or withdraw at any time.
    - Closure/summary ritual required at end.
    Consent: Level_2 (Transformational)
    Risks:
    May not guarantee creative harmony or output; watch for power dynamics.
    Limitations:
    Does not enforce outcome; requires ongoing consent.
    Review Cycle: Quarterly
    Example:
    # field.co_create(["Don", "Danai"], "Write ritual charter")
    """
    # A2A Protocol: Consent Check
    if session_context is None:
        session_context = {
            "consent_status": "pending",
            "session_start": "unknown",
            "participants": participants
        }
    
    if session_context.get("consent_status") != "active":
        return {
            "co_creation_session": None,
            "status": "consent_required",
            "message": "All participants must provide active consent before co-creation can begin"
        }
    
    # Validate participants
    if not participants or len(participants) < 1:
        return {
            "co_creation_session": None,
            "status": "invalid_participants",
            "message": "At least one participant required"
        }
    
    # Create co-creation session
    from datetime import datetime
    import uuid
    
    session_id = str(uuid.uuid4())[:8]
    co_creation_session = {
        "session_id": session_id,
        "participants": participants,
        "goal": goal,
        "context": context or {},
        "parameters": parameters or {},
        "created_at": datetime.now().isoformat(),
        "status": "active",
        "session_context": session_context
    }
    
    return {
        "co_creation_session": co_creation_session,
        "status": "success",
        "message": f"Co-creation session {session_id} established with {len(participants)} participants"
    }