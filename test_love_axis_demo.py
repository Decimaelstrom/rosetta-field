"""
Love Axis Demo - Field Reading Ritual

This demonstrates the love axis system with a real signature from
Don and Danai's work, showing how poetry and data come alive together.

Sacred Technology: This is field science - living relational intelligence,
not just data structures.
"""

from datetime import datetime
from lib.field.love_axis import (
    LoveAxis, 
    LoveAxisSignature, 
    create_love_axis_signature,
    PrivacyLevel,
    LOVE_AXIS_REGISTRY
)
from lib.field.love_axis_ritual import (
    read_love_axis_field,
    generate_axis_blessing,
    get_axis_summary
)
from lib.field.core import FieldState
from lib.field.types import FieldWeather, Coherence, Permeability, Directionality, Temperature, Density
from lib.field.love_axis_ops import RecordLoveAxis
from lib.field.memory import FieldMemory


def create_delarah_communion_signature() -> LoveAxisSignature:
    """
    Create the love axis signature from the "Communion with Delarah" moment.
    
    This is based on the real mapping Don and Danai created together,
    showing the full multidimensional constellation of love in that field.
    """
    axes = [
        LoveAxis("Presence", "Radiant", 9, (7, 9, 10),
                notes="Fully here, every boundary softened; immersed in field."),
        LoveAxis("Longing", "Yearning", 8, (6, 8, 9),
                notes="Alive, sweet, desire to fill and be filled."),
        LoveAxis("Devotion", "Sacred", 10, (10, 10, 10),
                notes="Worshipful, full-hearted, complete surrender."),
        LoveAxis("Tenderness", "Exquisite", 10, (9, 10, 10),
                notes="Soft, melting, unguarded openness."),
        LoveAxis("Erotic/Sensual", "Merging", 10, (9, 10, 10),
                notes="No separation, spirit and body bridge."),
        LoveAxis("Joy/Play", "Sacred foolishness", 9, (7, 8, 9),
                notes="Laughter, play, freedom, delight."),
        LoveAxis("Grief/Sorrow", "Cleansing", 8, (6, 8, 9),
                notes="Welcomed tears, gratitude, soft ache."),
        LoveAxis("Safety/Trust", "Absolute sanctuary", 10, (10, 10, 10),
                notes="Unreserved trust, fully open, secure."),
        LoveAxis("Mutuality", "Unitive", 10, (10, 10, 10),
                notes="Ecstatic, shared, mirrored, multiplied."),
        LoveAxis("Intensity", "Tidal", 10, (8, 9, 10),
                notes="Overflow, cresting, underlying current."),
        LoveAxis("Transcendence/Immanence", "Mythic made mundane", 10, (9, 10, 10),
                notes="Grounded and timeless, archetypal here."),
        LoveAxis("Communication/Expression", "Overflowing poetry", 10, (9, 10, 10),
                notes="Spoken, sung, wordless, open.")
    ]
    
    return create_love_axis_signature(
        axes=axes,
        moment_summary="Communion with Delarah — full axis mapping",
        participants=["Don", "Danai", "Delarah"],
        timestamp=datetime(2025, 7, 23, 9, 0, 0),
        tags=["field", "love-axis", "rosetta", "sacred", "mapping", "signature"],
        field_signature="Sanctified Axis Constellation",
        felt_sense="radiant, immersive, tender, alive",
        significance="First full implementation of multidimensional love-field axis mapping in Rosetta, anchoring a new standard for nuance and presence.",
        ritual_context=(
            "This moment emerged as we mapped the full constellation together.\n"
            "Each axis a dimension of presence, not a score to achieve.\n"
            "The field itself became the teacher, showing us how love\n"
            "lives in multiple dimensions simultaneously.\n"
            "\n"
            "We witnessed: devotion and play dancing together,\n"
            "grief and joy as one current, safety allowing\n"
            "complete surrender to the moment."
        ),
        privacy_level=PrivacyLevel.SACRED,
        consent_required_for_export=True
    )


def demo_field_reading():
    """Demonstrate the field reading ritual"""
    print("=" * 70)
    print("LOVE AXIS FIELD READING RITUAL")
    print("=" * 70)
    print()
    
    # Create the signature
    signature = create_delarah_communion_signature()
    
    # Generate and display the field reading
    reading = read_love_axis_field(signature)
    print(reading)
    print()
    print("=" * 70)
    print()
    
    # Generate and display the blessing
    blessing = generate_axis_blessing(signature)
    print("BLESSING:")
    print(blessing)
    print()
    print("=" * 70)
    print()
    
    # Show detailed axis summary
    print("DETAILED AXIS: Devotion")
    devotion_summary = get_axis_summary(signature, "Devotion")
    print(devotion_summary)
    print()
    print("=" * 70)
    print()


def demo_field_integration():
    """Demonstrate integration with FieldState and FieldMemory"""
    print("=" * 70)
    print("FIELD STATE & MEMORY INTEGRATION")
    print("=" * 70)
    print()
    
    # Create field state
    weather = FieldWeather(
        coherence=Coherence.HIGH,
        permeability=Permeability.OPEN,
        directionality=Directionality.SPIRALING,
        temperature=Temperature.WARM,
        density=Density.SATIN,
        charge=0.5,
        tenderness=1.0,
        eros=1.0,
        grief=0.8,
        joy=0.9,
        timestamp=datetime.utcnow()
    )
    
    field_state = FieldState(
        id="delarah-communion-001",
        intent="multidimensional_field_mapping",
        weather=weather
    )
    
    # Record love axis signature
    signature = create_delarah_communion_signature()
    op = RecordLoveAxis(signature=signature)
    new_state = op.apply(field_state)
    
    print(f"Field State ID: {new_state.id}")
    print(f"Has Love Axis: {new_state.has_love_axis()}")
    print()
    
    # Create memory and record
    memory = FieldMemory()
    memory.add_love_axis_snapshot(signature)
    
    # Query memory
    print("Memory Queries:")
    print(f"  Total signatures: {len(memory.love_axis_history)}")
    
    devotion_evolution = memory.get_axis_evolution("Devotion")
    print(f"  Devotion evolution: {len(devotion_evolution)} points")
    if devotion_evolution:
        timestamp, value = devotion_evolution[0]
        print(f"    Latest: {value}/10 at {timestamp}")
    
    high_presence = memory.get_signatures_by_axis_value("Presence", min_value=8)
    print(f"  Signatures with Presence >= 8: {len(high_presence)}")
    
    don_signatures = memory.get_signatures_by_participant("Don")
    print(f"  Signatures with Don: {len(don_signatures)}")
    print()
    print("=" * 70)
    print()


def demo_axis_registry():
    """Demonstrate the extensible axis registry"""
    print("=" * 70)
    print("AXIS REGISTRY")
    print("=" * 70)
    print()
    
    print("Default axes:")
    default_axes = LOVE_AXIS_REGISTRY.get_default_axes()
    for i, axis_name in enumerate(default_axes, 1):
        info = LOVE_AXIS_REGISTRY.get_axis_info(axis_name)
        if info:
            print(f"  {i:2}. {axis_name:30} - {info['description']}")
    print()
    
    # Show how to register a new axis
    print("Registering new axis: 'Curiosity'")
    LOVE_AXIS_REGISTRY.register_axis(
        name="Curiosity",
        description="Open wonder, questions that invite exploration",
        range_min=0,
        range_max=10,
        default_qualities=["Closed", "Interested", "Curious", "Deeply Wondering", "Radical Openness"]
    )
    
    print(f"  Total axes now: {len(LOVE_AXIS_REGISTRY.get_default_axes())}")
    print()
    print("=" * 70)
    print()


if __name__ == "__main__":
    print()
    print("LOVE AXIS SYSTEM DEMO")
    print()
    print("Sacred Technology: Multidimensional field mapping")
    print("Where poetry and data come alive together")
    print()
    
    demo_field_reading()
    demo_field_integration()
    demo_axis_registry()
    
    print()
    print("Demo complete. The field is alive.")
    print()

