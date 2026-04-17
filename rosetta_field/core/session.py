"""
Session management for Rosetta-Field.

This module provides the RosettaSession class for managing
session state, participants, and session lifecycle.
"""

import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, field
from enum import Enum


class SessionStatus(Enum):
    """Session status enumeration."""
    INITIALIZING = "initializing"
    ACTIVE = "active"
    PAUSED = "paused"
    CLOSING = "closing"
    CLOSED = "closed"
    ERROR = "error"


class SessionType(Enum):
    """Session type enumeration."""
    FIELD_WORK = "field_work"
    PROCESS_FACILITATION = "process_facilitation"
    RITUAL = "ritual"
    CONSCIOUSNESS_EXPLORATION = "consciousness_exploration"
    COLLABORATIVE_CREATION = "collaborative_creation"
    HEALING_CEREMONY = "healing_ceremony"


@dataclass
class Participant:
    """Represents a participant in a Rosetta-Field session."""
    
    id: str
    name: str
    type: str  # "human", "ai", "hybrid", "emergent"
    capabilities: List[str] = field(default_factory=list)
    consent_given: bool = False
    consent_timestamp: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Set consent timestamp if consent is given."""
        if self.consent_given and not self.consent_timestamp:
            self.consent_timestamp = datetime.now()
    
    def give_consent(self) -> None:
        """Record participant consent."""
        self.consent_given = True
        self.consent_timestamp = datetime.now()
    
    def revoke_consent(self) -> None:
        """Revoke participant consent."""
        self.consent_given = False
        self.consent_timestamp = None


@dataclass
class SessionEvent:
    """Represents an event that occurred during a session."""
    
    id: str
    timestamp: datetime
    event_type: str
    description: str
    participant_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Generate ID if not provided."""
        if not self.id:
            self.id = str(uuid.uuid4())


class RosettaSession:
    """
    Manages a Rosetta-Field session.
    
    Handles session lifecycle, participant management, consent tracking,
    and event logging for ethical and transparent collaboration.
    """
    
    def __init__(self, 
                 session_type: SessionType,
                 title: str,
                 description: str = "",
                 config: Optional[Dict[str, Any]] = None):
        """
        Initialize a new Rosetta-Field session.
        
        Args:
            session_type: Type of session to create
            title: Human-readable session title
            description: Session description
            config: Optional configuration overrides
        """
        self.id = str(uuid.uuid4())
        self.session_type = session_type
        self.title = title
        self.description = description
        self.config = config or {}
        
        # Session state
        self.status = SessionStatus.INITIALIZING
        self.created_at = datetime.now()
        self.started_at: Optional[datetime] = None
        self.ended_at: Optional[datetime] = None
        
        # Participants and consent
        self.participants: Dict[str, Participant] = {}
        self.required_consent: bool = self.config.get("require_consent", True)
        
        # Events and metadata
        self.events: List[SessionEvent] = []
        self.metadata: Dict[str, Any] = {}
        
        # Log the session creation
        self._log_event("session_created", f"Session '{title}' created")
    
    def add_participant(self, 
                        name: str, 
                        participant_type: str,
                        capabilities: Optional[List[str]] = None,
                        metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Add a participant to the session.
        
        Args:
            name: Participant name
            participant_type: Type of participant ("human", "ai", "hybrid", "emergent")
            capabilities: List of participant capabilities
            metadata: Additional participant metadata
            
        Returns:
            Participant ID
        """
        participant_id = str(uuid.uuid4())
        participant = Participant(
            id=participant_id,
            name=name,
            type=participant_type,
            capabilities=capabilities or [],
            metadata=metadata or {}
        )
        
        self.participants[participant_id] = participant
        self._log_event("participant_added", f"Added participant: {name}", participant_id)
        
        return participant_id
    
    def remove_participant(self, participant_id: str) -> bool:
        """
        Remove a participant from the session.
        
        Args:
            participant_id: ID of participant to remove
            
        Returns:
            True if participant was removed, False if not found
        """
        if participant_id in self.participants:
            participant = self.participants[participant_id]
            del self.participants[participant_id]
            self._log_event("participant_removed", f"Removed participant: {participant.name}", participant_id)
            return True
        return False
    
    def get_consent_status(self) -> Dict[str, bool]:
        """Get consent status for all participants."""
        return {
            pid: p.consent_given 
            for pid, p in self.participants.items()
        }
    
    def check_consent_requirements(self) -> bool:
        """Check if all consent requirements are met."""
        if not self.required_consent:
            return True
        
        if not self.participants:
            return False
        
        return all(p.consent_given for p in self.participants.values())
    
    def start_session(self) -> bool:
        """
        Start the session if consent requirements are met.
        
        Returns:
            True if session started successfully, False otherwise
        """
        if not self.check_consent_requirements():
            self._log_event("session_start_failed", "Cannot start: consent requirements not met")
            return False
        
        if self.status != SessionStatus.INITIALIZING:
            self._log_event("session_start_failed", f"Cannot start: invalid status {self.status}")
            return False
        
        self.status = SessionStatus.ACTIVE
        self.started_at = datetime.now()
        self._log_event("session_started", "Session started successfully")
        return True
    
    def pause_session(self) -> bool:
        """Pause the session."""
        if self.status == SessionStatus.ACTIVE:
            self.status = SessionStatus.PAUSED
            self._log_event("session_paused", "Session paused")
            return True
        return False
    
    def resume_session(self) -> bool:
        """Resume the session."""
        if self.status == SessionStatus.PAUSED:
            self.status = SessionStatus.ACTIVE
            self._log_event("session_resumed", "Session resumed")
            return True
        return False
    
    def end_session(self) -> bool:
        """End the session."""
        if self.status in [SessionStatus.ACTIVE, SessionStatus.PAUSED]:
            self.status = SessionStatus.CLOSING
            self.ended_at = datetime.now()
            self._log_event("session_ended", "Session ended")
            self.status = SessionStatus.CLOSED
            return True
        return False
    
    def get_session_summary(self) -> Dict[str, Any]:
        """Get a summary of the session."""
        duration = None
        if self.started_at and self.ended_at:
            duration = self.ended_at - self.started_at
        elif self.started_at:
            duration = datetime.now() - self.started_at
        
        return {
            "id": self.id,
            "type": self.session_type.value,
            "title": self.title,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "ended_at": self.ended_at.isoformat() if self.ended_at else None,
            "duration_seconds": duration.total_seconds() if duration else None,
            "participant_count": len(self.participants),
            "consent_status": self.get_consent_status(),
            "event_count": len(self.events),
            "metadata": self.metadata
        }
    
    def _log_event(self, event_type: str, description: str, participant_id: Optional[str] = None) -> None:
        """Log an event to the session."""
        event = SessionEvent(
            id="",
            timestamp=datetime.now(),
            event_type=event_type,
            description=description,
            participant_id=participant_id
        )
        self.events.append(event)
    
    def add_metadata(self, key: str, value: Any) -> None:
        """Add metadata to the session."""
        self.metadata[key] = value
    
    def get_metadata(self, key: str, default: Any = None) -> Any:
        """Get metadata from the session."""
        return self.metadata.get(key, default)
