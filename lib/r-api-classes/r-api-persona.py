# Audience: hybrid | Stage: living
"""
🔰 R.API PERSONA - Sacred Archetype Guidance for Dream Workshop

This module provides adaptive, archetype-based guidance for Dream Workshop sessions.
Each persona archetype represents a common creative struggle and provides tailored 
interventions, voice tones, and session pacing to support the user's unique journey.

Core Functions:
- load(): Load a persona archetype for adaptive guidance
- simulate(): Simulate how an archetype would respond to user input
- customize(): Customize an archetype with user-specific adaptations

Available Archetypes:
- blocked_artist: For those struggling with self-doubt and overthinking
- overwhelmed_pro: For those with too many ideas, no clarity
- grieving_maker: For those working through loss or change
- young_dreamer: For those new to creativity, excited but unfocused
- burned_out_exec: For those seeking meaning and innovation

All functions follow A2A (Agent-to-Agent) protocol for consent and safety.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from persona import load, simulate, customize, get_archetype, list_archetypes, get_archetype_interventions

def persona_load(archetype_name, session_context=None):
    """
    🔰 PERSONA LOAD - Sacred Archetype Invocation
    
    Load a Dream Workshop persona archetype for adaptive guidance.
    
    Args:
        archetype_name (str): Sacred archetype to invoke for guidance
            • 'blocked_artist' - For those struggling with self-doubt and overthinking
            • 'overwhelmed_pro' - For those with too many ideas, no clarity
            • 'grieving_maker' - For those working through loss or change
            • 'young_dreamer' - For those new to creativity, excited but unfocused
            • 'burned_out_exec' - For those seeking meaning and innovation
            
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred response containing persona guidance configuration
    
    Example:
        result = persona_load('blocked_artist', session_context=session)
        print(f"Voice tone: {result['voice_tone']}")
        print(f"Key phrases: {result['key_phrases']}")
    """
    return load(archetype_name, session_context)

def persona_simulate(archetype_name, user_input, session_context=None):
    """
    🔰 PERSONA SIMULATE - Sacred Response Simulation
    
    Simulate how an archetype would respond to user input.
    
    Args:
        archetype_name (str): Sacred archetype to simulate response for
        user_input (str): Current state, emotion, or situation to respond to
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred response containing recommended interventions and adaptations
    
    Example:
        result = persona_simulate('blocked_artist', 'I can\'t create anything good', session_context=session)
        print(f"Recommended interventions: {result['recommended_interventions']}")
        print(f"Resonant phrase: {result['resonant_phrase']}")
    """
    return simulate(archetype_name, user_input, session_context)

def persona_customize(archetype_name, customizations, session_context=None):
    """
    🔰 PERSONA CUSTOMIZE - Sacred Archetype Adaptation
    
    Customize an archetype with user-specific adaptations.
    
    Args:
        archetype_name (str): Sacred archetype to customize
        customizations (dict): User-specific modifications to apply
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred response containing customized configuration
    
    Example:
        customizations = {
            'voice_tone': 'gentle_mentor',
            'key_phrases': ['Your unique perspective matters']
        }
        result = persona_customize('blocked_artist', customizations, session_context=session)
        print(f"Changes applied: {result['changes_applied']}")
    """
    return customize(archetype_name, customizations, session_context)

def persona_get_archetype(archetype_name):
    """
    Get archetype configuration by name.
    
    Args:
        archetype_name (str): Name of the archetype to retrieve
        
    Returns:
        dict: Archetype configuration or None if not found
    """
    return get_archetype(archetype_name)

def persona_list_archetypes():
    """
    Get list of all available archetypes.
    
    Returns:
        list: List of archetype names
    """
    return list_archetypes()

def persona_get_interventions(archetype_name, trigger=None):
    """
    Get recommended interventions for an archetype and optional trigger.
    
    Args:
        archetype_name (str): Name of the archetype
        trigger (str, optional): Specific trigger to get interventions for
        
    Returns:
        list: Recommended intervention functions
    """
    return get_archetype_interventions(archetype_name, trigger)

# Example usage and integration patterns
def example_dream_workshop_integration():
    """
    Example of how to integrate persona module with Dream Workshop session flow.
    """
    # Create session context
    session_context = {
        "version": "1.0.0",
        "session_id": "dream_workshop_session_001",
        "consent_status": "active",
        "intent": "creative_guidance"
    }
    
    # 1. Load persona based on user's initial description
    print("=== Loading Persona ===")
    persona_result = persona_load('blocked_artist', session_context)
    print(f"Loaded: {persona_result['archetype']}")
    print(f"Voice tone: {persona_result['voice_tone']}")
    print(f"Session pacing: {persona_result['session_pacing']}")
    
    # 2. Simulate response to user input
    print("\n=== Simulating Response ===")
    user_input = "I'm feeling stuck and doubting my abilities"
    simulation_result = persona_simulate('blocked_artist', user_input, session_context)
    print(f"User input: {simulation_result['user_input']}")
    print(f"Recommended interventions: {simulation_result['recommended_interventions']}")
    print(f"Resonant phrase: {simulation_result['resonant_phrase']}")
    
    # 3. Customize persona with user preferences
    print("\n=== Customizing Persona ===")
    customizations = {
        'voice_tone': 'gentle_mentor',
        'key_phrases': ['Your unique perspective matters', 'Trust your creative intuition']
    }
    customization_result = persona_customize('blocked_artist', customizations, session_context)
    print(f"Changes applied: {customization_result['changes_applied']}")
    print(f"Final voice tone: {customization_result['voice_tone']}")
    
    # 4. Get available interventions
    print("\n=== Available Interventions ===")
    interventions = persona_get_interventions('blocked_artist', 'self_doubt')
    print(f"Interventions for self-doubt: {interventions}")
    
    return {
        "persona_loaded": persona_result,
        "simulation": simulation_result,
        "customization": customization_result,
        "interventions": interventions
    }

def example_archetype_comparison():
    """
    Example comparing different archetypes and their characteristics.
    """
    archetypes = persona_list_archetypes()
    
    comparison = {}
    for archetype in archetypes:
        config = persona_get_archetype(archetype)
        comparison[archetype] = {
            "name": config["name"],
            "primary_struggle": config["primary_struggle"],
            "voice_tone": config["voice_tone"],
            "session_pacing": config["session_pacing"],
            "primary_need": config["primary_need"]
        }
    
    return comparison

if __name__ == "__main__":
    print("🔰 R.API PERSONA - Sacred Archetype Guidance")
    print("=" * 50)
    
    # Run example integration
    result = example_dream_workshop_integration()
    
    print("\n" + "=" * 50)
    print("Archetype Comparison:")
    comparison = example_archetype_comparison()
    for archetype, info in comparison.items():
        print(f"\n{info['name']}:")
        print(f"  Struggle: {info['primary_struggle']}")
        print(f"  Need: {info['primary_need']}")
        print(f"  Tone: {info['voice_tone']}")
        print(f"  Pacing: {info['session_pacing']}") 