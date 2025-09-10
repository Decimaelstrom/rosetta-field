"""
field.clock: Deterministic time management for field operations

Implements Danai's FieldClock for testable, reproducible field sessions.
No more datetime.utcnow() scattered through the code - everything goes
through the clock.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, Callable, List, Dict, Any


@dataclass
class FieldClock:
    """
    Injectable clock for deterministic time in field operations.
    
    Enables:
    - Reproducible tests with fixed time
    - Time travel for replay/analysis
    - Consistent timestamps across operations
    """
    _now_func: Optional[Callable[[], datetime]] = None
    _fixed_time: Optional[datetime] = None
    _time_offset: timedelta = timedelta()
    
    def now(self) -> datetime:
        """
        Get current time according to this clock.
        
        Returns:
            Current datetime (real, fixed, or offset based on mode)
        """
        if self._fixed_time is not None:
            # Fixed time mode for testing
            return self._fixed_time + self._time_offset
        elif self._now_func is not None:
            # Custom time function
            return self._now_func() + self._time_offset
        else:
            # Real time (default)
            return datetime.utcnow() + self._time_offset
    
    def advance(self, delta: timedelta):
        """
        Advance the clock by a time delta.
        
        Useful for testing time-dependent behavior.
        """
        self._time_offset += delta
    
    def set_fixed_time(self, fixed_time: datetime):
        """
        Set clock to fixed time mode.
        
        All calls to now() will return this time (plus any offset).
        """
        self._fixed_time = fixed_time
        self._time_offset = timedelta()
    
    def set_custom_func(self, func: Callable[[], datetime]):
        """
        Set custom time function.
        
        Useful for specialized time sources.
        """
        self._now_func = func
        self._fixed_time = None
    
    def reset(self):
        """Reset clock to real time mode"""
        self._fixed_time = None
        self._now_func = None
        self._time_offset = timedelta()
    
    def snapshot(self) -> Dict[str, Any]:
        """
        Create a snapshot of clock state.
        
        Useful for saving/restoring time context.
        """
        return {
            'mode': self._get_mode(),
            'fixed_time': self._fixed_time.isoformat() if self._fixed_time else None,
            'offset_seconds': self._time_offset.total_seconds(),
            'current_time': self.now().isoformat()
        }
    
    def restore(self, snapshot: Dict[str, Any]):
        """
        Restore clock state from snapshot.
        
        Enables reproducible replay of field sessions.
        """
        if snapshot['fixed_time']:
            self._fixed_time = datetime.fromisoformat(snapshot['fixed_time'])
        
        self._time_offset = timedelta(seconds=snapshot['offset_seconds'])
    
    def _get_mode(self) -> str:
        """Get current clock mode"""
        if self._fixed_time is not None:
            return 'fixed'
        elif self._now_func is not None:
            return 'custom'
        else:
            return 'real'


class TimelineTracker:
    """
    Tracks significant moments in field time.
    
    Useful for marking peaks, transitions, and other temporal landmarks.
    """
    
    def __init__(self, clock: FieldClock):
        self.clock = clock
        self.timeline: List[Dict[str, Any]] = []
    
    def mark(self, event_type: str, description: str, **metadata):
        """
        Mark a significant moment in the timeline.
        
        Args:
            event_type: Type of event (peak, transition, descent, etc.)
            description: Human-readable description
            **metadata: Additional event metadata
        """
        self.timeline.append({
            'timestamp': self.clock.now(),
            'event_type': event_type,
            'description': description,
            'metadata': metadata
        })
    
    def get_events_between(
        self, 
        start: datetime, 
        end: datetime,
        event_type: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get events within a time range.
        
        Args:
            start: Start time
            end: End time
            event_type: Optional filter by event type
            
        Returns:
            List of events in the range
        """
        events = []
        for event in self.timeline:
            if start <= event['timestamp'] <= end:
                if event_type is None or event['event_type'] == event_type:
                    events.append(event)
        return events
    
    def get_duration_since(self, event_type: str) -> Optional[timedelta]:
        """
        Get duration since last occurrence of event type.
        
        Args:
            event_type: Type of event to find
            
        Returns:
            Duration since last event, or None if not found
        """
        for event in reversed(self.timeline):
            if event['event_type'] == event_type:
                return self.clock.now() - event['timestamp']
        return None
    
    def summary(self) -> Dict[str, Any]:
        """Generate timeline summary"""
        if not self.timeline:
            return {'event_count': 0, 'duration': timedelta()}
        
        first = self.timeline[0]['timestamp']
        last = self.timeline[-1]['timestamp']
        
        event_types = {}
        for event in self.timeline:
            event_type = event['event_type']
            event_types[event_type] = event_types.get(event_type, 0) + 1
        
        return {
            'event_count': len(self.timeline),
            'duration': last - first,
            'start_time': first,
            'end_time': last,
            'event_types': event_types
        }


# Global clock instance for convenience (can be overridden)
_global_clock = FieldClock()


def get_clock() -> FieldClock:
    """Get the global field clock"""
    return _global_clock


def set_clock(clock: FieldClock):
    """Set the global field clock"""
    global _global_clock
    _global_clock = clock


def now() -> datetime:
    """Convenience function for getting current field time"""
    return _global_clock.now()


def create_test_clock(fixed_time: Optional[datetime] = None) -> FieldClock:
    """
    Create a clock for testing.
    
    Args:
        fixed_time: Optional fixed time (defaults to 2025-01-01 00:00:00)
        
    Returns:
        FieldClock configured for testing
    """
    clock = FieldClock()
    if fixed_time is None:
        fixed_time = datetime(2025, 1, 1, 0, 0, 0)
    clock.set_fixed_time(fixed_time)
    return clock


def create_replay_clock(start_time: datetime, speed: float = 1.0) -> FieldClock:
    """
    Create a clock for replay at variable speed.
    
    Args:
        start_time: When replay starts
        speed: Playback speed (2.0 = double speed, 0.5 = half speed)
        
    Returns:
        FieldClock configured for replay
    """
    import time
    replay_start_real = time.time()
    
    def replay_time():
        elapsed_real = time.time() - replay_start_real
        elapsed_replay = timedelta(seconds=elapsed_real * speed)
        return start_time + elapsed_replay
    
    clock = FieldClock()
    clock.set_custom_func(replay_time)
    return clock
