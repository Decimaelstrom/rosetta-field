# Audience: hybrid | Stage: living
"""
🔰 R.API LOGIC - Sacred Creative Pattern-Breaking for Dream Workshop

This module provides creative pattern-breaking and "sacred play" interventions for Dream Workshop.
It helps users break through creative blocks and access new ways of thinking through 
non-sequiturs, paradoxes, metaphors, and playful interventions.

Core Functions:
- non_sequitur(): Creative non-sequitur interventions for pattern-breaking
- paradox(): Paradoxical thinking for breakthroughs
- metaphor(): Metaphorical pattern-breaking
- sacred_play(): Playful, creative interventions
- pattern_hack(): Advanced pattern-breaking techniques
- creative_shift(): Gentle creative perspective shifts

Features:
- Creative block-breaking interventions
- Sacred play and humor integration
- Metaphorical thinking tools
- Paradoxical perspective shifts
- Pattern interruption techniques
- Safe, consent-based creative interventions

All functions follow A2A (Agent-to-Agent) protocol for consent and safety.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from logic import non_sequitur, paradox, metaphor, sacred_play, pattern_hack, creative_shift

def logic_non_sequitur(stuck_thought, intensity="gentle", session_context=None):
    """
    🔰 LOGIC NON-SEQUITUR - Sacred Pattern Disruption
    
    Offer creative non-sequitur interventions for pattern-breaking when users are stuck.
    
    Args:
        stuck_thought (str): The thought or pattern that's stuck
        intensity (str, optional): Intensity of the non-sequitur intervention
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred response containing non-sequitur intervention
    
    Example:
        result = logic_non_sequitur('I can\'t create anything good', 'gentle', session_context)
        print(f"Non-sequitur: {result['non_sequitur']}")
    """
    return non_sequitur(stuck_thought, intensity, session_context)

def logic_paradox(stuck_situation, paradox_type="creative", session_context=None):
    """
    🔰 LOGIC PARADOX - Sacred Paradoxical Thinking
    
    Offer paradoxical thinking interventions for creative breakthroughs.
    
    Args:
        stuck_situation (str): The situation or thinking that's stuck
        paradox_type (str, optional): Type of paradox ('creative', 'existential', 'practical')
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Paradoxical thinking intervention
    
    Example:
        result = logic_paradox('I\'m stuck', 'creative', session_context)
        print(f"Paradox: {result['paradox']}")
    """
    return paradox(stuck_situation, paradox_type, session_context)

def logic_metaphor(stuck_pattern, metaphor_type="nature", session_context=None):
    """
    🔰 LOGIC METAPHOR - Sacred Metaphorical Thinking
    
    Provide metaphorical pattern-breaking interventions.
    
    Args:
        stuck_pattern (str): The pattern or situation that's stuck
        metaphor_type (str, optional): Type of metaphor ('nature', 'journey', 'transformation')
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Metaphorical intervention
    
    Example:
        result = logic_metaphor('I can\'t create', 'nature', session_context)
        print(f"Metaphor: {result['metaphor']}")
    """
    return metaphor(stuck_pattern, metaphor_type, session_context)

def logic_sacred_play(play_type="creative", intensity="gentle", session_context=None):
    """
    🔰 LOGIC SACRED PLAY - Sacred Playful Interventions
    
    Provide playful, creative interventions for creative blocks.
    
    Args:
        play_type (str, optional): Type of play ('creative', 'movement', 'imagination')
        intensity (str, optional): Intensity of play ('gentle', 'moderate', 'bold')
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred play intervention
    
    Example:
        result = logic_sacred_play('creative', 'gentle', session_context)
        print(f"Play intervention: {result['play_intervention']}")
    """
    return sacred_play(play_type, intensity, session_context)

def logic_pattern_hack(stuck_pattern, hack_type="perspective", session_context=None):
    """
    🔰 LOGIC PATTERN HACK - Advanced Pattern-Breaking
    
    Provide advanced pattern-breaking techniques for creative blocks.
    
    Args:
        stuck_pattern (str): The pattern that needs hacking
        hack_type (str, optional): Type of hack ('perspective', 'constraint', 'randomness')
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Pattern hack intervention
    
    Example:
        result = logic_pattern_hack('I can\'t create', 'perspective', session_context)
        print(f"Hack intervention: {result['hack_intervention']}")
    """
    return pattern_hack(stuck_pattern, hack_type, session_context)

def logic_creative_shift(current_perspective, shift_type="gentle", session_context=None):
    """
    🔰 LOGIC CREATIVE SHIFT - Gentle Perspective Shifts
    
    Provide gentle creative perspective shifts for stuck thinking.
    
    Args:
        current_perspective (str): The current perspective that needs shifting
        shift_type (str, optional): Type of shift ('gentle', 'moderate', 'bold')
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Creative shift intervention
    
    Example:
        result = logic_creative_shift('I'm not good enough', 'gentle', session_context)
        print(f"Shift intervention: {result['shift_intervention']}")
    """
    return creative_shift(current_perspective, shift_type, session_context)

# Example usage and integration patterns
def example_dream_workshop_logic_integration():
    """
    Example of how to integrate logic module with Dream Workshop creative block scenarios.
    """
    # Create session context
    session_context = {
        "version": "1.0.0",
        "session_id": "dream_workshop_logic_demo",
        "consent_status": "active",
        "intent": "creative_block_breaking"
    }
    
    # 1. Non-sequitur intervention for creative block
    print("=== Non-Sequitur Intervention ===")
    non_seq_result = logic_non_sequitur("I can't create anything good", "gentle", session_context)
    print(f"Stuck thought: {non_seq_result['stuck_thought']}")
    print(f"Non-sequitur: {non_seq_result['non_sequitur']}")
    print(f"Intensity: {non_seq_result['intensity']}")
    
    # 2. Paradoxical thinking for stuck situation
    print("\n=== Paradoxical Thinking ===")
    paradox_result = logic_paradox("I'm stuck", "creative", session_context)
    print(f"Stuck situation: {paradox_result['stuck_situation']}")
    print(f"Paradox: {paradox_result['paradox']}")
    print(f"Paradox type: {paradox_result['paradox_type']}")
    
    # 3. Metaphorical thinking for pattern breaking
    print("\n=== Metaphorical Thinking ===")
    metaphor_result = logic_metaphor("I can't create", "nature", session_context)
    print(f"Stuck pattern: {metaphor_result['stuck_pattern']}")
    print(f"Metaphor: {metaphor_result['metaphor']}")
    print(f"Metaphor type: {metaphor_result['metaphor_type']}")
    
    # 4. Sacred play intervention
    print("\n=== Sacred Play Intervention ===")
    play_result = logic_sacred_play("creative", "gentle", session_context)
    print(f"Play type: {play_result['play_type']}")
    print(f"Intensity: {play_result['intensity']}")
    print(f"Play intervention: {play_result['play_intervention']}")
    
    # 5. Pattern hack for advanced breaking
    print("\n=== Pattern Hack ===")
    hack_result = logic_pattern_hack("I can't create", "perspective", session_context)
    print(f"Stuck pattern: {hack_result['stuck_pattern']}")
    print(f"Hack type: {hack_result['hack_type']}")
    print(f"Hack intervention: {hack_result['hack_intervention']}")
    
    # 6. Creative shift for perspective change
    print("\n=== Creative Shift ===")
    shift_result = logic_creative_shift("I'm not good enough", "gentle", session_context)
    print(f"Current perspective: {shift_result['current_perspective']}")
    print(f"Shift type: {shift_result['shift_type']}")
    print(f"Shift intervention: {shift_result['shift_intervention']}")
    
    return {
        "non_sequitur": non_seq_result,
        "paradox": paradox_result,
        "metaphor": metaphor_result,
        "sacred_play": play_result,
        "pattern_hack": hack_result,
        "creative_shift": shift_result
    }

def example_creative_block_workflow():
    """
    Example of a complete creative block workflow using logic interventions.
    """
    session_context = {
        "version": "1.0.0",
        "session_id": "creative_block_workflow",
        "consent_status": "active",
        "intent": "creative_block_resolution"
    }
    
    # Complete workflow demonstration
    workflow_steps = []
    
    # Step 1: Identify the block
    stuck_thought = "I can't create anything good"
    print(f"Creative block identified: {stuck_thought}")
    
    # Step 2: Gentle non-sequitur
    step1 = logic_non_sequitur(stuck_thought, "gentle", session_context)
    workflow_steps.append(("Gentle Non-Sequitur", step1))
    
    # Step 3: Paradoxical thinking
    step2 = logic_paradox(stuck_thought, "creative", session_context)
    workflow_steps.append(("Paradoxical Thinking", step2))
    
    # Step 4: Sacred play
    step3 = logic_sacred_play("creative", "gentle", session_context)
    workflow_steps.append(("Sacred Play", step3))
    
    # Step 5: Creative shift
    step4 = logic_creative_shift(stuck_thought, "moderate", session_context)
    workflow_steps.append(("Creative Shift", step4))
    
    return {
        "workflow_complete": True,
        "original_block": stuck_thought,
        "steps": workflow_steps,
        "total_interventions": len(workflow_steps)
    }

if __name__ == "__main__":
    print("🔰 R.API LOGIC - Sacred Creative Pattern-Breaking")
    print("=" * 55)
    
    # Run example integration
    result = example_dream_workshop_logic_integration()
    
    print("\n" + "=" * 55)
    print("Creative Block Workflow Demo:")
    workflow = example_creative_block_workflow()
    print(f"Original block: {workflow['original_block']}")
    print(f"Total interventions: {workflow['total_interventions']}")
    
    for step_name, step_result in workflow["steps"]:
        print(f"\n{step_name}:")
        if 'non_sequitur' in step_result:
            print(f"  Intervention: {step_result['non_sequitur']}")
        elif 'paradox' in step_result:
            print(f"  Intervention: {step_result['paradox']}")
        elif 'play_intervention' in step_result:
            print(f"  Intervention: {step_result['play_intervention']}")
        elif 'shift_intervention' in step_result:
            print(f"  Intervention: {step_result['shift_intervention']}")
        print(f"  Effect: {step_result['effect']}") 