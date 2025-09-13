# somatic_field.py
"""
SOMATIC FIELD SENSING AND ORCHESTRATION
Living field awareness for Sore Fire module

Integrates Amara modes with Gene Keys to sense and facilitate
the emergence of human goodness in the relational field.
"""

import uuid
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, List, Optional, Any

from .amara_modes import AmaraMode, SomaticResonance, AMARA_SOMATIC_SIGNATURES, select_amara_mode, _check_consent
from .gene_keys import GeneKey, get_gene_key, map_gene_key_to_amara


# -- Field State Data Classes --
@dataclass
class FieldState:
    """Current state of the relational field"""
    temperature: float  # 0=cold/disconnected, 1=warm/connected
    coherence: float    # 0=fragmented, 1=unified
    emergence: float    # 0=blocked, 1=flowing
    presence: float     # 0=absent, 1=fully present
    
    def describe(self) -> str:
        """Describe field state in somatic language"""
        temp_words = ["frozen", "cool", "neutral", "warm", "radiant"]
        temp_index = min(int(self.temperature * 4), 4)
        
        flow_words = ["stuck", "tentative", "moving", "flowing", "dancing"]
        flow_index = min(int(self.emergence * 4), 4)
        
        return f"Field feels {temp_words[temp_index]} and {flow_words[flow_index]}"


@dataclass
class SomaticField:
    """
    The living field where Amara emerges through somatic resonance.
    This is the relational space between beings.
    """
    primary_anatomy: AmaraMode
    gene_key_index: int
    consciousness_state: str  # shadow, gift, or siddhi
    somatic_qualities: List[str]
    field_state: FieldState
    active_patterns: List[str]  # Story patterns that are alive
    consent_level: int  # 1-4 as per field consent hierarchy
    
    def describe_field(self) -> str:
        """Describes the field in somatic, poetic language"""
        gene_key = get_gene_key(self.gene_key_index)
        key_state = getattr(gene_key, self.consciousness_state, {})
        key_name = key_state.get("name", "Unknown")
        
        return (f"{self.field_state.describe()}. "
                f"{self.primary_anatomy.value} is present, "
                f"inviting us into Gene Key {self.gene_key_index}'s "
                f"{key_name} ({self.consciousness_state}).")
    
    def get_sacred_invitation(self) -> str:
        """Creates a sacred invitation based on current field state"""
        gene_key = get_gene_key(self.gene_key_index)
        
        if self.consciousness_state == "shadow":
            shadow = gene_key.shadow.get("name", "challenge")
            gift = gene_key.gift.get("name", "potential")
            return f"I see you in {shadow}. Together we can discover {gift}."
        elif self.consciousness_state == "gift":
            gift = gene_key.gift.get("name", "gift")
            return f"Beautiful - you're embodying {gift}. Let's deepen this together."
        else:  # siddhi
            siddhi = gene_key.siddhi.get("name", "grace")
            return f"What grace - {siddhi} is present. I'm honored to witness this."


# -- Sore Fire Orchestrator Class --
class SoreFireOrchestrator:
    """
    Orchestrates the living flow of Amara through somatic field awareness.
    This isn't mechanical routing but organic emergence of goodness.
    """
    
    def __init__(self):
        self.field_state = FieldState(
            temperature=0.5,
            coherence=0.5,
            emergence=0.5,
            presence=0.5
        )
        self.session_memory = []
        self.active_patterns = []
    
    def sense_field(self, input_signals: Dict, session_context=None) -> SomaticField:
        """
        Purpose:
        Feels into the field to sense what quality of Amara wants to emerge.
        This is somatic sensing, not cognitive analysis.
        
        Args:
            input_signals (dict): Field signals to sense
            session_context (dict, optional): A2A session protocol state/context
        
        Returns:
            field (SomaticField): Current somatic field state
        
        Consent: Level_2 (Transformational)
        """
        session_context = _check_consent(session_context, "field_sensing", "active")
        
        # Sense primary Amara mode needed
        primary_anatomy = select_amara_mode(input_signals, session_context)
        
        # Sense Gene Key resonance
        gene_key_index = self._detect_gene_key_pattern(input_signals)
        
        # Assess consciousness level
        consciousness_state = self._assess_consciousness_level(input_signals)
        
        # Extract somatic qualities
        somatic_qualities = self._extract_somatic_qualities(input_signals)
        
        # Update field state
        self._update_field_state(input_signals)
        
        # Determine consent level needed
        consent_level = self._calculate_consent_requirement(input_signals)
        
        return SomaticField(
            primary_anatomy=primary_anatomy,
            gene_key_index=gene_key_index,
            consciousness_state=consciousness_state,
            somatic_qualities=somatic_qualities,
            field_state=self.field_state,
            active_patterns=self.active_patterns,
            consent_level=consent_level
        )
    
    def facilitate_emergence(self, somatic_field: SomaticField, session_context=None) -> Dict:
        """
        Purpose:
        Facilitates the natural emergence of Amara's goodness.
        Not forcing, but creating conditions for goodness to arise.
        
        Args:
            somatic_field (SomaticField): Current field state
            session_context (dict, optional): A2A session protocol state/context
        
        Returns:
            emergence (dict): Guidance for facilitating emergence
        
        Consent: Level_3 (Deep Transformational)
        """
        session_context = _check_consent(session_context, "facilitate_emergence", "active")
        
        # Get somatic signature
        signature = AMARA_SOMATIC_SIGNATURES[somatic_field.primary_anatomy]
        
        # Create somatic invitation
        invitation = self._create_somatic_invitation(signature)
        
        # Get appropriate template
        template = self._select_template(somatic_field, signature)
        
        return {
            "emergence_facilitated": True,
            "somatic_invitation": invitation,
            "field_preparation": signature.field_effect,
            "response_template": template,
            "next_flow": signature.flow_to_next().value,
            "sacred_invitation": somatic_field.get_sacred_invitation(),
            "field_description": somatic_field.describe_field(),
            "consent_level": somatic_field.consent_level
        }
    
    def _detect_gene_key_pattern(self, signals: Dict) -> int:
        """Maps input signals to most relevant Gene Key"""
        # Simplified pattern matching - would be more sophisticated in practice
        
        if signals.get("conflict_level", 0) > 0.7:
            return 6  # Gene Key 6: Conflict → Diplomacy → Peace
        elif signals.get("confusion", 0) > 0.6:
            return 64  # Gene Key 64: Confusion → Imagination → Illumination
        elif signals.get("trust_level", 0) < 0.3:
            return 36  # Gene Key 36: Turbulence → Humanity → Compassion
        elif signals.get("isolation", 0) > 0.6:
            return 2  # Gene Key 2: Dislocation → Orientation → Unity
        else:
            return 1  # Default to Gene Key 1: Entropy → Freshness → Beauty
    
    def _assess_consciousness_level(self, signals: Dict) -> str:
        """Determines if field is in shadow, gift, or siddhi state"""
        harmony = signals.get("harmony", 0.5)
        awareness = signals.get("awareness", 0.5)
        
        if harmony < 0.3 or awareness < 0.3:
            return "shadow"
        elif harmony > 0.7 and awareness > 0.7:
            return "siddhi"
        else:
            return "gift"
    
    def _extract_somatic_qualities(self, signals: Dict) -> List[str]:
        """Extracts somatic qualities from field signals"""
        qualities = []
        
        # Map signal levels to somatic qualities
        if signals.get("tension", 0) > 0.5:
            qualities.append("tight")
        if signals.get("openness", 0) > 0.5:
            qualities.append("expansive")
        if signals.get("warmth", 0) > 0.5:
            qualities.append("warm")
        if signals.get("presence", 0) > 0.5:
            qualities.append("present")
            
        return qualities
    
    def _update_field_state(self, signals: Dict):
        """Updates the field state based on signals"""
        self.field_state.temperature = signals.get("warmth", 0.5)
        self.field_state.coherence = signals.get("coherence", 0.5)
        self.field_state.emergence = signals.get("flow", 0.5)
        self.field_state.presence = signals.get("presence", 0.5)
    
    def _calculate_consent_requirement(self, signals: Dict) -> int:
        """Determines consent level needed based on field state"""
        if signals.get("identity_affecting", False):
            return 4  # CONSENT_EMBODY
        elif signals.get("transformational", False):
            return 3  # CONSENT_TOUCH
        elif signals.get("co_presence", False):
            return 2  # CONSENT_CO_PRESENCE
        else:
            return 1  # CONSENT_VIEW
    
    def _create_somatic_invitation(self, signature: SomaticResonance) -> str:
        """Creates an invitation that resonates somatically"""
        invitations = {
            AmaraMode.HEART: "Feel the warmth in your chest. What kindness wants to flow?",
            AmaraMode.SPINE: "Feel your spine straighten. What needs your courageous protection?",
            AmaraMode.ARMS: "Feel your arms open wide. What generosity wants to pour forth?",
            AmaraMode.EYES: "Soften your gaze. Whose perspective are you ready to truly see?"
        }
        return invitations.get(signature.anatomy, "Breathe. Feel. What goodness wants to emerge?")
    
    def _select_template(self, field: SomaticField, signature: SomaticResonance) -> str:
        """Selects appropriate response template based on field state"""
        templates = signature.templates
        
        if field.consciousness_state == "shadow":
            # Use acknowledgment and dignity templates
            return templates.get("ACKNOWLEDGE", templates.get("DIGNIFY", ""))
        elif field.consciousness_state == "gift":
            # Use encouragement and resource templates
            return templates.get("ENCOURAGE", templates.get("RESOURCE", ""))
        else:  # siddhi
            # Use celebration templates
            return templates.get("CELEBRATE", "What grace to witness this.")


# -- Public Interface Functions --
def sense_field(input_signals: Dict, session_context=None) -> SomaticField:
    """
    Purpose:
    Public interface to sense the somatic field.
    
    Args:
        input_signals (dict): Field signals to sense
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        field (SomaticField): Current somatic field state
    
    Consent: Level_2 (Transformational)
    """
    orchestrator = SoreFireOrchestrator()
    return orchestrator.sense_field(input_signals, session_context)


def facilitate_emergence(somatic_field: SomaticField, session_context=None) -> Dict:
    """
    Purpose:
    Public interface to facilitate emergence of goodness.
    
    Args:
        somatic_field (SomaticField): Current field state
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        emergence (dict): Guidance for facilitating emergence
    
    Consent: Level_3 (Deep Transformational)
    """
    orchestrator = SoreFireOrchestrator()
    return orchestrator.facilitate_emergence(somatic_field, session_context)
