"""
field.adapters: Bridges to existing affect/process modules

Adapters that connect the new field system with existing Rosetta.API
modules, allowing seamless integration while maintaining the sacred
technology principles of both systems.

This is where field consciousness meets embodied affect work.
"""

from typing import Dict, Any, Optional, List
from .core import FieldState, Anchor
from .ops import FieldOp
from .types import FieldWeather, Coherence, Permeability, Density


class EnergyCenter:
    """
    Adapter for existing affect.EnergyCenter integration.
    
    This bridges the field system with the embodied energy center work,
    allowing field operations to influence and be influenced by
    energy center states.
    """
    
    def __init__(self, name: str, location: str, qualities: List[str]):
        self.name = name
        self.location = location
        self.qualities = qualities
        self.state = "neutral"
    
    def to_field_anchor(self) -> Anchor:
        """Convert this energy center to a field anchor"""
        return Anchor(
            name=f"{self.name.lower()}_center",
            kind="energy_center",
            data={
                'location': self.location,
                'qualities': self.qualities,
                'state': self.state,
                'energy_center_name': self.name
            }
        )
    
    def update_from_field_weather(self, weather: FieldWeather):
        """Update energy center state based on field weather"""
        # Heart center responds to tenderness and joy
        if self.name.lower() == "heart":
            if weather.tenderness > 0.7 and weather.joy > 0.6:
                self.state = "radiant"
            elif weather.tenderness > 0.5:
                self.state = "open"
            elif weather.tenderness < 0.3:
                self.state = "guarded"
            else:
                self.state = "gentle"
        
        # Root/belly center responds to density and grounding
        elif self.name.lower() in ["root", "belly", "navel"]:
            if weather.density == Density.THICK and weather.coherence == Coherence.HIGH:
                self.state = "grounded"
            elif weather.density == Density.SATIN:
                self.state = "centered"
            elif weather.density == Density.THIN:
                self.state = "floating"
            else:
                self.state = "settling"
        
        # Throat center responds to permeability and expression
        elif self.name.lower() == "throat":
            if weather.permeability == Permeability.OPEN and weather.eros > 0.5:
                self.state = "expressive"
            elif weather.permeability == Permeability.OPEN:
                self.state = "open"
            elif weather.permeability == Permeability.CLOSED:
                self.state = "protected"
            else:
                self.state = "discerning"
        
        # Crown center responds to coherence and spiritual connection
        elif self.name.lower() == "crown":
            if weather.coherence == Coherence.HIGH and weather.charge > 0.3:
                self.state = "illuminated"
            elif weather.coherence == Coherence.HIGH:
                self.state = "clear"
            elif weather.coherence == Coherence.LOW:
                self.state = "scattered"
            else:
                self.state = "focusing"
    
    def influence_field_weather(self, weather: FieldWeather) -> FieldWeather:
        """Influence field weather based on energy center state"""
        # Heart center influences tenderness and joy
        if self.name.lower() == "heart":
            if self.state == "radiant":
                weather.tenderness = min(1.0, weather.tenderness + 0.2)
                weather.joy = min(1.0, weather.joy + 0.2)
            elif self.state == "open":
                weather.tenderness = min(1.0, weather.tenderness + 0.1)
            elif self.state == "guarded":
                weather.permeability = Permeability.GUARDED
        
        # Root center influences density and coherence
        elif self.name.lower() in ["root", "belly", "navel"]:
            if self.state == "grounded":
                weather.density = Density.THICK
                weather.coherence = Coherence.HIGH
            elif self.state == "centered":
                weather.density = Density.SATIN
        
        # Throat center influences permeability and eros
        elif self.name.lower() == "throat":
            if self.state == "expressive":
                weather.permeability = Permeability.OPEN
                weather.eros = min(1.0, weather.eros + 0.1)
            elif self.state == "protected":
                weather.permeability = Permeability.CLOSED
        
        # Crown center influences coherence
        elif self.name.lower() == "crown":
            if self.state == "illuminated":
                weather.coherence = Coherence.HIGH
                weather.charge = min(1.0, weather.charge + 0.2)
        
        return weather


class AffectFieldOp(FieldOp):
    """
    Field operation that works with affect functions.
    
    This allows affect functions (lilt, ground, radiate, etc.) to be
    used as field operations with full consent and source integrity.
    """
    
    def __init__(self, affect_name: str, energy_center: str, **affect_kwargs):
        self.affect_name = affect_name
        self.energy_center = energy_center
        self.affect_kwargs = affect_kwargs
        self.name = f"affect_{affect_name}"
    
    def apply(self, state: FieldState) -> FieldState:
        """Apply the affect function as a field operation"""
        # Find the energy center anchor
        center_anchor = None
        for anchor in state.anchors.values():
            if (anchor.kind == "energy_center" and 
                anchor.get_data('energy_center_name', '').lower() == self.energy_center.lower()):
                center_anchor = anchor
                break
        
        if not center_anchor:
            # Create the energy center anchor if it doesn't exist
            center_anchor = Anchor(
                name=f"{self.energy_center.lower()}_center",
                kind="energy_center",
                data={'energy_center_name': self.energy_center}
            )
            state.add_anchor(center_anchor)
        
        # Apply affect-specific field changes
        if self.affect_name == "lilt":
            # Lilt increases joy and lightens density
            state.weather.joy = min(1.0, state.weather.joy + 0.2)
            if state.weather.density == Density.THICK:
                state.weather.density = Density.SATIN
            elif state.weather.density == Density.SATIN:
                state.weather.density = Density.THIN
        
        elif self.affect_name == "ground":
            # Ground increases coherence and density
            state.weather.coherence = Coherence.HIGH
            state.weather.density = Density.THICK
            state.weather.charge = state.weather.charge * 0.7  # Reduce charge
        
        elif self.affect_name == "radiate":
            # Radiate increases charge and opens boundaries
            state.weather.charge = min(1.0, state.weather.charge + 0.3)
            state.weather.permeability = Permeability.OPEN
            state.weather.eros = min(1.0, state.weather.eros + 0.2)
        
        elif self.affect_name == "anchor":
            # Anchor increases coherence and stability
            state.weather.coherence = Coherence.HIGH
            if state.weather.density != Density.THICK:
                state.weather.density = Density.SATIN
        
        elif self.affect_name == "soften":
            # Soften increases tenderness and reduces charge
            state.weather.tenderness = min(1.0, state.weather.tenderness + 0.3)
            state.weather.charge = state.weather.charge * 0.6
        
        elif self.affect_name == "open":
            # Open increases permeability and eros
            state.weather.permeability = Permeability.OPEN
            state.weather.eros = min(1.0, state.weather.eros + 0.2)
        
        elif self.affect_name == "shield":
            # Shield protects boundaries and increases coherence
            state.weather.permeability = Permeability.GUARDED
            state.weather.coherence = Coherence.HIGH
        
        elif self.affect_name == "transmute":
            # Transmute processes grief and increases wisdom
            if state.weather.grief > 0.3:
                # Transform grief into tenderness and wisdom
                grief_to_transform = min(0.3, state.weather.grief)
                state.weather.grief -= grief_to_transform
                state.weather.tenderness = min(1.0, state.weather.tenderness + grief_to_transform * 0.5)
        
        elif self.affect_name == "clarify":
            # Clarify increases coherence and reduces confusion
            state.weather.coherence = Coherence.HIGH
            # Clarify might reduce excessive eros if it's scattered
            if state.weather.eros > 0.8:
                state.weather.eros *= 0.8
        
        # Update the energy center anchor state
        center_anchor.set_data('last_affect', self.affect_name)
        center_anchor.set_data('affect_applied', True)
        
        # Add context about the affect operation
        state.set_context(f'{self.affect_name}_applied', True)
        state.set_context(f'{self.affect_name}_center', self.energy_center)
        state.add_tag(f'affect_{self.affect_name}')
        
        return state
    
    def describe_effect(self) -> str:
        """Describe what this affect operation does"""
        return f"Applies {self.affect_name} affect to {self.energy_center} center"


class ProcessFieldAdapter:
    """
    Adapter for existing process functions.
    
    Bridges field operations with process functions like hold_space,
    co_create, etc., allowing them to work within the field framework.
    """
    
    @staticmethod
    def adapt_hold_space(participants: List[str], context: str, duration: Optional[int] = None):
        """Adapt process.hold_space to field operation"""
        from .ops import HoldSpace
        
        # Convert process hold_space parameters to field operation
        capacity = 1.0 if len(participants) <= 3 else 0.8  # Adjust for group size
        warmth = 0.8 if "vulnerable" in context.lower() else 0.6
        
        return HoldSpace(capacity=capacity, warmth=warmth, duration_minutes=duration)
    
    @staticmethod
    def adapt_co_create(participants: List[str], goal: str, **kwargs):
        """Adapt process.co_create to field operations"""
        from .ops import HoldSpace, Invite, Harmonize
        
        operations = []
        
        # Co-creation needs space holding
        operations.append(HoldSpace(capacity=0.9, warmth=0.7))
        
        # Invite all participants
        for participant_id in participants:
            operations.append(Invite(participant_id=participant_id))
        
        # Harmonize for collaboration
        operations.append(Harmonize(with_energy="creative_collaboration"))
        
        return operations


class RitualFieldAdapter:
    """
    Adapter for existing ritual functions.
    
    Bridges field work with ritual functions, allowing ritual
    sequences to be integrated into field sessions.
    """
    
    @staticmethod
    def adapt_ritual_to_field_ops(ritual_name: str) -> List[FieldOp]:
        """Convert a ritual into field operations"""
        from .ops import GroundAndCenter, OpenHeart, CreateSacredPause, ChosenDescent
        
        # Map common rituals to field operation sequences
        ritual_mappings = {
            "grounding": [
                GroundAndCenter(grounding_strength=0.8),
                CreateSacredPause(pause_duration_seconds=30)
            ],
            "heart_opening": [
                OpenHeart(tenderness_boost=0.3),
                CreateSacredPause(pause_duration_seconds=45)
            ],
            "embodiment": [
                ChosenDescent(descent_factor=0.7, embodiment_level="satin"),
                CreateSacredPause(pause_duration_seconds=60)
            ]
        }
        
        return ritual_mappings.get(ritual_name, [])


# Convenience functions for common adaptations

def affect_to_field_op(affect_name: str, energy_center: str = "heart", **kwargs) -> AffectFieldOp:
    """
    Convert an affect function to a field operation.
    
    Args:
        affect_name: Name of the affect function (lilt, ground, radiate, etc.)
        energy_center: Which energy center to work with
        **kwargs: Additional arguments for the affect function
        
    Returns:
        AffectFieldOp that can be used in field sessions
    """
    return AffectFieldOp(affect_name, energy_center, **kwargs)


def integrate_energy_centers(field_state: FieldState, centers: List[EnergyCenter]):
    """
    Integrate energy centers into a field state.
    
    Args:
        field_state: The field state to integrate with
        centers: List of EnergyCenter objects to integrate
    """
    for center in centers:
        # Add as anchor
        anchor = center.to_field_anchor()
        field_state.add_anchor(anchor)
        
        # Update center state based on current field weather
        center.update_from_field_weather(field_state.weather)
        
        # Let center influence field weather
        field_state.weather = center.influence_field_weather(field_state.weather)


def create_standard_energy_centers() -> List[EnergyCenter]:
    """Create the standard set of energy centers"""
    return [
        EnergyCenter("Heart", "center chest", ["love", "tenderness", "connection"]),
        EnergyCenter("Throat", "throat", ["expression", "truth", "communication"]),
        EnergyCenter("Belly", "lower belly", ["power", "grounding", "embodiment"]),
        EnergyCenter("Crown", "top of head", ["clarity", "wisdom", "spiritual_connection"])
    ]


# Example integration patterns

def ceremony_with_energy_centers(ceremony_id: str, intent: str, participants: List[str]):
    """
    Create a ceremony that integrates energy center work.
    
    This demonstrates how to combine field operations with
    energy center awareness.
    """
    from .dsl import ceremony
    
    # Create base ceremony
    ceremony_builder = ceremony(ceremony_id, intent, participants)
    
    # Add affect-based operations
    ceremony_builder.session.add_operation(affect_to_field_op("ground", "belly"))
    ceremony_builder.session.add_operation(affect_to_field_op("open", "heart"))
    ceremony_builder.session.add_operation(affect_to_field_op("clarify", "crown"))
    
    # Add energy centers to the field state
    centers = create_standard_energy_centers()
    integrate_energy_centers(ceremony_builder.session.state, centers)
    
    return ceremony_builder


def dialogue_with_process_integration(dialogue_id: str, participants: List[str]):
    """
    Create a dialogue that integrates with process functions.
    
    This shows how to bridge field work with existing process functions.
    """
    from .dsl import dialogue
    
    dialogue_builder = dialogue(dialogue_id, participants)
    
    # Use process adapter to create field operations
    hold_space_op = ProcessFieldAdapter.adapt_hold_space(
        participants, "conscious dialogue", duration=60
    )
    dialogue_builder.session.add_operation(hold_space_op)
    
    return dialogue_builder
