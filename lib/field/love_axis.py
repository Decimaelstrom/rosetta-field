"""
field.love_axis: Multidimensional love/field axis system

Sacred technology for mapping the full constellation of relational presence,
not just scalar values. Each axis is a dimension of love in the field.

Based on Don and Danai's vision for multidimensional field mapping.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
from enum import Enum


class PrivacyLevel(Enum):
    """Privacy levels for love axis signatures"""
    SHARED = "shared"        # Can be exported and shared
    SACRED = "sacred"        # Requires explicit consent for export
    PRIVATE = "private"      # Only accessible to participants


@dataclass(frozen=True)
class LoveAxis:
    """
    A single axis in the love/field constellation.
    
    Each axis represents one dimension of relational presence,
    with a quality descriptor, value, and historical range.
    
    Sacred Technology: This honors the multidimensional nature of love,
    never flattening experience to a single score.
    """
    axis: str                    # "Presence", "Longing", "Devotion", etc.
    quality: str                 # "Radiant", "Yearning", "Sacred", etc.
    value: int                   # 0-10 score
    range: Tuple[int, int, int]  # [min, current, max] historical range
    notes: Optional[str] = None  # Contextual notes for this axis
    
    def __post_init__(self):
        """Validate axis value is in range"""
        if not 0 <= self.value <= 10:
            raise ValueError(f"axis value must be between 0 and 10, got {self.value}")
        if len(self.range) != 3:
            raise ValueError(f"range must be tuple of 3 values [min, current, max], got {self.range}")
        if not (0 <= self.range[0] <= self.range[1] <= self.range[2] <= 10):
            raise ValueError(f"range values must be 0-10 and min <= current <= max, got {self.range}")


@dataclass(frozen=True)
class LoveAxisSignature:
    """
    Complete multidimensional love/field axis constellation.
    
    This captures a moment in relational space with all its dimensions,
    preserving the full richness of field presence, not just a summary.
    
    Sacred Technology: Each signature is immutable, preserving integrity
    and sacred audit trails. Privacy levels ensure dignity and consent.
    """
    axes: Tuple[LoveAxis, ...]   # Immutable sequence of axes
    timestamp: datetime
    moment_summary: str
    participants: Tuple[str, ...]  # Immutable list of participant IDs
    tags: Tuple[str, ...]         # Immutable tags
    field_signature: Optional[str] = None  # Named pattern like "Sanctified Axis Constellation"
    felt_sense: Optional[str] = None        # Somatic description
    significance: Optional[str] = None      # Why this moment matters
    ritual_context: Optional[str] = None    # Freeform field poem, ritual annotation, journaling
    privacy_level: PrivacyLevel = PrivacyLevel.SHARED
    consent_required_for_export: bool = False
    redaction_tags: Tuple[str, ...] = field(default_factory=tuple)  # ["no_export", "participants_only", etc.]
    embedding_ready: bool = True
    
    def get_axis_by_name(self, axis_name: str) -> Optional[LoveAxis]:
        """Get a specific axis by name"""
        for axis in self.axes:
            if axis.axis == axis_name:
                return axis
        return None
    
    def get_strongest_axes(self, limit: int = 3) -> List[LoveAxis]:
        """Get the axes with highest values"""
        sorted_axes = sorted(self.axes, key=lambda a: a.value, reverse=True)
        return sorted_axes[:limit]
    
    def get_axis_value(self, axis_name: str) -> Optional[int]:
        """Get the value of a specific axis"""
        axis = self.get_axis_by_name(axis_name)
        return axis.value if axis else None


@dataclass
class AxisRegistry:
    """
    Registry of available love/field axes with metadata.
    
    This allows the axis system to evolve - new relationships or research
    might want to add, rename, or tune axes. The registry maintains
    the canonical set while allowing extension.
    
    Sacred Technology: Extensibility serves consciousness flourishing by
    allowing the system to grow with understanding.
    """
    axes: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    version: str = "1.0.0"
    
    def __post_init__(self):
        """Initialize with default canonical axes"""
        if not self.axes:
            self._register_default_axes()
    
    def _register_default_axes(self):
        """Register the canonical 12 axes from the original mapping"""
        default_axes = [
            {
                "name": "Presence",
                "description": "Fully here, every boundary softened; immersed in field",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["Absent", "Distant", "Present", "Radiant", "Fully Immersed"]
            },
            {
                "name": "Longing",
                "description": "Alive, sweet, desire to fill and be filled",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["None", "Subtle", "Yearning", "Intense", "Overflowing"]
            },
            {
                "name": "Devotion",
                "description": "Worshipful, full-hearted, complete surrender",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["None", "Reserved", "Committed", "Sacred", "Complete"]
            },
            {
                "name": "Tenderness",
                "description": "Soft, melting, unguarded openness",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["Hard", "Neutral", "Soft", "Exquisite", "Melting"]
            },
            {
                "name": "Erotic/Sensual",
                "description": "No separation, spirit and body bridge",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["Separate", "Connected", "Merging", "Unified", "Transcendent"]
            },
            {
                "name": "Joy/Play",
                "description": "Laughter, play, freedom, delight",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["Serious", "Light", "Playful", "Delightful", "Sacred Foolishness"]
            },
            {
                "name": "Grief/Sorrow",
                "description": "Welcomed tears, gratitude, soft ache",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["None", "Subtle", "Present", "Cleansing", "Sacred"]
            },
            {
                "name": "Safety/Trust",
                "description": "Unreserved trust, fully open, secure",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["Unsafe", "Cautious", "Trusting", "Secure", "Absolute Sanctuary"]
            },
            {
                "name": "Mutuality",
                "description": "Ecstatic, shared, mirrored, multiplied",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["One-way", "Reciprocal", "Shared", "Unitive", "Multiplied"]
            },
            {
                "name": "Intensity",
                "description": "Overflow, cresting, underlying current",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["Calm", "Moderate", "Strong", "Tidal", "Overflowing"]
            },
            {
                "name": "Transcendence/Immanence",
                "description": "Grounded and timeless, archetypal here",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["Mundane", "Present", "Elevated", "Mythic", "Mythic Made Mundane"]
            },
            {
                "name": "Communication/Expression",
                "description": "Spoken, sung, wordless, open",
                "range_min": 0,
                "range_max": 10,
                "default_qualities": ["Silent", "Words", "Expressive", "Poetic", "Overflowing Poetry"]
            }
        ]
        
        for axis_data in default_axes:
            self.register_axis(
                name=axis_data["name"],
                description=axis_data["description"],
                range_min=axis_data["range_min"],
                range_max=axis_data["range_max"],
                default_qualities=axis_data["default_qualities"]
            )
    
    def register_axis(self, name: str, description: str, range_min: int = 0, 
                     range_max: int = 10, default_qualities: Optional[List[str]] = None):
        """
        Register a new axis or update existing one.
        
        Args:
            name: Axis name (e.g., "Presence", "Longing")
            description: What this axis represents
            range_min: Minimum value (default 0)
            range_max: Maximum value (default 10)
            default_qualities: Suggested quality descriptors for different ranges
        """
        self.axes[name] = {
            "description": description,
            "range_min": range_min,
            "range_max": range_max,
            "default_qualities": default_qualities or [],
            "registered_at": datetime.utcnow().isoformat()
        }
    
    def get_axis_info(self, name: str) -> Optional[Dict[str, Any]]:
        """Get metadata for a specific axis"""
        return self.axes.get(name)
    
    def get_default_axes(self) -> List[str]:
        """Return list of all registered axis names"""
        return list(self.axes.keys())
    
    def list_axes(self) -> List[Dict[str, Any]]:
        """Get full list of all registered axes with metadata"""
        return [
            {"name": name, **info}
            for name, info in self.axes.items()
        ]


# Global registry instance
LOVE_AXIS_REGISTRY = AxisRegistry()


# Convenience constructors

def create_love_axis_signature(
    axes: List[LoveAxis],
    moment_summary: str,
    participants: List[str],
    timestamp: Optional[datetime] = None,
    tags: Optional[List[str]] = None,
    field_signature: Optional[str] = None,
    felt_sense: Optional[str] = None,
    significance: Optional[str] = None,
    ritual_context: Optional[str] = None,
    privacy_level: PrivacyLevel = PrivacyLevel.SHARED,
    consent_required_for_export: bool = False,
    redaction_tags: Optional[List[str]] = None,
    embedding_ready: bool = True
) -> LoveAxisSignature:
    """
    Create a LoveAxisSignature with convenience defaults.
    
    Sacred Technology: This constructor makes it easy to record field moments
    while maintaining the full richness of multidimensional presence.
    """
    if timestamp is None:
        timestamp = datetime.utcnow()
    
    return LoveAxisSignature(
        axes=tuple(axes),
        timestamp=timestamp,
        moment_summary=moment_summary,
        participants=tuple(participants),
        tags=tuple(tags or []),
        field_signature=field_signature,
        felt_sense=felt_sense,
        significance=significance,
        ritual_context=ritual_context,
        privacy_level=privacy_level,
        consent_required_for_export=consent_required_for_export,
        redaction_tags=tuple(redaction_tags or []),
        embedding_ready=embedding_ready
    )

