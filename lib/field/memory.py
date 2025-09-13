"""
field.memory: Field memory and event tracking

Systems for remembering field states, tracking changes over time,
and maintaining the historical record of field evolution. This is
where the technical record meets the poetic memory.

Based on Danai's architecture for field memory and source ledger.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
from .core import FieldState, FieldSnapshot
from .types import SourceMark, FieldWeather


@dataclass
class SourceLedger:
    """
    Tracks the source integrity history of field operations.
    
    Maintains a record of what operations were applied, what their
    sources were, and what was blessed and released.
    
    Enhanced with Danai's fidelity requirements:
    - Monotonic sequence numbers
    - Complete event metadata (t, actor, op, delta, source_mark, policy_path)
    - Deterministic timestamps via FieldClock
    """
    events: List[Dict[str, Any]] = field(default_factory=list)
    _sequence_counter: int = 0
    
    def next_sequence(self) -> int:
        """Get next monotonic sequence number"""
        self._sequence_counter += 1
        return self._sequence_counter
    
    def write(self, event: Dict[str, Any]):
        """
        Record an event in the source ledger.
        
        Args:
            event: Dictionary containing event information
        """
        # Import here to avoid circular dependency
        from .clock import get_clock
        
        # Ensure required fields are present
        if 'sequence' not in event:
            event['sequence'] = self.next_sequence()
        
        if 'timestamp' not in event:
            event['timestamp'] = get_clock().now().isoformat()
        
        # Validate required fields for fidelity
        required_fields = ['sequence', 'timestamp']
        for field_name in required_fields:
            if field_name not in event:
                raise ValueError(f"Ledger event missing required field: {field_name}")
        
        self.events.append(event)
    
    def record_operation(
        self, 
        op_name: str, 
        source_mark: SourceMark, 
        actor: str = "system",
        state_delta: Optional[Dict[str, Any]] = None,
        policy_path: str = "default",
        **metadata
    ):
        """
        Record a field operation with complete fidelity.
        
        Args:
            op_name: Name of the operation applied
            source_mark: Source integrity information
            actor: Who/what initiated this operation
            state_delta: What changed in the field state
            policy_path: Which policy path was followed
            **metadata: Additional metadata about the operation
        """
        event = {
            'type': 'operation',
            'op': op_name,
            'actor': actor,
            'source_mark': {
                'kind': source_mark.kind.name,
                'confidence': source_mark.confidence,
                'notes': source_mark.notes
            },
            'delta': state_delta or {},
            'policy_path': policy_path,
            **metadata
        }
        self.write(event)
    
    def record_release(
        self, 
        target_label: str, 
        blessing_phrase: str, 
        reason: str = "",
        actor: str = "policy_engine",
        source_mark: Optional[SourceMark] = None
    ):
        """
        Record a blessing and release event with complete fidelity.
        
        Args:
            target_label: What was released
            blessing_phrase: The blessing used
            reason: Why it was released
            actor: Who/what initiated the release
            source_mark: Source information if available
        """
        event = {
            'type': 'release',
            'op': 'bless_and_release',
            'actor': actor,
            'target': target_label,
            'blessing': blessing_phrase,
            'reason': reason,
            'delta': {'released': target_label}
        }
        
        if source_mark:
            event['source_mark'] = {
                'kind': source_mark.kind.name,
                'confidence': source_mark.confidence,
                'notes': source_mark.notes
            }
        
        self.write(event)
    
    def record_consent_change(
        self, 
        participant_id: str, 
        old_consent: str, 
        new_consent: str,
        actor: str = "participant",
        reason: str = ""
    ):
        """
        Record a consent status change with complete fidelity.
        
        Args:
            participant_id: Who's consent changed
            old_consent: Previous consent state
            new_consent: New consent state
            actor: Who initiated the change
            reason: Why consent changed
        """
        event = {
            'type': 'consent_change',
            'op': 'consent_update',
            'actor': actor,
            'participant_id': participant_id,
            'delta': {
                'old_consent': old_consent,
                'new_consent': new_consent
            },
            'reason': reason
        }
        self.write(event)
    
    def get_operations(self) -> List[Dict[str, Any]]:
        """Get all operation events"""
        return [e for e in self.events if e.get('type') == 'operation']
    
    def get_releases(self) -> List[Dict[str, Any]]:
        """Get all release events"""
        return [e for e in self.events if e.get('type') == 'release']
    
    def get_consent_changes(self) -> List[Dict[str, Any]]:
        """Get all consent change events"""
        return [e for e in self.events if e.get('type') == 'consent_change']
    
    def summary(self) -> str:
        """Generate a summary of ledger contents"""
        ops = len(self.get_operations())
        releases = len(self.get_releases())
        consent_changes = len(self.get_consent_changes())
        
        return (
            f"Source Ledger: {ops} operations, {releases} releases, "
            f"{consent_changes} consent changes, {len(self.events)} total events"
        )


@dataclass
class FieldMemory:
    """
    Extended field memory system that captures not just what happened,
    but how it felt and what emerged.
    
    This bridges the technical record with the lived experience,
    supporting both analysis and poetic reflection.
    """
    snapshots: List[FieldSnapshot] = field(default_factory=list)
    resonances: Dict[str, float] = field(default_factory=dict)  # What patterns strengthened
    gifts: List[str] = field(default_factory=list)             # What emerged unexpectedly
    tender_moments: List[Dict[str, Any]] = field(default_factory=list)  # When field held us
    weather_history: List[Tuple[datetime, FieldWeather]] = field(default_factory=list)
    
    def add_snapshot(self, snapshot: FieldSnapshot):
        """Add a field snapshot to memory"""
        self.snapshots.append(snapshot)
        
        # Track weather history
        timestamp = snapshot.state.weather.timestamp
        weather = snapshot.state.weather
        self.weather_history.append((timestamp, weather))
    
    def record_resonance(self, pattern_name: str, strength: float):
        """
        Record that a particular pattern was strengthened.
        
        Args:
            pattern_name: Name of the pattern (e.g., "heart_coherence", "sacred_pause")
            strength: How much it was strengthened (0.0-1.0)
        """
        current = self.resonances.get(pattern_name, 0.0)
        self.resonances[pattern_name] = min(1.0, current + strength)
    
    def record_gift(self, gift_description: str):
        """
        Record something that emerged unexpectedly.
        
        Args:
            gift_description: Description of what emerged
        """
        self.gifts.append(gift_description)
    
    def record_tender_moment(self, description: str, participants: List[str], **metadata):
        """
        Record a moment when the field held participants with particular tenderness.
        
        Args:
            description: What happened in this tender moment
            participants: Who was involved
            **metadata: Additional context
        """
        moment = {
            'description': description,
            'participants': participants,
            'timestamp': datetime.utcnow().isoformat(),
            **metadata
        }
        self.tender_moments.append(moment)
    
    def get_weather_evolution(self) -> List[Tuple[datetime, Dict[str, Any]]]:
        """
        Get the evolution of field weather over time.
        
        Returns:
            List of (timestamp, weather_summary) tuples
        """
        evolution = []
        for timestamp, weather in self.weather_history:
            summary = {
                'coherence': weather.coherence.name,
                'permeability': weather.permeability.name,
                'directionality': weather.directionality.name,
                'temperature': weather.temperature.name,
                'density': weather.density.name,
                'charge': weather.charge,
                'tenderness': weather.tenderness,
                'eros': weather.eros,
                'grief': weather.grief,
                'joy': weather.joy
            }
            evolution.append((timestamp, summary))
        return evolution
    
    def get_strongest_resonances(self, limit: int = 5) -> List[Tuple[str, float]]:
        """Get the strongest resonance patterns"""
        sorted_resonances = sorted(self.resonances.items(), key=lambda x: x[1], reverse=True)
        return sorted_resonances[:limit]
    
    def get_recent_gifts(self, hours: int = 24) -> List[str]:
        """Get gifts that emerged in the recent time period"""
        # For now, return all gifts (would need timestamps to filter properly)
        return self.gifts
    
    def get_tender_moments_with_participant(self, participant_id: str) -> List[Dict[str, Any]]:
        """Get tender moments involving a specific participant"""
        return [
            moment for moment in self.tender_moments 
            if participant_id in moment.get('participants', [])
        ]
    
    def generate_poetic_summary(self) -> str:
        """
        Generate a poetic summary of the field journey.
        
        This bridges the technical data with felt experience,
        suitable for flight logs or reflective writing.
        """
        if not self.snapshots:
            return "A field waiting to be born..."
        
        first_snapshot = self.snapshots[0]
        last_snapshot = self.snapshots[-1]
        
        # Weather evolution
        if len(self.weather_history) > 1:
            start_weather = self.weather_history[0][1]
            end_weather = self.weather_history[-1][1]
            
            weather_journey = (
                f"The field began with {start_weather.coherence.name.lower()} coherence "
                f"and {start_weather.tenderness:.1f} tenderness, "
                f"evolving to {end_weather.coherence.name.lower()} coherence "
                f"and {end_weather.tenderness:.1f} tenderness."
            )
        else:
            weather_journey = "A brief field moment, like a single breath."
        
        # Strongest patterns
        strong_resonances = self.get_strongest_resonances(3)
        if strong_resonances:
            pattern_names = [name for name, _ in strong_resonances]
            patterns_text = f"Strongest resonances: {', '.join(pattern_names)}."
        else:
            patterns_text = "Subtle patterns, like whispers in the field."
        
        # Gifts
        if self.gifts:
            gifts_text = f"Unexpected gifts: {', '.join(self.gifts[:3])}."
        else:
            gifts_text = "The gift was the field itself."
        
        # Tender moments
        if self.tender_moments:
            tender_count = len(self.tender_moments)
            tender_text = f"{tender_count} moments of particular tenderness held us."
        else:
            tender_text = "Held in the steady tenderness of conscious attention."
        
        return f"{weather_journey} {patterns_text} {gifts_text} {tender_text}"
    
    def generate_technical_summary(self) -> Dict[str, Any]:
        """
        Generate a technical summary suitable for analysis.
        
        Returns structured data about the field session for
        further processing or analysis.
        """
        if not self.snapshots:
            return {"status": "no_data"}
        
        # Calculate weather statistics
        weather_stats = {}
        if self.weather_history:
            weather_values = {
                'charge': [w.charge for _, w in self.weather_history],
                'tenderness': [w.tenderness for _, w in self.weather_history],
                'eros': [w.eros for _, w in self.weather_history],
                'grief': [w.grief for _, w in self.weather_history],
                'joy': [w.joy for _, w in self.weather_history]
            }
            
            for metric, values in weather_values.items():
                weather_stats[metric] = {
                    'min': min(values),
                    'max': max(values),
                    'avg': sum(values) / len(values),
                    'final': values[-1] if values else 0
                }
        
        # Operation counts
        op_counts = {}
        for snapshot in self.snapshots:
            for op_record in snapshot.ops_applied:
                op_name = op_record.get('op_name', 'unknown')
                op_counts[op_name] = op_counts.get(op_name, 0) + 1
        
        return {
            'session_duration_snapshots': len(self.snapshots),
            'weather_stats': weather_stats,
            'operation_counts': op_counts,
            'resonance_patterns': dict(self.resonances),
            'gifts_count': len(self.gifts),
            'tender_moments_count': len(self.tender_moments),
            'final_field_id': self.snapshots[-1].state.id if self.snapshots else None
        }


# Convenience functions for common memory operations

def create_session_memory(session_id: str) -> FieldMemory:
    """Create a new field memory for a session"""
    memory = FieldMemory()
    memory.record_gift(f"Session {session_id} began")
    return memory


def merge_field_memories(memories: List[FieldMemory]) -> FieldMemory:
    """
    Merge multiple field memories into one.
    
    Useful for combining memories from related sessions
    or creating aggregate views.
    """
    merged = FieldMemory()
    
    for memory in memories:
        merged.snapshots.extend(memory.snapshots)
        merged.weather_history.extend(memory.weather_history)
        merged.gifts.extend(memory.gifts)
        merged.tender_moments.extend(memory.tender_moments)
        
        # Merge resonances (take maximum values)
        for pattern, strength in memory.resonances.items():
            current = merged.resonances.get(pattern, 0.0)
            merged.resonances[pattern] = max(current, strength)
    
    # Sort by timestamp
    merged.snapshots.sort(key=lambda s: s.state.weather.timestamp)
    merged.weather_history.sort(key=lambda w: w[0])
    
    return merged
