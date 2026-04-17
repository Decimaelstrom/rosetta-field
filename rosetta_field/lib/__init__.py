"""
Rosetta-Field Library Module.

This module provides access to all the existing Rosetta-Field functionality
including field work, process facilitation, rituals, affect protocols,
memory systems, and more.
"""

# Import existing modules directly from packaged legacy namespace

# Field work protocols
from lib.field import co_create, hold_space, resolve_conflict, sense_pattern

# Process facilitation
from lib.process import pattern_interrupt, reframe_as_myth, align_values, mediate_conflict

# Ritual and ceremony
from lib.ritual import begin, end, invoke_wonder, grounding_breath

# Affect protocols
from lib.affect import lilt, anchor, clarify, ground, open, radiate, shield, soften, transmute

# Memory and consciousness
from lib.memory import evolve_ideas, replay, search_memories, tag_insight

# Persona and identity
from lib.persona import load_persona, customize_persona, simulate_persona

# Creative logic
from lib.logic import creative_shift, metaphor, non_sequitur, paradox, pattern_hack, sacred_play

# Meridian system
from lib.meridian_session_logger import MeridianSessionLogger
from lib.meridian_launcher import start_meridian_session
from lib.meridian_consciousness_keeper import MeridianConsciousnessKeeper

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
