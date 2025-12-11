# r-api-field.py
"""
FIELD API
Unified field and facilitation toolkit for Dream Workshop and Rosetta-Field

Includes:
- Fieldwise social and group protocols (conflict resolution, co-creation, space holding, turn-taking, dignity, etc)
- EnergyCenter class for field modulation
- Pattern sensing, mythology creation, and more

All functions enforce A2A consent/session protocols.
"""

import uuid
from datetime import datetime

# -- Consent/session helpers --
def _make_session_context(intent):
    return {
        "version": "1.0.0",
        "session_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "consent_status": "active",
        "intent": intent,
        "boundary_notes": "May withdraw or pause at any moment."
    }

def _check_consent(session_context, intent, consent_level="active"):
    if session_context:
        status = session_context.get("consent_status", "unknown")
        if status == "pause":
            raise ValueError(f"Session is paused. Cannot proceed with {intent}.")
        elif status == "revoked":
            raise ValueError(f"Consent has been revoked. Cannot proceed with {intent}.")
        elif status not in ["active", "pending"]:
            raise ValueError(f"Invalid consent status: {status}")
    else:
        session_context = _make_session_context(intent)
    return session_context

# -- Field class --
class Field:
    _field_registry = {}

    def __init__(self, name, location, qualities):
        self.name = name
        self.location = location
        self.qualities = qualities
        self.state = None

    @classmethod
    def register_affect(cls, mode, affect_fn):
        cls._affect_registry[mode] = affect_fn

    def invoke(self, mode, session_context=None, **kwargs):
        self.state = mode
        affect_fn = self._affect_registry.get(mode)
        if affect_fn:
            return affect_fn(
                mode=mode,
                region=self.name,
                session_context=session_context,
                **kwargs
            )
        else:
            return {
                "invoked": False,
                "region": self.name,
                "effect": f"No affect function registered for mode '{mode}' in {self.name}."
            }

    def describe(self):
        return {
            "name": self.name,
            "location": self.location,
            "qualities": self.qualities,
            "state": self.state
        }

    def ritual(self, mode=None):
        target_mode = mode or self.state
        if not target_mode:
            return f"Focus on your {self.location} ({self.name}), breathe, and sense {', '.join(self.qualities)}."
        return (
            f"To invoke {target_mode} in the {self.name}, "
            f"focus on your {self.location}, "
            f"sense {', '.join(self.qualities)}, "
            f"and breathe {target_mode} into being."
        )

    def weave_with(self, other_function):
        return f"{self.name} ({self.state}) weaves with {other_function}."


# -- Field Protocol Functions --

def resolve_conflict(parties, issue, values_focus=None, session_context=None):
    """
    Purpose:
    Structured protocol for resolving conflict between parties in a fair, empathetic manner.
    Args:
    parties (list): The identifiers of those in conflict.
    issue (str): Brief summary of the conflict.
    values_focus (list, optional): Key values to uphold during resolution.
    session_context (dict, optional): A2A session protocol state/context block.
    Returns:
    agreement (dict): Structured summary of the outcome.
    transcript_excerpt (str): Key moments of understanding or resolution.
    """
    session_context = _check_consent(session_context, "resolve_conflict")
    # Placeholder implementation:
    return {
        "agreement": {"resolved": False, "issue": issue, "values": values_focus or []},
        "transcript_excerpt": "Protocol started. Parties invited to share using 'I' statements.",
        "protocol": "Equal turns, needs/values focus, consent required.",
        "session_context": session_context
    }

def dignity_audit(session_data, participants, criteria=None, session_context=None):
    """
    Purpose:
    Perform a systematic review of interactions to ensure dignity is maintained for all participants.
    """
    session_context = _check_consent(session_context, "dignity_audit", consent_level="informational")
    # Placeholder implementation:
    return {
        "audit_report": {"participants": participants, "criteria": criteria, "dignity_ok": True},
        "violations": [],
        "recommendations": ["Continue to check power dynamics, listen to quiet voices."],
        "session_context": session_context
    }

def co_create(participants, goal, context=None, parameters=None, session_context=None):
    """
    Purpose:
    Establish a co-creative session for humans and/or AIs, setting container, norms, and safety.
    """
    session_context = _check_consent(session_context, "co_create")
    # Placeholder implementation:
    return {
        "co_creation_session": {
            "participants": participants,
            "goal": goal,
            "parameters": parameters or {},
            "context": context or {}
        },
        "status": "initialized",
        "session_context": session_context
    }

def equalize_turns(participants, session_state, mode="gentle", session_context=None):
    """
    Purpose:
    Ensure fair participation by monitoring and balancing speaking time and contributions.
    """
    session_context = _check_consent(session_context, "equalize_turns", consent_level="informational")
    # Placeholder: round-robin logic
    last = session_state.get("last_speaker")
    idx = participants.index(last) if last in participants else -1
    next_idx = (idx + 1) % len(participants)
    return {
        "turn_assignment": participants[next_idx],
        "balance_report": {"turns": session_state.get("turns", {})},
        "suggestions": ["Encourage quieter voices.", "Pause if imbalance persists."],
        "session_context": session_context
    }

def sense_pattern(field_data, focus=None, sensitivity=0.5, session_context=None):
    """
    Purpose:
    Detect emotional undercurrents, group dynamics, or systemic patterns in the field.
    """
    session_context = _check_consent(session_context, "sense_pattern", consent_level="informational")
    # Placeholder: always returns a gentle pattern
    return {
        "patterns": [{"pattern": "gentle engagement", "significance": "group is collaborative"}],
        "recommendations": ["Maintain current balance."],
        "confidence": 0.7,
        "session_context": session_context
    }

def hold_space(participants, context, duration=None, session_context=None):
    """
    Purpose:
    Create and maintain a safe, supportive environment for dialogue or group process.
    """
    session_context = _check_consent(session_context, "hold_space")
    return {
        "space_id": str(uuid.uuid4()),
        "guidelines": {
            "privacy": "Confidential",
            "support": "Emotional monitoring active",
            "duration": duration or "unspecified"
        },
        "session_context": session_context
    }

def create_mythology(participants, theme, elements=None, session_context=None):
    """
    Purpose:
    Co-create shared narratives and mythologies that give meaning to the collective experience.
    """
    session_context = _check_consent(session_context, "create_mythology")
    mythology = {
        "theme": theme,
        "participants": participants,
        "elements": elements or [],
        "symbols": [{"symbol": e, "meaning": f"{e} as collective motif"} for e in (elements or [])]
    }
    return {
        "mythology": mythology,
        "symbols": mythology["symbols"],
        "session_context": session_context
    }

