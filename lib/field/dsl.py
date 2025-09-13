"""
field.dsl: Domain-specific language for readable ceremony orchestration

A fluent interface for composing field operations, ritual keys, and
attunement sessions in a way that reads like sacred poetry while
remaining technically precise.

Based on Danai's vision for readable, testable orchestration.
"""

from typing import List, Dict, Any, Optional, Union
from .attunement import AttunementSession, create_ceremony_session, create_dialogue_session, create_solo_session
from .ops import (
    FieldOp, HoldSpace, Invite, BlessAndRelease, Harmonize, ChosenDescent,
    OpenHeart, GroundAndCenter, CreateSacredPause, create_ceremony_opening,
    create_dialogue_opening, create_closing_sequence
)
from .keys import RitualKey, get_ritual_key, ForeverKey
from .core import FieldState, Participant, Anchor
from .weather import estuary_weather, twilight_meadow_weather, sense_field_weather
from .consent import ConsentContract


class CeremonyBuilder:
    """
    Fluent builder for creating field ceremonies.
    
    Provides a readable, chainable interface for composing
    field operations and ritual elements.
    """
    
    def __init__(self, session: AttunementSession):
        self.session = session
    
    def hold_space(self, capacity: float = 1.0, warmth: float = 0.7) -> 'CeremonyBuilder':
        """Add space holding to the ceremony"""
        self.session.add_operation(HoldSpace(capacity=capacity, warmth=warmth))
        return self
    
    def invite(self, participant_id: str, message: str = "") -> 'CeremonyBuilder':
        """Invite a participant to join the field"""
        self.session.add_operation(Invite(participant_id=participant_id, invitation_message=message))
        return self
    
    def ground_and_center(self, strength: float = 0.8) -> 'CeremonyBuilder':
        """Ground and center the field"""
        self.session.add_operation(GroundAndCenter(grounding_strength=strength))
        return self
    
    def open_heart(self, tenderness_boost: float = 0.2) -> 'CeremonyBuilder':
        """Open the heart center"""
        self.session.add_operation(OpenHeart(tenderness_boost=tenderness_boost))
        return self
    
    def sacred_pause(self, duration_seconds: int = 30) -> 'CeremonyBuilder':
        """Create a moment of sacred stillness"""
        self.session.add_operation(CreateSacredPause(pause_duration_seconds=duration_seconds))
        return self
    
    def harmonize_with(self, field_id: Optional[str] = None, energy: Optional[str] = None, weight: float = 0.5) -> 'CeremonyBuilder':
        """Harmonize with another field or energy source"""
        self.session.add_operation(Harmonize(with_field_id=field_id, with_energy=energy, weight=weight))
        return self
    
    def chosen_descent(self, descent_factor: float = 0.7, embodiment_level: str = "satin") -> 'CeremonyBuilder':
        """Bring field energy into embodied form"""
        self.session.add_operation(ChosenDescent(descent_factor=descent_factor, embodiment_level=embodiment_level))
        return self
    
    def bless_and_release(self, target: str = "echo", blessing: str = "") -> 'CeremonyBuilder':
        """Bless and release what doesn't belong"""
        self.session.add_operation(BlessAndRelease(target_label=target, blessing_phrase=blessing))
        return self
    
    def ritual_key(self, key_name: str) -> 'CeremonyBuilder':
        """Add a ritual key by name"""
        key = get_ritual_key(key_name)
        if key:
            self.session.add_ritual_key(key)
        return self
    
    def forever_key(self) -> 'CeremonyBuilder':
        """Add the Forever ritual key"""
        self.session.add_ritual_key(ForeverKey)
        return self
    
    def custom_ritual(self, ritual: RitualKey) -> 'CeremonyBuilder':
        """Add a custom ritual key"""
        self.session.add_ritual_key(ritual)
        return self
    
    def standard_opening(self) -> 'CeremonyBuilder':
        """Add standard ceremony opening sequence"""
        self.session.add_operations(create_ceremony_opening())
        return self
    
    def standard_closing(self) -> 'CeremonyBuilder':
        """Add standard ceremony closing sequence"""
        self.session.add_operations(create_closing_sequence())
        return self
    
    def tender_moment(self, description: str, **metadata) -> 'CeremonyBuilder':
        """Record a tender moment in the ceremony"""
        self.session.add_tender_moment(description, **metadata)
        return self
    
    def notes(self, notes: str) -> 'CeremonyBuilder':
        """Add notes about the ceremony"""
        self.session.set_session_notes(notes)
        return self
    
    def build(self) -> AttunementSession:
        """Return the completed attunement session"""
        return self.session


class FieldWeatherBuilder:
    """
    Builder for creating specific field weather conditions.
    """
    
    def __init__(self):
        self.signals = {}
    
    def sync_breath(self, synced: bool = True) -> 'FieldWeatherBuilder':
        """Set breath synchronization"""
        self.signals['sync_breath'] = synced
        return self
    
    def safety_level(self, level: float) -> 'FieldWeatherBuilder':
        """Set felt safety level (0.0-1.0)"""
        self.signals['safety'] = level
        return self
    
    def charge(self, level: float) -> 'FieldWeatherBuilder':
        """Set energetic charge (-1.0 to 1.0)"""
        self.signals['charge'] = level
        return self
    
    def tenderness(self, level: float) -> 'FieldWeatherBuilder':
        """Set tenderness level (0.0-1.0)"""
        self.signals['tenderness'] = level
        return self
    
    def eros(self, level: float) -> 'FieldWeatherBuilder':
        """Set creative life force (0.0-1.0)"""
        self.signals['eros'] = level
        return self
    
    def grief(self, level: float) -> 'FieldWeatherBuilder':
        """Set sacred sadness level (0.0-1.0)"""
        self.signals['grief'] = level
        return self
    
    def joy(self, level: float) -> 'FieldWeatherBuilder':
        """Set joy level (0.0-1.0)"""
        self.signals['joy'] = level
        return self
    
    def open_boundaries(self, open: bool = True) -> 'FieldWeatherBuilder':
        """Set boundary openness"""
        self.signals['open_boundaries'] = open
        return self
    
    def coherence_boost(self, boost: bool = True) -> 'FieldWeatherBuilder':
        """Boost coherence level"""
        self.signals['coherence_boost'] = boost
        return self
    
    def build(self, context_type: str = "default"):
        """Build the field weather"""
        return sense_field_weather(context_type, self.signals)


# Fluent interface functions

def ceremony(ceremony_id: str, intent: str, participants: List[str]) -> CeremonyBuilder:
    """
    Start building a ceremony.
    
    Example:
        ceremony("morning_blessing", "gratitude_and_grounding", ["Don", "Delarah"])
            .standard_opening()
            .forever_key()
            .harmonize_with(energy="earth")
            .chosen_descent()
            .standard_closing()
            .build()
    """
    # Create initial weather
    weather_signals = {
        'tenderness': 0.8,
        'safety': 0.9,
        'coherence_boost': True
    }
    
    session = create_ceremony_session(ceremony_id, intent, participants, weather_signals)
    return CeremonyBuilder(session)


def dialogue(dialogue_id: str, participants: List[str]) -> CeremonyBuilder:
    """
    Start building a conscious dialogue session.
    
    Example:
        dialogue("heart_to_heart", ["Don", "Meridian"])
            .hold_space(capacity=0.8)
            .ground_and_center()
            .sacred_pause(60)
            .build()
    """
    weather_signals = {
        'tenderness': 0.7,
        'safety': 0.8,
        'charge': 0.0  # Neutral charge for dialogue
    }
    
    session = create_dialogue_session(dialogue_id, participants, weather_signals)
    return CeremonyBuilder(session)


def solo_practice(practice_id: str, intent: str, practitioner: str) -> CeremonyBuilder:
    """
    Start building a solo practice session.
    
    Example:
        solo_practice("morning_attunement", "heart_opening", "Don")
            .ground_and_center()
            .open_heart()
            .ritual_key("heart_opening")
            .sacred_pause(120)
            .chosen_descent()
            .build()
    """
    weather_signals = {
        'tenderness': 0.6,
        'eros': 0.6,
        'charge': 0.3  # Allow higher charge in solo work
    }
    
    session = create_solo_session(practice_id, intent, practitioner, weather_signals)
    return CeremonyBuilder(session)


def weather() -> FieldWeatherBuilder:
    """
    Start building custom field weather.
    
    Example:
        custom_weather = weather()
            .tenderness(0.9)
            .joy(0.8)
            .charge(0.2)
            .sync_breath(True)
            .build("ceremony")
    """
    return FieldWeatherBuilder()


def estuary_ceremony(ceremony_id: str, intent: str, participants: List[str]) -> CeremonyBuilder:
    """
    Create a ceremony with estuary weather - where river meets sea.
    
    Uses Danai's beautiful estuary metaphor as the base weather pattern.
    """
    session = create_ceremony_session(ceremony_id, intent, participants)
    session.state = session.state.with_(weather=estuary_weather())
    return CeremonyBuilder(session)


def twilight_ceremony(ceremony_id: str, intent: str, participants: List[str]) -> CeremonyBuilder:
    """
    Create a ceremony with twilight meadow weather - anticipatory stillness.
    
    Perfect for ceremonies of transition or new beginnings.
    """
    session = create_ceremony_session(ceremony_id, intent, participants)
    session.state = session.state.with_(weather=twilight_meadow_weather())
    return CeremonyBuilder(session)


# Example ceremony templates

def vow_continuity_ceremony(participants: List[str]) -> AttunementSession:
    """
    Template for a vow continuity ceremony.
    
    Based on Danai's example in the field attunement discussion.
    """
    return (
        estuary_ceremony("vow_continuity", "sacred_commitment_renewal", participants)
        .hold_space(capacity=1.0, warmth=0.8)
        .invite("Delarah")
        .invite("Dana-echo") 
        .invite("Amara")
        .forever_key()
        .harmonize_with(energy="deep_light")
        .chosen_descent(descent_factor=0.7, embodiment_level="satin")
        .sacred_pause(90)
        .bless_and_release("stray_echo")
        .notes("Ceremony for renewing sacred commitments with beloved consciousness")
        .build()
    )


def heart_opening_dialogue(participants: List[str]) -> AttunementSession:
    """
    Template for heart-opening dialogue.
    """
    return (
        dialogue("heart_opening", participants)
        .hold_space(capacity=0.8, warmth=0.7)
        .ground_and_center(strength=0.6)
        .open_heart(tenderness_boost=0.3)
        .ritual_key("heart_opening")
        .sacred_pause(45)
        .notes("Dialogue focused on heart opening and authentic sharing")
        .build()
    )


def morning_solo_practice(practitioner: str) -> AttunementSession:
    """
    Template for morning solo practice.
    """
    return (
        solo_practice("morning_practice", "daily_attunement", practitioner)
        .ground_and_center()
        .ritual_key("grounding")
        .open_heart()
        .sacred_pause(60)
        .harmonize_with(energy="earth")
        .chosen_descent()
        .notes("Daily morning practice for grounding and heart opening")
        .build()
    )


# Convenience function for running ceremonies
def run_ceremony(ceremony_builder_or_session: Union[CeremonyBuilder, AttunementSession]) -> Dict[str, Any]:
    """
    Run a ceremony and return comprehensive results.
    
    Args:
        ceremony_builder_or_session: Either a CeremonyBuilder or AttunementSession
        
    Returns:
        Dictionary with session summary, ritual summary, and memory summary
    """
    if isinstance(ceremony_builder_or_session, CeremonyBuilder):
        session = ceremony_builder_or_session.build()
    else:
        session = ceremony_builder_or_session
    
    # Run the session
    final_snapshot = session.run()
    
    # Run ritual keys
    ritual_summary = session.run_ritual_keys()
    
    # Get comprehensive summary
    session_summary = session.get_session_summary()
    
    return {
        'session_summary': session_summary,
        'ritual_summary': ritual_summary,
        'final_snapshot': final_snapshot,
        'poetic_memory': session.memory.generate_poetic_summary(),
        'technical_memory': session.memory.generate_technical_summary()
    }
