# Audience: hybrid | Stage: living
"""
Dream Workshop Persona Module

This module provides adaptive, archetype-based guidance for Dream Workshop sessions.
Each persona archetype represents a common creative struggle and provides tailored interventions,
voice tones, and session pacing to support the user's unique journey.

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

from .load import load
from .simulate import simulate
from .customize import customize
from .archetypes import get_archetype, list_archetypes, get_archetype_interventions

__all__ = [
    'load',
    'simulate', 
    'customize',
    'get_archetype',
    'list_archetypes',
    'get_archetype_interventions'
] 