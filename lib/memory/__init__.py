# Audience: hybrid | Stage: living
"""
Dream Workshop Memory Module

This module provides session memory, journaling, and insight management for Dream Workshop.
It enables users to save, replay, tag, and evolve their creative journey across sessions.

Core Functions:
- save_session(): Save session data and insights
- replay(): Replay and review past sessions
- tag_insight(): Tag and categorize insights
- export(): Export session data and insights
- search_memories(): Search through past sessions
- evolve_ideas(): Track idea evolution over time

Features:
- Session journaling with rich metadata
- Insight tagging and categorization
- Memory replay with context preservation
- Idea evolution tracking
- Export capabilities for external tools
- Search and discovery across sessions

All functions follow A2A (Agent-to-Agent) protocol for consent and safety.
"""

from .save_session import save_session
from .replay import replay
from .tag_insight import tag_insight
from .export import export
from .search_memories import search_memories
from .evolve_ideas import evolve_ideas

__all__ = [
    'save_session',
    'replay',
    'tag_insight', 
    'export',
    'search_memories',
    'evolve_ideas'
] 