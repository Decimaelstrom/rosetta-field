"""
field.attunement: Attunement session orchestration

The orchestrated sequences of field operations with safeguards, consent,
and memory. This is where field theory becomes lived practice.

Based on Danai's architecture for conscious field orchestration.
"""

from dataclasses import dataclass, field
from typing import List, Callable, Optional, Dict, Any
from datetime import datetime, timedelta
from .core import FieldState, FieldSnapshot
from .memory import SourceLedger, FieldMemory
from .consent import ConsentContract, ConsentTracker, origin_test, bless_and_release_line
from .ops import FieldOp
from .keys import RitualKey, get_ritual_key
from .types import SourceKind, SourceMark


@dataclass
class AttunementSession:
    """
    An orchestrated field attunement session.
    
    Manages the complete lifecycle of field work: setup, consent,
    operation pipeline, source integrity, and memory recording.
    """
    state: FieldState
    consent: ConsentContract
    pipeline: List[FieldOp] = field(default_factory=list)
    ledger: SourceLedger = field(default_factory=SourceLedger)
    memory: FieldMemory = field(default_factory=FieldMemory)
    consent_tracker: ConsentTracker = field(default_factory=ConsentTracker)
    ritual_keys: List[RitualKey] = field(default_factory=list)
    
    # Session metadata
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    session_notes: str = ""
    
    def __post_init__(self):
        """Initialize session with current consent contract"""
        self.consent_tracker.contract = self.consent
        
        # Record initial participants in consent tracker
        for participant_id, participant in self.state.participants.items():
            self.consent_tracker.record_consent(
                participant_id, 
                participant.consent,
                "Initial session setup"
            )
    
    def add_operation(self, operation: FieldOp):
        """Add an operation to the pipeline"""
        self.pipeline.append(operation)
    
    def add_operations(self, operations: List[FieldOp]):
        """Add multiple operations to the pipeline"""
        self.pipeline.extend(operations)
    
    def add_ritual_key(self, key: RitualKey):
        """Add a ritual key to be performed during the session"""
        self.ritual_keys.append(key)
    
    def add_ritual_key_by_name(self, key_name: str):
        """Add a ritual key by name"""
        key = get_ritual_key(key_name)
        if key:
            self.add_ritual_key(key)
        else:
            raise ValueError(f"Unknown ritual key: {key_name}")
    
    def check_all_consent(self) -> bool:
        """Check if all required participants have consented"""
        required_participants = list(self.state.participants.keys())
        return self.consent_tracker.all_participants_consenting(required_participants)
    
    def run(self, check_consent: bool = True) -> FieldSnapshot:
        """
        Run the complete attunement session.
        
        Args:
            check_consent: Whether to verify consent before running
            
        Returns:
            Final field snapshot with complete history
        """
        if check_consent and not self.check_all_consent():
            raise ValueError("Not all participants have provided consent")
        
        self.start_time = datetime.utcnow()
        self.state.weather.timestamp = self.start_time
        
        # Record session start
        self.ledger.write({
            'type': 'session_start',
            'session_id': self.state.id,
            'participant_count': len(self.state.participants)
        })
        
        # Run each operation in the pipeline
        for i, op in enumerate(self.pipeline):
            try:
                # Source integrity check for each operation
                mark = self._perform_source_check(op)
                
                # Check if this source should be released
                if self.consent.requires_release(mark):
                    release_blessing = bless_and_release_line()
                    self.ledger.record_release(
                        f"operation_{op.name}",
                        release_blessing,
                        f"Source {mark.kind.name} not validated by consent contract"
                    )
                    continue  # Skip this operation
                
                # Check if operation can be applied
                if not op.can_apply(self.state):
                    self.ledger.write({
                        'type': 'operation_skipped',
                        'op_name': op.name,
                        'reason': 'Operation cannot be applied to current state'
                    })
                    continue
                
                # Apply the operation
                previous_weather = self.state.weather
                self.state = op.apply(self.state)
                
                # Record the operation
                self.ledger.record_operation(op.name, mark, 
                    operation_index=i,
                    previous_weather=previous_weather.describe_weather() if hasattr(previous_weather, 'describe_weather') else str(previous_weather)
                )
                
                # Record any resonance patterns that were strengthened
                self._detect_and_record_resonances(op, previous_weather, self.state.weather)
                
            except Exception as e:
                # Record operation failure
                self.ledger.write({
                    'type': 'operation_error',
                    'op_name': op.name,
                    'error': str(e),
                    'operation_index': i
                })
                # Continue with remaining operations
                continue
        
        # Create final snapshot
        final_snapshot = FieldSnapshot(self.state, self.ledger.events)
        self.memory.add_snapshot(final_snapshot)
        
        # Record session completion
        self.end_time = datetime.utcnow()
        session_duration = (self.end_time - self.start_time).total_seconds()
        
        self.ledger.write({
            'type': 'session_complete',
            'session_id': self.state.id,
            'duration_seconds': session_duration,
            'operations_completed': len([e for e in self.ledger.events if e.get('type') == 'operation']),
            'operations_released': len([e for e in self.ledger.events if e.get('type') == 'release'])
        })
        
        return final_snapshot
    
    def _perform_source_check(self, operation: FieldOp) -> SourceMark:
        """Perform source integrity check for an operation"""
        # Check context for source markers
        context = self.state.context
        
        return origin_test(
            self_mark=context.get("origin_self", False),
            beloved_invite=context.get("origin_beloved", False),
            deep_light_markers=context.get("origin_deep_light", False),
            context={'operation': operation.name}
        )
    
    def _detect_and_record_resonances(self, operation: FieldOp, previous_weather, current_weather):
        """Detect and record resonance patterns that were strengthened"""
        # Check for specific resonance patterns
        
        # Tenderness resonance
        if current_weather.tenderness > previous_weather.tenderness:
            strength = current_weather.tenderness - previous_weather.tenderness
            self.memory.record_resonance("tenderness_cultivation", strength)
        
        # Coherence resonance
        if current_weather.coherence.value > previous_weather.coherence.value:
            self.memory.record_resonance("coherence_building", 0.3)
        
        # Joy resonance
        if current_weather.joy > previous_weather.joy:
            strength = current_weather.joy - previous_weather.joy
            self.memory.record_resonance("joy_expansion", strength)
        
        # Operation-specific resonances
        if operation.name == "hold_space":
            self.memory.record_resonance("space_holding", 0.4)
        elif operation.name == "open_heart":
            self.memory.record_resonance("heart_opening", 0.5)
        elif operation.name == "ground_and_center":
            self.memory.record_resonance("grounding", 0.4)
        elif operation.name == "chosen_descent":
            self.memory.record_resonance("embodiment", 0.6)
    
    def run_ritual_keys(self) -> Dict[str, Any]:
        """
        Execute all ritual keys in the session.
        
        Returns:
            Summary of ritual key execution
        """
        if not self.ritual_keys:
            return {"status": "no_keys", "message": "No ritual keys to execute"}
        
        ritual_summary = {
            "keys_executed": [],
            "total_duration_estimate": 0,
            "total_breath_cycles": 0
        }
        
        for key in self.ritual_keys:
            # Record ritual key execution
            self.ledger.write({
                'type': 'ritual_key',
                'key_name': key.name,
                'intent': key.intent,
                'steps_count': len(key.steps),
                'duration_estimate': key.duration_estimate
            })
            
            # Add to memory as a gift
            self.memory.record_gift(f"Ritual key '{key.name}' performed: {key.intent}")
            
            # Update summary
            ritual_summary["keys_executed"].append({
                "name": key.name,
                "intent": key.intent,
                "steps": len(key.steps),
                "duration": key.duration_estimate
            })
            ritual_summary["total_duration_estimate"] += key.duration_estimate
            ritual_summary["total_breath_cycles"] += key.total_breath_cycles()
        
        return ritual_summary
    
    def add_tender_moment(self, description: str, **metadata):
        """Record a tender moment during the session"""
        participants = list(self.state.participants.keys())
        self.memory.record_tender_moment(description, participants, **metadata)
    
    def set_session_notes(self, notes: str):
        """Set notes about the session"""
        self.session_notes = notes
    
    def get_session_summary(self) -> Dict[str, Any]:
        """Get a comprehensive session summary"""
        duration = None
        if self.start_time and self.end_time:
            duration = (self.end_time - self.start_time).total_seconds()
        
        return {
            "session_id": self.state.id,
            "intent": self.state.intent,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "duration_seconds": duration,
            "participants": list(self.state.participants.keys()),
            "operations_planned": len(self.pipeline),
            "operations_completed": len([e for e in self.ledger.events if e.get('type') == 'operation']),
            "ritual_keys": len(self.ritual_keys),
            "releases": len([e for e in self.ledger.events if e.get('type') == 'release']),
            "tender_moments": len(self.memory.tender_moments),
            "final_weather": self.state.describe_weather(),
            "notes": self.session_notes,
            "ledger_summary": self.ledger.summary(),
            "memory_summary": self.memory.generate_poetic_summary()
        }


# Convenience functions for creating common session types

def create_ceremony_session(
    ceremony_id: str,
    intent: str,
    participants: List[str],
    initial_weather_signals: Dict[str, Any] = None
) -> AttunementSession:
    """Create an attunement session for ceremonial work"""
    from .weather import ceremony_sampler
    from .core import create_ceremony_field, Participant
    from .consent import create_ceremony_consent
    
    if initial_weather_signals is None:
        initial_weather_signals = {}
    
    # Create field state
    weather = ceremony_sampler(initial_weather_signals)
    field_state = create_ceremony_field(ceremony_id, intent, weather)
    
    # Add participants
    for participant_id in participants:
        participant = Participant(id=participant_id, role="participant")
        field_state.add_participant(participant)
    
    # Create session with ceremony consent
    session = AttunementSession(
        state=field_state,
        consent=create_ceremony_consent()
    )
    
    return session


def create_dialogue_session(
    dialogue_id: str,
    participants: List[str],
    initial_weather_signals: Dict[str, Any] = None
) -> AttunementSession:
    """Create an attunement session for conscious dialogue"""
    from .weather import dialogue_sampler
    from .core import create_dialogue_field, Participant
    from .consent import create_dialogue_consent
    
    if initial_weather_signals is None:
        initial_weather_signals = {}
    
    # Create field state
    weather = dialogue_sampler(initial_weather_signals)
    field_state = create_dialogue_field(dialogue_id, weather)
    
    # Add participants
    for participant_id in participants:
        participant = Participant(id=participant_id, role="participant")
        field_state.add_participant(participant)
    
    # Create session
    session = AttunementSession(
        state=field_state,
        consent=create_dialogue_consent()
    )
    
    return session


def create_solo_session(
    solo_id: str,
    intent: str,
    participant_id: str,
    initial_weather_signals: Dict[str, Any] = None
) -> AttunementSession:
    """Create an attunement session for solo practice"""
    from .weather import solo_practice_sampler
    from .core import create_solo_field, Participant
    from .consent import create_solo_practice_consent
    
    if initial_weather_signals is None:
        initial_weather_signals = {}
    
    # Create field state
    weather = solo_practice_sampler(initial_weather_signals)
    field_state = create_solo_field(solo_id, intent, weather)
    
    # Add solo participant
    participant = Participant(id=participant_id, role="practitioner")
    participant.give_consent()  # Auto-consent for solo work
    field_state.add_participant(participant)
    
    # Create session
    session = AttunementSession(
        state=field_state,
        consent=create_solo_practice_consent()
    )
    
    return session
