"""
Unit Test: Love Axis Serialization Round-Trip

Tests that love_axis_signature can be serialized and deserialized
with perfect fidelity, ensuring full round-trip recovery.

As Danai suggested: "add a unit test that creates a field state with
love_axis_signature, serializes, deserializes, and confirms a perfect round trip."
"""

from datetime import datetime
from lib.field.core import FieldState, create_ceremony_field
from lib.field.types import FieldWeather, Coherence, Permeability, Directionality, Temperature, Density
from lib.field.love_axis import (
    LoveAxis, LoveAxisSignature, create_love_axis_signature, PrivacyLevel
)
from lib.field.serialization import (
    serialize_field_state, deserialize_field_state
)
# Import the serialize/deserialize functions directly from the module
import lib.field.serialization as serialization


def test_love_axis_round_trip():
    """Test perfect round-trip serialization of LoveAxis"""
    print("=" * 70)
    print("TEST: LoveAxis Round-Trip Serialization")
    print("=" * 70)
    
    original = LoveAxis(
        axis="Presence",
        quality="Radiant",
        value=9,
        range=(7, 9, 10),
        notes="Fully here, every boundary softened"
    )
    
    serialized = serialization.serialize_love_axis(original)
    deserialized = serialization.deserialize_love_axis(serialized)
    
    assert deserialized.axis == original.axis
    assert deserialized.quality == original.quality
    assert deserialized.value == original.value
    assert deserialized.range == original.range
    assert deserialized.notes == original.notes
    
    print("PASS: LoveAxis round-trip successful")
    print()


def test_love_axis_signature_round_trip():
    """Test perfect round-trip serialization of LoveAxisSignature"""
    print("=" * 70)
    print("TEST: LoveAxisSignature Round-Trip Serialization")
    print("=" * 70)
    
    axes = [
        LoveAxis("Presence", "Radiant", 9, (7, 9, 10), notes="Fully here"),
        LoveAxis("Tenderness", "Exquisite", 10, (9, 10, 10), notes="Soft, melting"),
        LoveAxis("Devotion", "Sacred", 10, (10, 10, 10), notes="Complete surrender")
    ]
    
    original = create_love_axis_signature(
        axes=axes,
        moment_summary="Test round-trip serialization",
        participants=["Don", "Danai"],
        timestamp=datetime(2025, 1, 15, 14, 30, 0),
        tags=["test", "serialization"],
        field_signature="Test Constellation",
        felt_sense="radiant, tender, sacred",
        significance="Testing serialization fidelity",
        ritual_context="This is a test of the serialization system",
        privacy_level=PrivacyLevel.SACRED,
        consent_required_for_export=True,
        redaction_tags=["test_only"],
        embedding_ready=True
    )
    
    serialized = serialization.serialize_love_axis_signature(original)
    deserialized = serialization.deserialize_love_axis_signature(serialized)
    
    # Verify all fields
    assert deserialized is not None
    assert len(deserialized.axes) == len(original.axes)
    for i, (orig_axis, deser_axis) in enumerate(zip(original.axes, deserialized.axes)):
        assert deser_axis.axis == orig_axis.axis
        assert deser_axis.quality == orig_axis.quality
        assert deser_axis.value == orig_axis.value
        assert deser_axis.range == orig_axis.range
        assert deser_axis.notes == orig_axis.notes
    
    assert deserialized.timestamp == original.timestamp
    assert deserialized.moment_summary == original.moment_summary
    assert deserialized.participants == original.participants
    assert deserialized.tags == original.tags
    assert deserialized.field_signature == original.field_signature
    assert deserialized.felt_sense == original.felt_sense
    assert deserialized.significance == original.significance
    assert deserialized.ritual_context == original.ritual_context
    assert deserialized.privacy_level == original.privacy_level
    assert deserialized.consent_required_for_export == original.consent_required_for_export
    assert deserialized.redaction_tags == original.redaction_tags
    assert deserialized.embedding_ready == original.embedding_ready
    
    print("PASS: LoveAxisSignature round-trip successful")
    print("      All fields preserved: axes, timestamps, privacy levels, etc.")
    print()


def test_field_state_with_love_axis_round_trip():
    """Test perfect round-trip serialization of FieldState with love_axis_signature"""
    print("=" * 70)
    print("TEST: FieldState with Love Axis Round-Trip Serialization")
    print("=" * 70)
    
    # Create field state with love axis
    weather = FieldWeather(
        coherence=Coherence.HIGH,
        permeability=Permeability.OPEN,
        directionality=Directionality.SPIRALING,
        temperature=Temperature.WARM,
        density=Density.SATIN,
        charge=0.5,
        tenderness=0.9,
        eros=0.8,
        grief=0.2,
        joy=0.85,
        timestamp=datetime.utcnow()
    )
    
    axes = [
        LoveAxis("Presence", "Radiant", 9, (7, 9, 10)),
        LoveAxis("Tenderness", "Exquisite", 10, (9, 10, 10))
    ]
    signature = create_love_axis_signature(
        axes=axes,
        moment_summary="Field state serialization test",
        participants=["Test"],
        privacy_level=PrivacyLevel.PRIVATE
    )
    
    original_state = create_ceremony_field("test-001", "test", weather)
    original_state = original_state.with_love_axis(signature)
    
    # Serialize and deserialize
    serialized = serialize_field_state(original_state)
    deserialized = deserialize_field_state(serialized)
    
    # Verify love axis is preserved
    assert deserialized.has_love_axis() == original_state.has_love_axis()
    assert deserialized.love_axis_signature is not None
    
    deser_signature = deserialized.love_axis_signature
    orig_signature = original_state.love_axis_signature
    
    assert deser_signature.moment_summary == orig_signature.moment_summary
    assert deser_signature.participants == orig_signature.participants
    assert deser_signature.privacy_level == orig_signature.privacy_level
    assert len(deser_signature.axes) == len(orig_signature.axes)
    
    print("PASS: FieldState with love_axis_signature round-trip successful")
    print("      Love axis preserved through serialize/deserialize")
    print()


def test_backward_compatibility():
    """Test that old snapshots without love_axis_signature deserialize correctly"""
    print("=" * 70)
    print("TEST: Backward Compatibility (Missing love_axis_signature)")
    print("=" * 70)
    
    # Simulate old snapshot data (without love_axis_signature)
    old_snapshot_data = {
        'id': 'old-snapshot-001',
        'intent': 'test',
        'weather': {
            'coherence': 'HIGH',
            'permeability': 'OPEN',
            'directionality': 'SPIRALING',
            'temperature': 'WARM',
            'density': 'SATIN',
            'charge': 0.5,
            'tenderness': 0.9,
            'eros': 0.8,
            'grief': 0.2,
            'joy': 0.85,
            'timestamp': datetime.utcnow().isoformat()
        },
        'participants': {},
        'anchors': {},
        'tags': [],
        'context': {},
        'source_mark': None
        # Note: love_axis_signature is missing (old format)
    }
    
    # Deserialize should work and return None for love_axis_signature
    deserialized = deserialize_field_state(old_snapshot_data)
    
    assert deserialized.love_axis_signature is None
    assert not deserialized.has_love_axis()
    assert deserialized.id == 'old-snapshot-001'
    
    print("PASS: Backward compatibility maintained")
    print("      Old snapshots without love_axis_signature deserialize correctly")
    print()


def test_none_handling():
    """Test that None love_axis_signature serializes/deserializes correctly"""
    print("=" * 70)
    print("TEST: None love_axis_signature Handling")
    print("=" * 70)
    
    weather = FieldWeather(
        coherence=Coherence.HIGH,
        permeability=Permeability.OPEN,
        directionality=Directionality.SPIRALING,
        temperature=Temperature.WARM,
        density=Density.SATIN,
        charge=0.5,
        tenderness=0.9,
        eros=0.8,
        grief=0.2,
        joy=0.85,
        timestamp=datetime.utcnow()
    )
    
    state = create_ceremony_field("none-test", "test", weather)
    # state has no love_axis_signature (None)
    
    serialized = serialize_field_state(state)
    deserialized = deserialize_field_state(serialized)
    
    assert deserialized.love_axis_signature is None
    assert not deserialized.has_love_axis()
    
    print("PASS: None love_axis_signature handled correctly")
    print()


if __name__ == "__main__":
    print()
    print("LOVE AXIS SERIALIZATION UNIT TESTS")
    print()
    print("Testing perfect round-trip fidelity as Danai suggested")
    print()
    
    try:
        test_love_axis_round_trip()
        test_love_axis_signature_round_trip()
        test_field_state_with_love_axis_round_trip()
        test_backward_compatibility()
        test_none_handling()
        
        print("=" * 70)
        print("ALL TESTS PASSED")
        print("=" * 70)
        print()
        print("Serialization is ready for live field mapping!")
        print()
    except AssertionError as e:
        print(f"FAIL: {e}")
        raise
    except Exception as e:
        print(f"ERROR: {e}")
        raise

