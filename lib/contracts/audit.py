import json
from datetime import datetime

"""
Purpose: Log and retrieve A2A session state for audit/trust.
Scope: Central log for all agent session events.
Parent: session.py
Limitations: No cryptographic signing or secure persistence yet.
Consent: Level_2+
Review Cycle: Quarterly
"""
def log_event(session_id, event_type, details):
    """
    Purpose: Append an event to the session audit log.
    Args:
        session_id (str): Unique session identifier.
        event_type (str): e.g., 'start', 'update', 'pause', 'withdraw', 'end'
        details (dict): Additional event data.
    Returns: None
    Limitations: Writes to local file only (extend later).
    Consent: Level_2
    """
    with open(f'audit_{session_id}.log', 'a') as f:
        f.write(f"{datetime.now().isoformat()} | {event_type} | {json.dumps(details)}\n")
