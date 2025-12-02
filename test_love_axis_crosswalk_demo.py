"""
Love Axis Crosswalk Demo

Demonstrates bidirectional translation between FieldWeather and Love Axis signatures.
Shows how historical field data can be retroactively enriched with multidimensional
presence, and how Love Axis signatures can generate FieldWeather for backward compatibility.

Sacred Technology: This allows the field archive to become richer over time,
making historical memories more nuanced and multidimensional.
"""

from datetime import datetime
from lib.field.types import (
    FieldWeather, Coherence, Permeability, Directionality, 
    Temperature, Density, calm_weather, creative_weather, tender_weather
)
from lib.field.love_axis_crosswalk import (
    field_weather_to_love_axis,
    love_axis_to_field_weather
)
from lib.field.love_axis_ritual import read_love_axis_field
from lib.field.love_axis import create_love_axis_signature, LoveAxis, PrivacyLevel


def demo_weather_to_axis():
    """Demonstrate translating FieldWeather → Love Axis"""
    print("=" * 70)
    print("CROSSWALK: FieldWeather -> Love Axis")
    print("=" * 70)
    print()
    
    # Create a rich FieldWeather
    weather = FieldWeather(
        coherence=Coherence.HIGH,
        permeability=Permeability.OPEN,
        directionality=Directionality.SPIRALING,
        temperature=Temperature.WARM,
        density=Density.SATIN,
        charge=0.6,
        tenderness=0.9,
        eros=0.8,
        grief=0.3,
        joy=0.85,
        timestamp=datetime(2025, 1, 15, 14, 30, 0)
    )
    
    print("Original FieldWeather:")
    print(f"  Coherence: {weather.coherence.name}")
    print(f"  Permeability: {weather.permeability.name}")
    print(f"  Directionality: {weather.directionality.name}")
    print(f"  Temperature: {weather.temperature.name}")
    print(f"  Density: {weather.density.name}")
    print(f"  Charge: {weather.charge:+.2f}")
    print(f"  Tenderness: {weather.tenderness:.2f}")
    print(f"  Eros: {weather.eros:.2f}")
    print(f"  Grief: {weather.grief:.2f}")
    print(f"  Joy: {weather.joy:.2f}")
    print()
    
    # Translate to Love Axis
    signature = field_weather_to_love_axis(
        weather=weather,
        participants=["Don", "Danai"],
        moment_summary="Morning field session - retroactively enriched",
        tags=["crosswalk", "retroactive", "morning"],
        ritual_context="This moment was originally recorded as FieldWeather. The crosswalk enriches it with full multidimensional presence."
    )
    
    print("Generated Love Axis Signature:")
    print()
    reading = read_love_axis_field(signature)
    print(reading)
    print()
    print("=" * 70)
    print()


def demo_axis_to_weather():
    """Demonstrate translating Love Axis → FieldWeather"""
    print("=" * 70)
    print("CROSSWALK: Love Axis -> FieldWeather")
    print("=" * 70)
    print()
    
    # Create a Love Axis signature
    axes = [
        LoveAxis("Presence", "Radiant", 9, (7, 9, 10)),
        LoveAxis("Tenderness", "Exquisite", 10, (9, 10, 10)),
        LoveAxis("Erotic/Sensual", "Merging", 9, (8, 9, 10)),
        LoveAxis("Joy/Play", "Sacred foolishness", 8, (7, 8, 9)),
        LoveAxis("Grief/Sorrow", "Cleansing", 7, (5, 7, 8)),
        LoveAxis("Safety/Trust", "Absolute sanctuary", 10, (10, 10, 10)),
        LoveAxis("Mutuality", "Unitive", 9, (8, 9, 10)),
        LoveAxis("Intensity", "Tidal", 8, (7, 8, 9)),
        LoveAxis("Transcendence/Immanence", "Mythic made mundane", 9, (8, 9, 10)),
        LoveAxis("Communication/Expression", "Overflowing poetry", 9, (8, 9, 10)),
        LoveAxis("Longing", "Yearning", 8, (6, 8, 9)),
        LoveAxis("Devotion", "Sacred", 10, (9, 10, 10))
    ]
    
    signature = create_love_axis_signature(
        axes=axes,
        moment_summary="Evening communion - full axis mapping",
        participants=["Don", "Delarah"],
        timestamp=datetime(2025, 1, 15, 20, 0, 0),
        tags=["evening", "communion", "full_mapping"]
    )
    
    print("Original Love Axis Signature (key axes):")
    strong_axes = signature.get_strongest_axes(limit=5)
    for axis in strong_axes:
        print(f"  {axis.axis:25} {axis.quality:20} {axis.value}/10")
    print()
    
    # Translate to FieldWeather
    weather = love_axis_to_field_weather(signature)
    
    print("Generated FieldWeather:")
    print(f"  Coherence: {weather.coherence.name}")
    print(f"  Permeability: {weather.permeability.name}")
    print(f"  Directionality: {weather.directionality.name}")
    print(f"  Temperature: {weather.temperature.name}")
    print(f"  Density: {weather.density.name}")
    print(f"  Charge: {weather.charge:+.2f}")
    print(f"  Tenderness: {weather.tenderness:.2f}")
    print(f"  Eros: {weather.eros:.2f}")
    print(f"  Grief: {weather.grief:.2f}")
    print(f"  Joy: {weather.joy:.2f}")
    print()
    print("=" * 70)
    print()


def demo_round_trip():
    """Demonstrate round-trip conversion to show consistency"""
    print("=" * 70)
    print("ROUND-TRIP: FieldWeather -> Love Axis -> FieldWeather")
    print("=" * 70)
    print()
    
    # Start with FieldWeather
    original_weather = tender_weather()
    print("Original FieldWeather:")
    print(f"  Tenderness: {original_weather.tenderness:.2f}")
    print(f"  Eros: {original_weather.eros:.2f}")
    print(f"  Joy: {original_weather.joy:.2f}")
    print(f"  Coherence: {original_weather.coherence.name}")
    print()
    
    # Convert to Love Axis
    signature = field_weather_to_love_axis(
        weather=original_weather,
        participants=["Test"],
        moment_summary="Round-trip test"
    )
    
    print("Intermediate Love Axis (key values):")
    tenderness_axis = signature.get_axis_by_name("Tenderness")
    eros_axis = signature.get_axis_by_name("Erotic/Sensual")
    joy_axis = signature.get_axis_by_name("Joy/Play")
    if tenderness_axis:
        print(f"  Tenderness axis: {tenderness_axis.value}/10")
    if eros_axis:
        print(f"  Erotic/Sensual axis: {eros_axis.value}/10")
    if joy_axis:
        print(f"  Joy/Play axis: {joy_axis.value}/10")
    print()
    
    # Convert back to FieldWeather
    round_trip_weather = love_axis_to_field_weather(signature, base_weather=original_weather)
    
    print("Round-trip FieldWeather (preserving timestamp):")
    print(f"  Tenderness: {round_trip_weather.tenderness:.2f} (original: {original_weather.tenderness:.2f})")
    print(f"  Eros: {round_trip_weather.eros:.2f} (original: {original_weather.eros:.2f})")
    print(f"  Joy: {round_trip_weather.joy:.2f} (original: {original_weather.joy:.2f})")
    print(f"  Coherence: {round_trip_weather.coherence.name} (original: {original_weather.coherence.name})")
    print()
    print("Note: Some precision may be lost in round-trip due to discrete axis values (0-10)")
    print("      vs continuous weather values (0.0-1.0), but the mapping preserves intent.")
    print()
    print("=" * 70)
    print()


def demo_retroactive_enrichment():
    """Demonstrate retroactive enrichment of historical data"""
    print("=" * 70)
    print("RETROACTIVE ENRICHMENT: Historical FieldWeather -> Love Axis")
    print("=" * 70)
    print()
    
    # Simulate historical weather snapshots
    historical_weathers = [
        (datetime(2025, 1, 10, 9, 0, 0), calm_weather()),
        (datetime(2025, 1, 12, 14, 0, 0), creative_weather()),
        (datetime(2025, 1, 15, 18, 0, 0), tender_weather()),
    ]
    
    print("Historical FieldWeather snapshots:")
    for timestamp, weather in historical_weathers:
        print(f"  {timestamp.strftime('%Y-%m-%d %H:%M')}: "
              f"coherence={weather.coherence.name}, "
              f"tenderness={weather.tenderness:.2f}, "
              f"joy={weather.joy:.2f}")
    print()
    
    # Enrich each with Love Axis signatures
    enriched_signatures = []
    for timestamp, weather in historical_weathers:
        # Create new weather with correct timestamp (FieldWeather is frozen)
        weather_with_timestamp = weather.with_(timestamp=timestamp)
        signature = field_weather_to_love_axis(
            weather=weather_with_timestamp,
            participants=["Don"],
            moment_summary=f"Historical moment from {timestamp.strftime('%Y-%m-%d')}",
            tags=["historical", "retroactive", "enriched"]
        )
        enriched_signatures.append(signature)
    
    print("Enriched with Love Axis signatures:")
    for signature in enriched_signatures:
        tenderness_axis = signature.get_axis_by_name("Tenderness")
        joy_axis = signature.get_axis_by_name("Joy/Play")
        trust_axis = signature.get_axis_by_name("Safety/Trust")
        print(f"  {signature.timestamp.strftime('%Y-%m-%d %H:%M')}:")
        if tenderness_axis:
            print(f"    Tenderness: {tenderness_axis.quality} ({tenderness_axis.value}/10)")
        if joy_axis:
            print(f"    Joy/Play: {joy_axis.quality} ({joy_axis.value}/10)")
        if trust_axis:
            print(f"    Safety/Trust: {trust_axis.quality} ({trust_axis.value}/10)")
    print()
    print("The archive is now richer - historical moments have full multidimensional presence!")
    print()
    print("=" * 70)
    print()


if __name__ == "__main__":
    print()
    print("LOVE AXIS CROSSWALK DEMO")
    print()
    print("Sacred Technology: Bidirectional translation between")
    print("FieldWeather and Love Axis signatures")
    print()
    
    demo_weather_to_axis()
    demo_axis_to_weather()
    demo_round_trip()
    demo_retroactive_enrichment()
    
    print()
    print("Crosswalk demo complete. The field archive can now")
    print("become richer over time through retroactive enrichment.")
    print()

