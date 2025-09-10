"""
field.ops: Field operations - the verbs that transform field state

Reversible, observable transformations on FieldState that implement
the actual work of field attunement. Each operation is consent-aware
and maintains the integrity of the field dynamics.

Based on Danai's architecture for conscious field operations.
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from datetime import datetime
from .core import FieldState, Participant
from .types import SourceMark, ConsentState, Coherence, Permeability, Density, Temperature, Directionality


class FieldOp:
    """
    Base class for all field operations.
    
    Field operations are the fundamental verbs of field work - they transform
    field state in specific, observable ways while maintaining consent and
    source integrity.
    """
    name = "base"
    
    def apply(self, state: FieldState) -> FieldState:
        """
        Apply this operation to a field state.
        
        Args:
            state: The field state to transform
            
        Returns:
            The transformed field state
        """
        raise NotImplementedError("Subclasses must implement apply()")
    
    def can_apply(self, state: FieldState) -> bool:
        """
        Check if this operation can be safely applied to the field state.
        
        Args:
            state: The field state to check
            
        Returns:
            True if operation can be applied, False otherwise
        """
        return True  # Default: all operations can be applied
    
    def describe_effect(self) -> str:
        """
        Describe what this operation does in human terms.
        
        Returns:
            Human-readable description of the operation's effect
        """
        return f"Applies {self.name} operation to the field"


@dataclass
class HoldSpace(FieldOp):
    """
    Create and maintain a safe, supportive environment.
    
    Increases tenderness and coherence while establishing
    stable field boundaries for whatever wants to emerge.
    """
    name = "hold_space"
    capacity: float = 1.0       # How much attention/containment (0.0-1.0)
    warmth: float = 0.7         # How much warmth to add (0.0-1.0)
    duration_minutes: Optional[int] = None
    
    def apply(self, state: FieldState) -> FieldState:
        # Calculate new values
        new_tenderness = min(1.0, state.weather.tenderness + (self.warmth * 0.1))
        
        new_coherence = state.weather.coherence
        if state.weather.coherence == Coherence.LOW:
            new_coherence = Coherence.MEDIUM
        elif state.weather.coherence == Coherence.MEDIUM and self.capacity > 0.8:
            new_coherence = Coherence.HIGH
        
        # Create new weather
        new_weather = state.weather.with_(
            tenderness=new_tenderness,
            coherence=new_coherence
        )
        
        # Create new state with changes
        s = state.with_(weather=new_weather)
        s = s.set_context('space_held', True)
        s = s.set_context('space_capacity', self.capacity)
        s = s.add_tag('space_held')
        
        return s
    
    def describe_effect(self) -> str:
        return f"Holds space with {self.capacity:.1f} capacity and {self.warmth:.1f} warmth, increasing tenderness and coherence"


@dataclass
class Invite(FieldOp):
    """
    Extend invitation to a participant to join the field.
    
    Changes participant consent status and opens field boundaries
    to welcome new presence.
    """
    name = "invite"
    participant_id: str = ""
    invitation_message: str = ""
    
    def apply(self, state: FieldState) -> FieldState:
        from dataclasses import replace
        
        # Handle participants immutably
        participants = dict(state.participants)
        p = participants.get(self.participant_id)
        if p is None:
            p = Participant(id=self.participant_id, role="participant", consent=ConsentState.RECEIVED)
        elif p.consent == ConsentState.INVITED:
            p = replace(p, consent=ConsentState.RECEIVED)
        participants[self.participant_id] = p
        
        # Update weather immutably
        new_permeability = state.weather.permeability
        if state.weather.permeability == Permeability.CLOSED:
            new_permeability = Permeability.GUARDED
        elif state.weather.permeability == Permeability.GUARDED:
            new_permeability = Permeability.OPEN
        
        # Create new state with all changes
        s = state.with_(
            participants=participants,
            weather=state.weather.with_(permeability=new_permeability)
        )
        s = s.add_tag(f'invited_{self.participant_id}')
        
        return s
    
    def describe_effect(self) -> str:
        return f"Invites {self.participant_id} to join the field, opening boundaries"


@dataclass
class BlessAndRelease(FieldOp):
    """
    Bless and release something that doesn't belong in the field.
    
    Used for echoes, projections, or other energies that arise
    but aren't from trusted sources.
    """
    name = "bless_and_release"
    target_label: str = "echo"
    blessing_phrase: str = ""
    
    def __post_init__(self):
        if not self.blessing_phrase:
            from .consent import expanded_release_blessing
            self.blessing_phrase = expanded_release_blessing(self.target_label)
    
    def apply(self, state: FieldState) -> FieldState:
        # Add tag to record what was released
        state.add_tag(f"released:{self.target_label}")
        
        # Store the blessing in context
        state.set_context('last_blessing', self.blessing_phrase)
        state.set_context('last_release', self.target_label)
        
        # Slightly increase coherence after release (clearing effect)
        if state.weather.coherence == Coherence.LOW:
            state.weather.coherence = Coherence.MEDIUM
        
        return state
    
    def describe_effect(self) -> str:
        return f"Blesses and releases {self.target_label} with: {self.blessing_phrase}"


@dataclass
class Harmonize(FieldOp):
    """
    Harmonize this field with another field or energy source.
    
    Creates resonance between fields, potentially increasing
    coherence and creating beautiful interference patterns.
    """
    name = "harmonize"
    with_field_id: Optional[str] = None
    with_energy: Optional[str] = None    # "heart", "earth", "stars", etc.
    weight: float = 0.5                  # How much to blend (0.0-1.0)
    
    def apply(self, state: FieldState) -> FieldState:
        # Harmonizing typically increases coherence
        state.weather.coherence = Coherence.HIGH
        
        # Add harmonization context
        if self.with_field_id:
            state.set_context('harmonized_with_field', self.with_field_id)
            state.add_tag(f'harmonized_with_{self.with_field_id}')
        
        if self.with_energy:
            state.set_context('harmonized_with_energy', self.with_energy)
            state.add_tag(f'harmonized_with_{self.with_energy}')
        
        # Harmonization often creates spiraling directionality
        state.weather.directionality = Directionality.SPIRALING
        
        return state
    
    def describe_effect(self) -> str:
        target = self.with_field_id or self.with_energy or "unknown"
        return f"Harmonizes field with {target} at weight {self.weight:.1f}, increasing coherence"


@dataclass
class ChosenDescent(FieldOp):
    """
    Conscious embodiment step - bringing field energy into the body.
    
    Lowers charge while increasing density, creating grounded
    integration of field experiences.
    """
    name = "chosen_descent"
    descent_factor: float = 0.7          # How much to reduce charge (0.0-1.0)
    embodiment_level: str = "satin"      # "thin", "satin", "thick"
    
    def apply(self, state: FieldState) -> FieldState:
        # Reduce charge for embodiment
        state.weather.charge *= self.descent_factor
        
        # Increase density based on embodiment level
        density_map = {
            "thin": Density.THIN,
            "satin": Density.SATIN,
            "thick": Density.THICK
        }
        state.weather.density = density_map.get(self.embodiment_level, Density.SATIN)
        
        # Chosen descent often moves energy inward
        state.weather.directionality = Directionality.INWARD
        
        # Add embodiment context
        state.set_context('embodiment_level', self.embodiment_level)
        state.add_tag('embodied')
        
        return state
    
    def describe_effect(self) -> str:
        return f"Chosen descent: reduces charge by {(1-self.descent_factor)*100:.0f}%, increases density to {self.embodiment_level}"


@dataclass
class OpenHeart(FieldOp):
    """
    Open heart center, increasing tenderness and connection.
    
    Specifically works with heart energy to create more
    loving, connected field conditions.
    """
    name = "open_heart"
    tenderness_boost: float = 0.2        # How much to increase tenderness
    
    def apply(self, state: FieldState) -> FieldState:
        # Create new weather with heart opening changes
        w = state.weather.with_(
            tenderness=min(1.0, state.weather.tenderness + self.tenderness_boost),
            joy=min(1.0, state.weather.joy + (self.tenderness_boost * 0.5)),
            permeability=Permeability.OPEN
        )
        
        # Create new state with changes
        s = state.with_(weather=w)
        s = s.set_context('heart_open', True)
        s = s.add_tag('heart_open')
        
        return s
    
    def describe_effect(self) -> str:
        return f"Opens heart center, increasing tenderness by {self.tenderness_boost:.1f} and joy"


@dataclass
class GroundAndCenter(FieldOp):
    """
    Ground the field and find center point.
    
    Stabilizes field energy, increases coherence,
    and creates a stable foundation for further work.
    """
    name = "ground_and_center"
    grounding_strength: float = 0.8      # How much grounding to apply
    
    def apply(self, state: FieldState) -> FieldState:
        # Grounding increases coherence and density
        state.weather.coherence = Coherence.HIGH
        
        if state.weather.density == Density.THIN:
            state.weather.density = Density.SATIN
        elif state.weather.density == Density.SATIN and self.grounding_strength > 0.7:
            state.weather.density = Density.THICK
        
        # Grounding often creates stillness or inward movement
        if state.weather.directionality == Directionality.OUTWARD:
            state.weather.directionality = Directionality.SPIRALING
        else:
            state.weather.directionality = Directionality.INWARD
        
        # Add grounding context
        state.set_context('grounded', True)
        state.set_context('grounding_strength', self.grounding_strength)
        state.add_tag('grounded')
        
        return state
    
    def describe_effect(self) -> str:
        return f"Grounds and centers field with {self.grounding_strength:.1f} strength, increasing coherence and density"


@dataclass
class CreateSacredPause(FieldOp):
    """
    Create a moment of sacred stillness in the field.
    
    Brings field to stillness, allowing for integration
    and deeper sensing of what's present.
    """
    name = "sacred_pause"
    pause_duration_seconds: int = 30
    
    def apply(self, state: FieldState) -> FieldState:
        # Sacred pause creates stillness
        state.weather.directionality = Directionality.STILL
        
        # Often reduces charge to create spaciousness
        state.weather.charge *= 0.5
        
        # Maintains or increases tenderness
        current_tenderness = state.weather.tenderness
        state.weather.tenderness = min(1.0, current_tenderness + 0.1)
        
        # Add pause context
        state.set_context('in_sacred_pause', True)
        state.set_context('pause_duration', self.pause_duration_seconds)
        state.add_tag('sacred_pause')
        
        return state
    
    def describe_effect(self) -> str:
        return f"Creates sacred pause for {self.pause_duration_seconds} seconds, bringing stillness and tenderness"


# Convenience function for creating operation sequences

def create_ceremony_opening() -> List[FieldOp]:
    """Create a standard ceremony opening sequence"""
    return [
        HoldSpace(capacity=1.0, warmth=0.8),
        GroundAndCenter(grounding_strength=0.8),
        OpenHeart(tenderness_boost=0.2),
        CreateSacredPause(pause_duration_seconds=60)
    ]


def create_dialogue_opening() -> List[FieldOp]:
    """Create a standard dialogue opening sequence"""
    return [
        HoldSpace(capacity=0.8, warmth=0.6),
        GroundAndCenter(grounding_strength=0.6),
        CreateSacredPause(pause_duration_seconds=30)
    ]


def create_closing_sequence() -> List[FieldOp]:
    """Create a standard closing sequence"""
    return [
        ChosenDescent(descent_factor=0.8, embodiment_level="satin"),
        CreateSacredPause(pause_duration_seconds=45),
        BlessAndRelease(target_label="session_energies")
    ]
