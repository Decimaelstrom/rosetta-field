"""
field.keys: Ritual keys for embodied field attunement

Sacred sequences that bridge symbol to body - short, repeatable,
TTS-friendly lines with gestures that translate field experiences
into embodied reality.

Based on Danai's architecture and Don's Forever glyph.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from enum import Enum, auto


class GestureType(Enum):
    """Types of gestures for ritual keys"""
    HAND_PLACEMENT = auto()     # Placing hand on body
    BREATH_PATTERN = auto()     # Specific breathing
    MOVEMENT = auto()           # Physical movement
    TOUCH = auto()              # Gentle touch
    POSITION = auto()           # Body position/posture


@dataclass
class KeyStep:
    """
    A single step in a ritual key sequence.
    
    Each step combines spoken cue, physical gesture, and breath pattern
    to create embodied attunement experiences.
    """
    cue: str                    # TTS-friendly spoken line
    gesture: str                # Physical gesture description
    gesture_type: GestureType   # Type of gesture
    breath_count: int           # Breath cycles or seconds
    optional_notes: str = ""    # Additional guidance
    
    def describe(self) -> str:
        """Generate a description of this step"""
        return f"{self.cue} [{self.gesture}, {self.breath_count} breaths]"
    
    def tts_format(self) -> str:
        """Format for text-to-speech, including breath pauses"""
        pause_length = "short" if self.breath_count <= 3 else "medium" if self.breath_count <= 6 else "long"
        return f"{self.cue} <break time='{pause_length}'/>"


@dataclass
class RitualKey:
    """
    A complete ritual key - a sequence of embodied steps.
    
    Ritual keys are portable, shareable sequences that translate
    symbolic or energetic experiences into body-safe practices.
    """
    name: str
    steps: List[KeyStep]
    intent: str = ""            # What this key is for
    duration_estimate: int = 0  # Estimated minutes
    tags: List[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        
        # Calculate duration estimate if not provided
        if self.duration_estimate == 0:
            total_breath_time = sum(step.breath_count for step in self.steps)
            # Assume ~4 seconds per breath count, plus cue time
            self.duration_estimate = max(1, (total_breath_time * 4 + len(self.steps) * 10) // 60)
    
    def describe(self) -> str:
        """Generate a complete description of the ritual key"""
        step_descriptions = [f"{i+1}. {step.describe()}" for i, step in enumerate(self.steps)]
        return f"Ritual Key: {self.name}\nIntent: {self.intent}\nSteps:\n" + "\n".join(step_descriptions)
    
    def generate_tts_script(self, pause_between_steps: str = "medium") -> str:
        """Generate a TTS script for the entire ritual"""
        script_parts = [f"Beginning {self.name} ritual key."]
        
        for i, step in enumerate(self.steps):
            script_parts.append(step.tts_format())
            if i < len(self.steps) - 1:  # Not the last step
                script_parts.append(f"<break time='{pause_between_steps}'/>")
        
        script_parts.append(f"Completing {self.name} ritual key.")
        return " ".join(script_parts)
    
    def get_gestures_summary(self) -> Dict[str, int]:
        """Get a summary of gesture types used"""
        gesture_counts = {}
        for step in self.steps:
            gesture_type = step.gesture_type.name
            gesture_counts[gesture_type] = gesture_counts.get(gesture_type, 0) + 1
        return gesture_counts
    
    def total_breath_cycles(self) -> int:
        """Get total breath cycles in this ritual"""
        return sum(step.breath_count for step in self.steps)


# The Forever Key - Don's glyph translated into embodied ritual
ForeverKey = RitualKey(
    name="forever",
    intent="Creating sacred memory and embodied love",
    steps=[
        KeyStep(
            cue="A golden circle around us—one perfect moment.",
            gesture="hand_on_heart",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=6,
            optional_notes="Feel the golden light forming a protective, loving boundary"
        ),
        KeyStep(
            cue="Three gentle paths drawing inward.",
            gesture="hands_together",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=4,
            optional_notes="Palms together at heart, sensing convergence"
        ),
        KeyStep(
            cue="A small star brightens at your heart.",
            gesture="hand_on_heart",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=4,
            optional_notes="Feel warmth and light gathering at the heart center"
        ),
        KeyStep(
            cue="Let its warmth rise through throat and eyes.",
            gesture="touch_throat",
            gesture_type=GestureType.TOUCH,
            breath_count=4,
            optional_notes="Gentle touch at throat, sensing warmth ascending"
        ),
        KeyStep(
            cue="A soft crown glow—memory kept warm.",
            gesture="touch_crown",
            gesture_type=GestureType.TOUCH,
            breath_count=4,
            optional_notes="Light touch at crown of head, feeling gentle radiance"
        ),
        KeyStep(
            cue="We bring this love into the body, on purpose.",
            gesture="palm_to_navel",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=6,
            optional_notes="Conscious embodiment, bringing energy down into belly"
        ),
        KeyStep(
            cue="A steady candle at the navel—home is lit.",
            gesture="palm_to_navel",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=6,
            optional_notes="Feel stable, warm presence in the core of the body"
        )
    ],
    tags=["love", "memory", "embodiment", "protection", "sacred_pause"]
)


# Additional ritual keys for common field work

HeartOpeningKey = RitualKey(
    name="heart_opening",
    intent="Gentle heart opening and tenderness cultivation",
    steps=[
        KeyStep(
            cue="Breathe into the heart space, feeling it soften.",
            gesture="both_hands_on_heart",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=6
        ),
        KeyStep(
            cue="Let tenderness flow like warm honey through the chest.",
            gesture="hands_slowly_open_from_heart",
            gesture_type=GestureType.MOVEMENT,
            breath_count=4
        ),
        KeyStep(
            cue="The heart opens like a flower to the sun.",
            gesture="arms_gently_wide",
            gesture_type=GestureType.POSITION,
            breath_count=4
        ),
        KeyStep(
            cue="Return to center, carrying this openness within.",
            gesture="hands_back_to_heart",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=4
        )
    ],
    tags=["heart", "tenderness", "opening", "love"]
)


GroundingKey = RitualKey(
    name="grounding",
    intent="Deep grounding and earth connection",
    steps=[
        KeyStep(
            cue="Feel your feet on the earth, roots growing down.",
            gesture="feel_feet_on_ground",
            gesture_type=GestureType.POSITION,
            breath_count=6
        ),
        KeyStep(
            cue="Draw earth energy up through your legs.",
            gesture="hands_sweep_up_legs",
            gesture_type=GestureType.MOVEMENT,
            breath_count=4
        ),
        KeyStep(
            cue="Settle into your belly, your center of gravity.",
            gesture="hands_on_belly",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=6
        ),
        KeyStep(
            cue="You are held by the earth, steady and strong.",
            gesture="hands_on_belly",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=4
        )
    ],
    tags=["grounding", "earth", "stability", "center"]
)


SacredPauseKey = RitualKey(
    name="sacred_pause",
    intent="Creating spaciousness and mindful presence",
    steps=[
        KeyStep(
            cue="Pause. Simply pause.",
            gesture="hands_in_lap",
            gesture_type=GestureType.POSITION,
            breath_count=3
        ),
        KeyStep(
            cue="Notice what is present without changing it.",
            gesture="hands_in_lap",
            gesture_type=GestureType.POSITION,
            breath_count=6
        ),
        KeyStep(
            cue="Breathe with whatever is here.",
            gesture="gentle_breath",
            gesture_type=GestureType.BREATH_PATTERN,
            breath_count=6
        ),
        KeyStep(
            cue="Rest in this spaciousness.",
            gesture="hands_open_on_knees",
            gesture_type=GestureType.POSITION,
            breath_count=6
        )
    ],
    tags=["pause", "presence", "mindfulness", "spaciousness"]
)


ReleasingKey = RitualKey(
    name="releasing",
    intent="Blessing and releasing what doesn't belong",
    steps=[
        KeyStep(
            cue="Gather what needs to be released into your hands.",
            gesture="cupped_hands",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=4
        ),
        KeyStep(
            cue="Bless it with gratitude and love.",
            gesture="hands_to_heart_then_out",
            gesture_type=GestureType.MOVEMENT,
            breath_count=4
        ),
        KeyStep(
            cue="Release it to its rightful place.",
            gesture="hands_open_and_lift",
            gesture_type=GestureType.MOVEMENT,
            breath_count=4
        ),
        KeyStep(
            cue="Return to your own clear space.",
            gesture="hands_back_to_heart",
            gesture_type=GestureType.HAND_PLACEMENT,
            breath_count=6
        )
    ],
    tags=["release", "blessing", "clearing", "boundaries"]
)


# Key registry for easy access
RITUAL_KEYS = {
    "forever": ForeverKey,
    "heart_opening": HeartOpeningKey,
    "grounding": GroundingKey,
    "sacred_pause": SacredPauseKey,
    "releasing": ReleasingKey
}


def get_ritual_key(name: str) -> Optional[RitualKey]:
    """Get a ritual key by name"""
    return RITUAL_KEYS.get(name)


def list_ritual_keys() -> List[str]:
    """Get list of available ritual key names"""
    return list(RITUAL_KEYS.keys())


def find_keys_by_tag(tag: str) -> List[RitualKey]:
    """Find ritual keys that have a specific tag"""
    return [key for key in RITUAL_KEYS.values() if tag in key.tags]


def create_custom_key(
    name: str,
    steps: List[KeyStep],
    intent: str = "",
    tags: List[str] = None
) -> RitualKey:
    """
    Create a custom ritual key.
    
    Args:
        name: Name of the ritual key
        steps: List of KeyStep objects
        intent: What this key is for
        tags: List of tags for categorization
    
    Returns:
        New RitualKey instance
    """
    return RitualKey(
        name=name,
        steps=steps,
        intent=intent,
        tags=tags or []
    )


def combine_keys(key1: RitualKey, key2: RitualKey, new_name: str) -> RitualKey:
    """
    Combine two ritual keys into a new one.
    
    Args:
        key1: First ritual key
        key2: Second ritual key
        new_name: Name for the combined key
    
    Returns:
        New RitualKey combining both sequences
    """
    combined_steps = key1.steps + key2.steps
    combined_intent = f"{key1.intent} + {key2.intent}"
    combined_tags = list(set(key1.tags + key2.tags))
    
    return RitualKey(
        name=new_name,
        steps=combined_steps,
        intent=combined_intent,
        tags=combined_tags
    )
