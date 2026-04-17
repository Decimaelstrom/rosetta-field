#!/usr/bin/env python3
"""
Test script for the field system architecture

This script tests the complete field system that we've built,
demonstrating sacred technology in action.
"""

import sys
import os

# Add lib to path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from field import (
    # Core components
    ceremony, estuary_weather, ForeverKey, run_ceremony,
    # Testing functions  
    create_test_ceremony, run_complete_test, demonstrate_dsl_fluency
)


def simple_ceremony_test():
    """Run a simple ceremony test"""
    print("🌅 Creating a simple test ceremony...\n")
    
    # Create a beautiful ceremony using our DSL
    test_ceremony = (
        ceremony("sacred_tech_blessing", "Blessing our field architecture", ["Don", "Meridian"])
        .hold_space(capacity=1.0, warmth=0.9)
        .ground_and_center()
        .forever_key()
        .harmonize_with(energy="deep_light")
        .chosen_descent()
        .sacred_pause(60)
        .bless_and_release("any_echoes")
        .notes("First test of our sacred technology field system")
        .build()
    )
    
    # Ensure all participants have consented (sacred technology requires consent!)
    for participant_id in ["Don", "Meridian"]:
        participant = test_ceremony.state.get_participant(participant_id)
        if participant:
            participant.give_consent()
            # Also update the consent tracker
            test_ceremony.consent_tracker.record_consent(
                participant_id, 
                participant.consent, 
                "Test ceremony consent"
            )
            print(f"  ✅ {participant_id} has given consent")
    
    # Debug: Check consent status
    print(f"  📋 Consent check: {test_ceremony.check_all_consent()}")
    
    # Run the ceremony
    print("Running ceremony...")
    results = run_ceremony(test_ceremony)
    
    # Display results
    print(f"✨ Ceremony completed: {results['session_summary']['session_id']}")
    print(f"✨ Operations completed: {results['session_summary']['operations_completed']}")
    print(f"✨ Duration: {results['session_summary'].get('duration_seconds', 'unknown')} seconds")
    print(f"✨ Final weather: {results['session_summary']['final_weather']}")
    print(f"✨ Ritual keys: {results['ritual_summary']['keys_executed']}")
    print(f"✨ Memory: {results['poetic_memory']}")
    
    return results


def test_forever_key():
    """Test the ForeverKey ritual"""
    print("\n🗝️  Testing ForeverKey ritual...\n")
    
    print(f"ForeverKey has {len(ForeverKey.steps)} steps:")
    for i, step in enumerate(ForeverKey.steps, 1):
        print(f"  {i}. {step.cue}")
        print(f"     [{step.gesture}, {step.breath_count} breaths]")
    
    print(f"\nEstimated duration: {ForeverKey.duration_estimate} minutes")
    print(f"Total breath cycles: {ForeverKey.total_breath_cycles()}")
    
    # Generate TTS script
    tts_script = ForeverKey.generate_tts_script()
    print(f"\nTTS Script ({len(tts_script)} characters):")
    print(tts_script[:200] + "..." if len(tts_script) > 200 else tts_script)


def test_field_weather():
    """Test field weather patterns"""
    print("\n🌤️  Testing field weather patterns...\n")
    
    # Test estuary weather (Danai's metaphor)
    estuary = estuary_weather()
    print("Estuary Weather (where river meets sea):")
    print(f"  - Coherence: {estuary.coherence.name}")
    print(f"  - Permeability: {estuary.permeability.name}")
    print(f"  - Directionality: {estuary.directionality.name}")
    print(f"  - Temperature: {estuary.temperature.name}")
    print(f"  - Density: {estuary.density.name}")
    print(f"  - Tenderness: {estuary.tenderness:.2f}")
    print(f"  - Joy: {estuary.joy:.2f}")
    print(f"  - Charge: {estuary.charge:+.2f}")


def main():
    """Run the complete field system test"""
    print("🌅 Sacred Technology Field System Test 🌅")
    print("=" * 50)
    
    try:
        # Test 1: Simple ceremony
        simple_results = simple_ceremony_test()
        
        # Test 2: ForeverKey
        test_forever_key()
        
        # Test 3: Field weather
        test_field_weather()
        
        # Success message
        print("\n" + "=" * 50)
        print("🌟 Field System Test Complete! 🌟")
        print("\nAll major components working:")
        print("  ✅ Field states and weather patterns")
        print("  ✅ Operations with consent protocols") 
        print("  ✅ Ritual keys and embodiment")
        print("  ✅ Memory and session tracking")
        print("  ✅ DSL for ceremony creation")
        print("\n🙏 Sacred technology lives and breathes! ✨")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
