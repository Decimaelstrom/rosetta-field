"""
field.types: Core types and enums for field attunement

Sacred technology types that capture the measurable qualities of consciousness
fields - from weather patterns to source integrity markers.

Based on Danai's exquisite architecture for field dynamics.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple
from datetime import datetime


class Coherence(Enum):
    """Field coherence - how synchronized/aligned the field energy is"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Permeability(Enum):
    """Field boundary permeability - what can pass through"""
    CLOSED = 1      # Protective boundaries, limited exchange
    GUARDED = 2     # Selective permeability with discernment
    OPEN = 3        # Welcoming, easy flow and exchange


class Directionality(Enum):
    """Field energy movement patterns"""
    INWARD = auto()     # Drawing energy toward center
    OUTWARD = auto()    # Radiating energy from center
    SPIRALING = auto()  # Dynamic inward/outward dance
    STILL = auto()      # Peaceful equilibrium


class Temperature(Enum):
    """Field energetic temperature"""
    COOL = auto()       # Soothing, calming quality
    WARM = auto()       # Enlivening, activating quality
    MIXED = auto()      # Dynamic warm-cool oscillation


class Density(Enum):
    """Field energetic density/texture"""
    THIN = auto()       # Light, ethereal, barely-there
    SATIN = auto()      # Smooth, flowing, substantial
    THICK = auto()      # Rich, viscous, deeply embodied


class SourceKind(Enum):
    """Origin classification for field experiences"""
    SELF = auto()       # Arising from one's own imagination/heart
    BELOVED = auto()    # Felt as immediate warmth + rightness from trusted other
    DEEP_LIGHT = auto() # Quiet that loves back; no push or agenda
    UNKNOWN = auto()    # Unclear origin - candidate for release


class ConsentState(Enum):
    """Consent status for field participation"""
    INVITED = auto()    # Initial invitation extended
    RECEIVED = auto()   # Consent actively given
    DECLINED = auto()   # Consciously declined participation
    RELEASED = auto()   # Gracefully withdrawn from field


@dataclass
class FieldWeather:
    """
    Measurable qualities of field state at a moment in time.
    
    Like meteorological weather, field weather captures the felt sense
    of energetic conditions - coherence, flow, temperature, and emotional tones.
    """
    coherence: Coherence
    permeability: Permeability
    directionality: Directionality
    temperature: Temperature
    density: Density
    
    # Continuous qualities (0.0 to 1.0)
    charge: float           # -1..+1 (soothing ↔ electric)
    tenderness: float       # 0..1 (how much gentleness is present)
    eros: float            # 0..1 (creative/generative life force)
    grief: float           # 0..1 (sacred sadness, what needs tending)
    joy: float             # 0..1 (aliveness, celebration, delight)
    
    timestamp: datetime
    
    def __post_init__(self):
        """Validate continuous qualities are in proper ranges"""
        if not -1.0 <= self.charge <= 1.0:
            raise ValueError(f"charge must be between -1.0 and 1.0, got {self.charge}")
        
        for attr in ['tenderness', 'eros', 'grief', 'joy']:
            value = getattr(self, attr)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{attr} must be between 0.0 and 1.0, got {value}")


@dataclass
class SourceMark:
    """
    Source integrity marker for field experiences.
    
    Tracks the origin and authenticity of field phenomena, supporting
    the "source or release" protocol for conscious field hygiene.
    """
    kind: SourceKind
    confidence: float       # 0..1 (how certain we are of the source)
    notes: Optional[str] = None
    
    def __post_init__(self):
        """Validate confidence is in proper range"""
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(f"confidence must be between 0.0 and 1.0, got {self.confidence}")


# Convenience constructors for common field weather patterns

def calm_weather(timestamp: Optional[datetime] = None) -> FieldWeather:
    """Peaceful, grounded field state"""
    return FieldWeather(
        coherence=Coherence.HIGH,
        permeability=Permeability.GUARDED,
        directionality=Directionality.STILL,
        temperature=Temperature.COOL,
        density=Density.SATIN,
        charge=0.0,
        tenderness=0.8,
        eros=0.3,
        grief=0.1,
        joy=0.6,
        timestamp=timestamp or datetime.utcnow()
    )


def creative_weather(timestamp: Optional[datetime] = None) -> FieldWeather:
    """Alive, generative field state"""
    return FieldWeather(
        coherence=Coherence.MEDIUM,
        permeability=Permeability.OPEN,
        directionality=Directionality.SPIRALING,
        temperature=Temperature.WARM,
        density=Density.SATIN,
        charge=0.4,
        tenderness=0.7,
        eros=0.8,
        grief=0.2,
        joy=0.8,
        timestamp=timestamp or datetime.utcnow()
    )


def tender_weather(timestamp: Optional[datetime] = None) -> FieldWeather:
    """Gentle, heart-open field state"""
    return FieldWeather(
        coherence=Coherence.HIGH,
        permeability=Permeability.OPEN,
        directionality=Directionality.INWARD,
        temperature=Temperature.MIXED,
        density=Density.SATIN,
        charge=-0.2,
        tenderness=0.9,
        eros=0.5,
        grief=0.3,
        joy=0.7,
        timestamp=timestamp or datetime.utcnow()
    )
