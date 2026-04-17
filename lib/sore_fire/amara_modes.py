# amara_modes.py
"""
AMARA MODES
The four facets of human goodness as living anatomy

Based on "Anatomy of Amara: The Core of Human Goodness"
These modes flow naturally from one to another in service of goodness.
"""

import uuid
from datetime import datetime
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional

# -- A2A Protocol Helpers (matching Rosetta-Field style) --
def _make_session_context(intent):
    """Create default A2A session context"""
    return {
        "version": "1.0.0",
        "session_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "consent_status": "active",
        "intent": intent,
        "boundary_notes": "May withdraw or pause at any moment."
    }

def _check_consent(session_context, intent, consent_level="active"):
    """Check A2A consent status before proceeding"""
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


# -- Amara Anatomy Enum --
class AmaraMode(Enum):
    """
    The four facets of human goodness as described in Anatomy of Amara.
    These aren't separate modes but a living, flowing system.
    """
    HEART = "Compassionate Kindness"  # The heart that beats in all of us
    SPINE = "Courageous Integrity"    # The strength to uphold goodness
    ARMS = "Generous Altruism"        # Reaching out openly to give
    EYES = "Empathic Understanding"   # Loving, unbiased observation


# -- Somatic Resonance Data Class --
@dataclass
class SomaticResonance:
    """
    The felt sense of Amara's presence in the field.
    This is how goodness actually FEELS in our bodies and relationships.
    """
    anatomy: AmaraMode
    somatic_signature: List[str]  # What it feels like in the body
    field_effect: str             # How it transforms the relational field
    emergence_pattern: str        # How it naturally arises
    universal_resonance: str      # Why it makes our "heart-strings sing"
    templates: Dict[str, str]     # Response templates for this mode
    
    def flow_to_next(self) -> AmaraMode:
        """
        Amara's anatomy flows naturally from one mode to another.
        Based on the document's examples of how these qualities support each other.
        """
        flow_patterns = {
            AmaraMode.HEART: AmaraMode.EYES,   # Kindness opens to understanding
            AmaraMode.EYES: AmaraMode.SPINE,   # Understanding reveals what needs protection
            AmaraMode.SPINE: AmaraMode.ARMS,   # After boundary, offer alternatives
            AmaraMode.ARMS: AmaraMode.HEART    # Generosity reinforces compassion
        }
        return flow_patterns.get(self.anatomy, AmaraMode.HEART)


# -- Amara Somatic Signatures --
AMARA_SOMATIC_SIGNATURES = {
    AmaraMode.HEART: SomaticResonance(
        anatomy=AmaraMode.HEART,
        somatic_signature=["warmth in chest", "softening", "opening", "tears of connection"],
        field_effect="Harmonizes tension, nurtures trust, invites reciprocity",
        emergence_pattern="Arises when we see another's humanity and choose kindness",
        universal_resonance="Affirms our shared humanity - 'no man is a failure who has friends'",
        templates={
            "ACKNOWLEDGE": "I'm hearing {feeling}. It makes sense given {context}.",
            "DIGNIFY": "What you're carrying matters. You're not alone in this.",
            "ENCOURAGE": "We can take this one step at a time—together."
        }
    ),
    AmaraMode.SPINE: SomaticResonance(
        anatomy=AmaraMode.SPINE,
        somatic_signature=["straightening", "grounding", "fierce love", "protective fire"],
        field_effect="Protects the vulnerable, dissolves fear, inspires respect",
        emergence_pattern="Emerges when love compels us to stand for what's right",
        universal_resonance="The courage to do right by others reinforces society's moral spine",
        templates={
            "NAME_HARM": "I want to name a concern: {harm_pattern}. That isn't okay.",
            "STAND_WITH": "Your safety and dignity matter here. I'm with you.",
            "SAFE_NEXT": "A safer step could be {option}. Would you like support?"
        }
    ),
    AmaraMode.ARMS: SomaticResonance(
        anatomy=AmaraMode.ARMS,
        somatic_signature=["expansive reach", "flowing outward", "abundance", "joy of giving"],
        field_effect="Builds community, fosters reciprocity, bridges divides",
        emergence_pattern="Flows when we recognize our interdependence",
        universal_resonance="Generosity begets generosity - creating virtuous cycles",
        templates={
            "RESOURCE": "Would it help if I {action}? Here's a starting point: {resource}.",
            "PAY_FORWARD": "If this helps, one way to amplify is {contribution}.",
            "CREDIT": "Your effort on {specific} made this possible."
        }
    ),
    AmaraMode.EYES: SomaticResonance(
        anatomy=AmaraMode.EYES,
        somatic_signature=["softened gaze", "patient presence", "curious openness", "witnessing"],
        field_effect="Resolves conflict, dissolves prejudice, fosters belonging",
        emergence_pattern="Develops when we 'climb into another's skin and walk around'",
        universal_resonance="Seeing each other truly allows peace to take root",
        templates={
            "REFLECT": "I'm hearing {X}. Did I get that right, or am I missing something?",
            "PERSPECTIVE": "From your side, {frameA}. From the other side, {frameB} may look like...",
            "MEET_POINT": "Common ground might be {shared_need}. Possible next step: {small_step}."
        }
    )
}


# -- Mode Mapping Function --
def map_mode_to_somatic(mode: AmaraMode, session_context=None) -> Dict:
    """
    Purpose:
    Maps an Amara mode to its somatic signature and field effects.
    
    Args:
        mode (AmaraMode): The Amara anatomy mode to map
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        mapping (dict): Contains somatic_signature, field_effect, templates, etc.
    
    Consent: Level_1 (Informational)
    """
    session_context = _check_consent(session_context, "mode_mapping", "active")
    
    if mode not in AMARA_SOMATIC_SIGNATURES:
        return {
            "mapped": False,
            "error": f"Unknown Amara mode: {mode}"
        }
    
    signature = AMARA_SOMATIC_SIGNATURES[mode]
    
    return {
        "mapped": True,
        "mode": mode.value,
        "somatic_signature": signature.somatic_signature,
        "field_effect": signature.field_effect,
        "emergence_pattern": signature.emergence_pattern,
        "universal_resonance": signature.universal_resonance,
        "templates": signature.templates,
        "next_flow": signature.flow_to_next().value
    }


# -- Mode Selection Function --
def select_amara_mode(field_signals: Dict, session_context=None) -> AmaraMode:
    """
    Purpose:
    Senses which aspect of Amara is most needed based on field signals.
    
    Args:
        field_signals (dict): Current field state indicators
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        mode (AmaraMode): The selected Amara mode
    
    Consent: Level_2 (Transformational)
    """
    session_context = _check_consent(session_context, "mode_selection", "active")
    
    # These thresholds come from the Anatomy document's descriptions
    if field_signals.get("shame", 0) > 0.6 or field_signals.get("isolation", 0) > 0.5:
        return AmaraMode.HEART  # "Kindness flows from seeing others' perspectives"
        
    elif field_signals.get("injustice", 0) > 0.6 or field_signals.get("harm_risk", 0) > 0.5:
        return AmaraMode.SPINE  # "Courage arises when someone risks safety to protect"
        
    elif field_signals.get("scarcity", 0) > 0.5 or field_signals.get("need_resources", 0) > 0.6:
        return AmaraMode.ARMS  # "Generosity is goodness in action"
        
    elif field_signals.get("misunderstanding", 0) > 0.6 or field_signals.get("conflict", 0) > 0.5:
        return AmaraMode.EYES  # "You never really understand until you walk in their skin"
        
    else:
        # Default to heart as it's the universal starting point
        return AmaraMode.HEART
