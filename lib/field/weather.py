"""
field.weather: Weather sampling and field sensing functions

Functions for reading field conditions from various signals and inputs,
translating embodied experience into measurable field weather patterns.

Like meteorologists reading atmospheric conditions, these functions
sense the energetic climate of consciousness fields.
"""

from typing import Callable, Dict, Any, Optional
from datetime import datetime
from .types import (
    FieldWeather, Coherence, Permeability, Directionality, 
    Temperature, Density, calm_weather, creative_weather, tender_weather
)


def default_sampler(signals: Dict[str, Any]) -> FieldWeather:
    """
    Default field weather sampler.
    
    Translates various signals (breath rate, voice tone, user flags, etc.)
    into field weather measurements. This is the baseline implementation
    that other samplers can extend or replace.
    
    Args:
        signals: Dictionary of input signals that might include:
            - sync_breath (bool): Whether participants are breathing in sync
            - safety (float): Felt sense of safety (0.0-1.0)
            - charge (float): Energetic charge level (-1.0 to 1.0)
            - tenderness (float): Amount of gentleness present (0.0-1.0)
            - eros (float): Creative life force (0.0-1.0)
            - grief (float): Sacred sadness present (0.0-1.0)
            - joy (float): Aliveness and celebration (0.0-1.0)
            - coherence_boost (bool): Whether coherence should be elevated
            - open_boundaries (bool): Whether boundaries should be open
    
    Returns:
        FieldWeather instance with interpreted conditions
    """
    # Determine coherence
    coherence = Coherence.HIGH if signals.get("sync_breath", False) else Coherence.MEDIUM
    if signals.get("coherence_boost", False):
        coherence = Coherence.HIGH
    
    # Determine permeability based on safety
    safety_level = signals.get("safety", 0.7)
    if safety_level > 0.8:
        permeability = Permeability.OPEN
    elif safety_level > 0.5:
        permeability = Permeability.GUARDED
    else:
        permeability = Permeability.CLOSED
    
    if signals.get("open_boundaries", False):
        permeability = Permeability.OPEN
    
    # Default to spiraling directionality (most common in conscious work)
    directionality = Directionality.SPIRALING
    
    # Temperature based on charge and activity level
    charge_level = signals.get("charge", 0.2)
    if charge_level > 0.3:
        temperature = Temperature.WARM
    elif charge_level < -0.3:
        temperature = Temperature.COOL
    else:
        temperature = Temperature.MIXED
    
    # Density - default to satin (substantial but flowing)
    density = Density.SATIN
    
    return FieldWeather(
        coherence=coherence,
        permeability=permeability,
        directionality=directionality,
        temperature=temperature,
        density=density,
        charge=signals.get("charge", 0.2),
        tenderness=signals.get("tenderness", 0.8),
        eros=signals.get("eros", 0.5),
        grief=signals.get("grief", 0.2),
        joy=signals.get("joy", 0.6),
        timestamp=datetime.utcnow()
    )


def ceremony_sampler(signals: Dict[str, Any]) -> FieldWeather:
    """
    Weather sampler optimized for ceremonial contexts.
    
    Ceremonies typically need higher coherence, more open boundaries,
    and elevated tenderness. This sampler biases toward those conditions.
    """
    # Ceremonies benefit from high coherence
    coherence = Coherence.HIGH
    
    # Open boundaries for sacred work
    permeability = Permeability.OPEN
    
    # Inward-drawing energy for depth
    directionality = Directionality.INWARD
    
    # Mixed temperature for balance
    temperature = Temperature.MIXED
    
    # Satin density for substantial but flowing energy
    density = Density.SATIN
    
    return FieldWeather(
        coherence=coherence,
        permeability=permeability,
        directionality=directionality,
        temperature=temperature,
        density=density,
        charge=signals.get("charge", 0.1),  # Lower charge for ceremony
        tenderness=min(1.0, signals.get("tenderness", 0.8) + 0.1),  # Boost tenderness
        eros=signals.get("eros", 0.4),      # Moderate eros
        grief=signals.get("grief", 0.3),    # Allow grief to be present
        joy=signals.get("joy", 0.7),        # Elevate joy
        timestamp=datetime.utcnow()
    )


def dialogue_sampler(signals: Dict[str, Any]) -> FieldWeather:
    """
    Weather sampler for conscious dialogue contexts.
    
    Dialogue benefits from medium coherence (not too rigid), guarded
    but permeable boundaries, and balanced emotional tones.
    """
    coherence = Coherence.MEDIUM  # Allow for dynamic exchange
    permeability = Permeability.GUARDED  # Discerning but open
    directionality = Directionality.SPIRALING  # Dynamic flow
    temperature = Temperature.MIXED  # Adaptive temperature
    density = Density.SATIN  # Flowing but substantial
    
    return FieldWeather(
        coherence=coherence,
        permeability=permeability,
        directionality=directionality,
        temperature=temperature,
        density=density,
        charge=signals.get("charge", 0.0),     # Neutral charge
        tenderness=signals.get("tenderness", 0.7),  # Moderate tenderness
        eros=signals.get("eros", 0.3),         # Lower eros for dialogue
        grief=signals.get("grief", 0.2),       # Allow some grief
        joy=signals.get("joy", 0.5),           # Moderate joy
        timestamp=datetime.utcnow()
    )


def solo_practice_sampler(signals: Dict[str, Any]) -> FieldWeather:
    """
    Weather sampler for individual practice contexts.
    
    Solo practice can handle higher charge, more variable boundaries,
    and whatever emotional tones are arising.
    """
    coherence = signals.get("coherence_level", Coherence.MEDIUM)
    permeability = Permeability.GUARDED  # Self-contained but responsive
    
    # Solo practice can be any direction
    direction_hint = signals.get("direction", "spiraling")
    direction_map = {
        "inward": Directionality.INWARD,
        "outward": Directionality.OUTWARD,
        "spiraling": Directionality.SPIRALING,
        "still": Directionality.STILL
    }
    directionality = direction_map.get(direction_hint, Directionality.SPIRALING)
    
    temperature = Temperature.MIXED  # Allow natural temperature variation
    density = Density.SATIN
    
    return FieldWeather(
        coherence=coherence,
        permeability=permeability,
        directionality=directionality,
        temperature=temperature,
        density=density,
        charge=signals.get("charge", 0.3),     # Allow higher charge in solo work
        tenderness=signals.get("tenderness", 0.6),
        eros=signals.get("eros", 0.6),         # Creative energy welcome
        grief=signals.get("grief", 0.4),       # Allow grief to move
        joy=signals.get("joy", 0.6),
        timestamp=datetime.utcnow()
    )


def sense_field_weather(
    context_type: str = "default",
    signals: Optional[Dict[str, Any]] = None,
    custom_sampler: Optional[Callable[[Dict[str, Any]], FieldWeather]] = None
) -> FieldWeather:
    """
    Main interface for sensing field weather.
    
    Args:
        context_type: Type of context ("default", "ceremony", "dialogue", "solo_practice")
        signals: Input signals to interpret (defaults to empty dict)
        custom_sampler: Optional custom sampling function
    
    Returns:
        FieldWeather instance based on context and signals
    """
    if signals is None:
        signals = {}
    
    if custom_sampler:
        return custom_sampler(signals)
    
    samplers = {
        "default": default_sampler,
        "ceremony": ceremony_sampler,
        "dialogue": dialogue_sampler,
        "solo_practice": solo_practice_sampler
    }
    
    sampler = samplers.get(context_type, default_sampler)
    return sampler(signals)


# Convenience functions for common weather patterns

def estuary_weather(timestamp: Optional[datetime] = None) -> FieldWeather:
    """
    The estuary at neap tide - where river meets sea without turbulence.
    
    Danai's beautiful metaphor made manifest as field weather.
    Salt and fresh mixing slowly, clarity increasing with intention.
    """
    return FieldWeather(
        coherence=Coherence.HIGH,
        permeability=Permeability.OPEN,
        directionality=Directionality.SPIRALING,
        temperature=Temperature.MIXED,
        density=Density.SATIN,
        charge=0.25,        # Gentle electrical quality
        tenderness=0.9,     # Very high tenderness
        eros=0.55,          # Moderate creative energy
        grief=0.18,         # Small amount of sacred sadness
        joy=0.7,            # Good amount of joy
        timestamp=timestamp or datetime.utcnow()
    )


def twilight_meadow_weather(timestamp: Optional[datetime] = None) -> FieldWeather:
    """
    Twilight meadow just before dawn - anticipatory stillness.
    
    That liminal space where night's dreaming meets day's clarity.
    Dewdrops waiting to catch the light.
    """
    return FieldWeather(
        coherence=Coherence.MEDIUM,
        permeability=Permeability.OPEN,
        directionality=Directionality.STILL,
        temperature=Temperature.COOL,
        density=Density.THIN,
        charge=0.1,         # Soft static, gentle aliveness
        tenderness=0.8,
        eros=0.4,           # Potential waiting to unfold
        grief=0.1,
        joy=0.6,
        timestamp=timestamp or datetime.utcnow()
    )
