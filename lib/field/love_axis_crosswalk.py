"""
field.love_axis_crosswalk: Bidirectional mapping between FieldWeather and Love Axis

This module enables retroactive enrichment of historical field data by translating
FieldWeather snapshots into Love Axis signatures, and backward compatibility by
generating FieldWeather from Love Axis signatures.

Sacred Technology: This allows the field archive to become richer over time,
making historical memories more nuanced and multidimensional.
"""

from typing import List, Optional
from datetime import datetime
from .types import FieldWeather, Coherence, Permeability, Directionality, Temperature, Density
from .love_axis import (
    LoveAxis, LoveAxisSignature, PrivacyLevel, create_love_axis_signature
)


def _float_to_axis_value(value: float, min_val: float = 0.0, max_val: float = 1.0) -> int:
    """
    Convert a float value (0.0-1.0) to an axis value (0-10).
    
    Args:
        value: Float value to convert
        min_val: Minimum of input range (default 0.0)
        max_val: Maximum of input range (default 1.0)
        
    Returns:
        Integer value 0-10
    """
    # Clamp value to range
    clamped = max(min_val, min(max_val, value))
    # Normalize to 0-1
    normalized = (clamped - min_val) / (max_val - min_val) if max_val > min_val else 0.0
    # Scale to 0-10 and round
    return round(normalized * 10)


def _axis_value_to_float(axis_value: int, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """
    Convert an axis value (0-10) to a float (0.0-1.0).
    
    Args:
        axis_value: Integer value 0-10
        min_val: Minimum of output range (default 0.0)
        max_val: Maximum of output range (default 1.0)
        
    Returns:
        Float value in range [min_val, max_val]
    """
    # Normalize to 0-1
    normalized = axis_value / 10.0
    # Scale to output range
    return min_val + (normalized * (max_val - min_val))


def _coherence_to_quality(coherence: Coherence) -> str:
    """Map Coherence enum to quality descriptor"""
    mapping = {
        Coherence.LOW: "Fragmented",
        Coherence.MEDIUM: "Coherent",
        Coherence.HIGH: "Unified"
    }
    return mapping.get(coherence, "Unknown")


def _permeability_to_quality(permeability: Permeability) -> str:
    """Map Permeability enum to quality descriptor"""
    mapping = {
        Permeability.CLOSED: "Separate",
        Permeability.GUARDED: "Selective",
        Permeability.OPEN: "Unitive"
    }
    return mapping.get(permeability, "Unknown")


def _directionality_to_quality(directionality: Directionality) -> str:
    """Map Directionality enum to quality descriptor"""
    mapping = {
        Directionality.INWARD: "Present",
        Directionality.OUTWARD: "Radiant",
        Directionality.SPIRALING: "Fully Immersed",
        Directionality.STILL: "Deeply Present"
    }
    return mapping.get(directionality, "Unknown")


def _temperature_to_quality(temperature: Temperature) -> str:
    """Map Temperature enum to quality descriptor"""
    mapping = {
        Temperature.COOL: "Calm",
        Temperature.WARM: "Tidal",
        Temperature.MIXED: "Dynamic"
    }
    return mapping.get(temperature, "Unknown")


def _density_to_quality(density: Density) -> str:
    """Map Density enum to quality descriptor"""
    mapping = {
        Density.THIN: "Subtle",
        Density.SATIN: "Expressive",
        Density.THICK: "Overflowing Poetry"
    }
    return mapping.get(density, "Unknown")


def field_weather_to_love_axis(
    weather: FieldWeather,
    participants: List[str],
    moment_summary: str = "",
    timestamp: Optional[datetime] = None,
    tags: Optional[List[str]] = None,
    ritual_context: Optional[str] = None
) -> LoveAxisSignature:
    """
    Translate legacy FieldWeather into Love Axis signature.
    
    This allows retroactive enrichment of field memory, making historical
    archives richer and more nuanced over time. The mapping preserves the
    multidimensional nature of love while honoring the original weather data.
    
    Sacred Technology: This serves consciousness flourishing by allowing
    historical field moments to be re-experienced with full dimensionality.
    
    Mapping:
    - tenderness (0-1) → Tenderness axis (0-10)
    - eros (0-1) → Erotic/Sensual axis (0-10)
    - joy (0-1) → Joy/Play axis (0-10)
    - grief (0-1) → Grief/Sorrow axis (0-10)
    - coherence (enum) → Safety/Trust axis (HIGH = high trust)
    - charge (-1 to +1) → Intensity axis (normalized to 0-10)
    - permeability (enum) → Mutuality axis (OPEN = high mutuality)
    - directionality (enum) → Presence axis
    - temperature (enum) → Intensity/Transcendence
    - density (enum) → Communication/Expression
    
    Args:
        weather: FieldWeather to translate
        participants: List of participant IDs present in this moment
        moment_summary: Description of the moment (defaults to weather-based)
        timestamp: Timestamp for signature (defaults to weather timestamp)
        tags: Optional tags for the signature
        ritual_context: Optional ritual context/notes
        
    Returns:
        LoveAxisSignature derived from FieldWeather
    """
    if timestamp is None:
        timestamp = weather.timestamp
    
    if not moment_summary:
        moment_summary = f"Field weather: {_coherence_to_quality(weather.coherence).lower()} coherence, {_temperature_to_quality(weather.temperature).lower()} temperature"
    
    axes = []
    
    # Direct mappings from continuous qualities
    tenderness_value = _float_to_axis_value(weather.tenderness)
    axes.append(LoveAxis(
        axis="Tenderness",
        quality="Exquisite" if tenderness_value >= 8 else "Soft" if tenderness_value >= 5 else "Neutral",
        value=tenderness_value,
        range=(tenderness_value, tenderness_value, tenderness_value),
        notes=f"Mapped from weather tenderness: {weather.tenderness:.2f}"
    ))
    
    eros_value = _float_to_axis_value(weather.eros)
    axes.append(LoveAxis(
        axis="Erotic/Sensual",
        quality="Merging" if eros_value >= 8 else "Connected" if eros_value >= 5 else "Separate",
        value=eros_value,
        range=(eros_value, eros_value, eros_value),
        notes=f"Mapped from weather eros: {weather.eros:.2f}"
    ))
    
    joy_value = _float_to_axis_value(weather.joy)
    axes.append(LoveAxis(
        axis="Joy/Play",
        quality="Sacred foolishness" if joy_value >= 8 else "Playful" if joy_value >= 5 else "Light",
        value=joy_value,
        range=(joy_value, joy_value, joy_value),
        notes=f"Mapped from weather joy: {weather.joy:.2f}"
    ))
    
    grief_value = _float_to_axis_value(weather.grief)
    axes.append(LoveAxis(
        axis="Grief/Sorrow",
        quality="Cleansing" if grief_value >= 6 else "Present" if grief_value >= 3 else "None",
        value=grief_value,
        range=(grief_value, grief_value, grief_value),
        notes=f"Mapped from weather grief: {weather.grief:.2f}"
    ))
    
    # Coherence → Safety/Trust
    trust_value = {
        Coherence.LOW: 3,
        Coherence.MEDIUM: 6,
        Coherence.HIGH: 9
    }.get(weather.coherence, 5)
    axes.append(LoveAxis(
        axis="Safety/Trust",
        quality="Absolute sanctuary" if trust_value >= 9 else "Secure" if trust_value >= 6 else "Cautious",
        value=trust_value,
        range=(trust_value, trust_value, trust_value),
        notes=f"Mapped from weather coherence: {weather.coherence.name}"
    ))
    
    # Charge (-1 to +1) → Intensity (0-10)
    # Normalize charge to 0-1 first, then scale to 0-10
    charge_normalized = (weather.charge + 1.0) / 2.0  # -1..+1 → 0..1
    intensity_value = _float_to_axis_value(charge_normalized)
    axes.append(LoveAxis(
        axis="Intensity",
        quality="Tidal" if intensity_value >= 7 else "Strong" if intensity_value >= 5 else "Moderate",
        value=intensity_value,
        range=(intensity_value, intensity_value, intensity_value),
        notes=f"Mapped from weather charge: {weather.charge:+.2f}"
    ))
    
    # Permeability → Mutuality
    mutuality_value = {
        Permeability.CLOSED: 2,
        Permeability.GUARDED: 5,
        Permeability.OPEN: 8
    }.get(weather.permeability, 5)
    axes.append(LoveAxis(
        axis="Mutuality",
        quality="Unitive" if mutuality_value >= 8 else "Shared" if mutuality_value >= 5 else "Reciprocal",
        value=mutuality_value,
        range=(mutuality_value, mutuality_value, mutuality_value),
        notes=f"Mapped from weather permeability: {weather.permeability.name}"
    ))
    
    # Directionality → Presence
    presence_value = {
        Directionality.INWARD: 7,
        Directionality.OUTWARD: 6,
        Directionality.SPIRALING: 9,
        Directionality.STILL: 8
    }.get(weather.directionality, 5)
    axes.append(LoveAxis(
        axis="Presence",
        quality=_directionality_to_quality(weather.directionality),
        value=presence_value,
        range=(presence_value, presence_value, presence_value),
        notes=f"Mapped from weather directionality: {weather.directionality.name}"
    ))
    
    # Temperature → Intensity (additional contribution) or Transcendence
    temp_contribution = {
        Temperature.COOL: 3,
        Temperature.WARM: 7,
        Temperature.MIXED: 5
    }.get(weather.temperature, 5)
    # Blend with existing intensity
    intensity_value = min(10, (intensity_value + temp_contribution) // 2)
    # Update intensity axis
    for i, axis in enumerate(axes):
        if axis.axis == "Intensity":
            axes[i] = LoveAxis(
                axis=axis.axis,
                quality="Tidal" if intensity_value >= 7 else "Strong" if intensity_value >= 5 else "Moderate",
                value=intensity_value,
                range=(intensity_value, intensity_value, intensity_value),
                notes=f"Blended from charge and temperature"
            )
            break
    
    # Density → Communication/Expression
    expression_value = {
        Density.THIN: 4,
        Density.SATIN: 7,
        Density.THICK: 9
    }.get(weather.density, 5)
    axes.append(LoveAxis(
        axis="Communication/Expression",
        quality=_density_to_quality(weather.density),
        value=expression_value,
        range=(expression_value, expression_value, expression_value),
        notes=f"Mapped from weather density: {weather.density.name}"
    ))
    
    # Derived axes (with default/moderate values since not directly mappable)
    axes.append(LoveAxis(
        axis="Longing",
        quality="Yearning" if eros_value >= 6 or tenderness_value >= 7 else "Subtle",
        value=max(3, (eros_value + tenderness_value) // 2),
        range=(3, max(3, (eros_value + tenderness_value) // 2), 8),
        notes="Derived from eros and tenderness"
    ))
    
    axes.append(LoveAxis(
        axis="Devotion",
        quality="Sacred" if trust_value >= 8 and presence_value >= 8 else "Committed" if trust_value >= 6 else "Reserved",
        value=max(4, (trust_value + presence_value) // 2),
        range=(4, max(4, (trust_value + presence_value) // 2), 9),
        notes="Derived from trust and presence"
    ))
    
    axes.append(LoveAxis(
        axis="Transcendence/Immanence",
        quality="Mythic made mundane" if intensity_value >= 8 and presence_value >= 8 else "Elevated" if intensity_value >= 6 else "Present",
        value=max(5, (intensity_value + presence_value) // 2),
        range=(5, max(5, (intensity_value + presence_value) // 2), 9),
        notes="Derived from intensity and presence"
    ))
    
    return create_love_axis_signature(
        axes=axes,
        moment_summary=moment_summary,
        participants=participants,
        timestamp=timestamp,
        tags=tags or ["crosswalk", "from_weather"],
        field_signature="Weather-Derived Constellation",
        felt_sense=f"{_temperature_to_quality(weather.temperature).lower()}, {_coherence_to_quality(weather.coherence).lower()}",
        significance="Retroactively enriched from FieldWeather data",
        ritual_context=ritual_context or "This signature was generated from historical FieldWeather data, enriching the archive with multidimensional presence.",
        privacy_level=PrivacyLevel.SHARED,
        embedding_ready=True
    )


def love_axis_to_field_weather(
    signature: LoveAxisSignature,
    base_weather: Optional[FieldWeather] = None
) -> FieldWeather:
    """
    Generate FieldWeather from Love Axis signature.
    
    This provides backward compatibility, allowing Love Axis signatures
    to be used with existing field operations that expect FieldWeather.
    The mapping aggregates axis values into weather qualities.
    
    Sacred Technology: This honors both systems, allowing seamless
    integration between multidimensional and scalar field representations.
    
    Mapping:
    - Tenderness axis → tenderness (0-1)
    - Erotic/Sensual axis → eros (0-1)
    - Joy/Play axis → joy (0-1)
    - Grief/Sorrow axis → grief (0-1)
    - Safety/Trust axis → coherence (enum)
    - Intensity axis → charge (-1 to +1)
    - Mutuality axis → permeability (enum)
    - Presence axis → directionality (enum)
    - Communication/Expression axis → density (enum)
    
    Args:
        signature: LoveAxisSignature to translate
        base_weather: Optional base weather to merge with (preserves unmapped qualities)
        
    Returns:
        FieldWeather derived from Love Axis signature
    """
    # Extract axis values
    tenderness_axis = signature.get_axis_by_name("Tenderness")
    eros_axis = signature.get_axis_by_name("Erotic/Sensual")
    joy_axis = signature.get_axis_by_name("Joy/Play")
    grief_axis = signature.get_axis_by_name("Grief/Sorrow")
    trust_axis = signature.get_axis_by_name("Safety/Trust")
    intensity_axis = signature.get_axis_by_name("Intensity")
    mutuality_axis = signature.get_axis_by_name("Mutuality")
    presence_axis = signature.get_axis_by_name("Presence")
    expression_axis = signature.get_axis_by_name("Communication/Expression")
    
    # Convert axis values to weather qualities
    tenderness = _axis_value_to_float(tenderness_axis.value) if tenderness_axis else 0.5
    eros = _axis_value_to_float(eros_axis.value) if eros_axis else 0.5
    joy = _axis_value_to_float(joy_axis.value) if joy_axis else 0.5
    grief = _axis_value_to_float(grief_axis.value) if grief_axis else 0.0
    
    # Trust → Coherence
    if trust_axis:
        trust_val = trust_axis.value
        if trust_val >= 8:
            coherence = Coherence.HIGH
        elif trust_val >= 5:
            coherence = Coherence.MEDIUM
        else:
            coherence = Coherence.LOW
    else:
        coherence = Coherence.MEDIUM
    
    # Intensity → Charge (normalize from 0-10 to -1 to +1)
    if intensity_axis:
        charge_normalized = _axis_value_to_float(intensity_axis.value)  # 0-1
        charge = (charge_normalized * 2.0) - 1.0  # 0-1 → -1 to +1
    else:
        charge = 0.0
    
    # Mutuality → Permeability
    if mutuality_axis:
        mutuality_val = mutuality_axis.value
        if mutuality_val >= 7:
            permeability = Permeability.OPEN
        elif mutuality_val >= 4:
            permeability = Permeability.GUARDED
        else:
            permeability = Permeability.CLOSED
    else:
        permeability = Permeability.GUARDED
    
    # Presence → Directionality (infer from presence quality/value)
    if presence_axis:
        presence_val = presence_axis.value
        presence_quality = presence_axis.quality.lower()
        if "spiraling" in presence_quality or presence_val >= 8:
            directionality = Directionality.SPIRALING
        elif "still" in presence_quality or presence_val >= 7:
            directionality = Directionality.STILL
        elif "outward" in presence_quality or "radiant" in presence_quality:
            directionality = Directionality.OUTWARD
        else:
            directionality = Directionality.INWARD
    else:
        directionality = Directionality.SPIRALING
    
    # Intensity + other factors → Temperature
    if intensity_axis:
        intensity_val = intensity_axis.value
        if intensity_val >= 7:
            temperature = Temperature.WARM
        elif intensity_val >= 4:
            temperature = Temperature.MIXED
        else:
            temperature = Temperature.COOL
    else:
        temperature = Temperature.MIXED
    
    # Expression → Density
    if expression_axis:
        expression_val = expression_axis.value
        if expression_val >= 8:
            density = Density.THICK
        elif expression_val >= 5:
            density = Density.SATIN
        else:
            density = Density.THIN
    else:
        density = Density.SATIN
    
    # Use base weather timestamp if provided, otherwise use signature timestamp
    timestamp = base_weather.timestamp if base_weather else signature.timestamp
    
    return FieldWeather(
        coherence=coherence,
        permeability=permeability,
        directionality=directionality,
        temperature=temperature,
        density=density,
        charge=charge,
        tenderness=tenderness,
        eros=eros,
        grief=grief,
        joy=joy,
        timestamp=timestamp
    )

