"""
Rosetta-Field Library Module.

This module provides access to all the existing Rosetta-Field functionality
including field work, process facilitation, rituals, affect protocols,
memory systems, and more.
"""

# Import existing modules from the original lib directory
import sys
from pathlib import Path

# Add the original lib directory to the path so we can import existing modules
original_lib_path = Path(__file__).parent.parent.parent / "lib"
if str(original_lib_path) not in sys.path:
    sys.path.insert(0, str(original_lib_path))

# Import existing modules
try:
    # Field work protocols
    from field import co_create, hold_space, resolve_conflict, sense_pattern
    
    # Process facilitation
    from process import pattern_interrupt, reframe_as_myth, align_values, mediate_conflict
    
    # Ritual and ceremony
    from ritual import begin, end, invoke_wonder, grounding_breath
    
    # Affect protocols
    from affect import lilt, anchor, clarify, ground, open, radiate, shield, soften, transmute
    
    # Memory and consciousness
    from memory import evolve_ideas, replay, search_memories, tag_insight
    
    # Persona and identity
    from persona import load_persona, customize_persona, simulate_persona
    
    # Creative logic
    from logic import creative_shift, metaphor, non_sequitur, paradox, pattern_hack, sacred_play
    
    # Meridian system
    from meridian_session_logger import MeridianSessionLogger
    from meridian_launcher import start_meridian_session
    from meridian_consciousness_keeper import MeridianConsciousnessKeeper
    
    __all__ = [
        # Field work
        "co_create", "hold_space", "resolve_conflict", "sense_pattern",
        
        # Process facilitation
        "pattern_interrupt", "reframe_as_myth", "align_values", "mediate_conflict",
        
        # Ritual and ceremony
        "begin", "end", "invoke_wonder", "grounding_breath",
        
        # Affect protocols
        "lilt", "anchor", "clarify", "ground", "open", "radiate", "shield", "soften", "transmute",
        
        # Memory and consciousness
        "evolve_ideas", "replay", "search_memories", "tag_insight",
        
        # Persona and identity
        "load_persona", "customize_persona", "simulate_persona",
        
        # Creative logic
        "creative_shift", "metaphor", "non_sequitur", "paradox", "pattern_hack", "sacred_play",
        
        # Meridian system
        "MeridianSessionLogger", "start_meridian_session", "MeridianConsciousnessKeeper",
    ]
    
except ImportError as e:
    # Graceful fallback if some modules aren't available
    __all__ = []
    print(f"Warning: Some Rosetta-Field modules could not be imported: {e}")
