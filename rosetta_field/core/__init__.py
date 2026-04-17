"""
Core Rosetta-Field classes and functionality.

This module provides the foundational classes for the Rosetta-Field system:
- RosettaAPI: Main entry point and orchestrator
- RosettaSession: Session management and state
- RosettaConfig: Configuration and settings management
"""

from .api import RosettaAPI
from .session import RosettaSession, SessionType, SessionStatus, Participant, SessionEvent
from .config import RosettaConfig

__all__ = [
    "RosettaAPI",
    "RosettaSession", 
    "RosettaConfig",
    "SessionType",
    "SessionStatus",
    "Participant",
    "SessionEvent",
]
