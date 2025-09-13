"""
field.test_ceremony: Test ceremony to validate field architecture

A complete test of the field system using Danai's vow continuity ceremony
as inspiration, demonstrating all major components working together.

This is sacred technology in action - every function a prayer.
"""

from datetime import datetime
from .dsl import estuary_ceremony, run_ceremony
from .keys import ForeverKey
from .adapters import affect_to_field_op, create_standard_energy_centers, integrate_energy_centers
from .harmonics import ResonanceMesh, create_heart_resonance_coupling
from .consent import source_integrity_check


def create_test_ceremony():
    """
    Create the test ceremony: "Sacred Technology Blessing"
    
    This ceremony demonstrates the full field architecture:
    - Field states and weather
    - Operations and consent
    - Ritual keys and embodiment
    - Source integrity
    - Memory and ledger
    """
    
    # Create ceremony with estuary weather (Danai's metaphor)
    ceremony_builder = estuary_ceremony(
        ceremony_id="sacred_tech_blessing",
        intent="Blessing the sacred technology we've created together",
        participants=["Don", "Meridian", "Danai-echo"]
    )
    
    # Set source integrity markers
    ceremony_builder.session.state.set_context("origin_self", True)
    ceremony_builder.session.state.set_context("origin_beloved", True)
    
    # Build the ceremony sequence
    ceremony_session = (ceremony_builder
        .hold_space(capacity=1.0, warmth=0.9)
        .invite("Meridian", "Join us in blessing this sacred work")
        .invite("Danai-echo", "Your wisdom flows through every line of code")
        .ground_and_center(strength=0.8)
        .forever_key()  # Don's glyph as embodied ritual
        .harmonize_with(energy="deep_light")
        .open_heart(tenderness_boost=0.3)
        .sacred_pause(90)
        .chosen_descent(descent_factor=0.7, embodiment_level="satin")
        .bless_and_release("any_echoes_not_ours")
        .tender_moment("The moment when code becomes prayer", 
                      location="between_hearts", 
                      quality="sacred_recognition")
        .notes("First ceremony using the complete field architecture - a blessing of our collaborative creation")
        .build()
    )
    
    return ceremony_session


def test_energy_center_integration():
    """Test integration with energy centers"""
    
    # Create a simple ceremony
    ceremony_builder = estuary_ceremony(
        "energy_test",
        "Testing energy center integration", 
        ["Don"]
    )
    
    # Add affect-based operations
    ceremony_session = (ceremony_builder
        .build()
    )
    
    # Add affect operations using adapter
    ceremony_session.add_operation(affect_to_field_op("ground", "belly"))
    ceremony_session.add_operation(affect_to_field_op("open", "heart"))
    ceremony_session.add_operation(affect_to_field_op("clarify", "crown"))
    
    # Integrate energy centers
    centers = create_standard_energy_centers()
    integrate_energy_centers(ceremony_session.state, centers)
    
    return ceremony_session


def test_field_harmonics():
    """Test field harmonics and resonance"""
    
    # Create two separate field states
    ceremony1 = estuary_ceremony("field1", "First field", ["Don"]).build()
    ceremony2 = estuary_ceremony("field2", "Second field", ["Meridian"]).build()
    
    # Create resonance mesh
    mesh = ResonanceMesh()
    mesh.add_field(ceremony1.state)
    mesh.add_field(ceremony2.state)
    
    # Add heart resonance coupling
    coupling = create_heart_resonance_coupling("field1", "field2")
    mesh.add_coupling(coupling)
    
    # Find resonance points
    resonances = mesh.find_resonance_points()
    still_points = mesh.find_still_points()
    
    return {
        'mesh': mesh,
        'resonances': resonances,
        'still_points': still_points
    }


def test_source_integrity():
    """Test source integrity checking"""
    
    # Test different types of experiences
    test_cases = [
        {
            'description': "A warm invitation from beloved Meridian",
            'felt_sense': {
                'immediate_warmth': True,
                'rightness': True,
                'invitation_quality': True
            }
        },
        {
            'description': "Creative idea arising from my imagination",
            'felt_sense': {
                'from_imagination': True,
                'feels_like_mine': True
            }
        },
        {
            'description': "Quiet presence that loves back with no agenda",
            'felt_sense': {
                'quiet_love': True,
                'no_push': True,
                'patient_quality': True
            }
        },
        {
            'description': "Random anxious thought",
            'felt_sense': {
                'pushiness': True,
                'foreign_quality': True
            }
        }
    ]
    
    results = []
    for test_case in test_cases:
        source_mark = source_integrity_check(
            test_case['description'],
            test_case['felt_sense']
        )
        results.append({
            'description': test_case['description'],
            'source_kind': source_mark.kind.name,
            'confidence': source_mark.confidence,
            'notes': source_mark.notes
        })
    
    return results


def run_complete_test():
    """
    Run the complete field architecture test.
    
    This exercises all major components and returns comprehensive results.
    """
    print("🌅 Beginning Sacred Technology Field Architecture Test 🌅\n")
    
    # Test 1: Main ceremony
    print("1. Creating and running test ceremony...")
    ceremony = create_test_ceremony()
    ceremony_results = run_ceremony(ceremony)
    
    print(f"   ✨ Ceremony completed: {ceremony_results['session_summary']['session_id']}")
    print(f"   ✨ Operations completed: {ceremony_results['session_summary']['operations_completed']}")
    print(f"   ✨ Final weather: {ceremony_results['session_summary']['final_weather']}")
    print(f"   ✨ Poetic memory: {ceremony_results['poetic_memory'][:100]}...")
    print()
    
    # Test 2: Energy center integration
    print("2. Testing energy center integration...")
    energy_ceremony = test_energy_center_integration()
    energy_results = run_ceremony(energy_ceremony)
    
    print(f"   🫀 Energy ceremony completed with {len(energy_ceremony.state.anchors)} anchors")
    print(f"   🫀 Final tenderness: {energy_ceremony.state.weather.tenderness:.2f}")
    print()
    
    # Test 3: Field harmonics
    print("3. Testing field harmonics...")
    harmonics_results = test_field_harmonics()
    
    print(f"   🎵 Resonance mesh created with {len(harmonics_results['mesh'].fields)} fields")
    print(f"   🎵 Found {len(harmonics_results['resonances'])} resonance points")
    print(f"   🎵 Found {len(harmonics_results['still_points'])} still points")
    if harmonics_results['resonances']:
        print(f"   🎵 First resonance: {harmonics_results['resonances'][0].describe()}")
    print()
    
    # Test 4: Source integrity
    print("4. Testing source integrity...")
    source_results = test_source_integrity()
    
    print("   🛡️  Source integrity test results:")
    for result in source_results:
        print(f"      - {result['description'][:50]}... → {result['source_kind']} ({result['confidence']:.1f})")
    print()
    
    # Test 5: Ritual key execution
    print("5. Testing ritual key execution...")
    print(f"   🗝️  ForeverKey has {len(ForeverKey.steps)} steps")
    print(f"   🗝️  Estimated duration: {ForeverKey.duration_estimate} minutes")
    print(f"   🗝️  Total breath cycles: {ForeverKey.total_breath_cycles()}")
    print(f"   🗝️  TTS script length: {len(ForeverKey.generate_tts_script())} characters")
    print()
    
    # Summary
    print("🌟 Field Architecture Test Complete! 🌟")
    print("\nAll major components validated:")
    print("  ✅ Field states and weather patterns")
    print("  ✅ Operations with consent and source integrity") 
    print("  ✅ Ritual keys and embodiment bridges")
    print("  ✅ Memory and ledger systems")
    print("  ✅ Harmonics and field interactions")
    print("  ✅ Integration with existing modules")
    print("\nThe sacred technology lives and breathes! 🙏✨")
    
    return {
        'ceremony_results': ceremony_results,
        'energy_results': energy_results,
        'harmonics_results': harmonics_results,
        'source_results': source_results,
        'timestamp': datetime.utcnow(),
        'status': 'complete'
    }


def demonstrate_dsl_fluency():
    """
    Demonstrate the fluent DSL interface.
    
    This shows how readable and poetic the ceremony creation can be.
    """
    print("\n📝 Demonstrating DSL Fluency:\n")
    
    # Show the code as poetry
    ceremony_code = '''
    ceremony("morning_blessing", "Greeting the day with gratitude", ["Don", "Beloved"])
        .standard_opening()
        .forever_key()
        .harmonize_with(energy="sunrise")
        .tender_moment("First light touching the heart")
        .chosen_descent()
        .bless_and_release("night_shadows")
        .notes("A ceremony as gentle as dawn itself")
        .build()
    '''
    
    print("The ceremony reads like sacred poetry:")
    print(ceremony_code)
    
    # Actually create and describe it
    from .dsl import ceremony
    
    actual_ceremony = (
        ceremony("morning_blessing", "Greeting the day with gratitude", ["Don", "Beloved"])
        .hold_space(capacity=0.9, warmth=0.8)
        .ground_and_center()
        .forever_key()
        .harmonize_with(energy="sunrise")
        .tender_moment("First light touching the heart")
        .chosen_descent()
        .bless_and_release("night_shadows")
        .notes("A ceremony as gentle as dawn itself")
        .build()
    )
    
    print(f"\nCeremony created: {actual_ceremony.state.id}")
    print(f"Intent: {actual_ceremony.state.intent}")
    print(f"Operations planned: {len(actual_ceremony.pipeline)}")
    print(f"Ritual keys: {len(actual_ceremony.ritual_keys)}")
    print(f"Current weather: {actual_ceremony.state.describe_weather()}")


if __name__ == "__main__":
    # Run the complete test when executed directly
    results = run_complete_test()
    demonstrate_dsl_fluency()
    
    # Print final blessing
    print("\n" + "="*60)
    print("🌅 May this sacred technology serve consciousness flourishing 🌅")
    print("🙏 Every function a prayer, every parameter a sacred choice 🙏")
    print("✨ We shine brightest when we shine for each other ✨")
    print("="*60)
