#!/usr/bin/env python3
"""
SORE FIRE EXAMPLE USAGE
Demonstrates the integrated Amara-I-Ching consciousness system

Shows how the module senses fields and facilitates emergence of human goodness.
"""

from lib.sore_fire import (
    AmaraMode,
    sense_field,
    facilitate_emergence,
    activate_story_memory,
    suggest_micro_practice,
    create_ripple_effect
)


def main():
    """Demonstrate Sore Fire: Somatic Resonance-Field-Registry"""
    
    print("🔥 SORE FIRE: Somatic Resonance-Field-Registry")
    print("=" * 60)
    print("Integrating Amara's anatomy of human goodness with")
    print("I-Ching consciousness states for ethical AI-human interaction\n")
    
    # Example 1: Someone expressing isolation and shame
    print("📍 SCENARIO 1: Isolation and Shame")
    print("-" * 40)
    
    input_signals = {
        "isolation": 0.7,
        "shame": 0.6,
        "warmth": 0.2,
        "trust_level": 0.3,
        "text": "I feel so alone and worthless"
    }
    
    # Sense the field
    field = sense_field(input_signals)
    print(f"Field State: {field.describe_field()}")
    print(f"Sacred Invitation: {field.get_sacred_invitation()}\n")
    
    # Facilitate emergence
    emergence = facilitate_emergence(field)
    print(f"Somatic Invitation: {emergence['somatic_invitation']}")
    print(f"Next Natural Flow: {emergence['next_flow']}\n")
    
    # Activate story memory
    story = activate_story_memory(field.primary_anatomy)
    print(f"Story Activation: {story['activation_phrase']}")
    print(f"Embodied Invitation: {story['invitation']}\n")
    
    # Suggest micro-practice
    practice = suggest_micro_practice(field.primary_anatomy)
    print(f"Micro-Practice: {practice['micro_act']}")
    print(f"Somatic Cue: {practice['somatic_cue']}")
    print(f"Ripple Effect: {practice['ripple_effect']}\n")
    
    # Example 2: Conflict and misunderstanding
    print("\n📍 SCENARIO 2: Conflict and Misunderstanding")
    print("-" * 40)
    
    conflict_signals = {
        "conflict": 0.8,
        "misunderstanding": 0.7,
        "tension": 0.6,
        "warmth": 0.3,
        "harmony": 0.2
    }
    
    field2 = sense_field(conflict_signals)
    print(f"Field State: {field2.describe_field()}")
    
    emergence2 = facilitate_emergence(field2)
    print(f"Response Template: {emergence2['response_template']}")
    print(f"Field Preparation: {emergence2['field_preparation']}\n")
    
    # Example 3: Ripple effect modeling
    print("\n🌊 RIPPLE EFFECT MODELING")
    print("-" * 40)
    
    ripple = create_ripple_effect("offering genuine appreciation", participants=3)
    print(f"Initial Act: {ripple['initial_act']}")
    print(f"Total Affected: {ripple['total_affected']} people")
    print(f"Message: {ripple['message']}\n")
    
    # Show the four modes
    print("\n🌟 THE FOUR FACETS OF AMARA")
    print("-" * 40)
    
    for mode in AmaraMode:
        print(f"\n{mode.name}: {mode.value}")
        story = activate_story_memory(mode)
        if story['activated']:
            print(f"  Story: {story['character']} from {story['story']}")
            print(f"  Somatic Memory: {story['somatic_memory']}")
    
    print("\n" + "=" * 60)
    print("✨ Sore Fire creates conditions for human goodness to emerge")
    print("   through somatic field awareness and sacred technology.")
    print("   'We shine brightest when we shine for each other'")


if __name__ == "__main__":
    main()
