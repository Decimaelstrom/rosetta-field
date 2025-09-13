"""
field.bus: Event bus for field instrumentation and UI hooks

Implements Danai's FieldBus for observable field events, enabling
instrumentation, real-time visualization, and reactive patterns.

"Add a tiny FieldBus for instrumentation and UI" - this makes field
dynamics visible and interactive.
"""

from dataclasses import dataclass, field
from typing import Callable, Dict, Any, List, Optional
from enum import Enum, auto


class FieldEvent(Enum):
    """Types of field events that can be observed"""
    # Core field events
    FIELD_CREATED = auto()
    FIELD_UPDATED = auto()
    FIELD_SNAPSHOT = auto()
    
    # Operation events
    OP_STARTED = auto()
    OP_COMPLETED = auto()
    OP_FAILED = auto()
    OP_SKIPPED = auto()
    
    # Source integrity events
    ORIGIN_CHECK = auto()
    SOURCE_VALIDATED = auto()
    SOURCE_RELEASED = auto()
    
    # Consent events
    CONSENT_REQUESTED = auto()
    CONSENT_GRANTED = auto()
    CONSENT_DENIED = auto()
    CONSENT_WITHDRAWN = auto()
    
    # Field dynamics events
    PEAK_MOMENT = auto()
    DESCENT_STARTED = auto()
    DESCENT_COMPLETED = auto()
    RELEASE_PERFORMED = auto()
    
    # Weather events
    WEATHER_SHIFTED = auto()
    COHERENCE_CHANGED = auto()
    TENDERNESS_PEAK = auto()
    JOY_PEAK = auto()
    
    # Ritual events
    RITUAL_STARTED = auto()
    RITUAL_STEP = auto()
    RITUAL_COMPLETED = auto()
    
    # Harmonic events
    RESONANCE_DETECTED = auto()
    STILLNESS_EMERGED = auto()
    FIELDS_COUPLED = auto()
    
    # Session events
    SESSION_STARTED = auto()
    SESSION_PAUSED = auto()
    SESSION_RESUMED = auto()
    SESSION_COMPLETED = auto()


@dataclass
class EventData:
    """Data associated with a field event"""
    event_type: FieldEvent
    timestamp: Any  # Will use FieldClock.now()
    source: str  # What generated this event
    data: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def describe(self) -> str:
        """Generate human-readable description"""
        return f"{self.event_type.name} from {self.source} at {self.timestamp}"


# Type alias for event handlers
EventHandler = Callable[[EventData], None]


class FieldBus:
    """
    Event bus for field operations and dynamics.
    
    Enables:
    - Real-time monitoring of field state
    - UI updates and visualizations
    - Analytics and instrumentation
    - Reactive patterns and side effects
    """
    
    def __init__(self):
        self.handlers: Dict[FieldEvent, List[EventHandler]] = {}
        self.event_history: List[EventData] = []
        self.is_recording: bool = True
        self.max_history: int = 1000
    
    def on(self, event_type: FieldEvent, handler: EventHandler):
        """
        Register a handler for an event type.
        
        Args:
            event_type: Type of event to handle
            handler: Function to call when event occurs
        """
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)
    
    def off(self, event_type: FieldEvent, handler: EventHandler):
        """
        Unregister a handler.
        
        Args:
            event_type: Event type
            handler: Handler to remove
        """
        if event_type in self.handlers:
            if handler in self.handlers[event_type]:
                self.handlers[event_type].remove(handler)
    
    def emit(self, event_type: FieldEvent, source: str, **data):
        """
        Emit an event to all registered handlers.
        
        Args:
            event_type: Type of event
            source: What generated this event
            **data: Event data and metadata
        """
        # Import here to avoid circular dependency
        from .clock import get_clock
        
        # Create event data
        event = EventData(
            event_type=event_type,
            timestamp=get_clock().now(),
            source=source,
            data=data,
            metadata={'sequence': len(self.event_history)}
        )
        
        # Record if enabled
        if self.is_recording:
            self.event_history.append(event)
            # Trim history if too long
            if len(self.event_history) > self.max_history:
                self.event_history = self.event_history[-self.max_history:]
        
        # Call handlers
        if event_type in self.handlers:
            for handler in self.handlers[event_type]:
                try:
                    handler(event)
                except Exception as e:
                    # Log but don't crash on handler errors
                    print(f"Handler error for {event_type.name}: {e}")
    
    def on_origin_check(self, handler: EventHandler):
        """Convenience method for origin check events"""
        self.on(FieldEvent.ORIGIN_CHECK, handler)
    
    def on_peak(self, handler: EventHandler):
        """Convenience method for peak moment events"""
        self.on(FieldEvent.PEAK_MOMENT, handler)
    
    def on_descent(self, handler: EventHandler):
        """Convenience method for descent events"""
        self.on(FieldEvent.DESCENT_STARTED, handler)
        self.on(FieldEvent.DESCENT_COMPLETED, handler)
    
    def on_release(self, handler: EventHandler):
        """Convenience method for release events"""
        self.on(FieldEvent.RELEASE_PERFORMED, handler)
        self.on(FieldEvent.SOURCE_RELEASED, handler)
    
    def get_recent_events(
        self, 
        count: int = 10,
        event_type: Optional[FieldEvent] = None
    ) -> List[EventData]:
        """
        Get recent events from history.
        
        Args:
            count: Number of events to return
            event_type: Optional filter by type
            
        Returns:
            List of recent events
        """
        if event_type is None:
            return self.event_history[-count:]
        
        filtered = [e for e in self.event_history if e.event_type == event_type]
        return filtered[-count:]
    
    def clear_history(self):
        """Clear event history"""
        self.event_history = []
    
    def pause_recording(self):
        """Pause event recording"""
        self.is_recording = False
    
    def resume_recording(self):
        """Resume event recording"""
        self.is_recording = True
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get event statistics"""
        stats = {
            'total_events': len(self.event_history),
            'event_types': {},
            'sources': {},
            'handlers_registered': sum(len(h) for h in self.handlers.values())
        }
        
        for event in self.event_history:
            # Count by type
            event_name = event.event_type.name
            stats['event_types'][event_name] = stats['event_types'].get(event_name, 0) + 1
            
            # Count by source
            stats['sources'][event.source] = stats['sources'].get(event.source, 0) + 1
        
        return stats


class ConsoleLogger:
    """
    Simple console logger for field events.
    
    Useful for debugging and development.
    """
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
    
    def log_event(self, event: EventData):
        """Log an event to console"""
        if self.verbose:
            print(f"[{event.timestamp}] {event.event_type.name} from {event.source}")
            if event.data:
                print(f"  Data: {event.data}")
        else:
            # Simplified logging for key events
            if event.event_type in [
                FieldEvent.PEAK_MOMENT,
                FieldEvent.DESCENT_STARTED,
                FieldEvent.RELEASE_PERFORMED,
                FieldEvent.RESONANCE_DETECTED,
                FieldEvent.STILLNESS_EMERGED
            ]:
                print(f"✨ {event.event_type.name}: {event.data.get('description', '')}")


class MetricsCollector:
    """
    Collects metrics from field events.
    
    Useful for analytics and performance monitoring.
    """
    
    def __init__(self):
        self.metrics = {
            'operations_completed': 0,
            'operations_failed': 0,
            'operations_skipped': 0,
            'sources_validated': 0,
            'sources_released': 0,
            'consent_granted': 0,
            'consent_denied': 0,
            'peak_moments': 0,
            'descents': 0,
            'releases': 0,
            'resonances': 0,
            'stillnesses': 0
        }
    
    def collect_event(self, event: EventData):
        """Collect metrics from an event"""
        metric_map = {
            FieldEvent.OP_COMPLETED: 'operations_completed',
            FieldEvent.OP_FAILED: 'operations_failed',
            FieldEvent.OP_SKIPPED: 'operations_skipped',
            FieldEvent.SOURCE_VALIDATED: 'sources_validated',
            FieldEvent.SOURCE_RELEASED: 'sources_released',
            FieldEvent.CONSENT_GRANTED: 'consent_granted',
            FieldEvent.CONSENT_DENIED: 'consent_denied',
            FieldEvent.PEAK_MOMENT: 'peak_moments',
            FieldEvent.DESCENT_COMPLETED: 'descents',
            FieldEvent.RELEASE_PERFORMED: 'releases',
            FieldEvent.RESONANCE_DETECTED: 'resonances',
            FieldEvent.STILLNESS_EMERGED: 'stillnesses'
        }
        
        metric_key = metric_map.get(event.event_type)
        if metric_key:
            self.metrics[metric_key] += 1
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current metrics"""
        return self.metrics.copy()
    
    def reset(self):
        """Reset all metrics"""
        for key in self.metrics:
            self.metrics[key] = 0


# Global bus instance
_global_bus = FieldBus()


def get_bus() -> FieldBus:
    """Get the global field bus"""
    return _global_bus


def set_bus(bus: FieldBus):
    """Set the global field bus"""
    global _global_bus
    _global_bus = bus


def emit(event_type: FieldEvent, source: str, **data):
    """Convenience function for emitting events"""
    _global_bus.emit(event_type, source, **data)


# Convenience functions for common event patterns

def emit_origin_check(source_kind: str, confidence: float, result: bool):
    """Emit an origin check event"""
    emit(
        FieldEvent.ORIGIN_CHECK,
        'origin_test',
        source_kind=source_kind,
        confidence=confidence,
        validated=result
    )


def emit_peak_moment(description: str, intensity: float):
    """Emit a peak moment event"""
    emit(
        FieldEvent.PEAK_MOMENT,
        'field_dynamics',
        description=description,
        intensity=intensity
    )


def emit_descent(started: bool, depth: float = 0.0):
    """Emit a descent event"""
    event_type = FieldEvent.DESCENT_STARTED if started else FieldEvent.DESCENT_COMPLETED
    emit(
        event_type,
        'field_dynamics',
        depth=depth
    )


def emit_release(target: str, blessing: str):
    """Emit a release event"""
    emit(
        FieldEvent.RELEASE_PERFORMED,
        'field_operations',
        target=target,
        blessing=blessing
    )
