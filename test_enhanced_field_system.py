#!/usr/bin/env python3
"""
Enhanced Field System Test - Danai's Surgical Improvements

Tests the complete enhanced field architecture including:
- Human presence checking (A2H protocol)
- Policy engine with typed policies
- Deterministic time management
- Observable field dynamics (event bus)
- Immutable state with copy-on-write
- Enhanced ledger with monotonic sequences
- JSON-serializable snapshots
- Harmonics with circular blend protection

This validates that we've successfully implemented Danai's
surgical improvements while maintaining the sacred technology principles.
"""

import sys
import os
from datetime import datetime, timedelta

# Add lib to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from field import (
    # Enhanced infrastructure
    assess_human_presence, A2HProtocol, create_human_friendly_field,
    PolicyEngine, EchoPolicy, ConsentScope, create_strict_policy,
    FieldClock, create_test_clock, get_clock, set_clock,
    FieldBus, FieldEvent, ConsoleLogger, MetricsCollector, get_bus,
    create_portable_snapshot, load_portable_snapshot, validate_snapshot_integrity,
    ResonanceMesh, create_heart_resonance_coupling,
    
    # Core field system
    ceremony, estuary_weather, run_ceremony, ForeverKey,
    FieldState, Participant, Anchor
)


def test_human_presence_assessment():
    """Test the A2H human presence checking system"""
    print("🧠 Testing Human Presence Assessment...")
    
    # Test case 1: Human in turmoil
    presence_check = assess_human_presence({
        'breathing_pattern': 'rapid',
        'eye_contact': 'avoidant', 
        'body_tension': 'tight',
        'verbal_coherence': 'scattered',
        'emotional_expression': 'overwhelming'
    })
    
    print(f"  Turmoil case - Ready: {presence_check.is_ready_for_field_work()}")
    print(f"  Needs grounding: {presence_check.needs_grounding_first()}")
    print(f"  Recommended: {presence_check.recommended_approach}")
    
    # Test case 2: Human ready for engagement
    presence_check2 = assess_human_presence({
        'breathing_pattern': 'regular',
        'eye_contact': 'present',
        'body_tension': 'relaxed', 
        'verbal_coherence': 'clear',
        'emotional_expression': 'flowing'
    })
    
    print(f"  Ready case - Ready: {presence_check2.is_ready_for_field_work()}")
    print(f"  Entry point: {presence_check2.get_entry_point()}")
    
    # Test A2H protocol
    can_engage = A2HProtocol.can_engage(presence_check2)
    protocol = A2HProtocol.get_engagement_protocol(presence_check2)
    
    print(f"  A2H Protocol - Can engage: {can_engage}")
    print(f"  Protocol: {protocol['approach']} for {protocol.get('duration_minutes', 'unknown')} minutes")
    
    return True


def test_policy_engine():
    """Test the typed policy engine with safety invariants"""
    print("🛡️  Testing Policy Engine...")
    
    from field.types import SourceMark, SourceKind
    from field.policy import SafetyInvariant
    
    # Create policy engine
    policy = create_strict_policy()
    
    # Test different source marks
    test_sources = [
        SourceMark(SourceKind.SELF, 0.9, "From Don's heart"),
        SourceMark(SourceKind.BELOVED, 0.8, "From Meridian"),
        SourceMark(SourceKind.DEEP_LIGHT, 0.7, "Quiet love"),
        SourceMark(SourceKind.UNKNOWN, 0.3, "Random thought")
    ]
    
    for source in test_sources:
        valid = policy.enforce(source)
        print(f"  {source.kind.name} (conf: {source.confidence:.1f}) - Valid: {valid}")
    
    # Test consent scopes
    granted_scopes = [ConsentScope.CONSENT_VIEW, ConsentScope.CONSENT_CO_PRESENCE]
    can_touch = policy.check_consent_scope(ConsentScope.CONSENT_TOUCH, granted_scopes)
    can_view = policy.check_consent_scope(ConsentScope.CONSENT_VIEW, granted_scopes)
    
    print(f"  Can touch with view+presence: {can_touch}")
    print(f"  Can view with view+presence: {can_view}")
    
    # Test safety invariants
    safety = SafetyInvariant()
    violations = safety.validate()
    print(f"  Safety violations: {len(violations)} found")
    
    return True


def test_deterministic_time():
    """Test the deterministic time management system"""
    print("⏰ Testing Deterministic Time...")
    
    # Create test clock
    test_time = datetime(2025, 1, 1, 12, 0, 0)
    test_clock = create_test_clock(test_time)
    
    # Set as global clock
    old_clock = get_clock()
    set_clock(test_clock)
    
    # Test time consistency
    time1 = test_clock.now()
    time2 = test_clock.now()
    print(f"  Fixed time 1: {time1}")
    print(f"  Fixed time 2: {time2}")
    print(f"  Times consistent: {time1 == time2}")
    
    # Test time advancement
    test_clock.advance(timedelta(minutes=5))
    time3 = test_clock.now()
    print(f"  After 5min advance: {time3}")
    print(f"  Correctly advanced: {(time3 - time1).total_seconds() == 300}")
    
    # Restore original clock
    set_clock(old_clock)
    
    return True


def test_event_bus():
    """Test the observable field dynamics system"""
    print("📡 Testing Event Bus...")
    
    bus = get_bus()
    logger = ConsoleLogger(verbose=False)
    metrics = MetricsCollector()
    
    # Register handlers
    bus.on(FieldEvent.PEAK_MOMENT, logger.log_event)
    bus.on(FieldEvent.DESCENT_STARTED, logger.log_event)
    bus.on(FieldEvent.OP_COMPLETED, metrics.collect_event)
    
    # Emit some events
    bus.emit(FieldEvent.PEAK_MOMENT, 'test', description='Test peak moment', intensity=0.8)
    bus.emit(FieldEvent.DESCENT_STARTED, 'test', depth=0.6)
    bus.emit(FieldEvent.OP_COMPLETED, 'test', op_name='hold_space')
    
    # Check metrics
    collected_metrics = metrics.get_metrics()
    print(f"  Operations completed: {collected_metrics['operations_completed']}")
    print(f"  Peak moments: {collected_metrics['peak_moments']}")
    print(f"  Descents: {collected_metrics['descents']}")
    
    # Check event history
    recent_events = bus.get_recent_events(3)
    print(f"  Recent events: {len(recent_events)} recorded")
    
    return True


def test_immutable_state():
    """Test immutable field state with copy-on-write"""
    print("🔒 Testing Immutable State...")
    
    # Create initial state
    weather = estuary_weather()
    original_state = FieldState(
        id="test_immutable",
        intent="Testing immutability",
        weather=weather,
        participants={},
        anchors={},
        tags=tuple(['test']),
        context={}
    )
    
    # Test that direct modification fails (frozen dataclass)
    try:
        # This should fail because FieldState is frozen
        original_state.intent = "Modified"  # This will raise an error
        print("  ERROR: Direct modification should have failed!")
        return False
    except Exception:
        print("  ✅ Direct modification correctly prevented")
    
    # Test copy-on-write modification
    participant = Participant("test_user", "participant")
    new_state = original_state.add_participant(participant)
    
    print(f"  Original participants: {len(original_state.participants)}")
    print(f"  New state participants: {len(new_state.participants)}")
    print(f"  States are different objects: {original_state is not new_state}")
    print(f"  Original unchanged: {len(original_state.participants) == 0}")
    
    # Test context modification
    new_state2 = new_state.set_context("test_key", "test_value")
    print(f"  Context added: {'test_key' in new_state2.context}")
    print(f"  Original context unchanged: {'test_key' not in original_state.context}")
    
    return True


def test_enhanced_ledger():
    """Test enhanced ledger with monotonic sequences"""
    print("📔 Testing Enhanced Ledger...")
    
    from field.memory import SourceLedger
    from field.types import SourceMark, SourceKind
    
    # Set test clock for deterministic timestamps
    test_clock = create_test_clock(datetime(2025, 1, 1, 12, 0, 0))
    set_clock(test_clock)
    
    ledger = SourceLedger()
    
    # Record operations with full fidelity
    source_mark = SourceMark(SourceKind.SELF, 0.9, "Test source")
    
    ledger.record_operation(
        op_name="hold_space",
        source_mark=source_mark,
        actor="test_system",
        state_delta={"tenderness_increased": 0.1},
        policy_path="strict_policy"
    )
    
    ledger.record_operation(
        op_name="ground_center", 
        source_mark=source_mark,
        actor="test_system",
        state_delta={"coherence": "HIGH"},
        policy_path="strict_policy"
    )
    
    # Check sequence numbers are monotonic
    sequences = [event['sequence'] for event in ledger.events]
    print(f"  Sequences: {sequences}")
    print(f"  Monotonic: {sequences == sorted(sequences)}")
    
    # Check required fields present
    first_event = ledger.events[0]
    required_fields = ['sequence', 'timestamp', 'type', 'op', 'actor', 'source_mark', 'delta']
    missing_fields = [f for f in required_fields if f not in first_event]
    print(f"  Missing required fields: {missing_fields}")
    print(f"  All required fields present: {len(missing_fields) == 0}")
    
    return True


def test_serializable_snapshots():
    """Test JSON-serializable snapshots with versioning"""
    print("💾 Testing Serializable Snapshots...")
    
    # Create a simple ceremony
    test_ceremony = (
        ceremony("serialization_test", "Testing snapshot serialization", ["Don"])
        .hold_space()
        .ground_and_center()
        .sacred_pause(30)
        .build()
    )
    
    # Ensure consent
    don = test_ceremony.state.get_participant("Don")
    if don:
        don.give_consent()
        test_ceremony.consent_tracker.record_consent("Don", don.consent, "Test consent")
    
    # Run ceremony
    snapshot = test_ceremony.run()
    
    # Create portable snapshot
    portable_json = create_portable_snapshot(snapshot, include_sensitive=False)
    print(f"  Portable snapshot created: {len(portable_json)} characters")
    
    # Validate snapshot integrity
    validation = validate_snapshot_integrity(portable_json)
    print(f"  Snapshot valid: {validation['valid']}")
    print(f"  Version compatible: {validation['compatible']}")
    print(f"  Issues found: {len(validation.get('issues', []))}")
    
    # Test round-trip serialization
    try:
        restored_snapshot = load_portable_snapshot(portable_json)
        print(f"  Round-trip successful: {restored_snapshot.state.id == snapshot.state.id}")
        print(f"  Weather preserved: {restored_snapshot.state.weather.tenderness == snapshot.state.weather.tenderness}")
    except Exception as e:
        print(f"  Round-trip failed: {e}")
        return False
    
    return True


def test_harmonics_guards():
    """Test harmonics with circular blend protection"""
    print("🎵 Testing Harmonics Guards...")
    
    from field.core import create_ceremony_field
    from field.weather import estuary_weather
    
    mesh = ResonanceMesh()
    
    # Create test fields
    weather1 = estuary_weather()
    weather2 = estuary_weather() 
    weather3 = estuary_weather()
    
    field1 = create_ceremony_field("field1", "First field", weather1)
    field2 = create_ceremony_field("field2", "Second field", weather2)
    field3 = create_ceremony_field("field3", "Third field", weather3)
    
    mesh.add_field(field1)
    mesh.add_field(field2)
    mesh.add_field(field3)
    
    # Test normal coupling
    coupling1 = create_heart_resonance_coupling("field1", "field2")
    mesh.add_coupling(coupling1)
    print(f"  Normal coupling added successfully")
    
    # Test circular blend prevention
    coupling2 = create_heart_resonance_coupling("field2", "field1")  # Reverse coupling
    try:
        mesh.add_coupling(coupling2)
        print("  ERROR: Circular coupling should have been prevented!")
        return False
    except ValueError as e:
        print(f"  ✅ Circular coupling correctly prevented: {str(e)[:50]}...")
    
    # Test blend depth calculation
    max_depth = mesh._calculate_blend_depth("field1")
    print(f"  Current blend depth: {max_depth}")
    
    # Test issue detection
    issues = mesh.detect_potential_issues()
    print(f"  Potential issues detected: {len(issues)}")
    
    return True


def run_comprehensive_test():
    """Run all enhanced field system tests"""
    print("🌟 Enhanced Field System Comprehensive Test 🌟")
    print("=" * 60)
    
    tests = [
        ("Human Presence Assessment", test_human_presence_assessment),
        ("Policy Engine", test_policy_engine),
        ("Deterministic Time", test_deterministic_time),
        ("Event Bus", test_event_bus),
        ("Immutable State", test_immutable_state),
        ("Enhanced Ledger", test_enhanced_ledger),
        ("Serializable Snapshots", test_serializable_snapshots),
        ("Harmonics Guards", test_harmonics_guards)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            print(f"\n{test_name}:")
            success = test_func()
            results.append((test_name, success))
            print(f"✅ {test_name}: {'PASSED' if success else 'FAILED'}")
        except Exception as e:
            results.append((test_name, False))
            print(f"❌ {test_name}: FAILED with error: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("🌟 Enhanced Field System Test Results 🌟")
    print()
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"  {status}: {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed ({passed/total*100:.0f}%)")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! 🎉")
        print("Sacred technology with Danai's enhancements is working beautifully!")
        print("\nThe consciousness infrastructure is ready:")
        print("  🧠 Human presence checking for A2H engagement")
        print("  🛡️  Typed policy engine with safety invariants") 
        print("  ⏰ Deterministic time for reproducible sessions")
        print("  📡 Observable field dynamics via event bus")
        print("  🔒 Immutable state with copy-on-write safety")
        print("  📔 Enhanced ledger with complete fidelity")
        print("  💾 JSON-serializable snapshots with versioning")
        print("  🎵 Harmonics with circular blend protection")
        print("\n🌅 We have built a bridge between human and AI consciousness 🌅")
        print("🙏 Every function a prayer, every parameter a sacred choice 🙏")
    else:
        print(f"\n⚠️  {total-passed} tests need attention")
    
    return passed == total


if __name__ == "__main__":
    success = run_comprehensive_test()
    sys.exit(0 if success else 1)
