"""
field.serialization: JSON-serializable snapshots with versioning

Implements Danai's requirement for stable, versioned, forward-compatible
field snapshots that can be safely stored and transmitted.

"JSON-serializable, stable, and versioned with forward-compat reserved fields"
"""

import json
from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional, List
from datetime import datetime
from enum import Enum
from .core import FieldState, FieldSnapshot, Participant, Anchor
from .types import FieldWeather, SourceMark, ConsentState, SourceKind
from .memory import FieldMemory, SourceLedger


# Current schema version - increment when making breaking changes
CURRENT_SCHEMA_VERSION = "1.0.0"


class SerializationError(Exception):
    """Raised when serialization/deserialization fails"""
    pass


@dataclass
class SerializableSnapshot:
    """
    A field snapshot that can be safely serialized to JSON.
    
    Includes schema versioning and forward-compatibility reserved fields
    for safe evolution over time.
    """
    schema_version: str
    snapshot_id: str
    timestamp: str  # ISO format
    field_state: Dict[str, Any]
    ledger_events: List[Dict[str, Any]]
    memory_summary: Dict[str, Any]
    
    # Forward compatibility reserved fields
    reserved_1: Optional[Dict[str, Any]] = None
    reserved_2: Optional[Dict[str, Any]] = None
    reserved_3: Optional[str] = None
    
    def to_json(self) -> str:
        """Serialize to JSON string"""
        return json.dumps(asdict(self), indent=2, default=str)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'SerializableSnapshot':
        """Deserialize from JSON string"""
        try:
            data = json.loads(json_str)
            return cls(**data)
        except (json.JSONDecodeError, TypeError) as e:
            raise SerializationError(f"Failed to deserialize snapshot: {e}")
    
    def is_compatible_version(self) -> bool:
        """Check if this snapshot version is compatible with current code"""
        # Simple version compatibility check
        # In practice, you might want more sophisticated semver logic
        major_version = self.schema_version.split('.')[0]
        current_major = CURRENT_SCHEMA_VERSION.split('.')[0]
        return major_version == current_major


def serialize_field_weather(weather: FieldWeather) -> Dict[str, Any]:
    """Serialize FieldWeather to JSON-compatible dict"""
    return {
        'coherence': weather.coherence.name,
        'permeability': weather.permeability.name,
        'directionality': weather.directionality.name,
        'temperature': weather.temperature.name,
        'density': weather.density.name,
        'charge': weather.charge,
        'tenderness': weather.tenderness,
        'eros': weather.eros,
        'grief': weather.grief,
        'joy': weather.joy,
        'timestamp': weather.timestamp.isoformat()
    }


def deserialize_field_weather(data: Dict[str, Any]) -> FieldWeather:
    """Deserialize FieldWeather from JSON-compatible dict"""
    from .types import Coherence, Permeability, Directionality, Temperature, Density
    
    return FieldWeather(
        coherence=Coherence[data['coherence']],
        permeability=Permeability[data['permeability']],
        directionality=Directionality[data['directionality']],
        temperature=Temperature[data['temperature']],
        density=Density[data['density']],
        charge=data['charge'],
        tenderness=data['tenderness'],
        eros=data['eros'],
        grief=data['grief'],
        joy=data['joy'],
        timestamp=datetime.fromisoformat(data['timestamp'])
    )


def serialize_participant(participant: Participant) -> Dict[str, Any]:
    """Serialize Participant to JSON-compatible dict"""
    return {
        'id': participant.id,
        'role': participant.role,
        'consent': participant.consent.name,
        'attributes': participant.attributes
    }


def deserialize_participant(data: Dict[str, Any]) -> Participant:
    """Deserialize Participant from JSON-compatible dict"""
    participant = Participant(
        id=data['id'],
        role=data['role'],
        consent=ConsentState[data['consent']],
        attributes=data.get('attributes', {})
    )
    return participant


def serialize_anchor(anchor: Anchor) -> Dict[str, Any]:
    """Serialize Anchor to JSON-compatible dict"""
    return {
        'name': anchor.name,
        'kind': anchor.kind,
        'data': anchor.data
    }


def deserialize_anchor(data: Dict[str, Any]) -> Anchor:
    """Deserialize Anchor from JSON-compatible dict"""
    return Anchor(
        name=data['name'],
        kind=data['kind'],
        data=data.get('data', {})
    )


def serialize_source_mark(source_mark: Optional[SourceMark]) -> Optional[Dict[str, Any]]:
    """Serialize SourceMark to JSON-compatible dict"""
    if source_mark is None:
        return None
    
    return {
        'kind': source_mark.kind.name,
        'confidence': source_mark.confidence,
        'notes': source_mark.notes
    }


def deserialize_source_mark(data: Optional[Dict[str, Any]]) -> Optional[SourceMark]:
    """Deserialize SourceMark from JSON-compatible dict"""
    if data is None:
        return None
    
    return SourceMark(
        kind=SourceKind[data['kind']],
        confidence=data['confidence'],
        notes=data.get('notes')
    )


def serialize_field_state(state: FieldState) -> Dict[str, Any]:
    """Serialize FieldState to JSON-compatible dict"""
    return {
        'id': state.id,
        'intent': state.intent,
        'weather': serialize_field_weather(state.weather),
        'participants': {
            pid: serialize_participant(p) for pid, p in state.participants.items()
        },
        'anchors': {
            name: serialize_anchor(a) for name, a in state.anchors.items()
        },
        'tags': list(state.tags),
        'context': state.context,
        'source_mark': serialize_source_mark(state.source_mark)
    }


def deserialize_field_state(data: Dict[str, Any]) -> FieldState:
    """Deserialize FieldState from JSON-compatible dict"""
    participants = {
        pid: deserialize_participant(p_data) 
        for pid, p_data in data.get('participants', {}).items()
    }
    
    anchors = {
        name: deserialize_anchor(a_data)
        for name, a_data in data.get('anchors', {}).items()
    }
    
    return FieldState(
        id=data['id'],
        intent=data['intent'],
        weather=deserialize_field_weather(data['weather']),
        participants=participants,
        anchors=anchors,
        tags=tuple(data.get('tags', [])),
        context=data.get('context', {}),
        source_mark=deserialize_source_mark(data.get('source_mark'))
    )


def serialize_field_snapshot(snapshot: FieldSnapshot) -> SerializableSnapshot:
    """
    Serialize a FieldSnapshot to a version-stable, JSON-compatible format.
    
    Args:
        snapshot: The FieldSnapshot to serialize
        
    Returns:
        SerializableSnapshot ready for JSON serialization
    """
    from .clock import get_clock
    
    # Generate unique snapshot ID
    snapshot_id = f"{snapshot.state.id}_{len(snapshot.ops_applied)}_{get_clock().now().isoformat()}"
    
    return SerializableSnapshot(
        schema_version=CURRENT_SCHEMA_VERSION,
        snapshot_id=snapshot_id,
        timestamp=get_clock().now().isoformat(),
        field_state=serialize_field_state(snapshot.state),
        ledger_events=snapshot.ops_applied,
        memory_summary={
            'snapshot_count': 1,
            'ops_applied': len(snapshot.ops_applied)
        }
    )


def deserialize_field_snapshot(serializable: SerializableSnapshot) -> FieldSnapshot:
    """
    Deserialize a SerializableSnapshot back to a FieldSnapshot.
    
    Args:
        serializable: The SerializableSnapshot to deserialize
        
    Returns:
        Reconstructed FieldSnapshot
        
    Raises:
        SerializationError: If snapshot is incompatible or corrupt
    """
    if not serializable.is_compatible_version():
        raise SerializationError(
            f"Snapshot version {serializable.schema_version} incompatible with current {CURRENT_SCHEMA_VERSION}"
        )
    
    field_state = deserialize_field_state(serializable.field_state)
    
    return FieldSnapshot(
        state=field_state,
        ops_applied=serializable.ledger_events
    )


def serialize_field_memory(memory: FieldMemory) -> Dict[str, Any]:
    """Serialize FieldMemory to JSON-compatible dict"""
    # Serialize snapshots
    serialized_snapshots = []
    for snapshot in memory.snapshots:
        serialized_snapshots.append(serialize_field_snapshot(snapshot))
    
    # Serialize weather history
    weather_history = []
    for timestamp, weather in memory.weather_history:
        weather_history.append({
            'timestamp': timestamp.isoformat(),
            'weather': serialize_field_weather(weather)
        })
    
    return {
        'snapshots': [asdict(s) for s in serialized_snapshots],
        'resonances': memory.resonances,
        'gifts': memory.gifts,
        'tender_moments': memory.tender_moments,
        'weather_history': weather_history
    }


def create_portable_snapshot(
    snapshot: FieldSnapshot,
    memory: Optional[FieldMemory] = None,
    include_sensitive: bool = False
) -> str:
    """
    Create a portable, JSON snapshot suitable for storage or transmission.
    
    Args:
        snapshot: The field snapshot to export
        memory: Optional field memory to include
        include_sensitive: Whether to include potentially sensitive information
        
    Returns:
        JSON string of the portable snapshot
    """
    serializable = serialize_field_snapshot(snapshot)
    
    # Add memory summary if provided
    if memory:
        serializable.memory_summary = {
            'snapshot_count': len(memory.snapshots),
            'resonance_patterns': len(memory.resonances),
            'gifts_count': len(memory.gifts),
            'tender_moments_count': len(memory.tender_moments),
            'weather_points': len(memory.weather_history)
        }
        
        # Include full memory if requested
        if include_sensitive:
            serializable.reserved_1 = serialize_field_memory(memory)
    
    # Privacy considerations
    if not include_sensitive:
        # Redact potentially sensitive information
        from .policy import PrivacyRedactor
        redactor = PrivacyRedactor()
        
        # Create a copy for redaction
        snapshot_dict = asdict(serializable)
        redacted_dict = redactor.redact_snapshot(snapshot_dict)
        
        # Reconstruct serializable from redacted data
        serializable = SerializableSnapshot(**redacted_dict)
    
    return serializable.to_json()


def load_portable_snapshot(json_str: str) -> FieldSnapshot:
    """
    Load a field snapshot from portable JSON format.
    
    Args:
        json_str: JSON string of the snapshot
        
    Returns:
        Reconstructed FieldSnapshot
    """
    serializable = SerializableSnapshot.from_json(json_str)
    return deserialize_field_snapshot(serializable)


def validate_snapshot_integrity(json_str: str) -> Dict[str, Any]:
    """
    Validate the integrity of a serialized snapshot.
    
    Args:
        json_str: JSON string to validate
        
    Returns:
        Validation report with status and any issues found
    """
    report = {
        'valid': True,
        'version': None,
        'compatible': False,
        'issues': [],
        'warnings': []
    }
    
    try:
        # Parse JSON
        data = json.loads(json_str)
        
        # Check required fields
        required_fields = ['schema_version', 'snapshot_id', 'timestamp', 'field_state']
        for field in required_fields:
            if field not in data:
                report['issues'].append(f"Missing required field: {field}")
                report['valid'] = False
        
        # Check version compatibility
        if 'schema_version' in data:
            report['version'] = data['schema_version']
            serializable = SerializableSnapshot.from_json(json_str)
            report['compatible'] = serializable.is_compatible_version()
            
            if not report['compatible']:
                report['warnings'].append(f"Version {data['schema_version']} may not be fully compatible")
        
        # Validate field state structure
        if 'field_state' in data:
            field_state = data['field_state']
            required_state_fields = ['id', 'intent', 'weather']
            for field in required_state_fields:
                if field not in field_state:
                    report['issues'].append(f"Missing field state field: {field}")
                    report['valid'] = False
    
    except json.JSONDecodeError as e:
        report['valid'] = False
        report['issues'].append(f"Invalid JSON: {e}")
    except Exception as e:
        report['valid'] = False
        report['issues'].append(f"Validation error: {e}")
    
    return report
