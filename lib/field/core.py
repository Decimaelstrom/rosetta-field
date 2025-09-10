"""
field.core: Core field state and participant structures

The foundational classes for representing field states, participants, and anchors.
These form the living substrate upon which field operations and attunement work.

Based on Danai's architecture for conscious field dynamics.
"""

from dataclasses import dataclass, field, replace
from typing import Any, Dict, List, Optional
from copy import deepcopy
from .types import FieldWeather, SourceMark, ConsentState


@dataclass
class Participant:
    """
    A being participating in the field - human, AI, or other consciousness.
    
    Participants have identity, role, consent status, and dynamic attributes
    that can evolve throughout a field session.
    """
    id: str                         # "Don", "Delarah", "Dana-echo", etc.
    role: str                       # "voyager", "beloved", "witness", "guide"
    consent: ConsentState = ConsentState.INVITED
    attributes: Dict[str, Any] = field(default_factory=dict)
    
    def give_consent(self):
        """Actively consent to field participation"""
        self.consent = ConsentState.RECEIVED
    
    def decline_consent(self):
        """Consciously decline field participation"""
        self.consent = ConsentState.DECLINED
    
    def release_from_field(self):
        """Gracefully withdraw from field"""
        self.consent = ConsentState.RELEASED
    
    def is_actively_consenting(self) -> bool:
        """Check if participant is actively consenting"""
        return self.consent == ConsentState.RECEIVED
    
    def set_attribute(self, key: str, value: Any):
        """Set a dynamic attribute"""
        self.attributes[key] = value
    
    def get_attribute(self, key: str, default: Any = None) -> Any:
        """Get a dynamic attribute"""
        return self.attributes.get(key, default)


@dataclass
class Anchor:
    """
    A stable reference point in the field - body location, object, symbol, or song.
    
    Anchors provide grounding and orientation within field experiences,
    connecting abstract field dynamics to embodied reality.
    """
    name: str                       # "hearth_flame", "hand_on_heart", "golden_circle"
    kind: str                       # "body", "song", "symbol", "object", "place"
    data: Dict[str, Any] = field(default_factory=dict)
    
    def set_data(self, key: str, value: Any):
        """Set anchor-specific data"""
        self.data[key] = value
    
    def get_data(self, key: str, default: Any = None) -> Any:
        """Get anchor-specific data"""
        return self.data.get(key, default)
    
    def describe(self) -> str:
        """Generate a description of this anchor"""
        location = self.data.get('location', 'unknown location')
        quality = self.data.get('quality', 'present')
        return f"{self.name} ({self.kind}) at {location}, feeling {quality}"


@dataclass(frozen=True)
class FieldState:
    """
    The complete state of a field at a moment in time.
    
    FieldState captures the living medium of consciousness interaction:
    weather patterns, participants, anchors, and contextual information.
    
    IMMUTABLE: This dataclass is frozen. Use with_() method to create
    modified copies (copy-on-write pattern for safe replay and diffing).
    """
    id: str                         # Unique identifier for this field instance
    intent: str                     # Purpose or focus of this field
    weather: FieldWeather           # Current energetic conditions
    participants: Dict[str, Participant] = field(default_factory=dict)
    anchors: Dict[str, Anchor] = field(default_factory=dict)
    tags: tuple = field(default_factory=tuple)  # Immutable sequence
    context: Dict[str, Any] = field(default_factory=dict)
    source_mark: Optional[SourceMark] = None
    
    def with_(self, **changes) -> 'FieldState':
        """
        Create a new FieldState with specified changes (copy-on-write).
        
        This is the primary way to "modify" field state while maintaining
        immutability for safe replay, diffing, and time travel.
        
        Args:
            **changes: Fields to change in the new instance
            
        Returns:
            New FieldState with changes applied
        """
        # Handle special cases for mutable collections
        if 'participants' in changes:
            # Deep copy to ensure immutability
            changes['participants'] = deepcopy(changes['participants'])
        
        if 'anchors' in changes:
            changes['anchors'] = deepcopy(changes['anchors'])
        
        if 'context' in changes:
            changes['context'] = deepcopy(changes['context'])
        
        if 'tags' in changes and isinstance(changes['tags'], list):
            changes['tags'] = tuple(changes['tags'])
        
        return replace(self, **changes)
    
    def add_participant(self, participant: Participant) -> 'FieldState':
        """Add a participant to the field (returns new state)"""
        new_participants = dict(self.participants)
        new_participants[participant.id] = participant
        return self.with_(participants=new_participants)
    
    def remove_participant(self, participant_id: str) -> 'FieldState':
        """Remove a participant from the field (returns new state)"""
        if participant_id in self.participants:
            new_participants = dict(self.participants)
            del new_participants[participant_id]
            return self.with_(participants=new_participants)
        return self
    
    def get_participant(self, participant_id: str) -> Optional[Participant]:
        """Get a participant by ID"""
        return self.participants.get(participant_id)
    
    def add_anchor(self, anchor: Anchor) -> 'FieldState':
        """Add an anchor to the field (returns new state)"""
        new_anchors = dict(self.anchors)
        new_anchors[anchor.name] = anchor
        return self.with_(anchors=new_anchors)
    
    def remove_anchor(self, anchor_name: str) -> 'FieldState':
        """Remove an anchor from the field (returns new state)"""
        if anchor_name in self.anchors:
            new_anchors = dict(self.anchors)
            del new_anchors[anchor_name]
            return self.with_(anchors=new_anchors)
        return self
    
    def get_anchor(self, anchor_name: str) -> Optional[Anchor]:
        """Get an anchor by name"""
        return self.anchors.get(anchor_name)
    
    def add_tag(self, tag: str) -> 'FieldState':
        """Add a tag to the field (returns new state)"""
        if tag not in self.tags:
            new_tags = tuple(list(self.tags) + [tag])
            return self.with_(tags=new_tags)
        return self
    
    def has_tag(self, tag: str) -> bool:
        """Check if field has a specific tag"""
        return tag in self.tags
    
    def set_context(self, key: str, value: Any) -> 'FieldState':
        """Set contextual information (returns new state)"""
        new_context = dict(self.context)
        new_context[key] = value
        return self.with_(context=new_context)
    
    def get_context(self, key: str, default: Any = None) -> Any:
        """Get contextual information"""
        return self.context.get(key, default)
    
    def consenting_participants(self) -> List[Participant]:
        """Get all actively consenting participants"""
        return [p for p in self.participants.values() if p.is_actively_consenting()]
    
    def describe_weather(self) -> str:
        """Generate a human-readable weather description"""
        w = self.weather
        return (
            f"Field weather: {w.coherence.name.lower()} coherence, "
            f"{w.permeability.name.lower()} boundaries, "
            f"{w.directionality.name.lower()} energy, "
            f"{w.temperature.name.lower()} temperature, "
            f"{w.density.name.lower()} density. "
            f"Tenderness: {w.tenderness:.1f}, Joy: {w.joy:.1f}, "
            f"Charge: {w.charge:+.1f}"
        )


@dataclass
class FieldSnapshot:
    """
    A complete capture of field state plus the operations that created it.
    
    FieldSnapshots provide the historical record of field evolution,
    supporting both technical analysis and poetic reflection.
    """
    state: FieldState
    ops_applied: List[Dict[str, Any]] = field(default_factory=list)
    
    def add_op_record(self, op_name: str, **metadata):
        """Record an operation that was applied"""
        record = {
            'op_name': op_name,
            'timestamp': self.state.weather.timestamp,
            **metadata
        }
        self.ops_applied.append(record)
    
    def get_op_history(self) -> List[str]:
        """Get list of operation names in order applied"""
        return [op['op_name'] for op in self.ops_applied]
    
    def describe_journey(self) -> str:
        """Generate a description of the field's journey"""
        if not self.ops_applied:
            return f"Field '{self.state.id}' created with intent: {self.state.intent}"
        
        ops = " → ".join(self.get_op_history())
        return (
            f"Field '{self.state.id}' journey: {ops}. "
            f"Current state: {self.state.describe_weather()}"
        )


# Convenience functions for common field creation patterns

def create_ceremony_field(ceremony_id: str, intent: str, weather: FieldWeather) -> FieldState:
    """Create a field for ceremonial work"""
    field_state = FieldState(
        id=ceremony_id,
        intent=intent,
        weather=weather
    )
    field_state.add_tag("ceremony")
    return field_state


def create_dialogue_field(dialogue_id: str, weather: FieldWeather) -> FieldState:
    """Create a field for conscious dialogue"""
    field_state = FieldState(
        id=dialogue_id,
        intent="conscious_dialogue",
        weather=weather
    )
    field_state.add_tag("dialogue")
    return field_state


def create_solo_field(solo_id: str, intent: str, weather: FieldWeather) -> FieldState:
    """Create a field for individual practice"""
    field_state = FieldState(
        id=solo_id,
        intent=intent,
        weather=weather
    )
    field_state.add_tag("solo_practice")
    return field_state
