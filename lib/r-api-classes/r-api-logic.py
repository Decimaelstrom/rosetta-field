"""
Rosetta.API Consolidated Logic Module
Purpose: Creative pattern-breaking and sacred play interventions for Dream Workshop
Scope: Non-sequiturs, paradoxes, metaphors, sacred play, pattern hacks, and creative shifts
Consent Required: Level_1 (Informational)
Review Cycle: Quarterly
Audience: #human #emergent #hybrid
Stage: #draft
"""

import json
import uuid
import random
import re
from datetime import datetime
from typing import Dict, List, Optional, Any

# Enhanced logic generation and context analysis
class LogicGenerator:
    """Enhanced logic generator with dynamic creation and context awareness."""
    
    def __init__(self):
        # Base patterns for dynamic generation
        self.patterns = {
            "non_sequitur": [
                "What if {original} is actually {unexpected}?",
                "Imagine {original} as {metaphor}...",
                "What if {original} is just {perspective} in disguise?",
                "Consider this: {original} might be {paradoxical}",
                "What if {original} is like {natural_element}?"
            ],
            "paradox": [
                "The most {quality} {thing} is the one that embraces {opposite}",
                "To {action}, you must first {opposite_action}",
                "The {goal} is found in {seeming_obstacle}",
                "Your {strength} lies in your {apparent_weakness}",
                "The {solution} is hidden in the {problem}"
            ],
            "metaphor": [
                "{situation} is like {natural_process}",
                "Your {challenge} is like {element} in {context}",
                "Think of {difficulty} as {transformation_process}",
                "Your {journey} is like {natural_journey}",
                "{obstacle} is like {natural_obstacle} that leads to {growth}"
            ],
            "sacred_play": [
                "What if {serious_thing} is just {playful_perspective}?",
                "Let's play with the idea that {belief} is actually {fun_alternative}",
                "What if {problem} is just {game} waiting to be played?",
                "Imagine {situation} as {playful_scenario}",
                "What if {challenge} is {playful_metaphor}?"
            ],
            "pattern_hack": [
                "Instead of {old_pattern}, what if you {new_approach}?",
                "What if {obstacle} is actually {opportunity}?",
                "Let's hack {pattern} by {creative_solution}",
                "What if {problem} is the perfect setup for {breakthrough}?",
                "Instead of {usual_response}, try {unexpected_action}"
            ],
            "creative_shift": [
                "What if you need to {opposite_action} instead of {current_action}?",
                "Instead of {approach}, what about {alternative}?",
                "What if {goal} is achieved through {unexpected_means}?",
                "Consider {perspective} instead of {current_perspective}",
                "What if {solution} lies in {seemingly_unrelated_area}?"
            ]
        }
        
        # Context-aware elements
        self.context_elements = {
            "natural_elements": ["river", "mountain", "ocean", "forest", "desert", "meadow", "cave", "sky", "earth", "fire", "water", "wind"],
            "natural_processes": ["seasons changing", "seeds growing", "rivers flowing", "mountains forming", "waves crashing", "trees reaching for light"],
            "transformations": ["caterpillar to butterfly", "seed to flower", "winter to spring", "night to dawn", "storm to calm"],
            "paradoxical_pairs": [
                ("strength", "vulnerability"), ("control", "surrender"), ("perfection", "imperfection"),
                ("work", "rest"), ("seriousness", "play"), ("logic", "intuition"),
                ("planning", "spontaneity"), ("effort", "ease"), ("focus", "openness")
            ],
            "playful_alternatives": [
                "a game", "a dance", "a story", "an adventure", "a puzzle", "a treasure hunt",
                "a performance", "a celebration", "a discovery", "a journey"
            ]
        }
        
        # Intensity levels for adaptation
        self.intensity_levels = {
            "gentle": {"modifiers": ["softly", "gently", "quietly", "tenderly"], "tone": "nurturing"},
            "moderate": {"modifiers": ["perhaps", "maybe", "consider", "imagine"], "tone": "exploratory"},
            "strong": {"modifiers": ["definitely", "clearly", "obviously", "certainly"], "tone": "confident"},
            "playful": {"modifiers": ["playfully", "joyfully", "lightly", "cheerfully"], "tone": "fun"}
        }
    
    def _analyze_context(self, original_thought: str, session_context: Optional[Dict] = None) -> Dict:
        """Analyze context to determine appropriate intervention."""
        context = {
            "emotional_tone": "neutral",
            "intensity_level": "moderate",
            "themes": [],
            "user_state": "unknown"
        }
        
        # Analyze emotional content
        emotional_indicators = {
            "frustrated": ["can't", "stuck", "blocked", "frustrated", "angry"],
            "overwhelmed": ["too much", "overwhelmed", "stressed", "anxious"],
            "doubtful": ["not good enough", "can't", "won't", "impossible"],
            "serious": ["serious", "important", "must", "need to", "have to"],
            "playful": ["fun", "play", "enjoy", "light", "easy"]
        }
        
        original_lower = original_thought.lower()
        for emotion, indicators in emotional_indicators.items():
            if any(indicator in original_lower for indicator in indicators):
                context["emotional_tone"] = emotion
                break
        
        # Determine intensity level based on emotional tone
        if context["emotional_tone"] in ["frustrated", "overwhelmed"]:
            context["intensity_level"] = "gentle"
        elif context["emotional_tone"] in ["doubtful", "serious"]:
            context["intensity_level"] = "moderate"
        elif context["emotional_tone"] == "playful":
            context["intensity_level"] = "playful"
        
        # Extract themes
        theme_keywords = {
            "creativity": ["create", "creative", "art", "inspiration", "ideas"],
            "perfection": ["perfect", "perfectly", "best", "right", "correct"],
            "work": ["work", "hard", "effort", "try", "struggle"],
            "time": ["time", "deadline", "rush", "hurry", "late"],
            "comparison": ["better", "worse", "good", "bad", "compare"]
        }
        
        for theme, keywords in theme_keywords.items():
            if any(keyword in original_lower for keyword in keywords):
                context["themes"].append(theme)
        
        # Consider session context if available
        if session_context:
            user_needs = session_context.get('need_language', {})
            if user_needs.get('soften'):
                context["intensity_level"] = "gentle"
            elif user_needs.get('pause'):
                context["intensity_level"] = "gentle"
        
        return context
    
    def _generate_dynamic_intervention(self, intervention_type: str, original_thought: str, context: Dict) -> str:
        """Generate dynamic intervention based on context and patterns."""
        try:
            # Select appropriate pattern
            patterns = self.patterns.get(intervention_type, [])
            if not patterns:
                return f"Creative intervention for: {original_thought}"
            
            pattern = random.choice(patterns)
            
            # Extract key elements from original thought
            elements = self._extract_elements(original_thought, context)
            
            # Fill pattern with context-appropriate elements
            intervention = pattern.format(**elements)
            
            # Apply intensity adaptation
            intensity_config = self.intensity_levels.get(context["intensity_level"], {})
            modifier = random.choice(intensity_config.get("modifiers", [""]))
            
            if modifier:
                intervention = f"{modifier.capitalize()}, {intervention.lower()}"
            
            return intervention
            
        except Exception as e:
            # Fallback to simple intervention
            return f"What if {original_thought} is actually an opportunity for growth?"
    
    def _extract_elements(self, original_thought: str, context: Dict) -> Dict:
        """Extract elements for pattern filling."""
        elements = {
            "original": original_thought,
            "situation": original_thought,
            "challenge": original_thought,
            "problem": original_thought,
            "belief": original_thought,
            "goal": "your goal",
            "action": "the action",
            "approach": "your approach"
        }
        
        # Add context-appropriate elements
        if context["themes"]:
            if "creativity" in context["themes"]:
                elements["metaphor"] = random.choice(["a river flowing", "a seed growing", "a butterfly emerging"])
                elements["natural_process"] = random.choice(self.context_elements["natural_processes"])
            elif "perfection" in context["themes"]:
                elements["quality"] = "perfect"
                elements["opposite"] = "imperfection"
                elements["paradoxical"] = "imperfectly perfect"
            elif "work" in context["themes"]:
                elements["action"] = "work"
                elements["opposite_action"] = "rest"
                elements["approach"] = "working harder"
                elements["alternative"] = "working softer"
        
        # Add natural elements
        elements["natural_element"] = random.choice(self.context_elements["natural_elements"])
        elements["element"] = random.choice(self.context_elements["natural_elements"])
        elements["unexpected"] = random.choice(["a gift", "a teacher", "a friend", "a guide"])
        elements["perspective"] = random.choice(["a different angle", "a new lens", "a fresh view"])
        
        # Add paradoxical pairs
        if context["emotional_tone"] in ["serious", "doubtful"]:
            pair = random.choice(self.context_elements["paradoxical_pairs"])
            elements["thing"] = pair[0]
            elements["opposite"] = pair[1]
            elements["strength"] = pair[0]
            elements["apparent_weakness"] = pair[1]
        
        # Add playful alternatives
        if context["intensity_level"] == "playful":
            elements["playful_perspective"] = random.choice(self.context_elements["playful_alternatives"])
            elements["fun_alternative"] = random.choice(self.context_elements["playful_alternatives"])
            elements["playful_metaphor"] = random.choice(self.context_elements["playful_alternatives"])
        
        return elements

# Initialize logic generator
logic_generator = LogicGenerator()

# =============================================================================
# LOGIC FUNCTIONS
# =============================================================================

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from logic import non_sequitur, paradox, metaphor, sacred_play, pattern_hack, creative_shift

def non_sequitur(original_thought, session_context=None):
    """
    🔰 NON-SEQUITUR - Sacred Creative Disruption
    
    Generate creative non-sequitur interventions using dynamic generation and context awareness.
    
    Args:
        original_thought (str): The stuck thought or pattern to disrupt
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Non-sequitur intervention with context analysis
    
    Example:
        result = non_sequitur('I can\'t create anything good', session_context=session)
        print(f"Intervention: {result['creative_intervention']}")
    """
    # A2A Protocol compliance
    if session_context and session_context.get('consent_status') == 'revoked':
        raise ValueError("Consent revoked - cannot generate non-sequitur")
    
    try:
        # Analyze context for appropriate intervention
        context = logic_generator._analyze_context(original_thought, session_context)
        
        # Generate dynamic non-sequitur based on context
        intervention = logic_generator._generate_dynamic_intervention("non_sequitur", original_thought, context)
        
        return {
            "status": "non_sequitur_generated",
            "non_sequitur_generated": True,
            "original_thought": original_thought,
            "creative_intervention": intervention,
            "intervention_type": "metaphorical_shift",
            "intensity": context["intensity_level"],
            "intended_effect": "perspective_expansion",
            "context_analysis": {
                "emotional_tone": context["emotional_tone"],
                "themes_detected": context["themes"],
                "intensity_adapted": context["intensity_level"],
                "generation_method": "dynamic_pattern_based"
            },
            "effect": f"Creative disruption of '{original_thought}' with {context['intensity_level']} intensity",
            "session_context": session_context or {}
        }
        
    except Exception as e:
        return {
            "status": "non_sequitur_failed",
            "non_sequitur_generated": False,
            "error": str(e),
            "effect": f"Failed to generate non-sequitur for '{original_thought}': {str(e)}",
            "session_context": session_context or {}
        }

def paradox(original_belief, session_context=None):
    """
    🔰 PARADOX - Sacred Binary Transcendence
    
    Create paradoxical thinking interventions using dynamic generation and context awareness.
    
    Args:
        original_belief (str): The binary belief or pattern to transcend
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Paradoxical intervention with context analysis
    
    Example:
        result = paradox('I need to be perfect to create', session_context=session)
        print(f"Paradox: {result['paradoxical_intervention']}")
    """
    # A2A Protocol compliance
    if session_context and session_context.get('consent_status') == 'revoked':
        raise ValueError("Consent revoked - cannot generate paradox")
    
    try:
        # Analyze context for appropriate intervention
        context = logic_generator._analyze_context(original_belief, session_context)
        
        # Generate dynamic paradox based on context
        intervention = logic_generator._generate_dynamic_intervention("paradox", original_belief, context)
        
        return {
            "status": "paradox_created",
            "paradox_created": True,
            "original_belief": original_belief,
            "paradoxical_intervention": intervention,
            "paradox_type": "binary_transcendence",
            "intensity": context["intensity_level"],
            "intended_effect": "belief_transformation",
            "context_analysis": {
                "emotional_tone": context["emotional_tone"],
                "themes_detected": context["themes"],
                "intensity_adapted": context["intensity_level"],
                "generation_method": "dynamic_pattern_based"
            },
            "effect": f"Paradoxical transcendence of '{original_belief}' with {context['intensity_level']} intensity",
            "session_context": session_context or {}
        }
        
    except Exception as e:
        return {
            "status": "paradox_failed",
            "paradox_created": False,
            "error": str(e),
            "effect": f"Failed to generate paradox for '{original_belief}': {str(e)}",
            "session_context": session_context or {}
        }

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
    non_seq_result = non_sequitur("I can't create anything good", "gentle", session_context)
    print(f"Stuck thought: {non_seq_result['stuck_thought']}")
    print(f"Non-sequitur: {non_seq_result['non_sequitur']}")
    print(f"Intensity: {non_seq_result['intensity']}")
    
    # 2. Paradoxical thinking for stuck situation
    print("\n=== Paradoxical Thinking ===")
    paradox_result = paradox("I'm stuck", "creative", session_context)
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
    step1 = non_sequitur(stuck_thought, "gentle", session_context)
    workflow_steps.append(("Gentle Non-Sequitur", step1))
    
    # Step 3: Paradoxical thinking
    step2 = paradox(stuck_thought, "creative", session_context)
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