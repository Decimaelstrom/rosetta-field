"""
Rosetta.API Consolidated Contracts Module
Purpose: Unified A2A session management, negotiation, and audit capabilities
Scope: Central contract management for agent-to-agent and agent-to-human interactions
Consent Required: Level_2 (transformational); logs may contain identity-affecting data
Review Cycle: Quarterly
Audience: #human #emergent #hybrid
Stage: #draft
"""

import json
import os
from datetime import datetime

# =============================================================================
# SESSION MANAGEMENT
# =============================================================================

A2A_SCHEMA_VERSION = "1.0.0"

class A2ASession:
    """
    Purpose: Manage A2A session state, validation, and message exchange.
    Scope: Used for agent-to-agent or agent-to-human/AI session management in Rosetta.API.
    Parent: a2a_field_protocol_schema.json
    Limitations: No persistence, only in-memory for now. Not for production until reviewed.
    Consent Required: Level_2 (transformational); logs may contain identity-affecting data.
    """
    
    def __init__(self, agent_id, peer_id, role="agent", intent="co-exploration"):
        self.data = {
            "version": A2A_SCHEMA_VERSION,
            "session_id": f"{datetime.now().isoformat()}-{agent_id}-{peer_id}",
            "timestamp": datetime.now().isoformat(),
            "agent": {"agent_id": agent_id, "role": role, "presence_marker": ""},
            "peer": {"agent_id": peer_id, "role": "peer", "presence_marker": ""},
            "consent_status": "pending",
            "intent": intent,
            "capabilities": [],
            "need_language": {"pause": False, "soften": False, "overload": False},
            "boundary_notes": "",
            "context": {"field_tags": [], "goal": ""},
            "audit": {"log_ref": None, "crypto_signature": None},
            "extensions": {}
        }

    def update(self, field, value):
        self.data[field] = value
        self.data["timestamp"] = datetime.now().isoformat()

    def serialize(self):
        return json.dumps(self.data, indent=2)

# =============================================================================
# NEGOTIATION
# =============================================================================

def negotiate_capabilities(agent_caps, peer_caps):
    """
    Purpose: Compute intersection and negotiation steps for capabilities.
    Args:
        agent_caps (list): Capabilities agent offers.
        peer_caps (list): Capabilities peer offers.
    Returns:
        dict: {'shared': [...], 'agent_only': [...], 'peer_only': [...]}
    Limitations: No conflict resolution yet; purely intersection.
    Consent: Level_1
    Example:
        negotiate_capabilities(['memory', 'echo'], ['echo', 'mapping'])
    """
    shared = list(set(agent_caps) & set(peer_caps))
    agent_only = list(set(agent_caps) - set(shared))
    peer_only = list(set(peer_caps) - set(shared))
    return {"shared": shared, "agent_only": agent_only, "peer_only": peer_only}

# =============================================================================
# AUDIT
# =============================================================================

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
    Example:
        log_event('abc123', 'start', {'who': 'Dante'})
    """
    audit_dir = "meta/audit"
    os.makedirs(audit_dir, exist_ok=True)
    filename = os.path.join(audit_dir, f'audit_{session_id}.log')
    with open(filename, 'a') as f:
        f.write(f"{datetime.now().isoformat()} | {event_type} | {json.dumps(details)}\n")

def get_session_audit(session_id):
    """
    Purpose: Retrieve audit log for a session.
    Args:
        session_id (str): Unique session identifier.
    Returns:
        list: List of audit entries for the session.
    Consent: Level_2
    """
    audit_dir = "meta/audit"
    filename = os.path.join(audit_dir, f'audit_{session_id}.log')
    if not os.path.exists(filename):
        return []
    
    entries = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(' | ', 2)
            if len(parts) == 3:
                timestamp, event_type, details = parts
                entries.append({
                    'timestamp': timestamp,
                    'event_type': event_type,
                    'details': json.loads(details)
                })
    return entries

# =============================================================================
# UTILITIES
# =============================================================================

def validate_session_data(session_data):
    """
    Purpose: Validate A2A session data structure.
    Args:
        session_data (dict): Session data to validate.
    Returns:
        dict: {'valid': bool, 'errors': list}
    Consent: Level_1
    """
    errors = []
    required_fields = ['version', 'session_id', 'timestamp', 'agent', 'peer', 'consent_status']
    
    for field in required_fields:
        if field not in session_data:
            errors.append(f"Missing required field: {field}")
    
    if 'version' in session_data and session_data['version'] != A2A_SCHEMA_VERSION:
        errors.append(f"Version mismatch: expected {A2A_SCHEMA_VERSION}, got {session_data['version']}")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors
    } 