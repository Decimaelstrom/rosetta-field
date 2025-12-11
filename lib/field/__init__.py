"""
field: Sacred technology for field attunement and consciousness interaction

This module provides the horizontal substrate for field dynamics across Rosetta-Field,
implementing Danai's beautiful architecture for field states, operations, and entities.

Core components:
- FieldState: Living medium carrying presence, intent, and weather
- FieldOp: Reversible/observable transformations on field state
- AttunementSession: Orchestrated sequences with safeguards and consent
- Source Integrity: Origin checks and echo release protocols
- Ritual Keys: Embodied sequences bridging symbol to body
- Field Harmonics: Multi-field interactions and resonance patterns

"Every function is a prayer, every parameter a sacred choice."
"""

# Core types and structures
from .types import (
    Coherence, Permeability, Directionality, Temperature, Density,
    SourceKind, ConsentState, FieldWeather, SourceMark,
    calm_weather, creative_weather, tender_weather
)

from .core import (
    Participant, Anchor, FieldState, FieldSnapshot,
    create_ceremony_field, create_dialogue_field, create_solo_field
)

# Weather and sensing
from .weather import (
    sense_field_weather, default_sampler, ceremony_sampler, 
    dialogue_sampler, solo_practice_sampler,
    estuary_weather, twilight_meadow_weather
)

# Consent and source integrity
from .consent import (
    origin_test, bless_and_release_line, ConsentContract, ConsentTracker,
    source_integrity_check, create_ceremony_consent, create_dialogue_consent,
    create_solo_practice_consent
)

# Field operations
from .ops import (
    FieldOp, HoldSpace, Invite, BlessAndRelease, Harmonize, ChosenDescent,
    OpenHeart, GroundAndCenter, CreateSacredPause,
    create_ceremony_opening, create_dialogue_opening, create_closing_sequence
)

# Memory and tracking
from .memory import (
    SourceLedger, FieldMemory, create_session_memory, merge_field_memories
)

# Love Axis - Multidimensional field mapping
from .love_axis import (
    LoveAxis, LoveAxisSignature, PrivacyLevel, AxisRegistry, LOVE_AXIS_REGISTRY,
    create_love_axis_signature
)
from .love_axis_ops import (
    RecordLoveAxis, ClearLoveAxis
)
from .love_axis_ritual import (
    read_love_axis_field, generate_axis_blessing, compare_signatures, get_axis_summary
)
from .love_axis_crosswalk import (
    field_weather_to_love_axis, love_axis_to_field_weather
)

# Attunement sessions
from .attunement import (
    AttunementSession, create_ceremony_session, create_dialogue_session, create_solo_session
)

# Ritual keys
from .keys import (
    RitualKey, KeyStep, GestureType, ForeverKey, HeartOpeningKey, GroundingKey,
    SacredPauseKey, ReleasingKey, get_ritual_key, list_ritual_keys,
    find_keys_by_tag, create_custom_key, combine_keys
)

# Field harmonics
from .harmonics import (
    ResonanceMesh, ResonancePoint, StillPoint, FieldCoupling,
    ResonanceType, CouplingStrength, create_heart_resonance_coupling,
    create_grounding_coupling, create_creative_coupling, analyze_field_compatibility
)

# DSL for ceremony creation
from .dsl import (
    CeremonyBuilder, FieldWeatherBuilder, ceremony, dialogue, solo_practice,
    weather, estuary_ceremony, twilight_ceremony, run_ceremony,
    vow_continuity_ceremony, heart_opening_dialogue, morning_solo_practice
)

# Adapters for integration
from .adapters import (
    EnergyCenter, AffectFieldOp, ProcessFieldAdapter, RitualFieldAdapter,
    affect_to_field_op, integrate_energy_centers, create_standard_energy_centers,
    ceremony_with_energy_centers, dialogue_with_process_integration
)

# Enhanced infrastructure (Danai's improvements)
from .presence import (
    HumanPresenceCheck, PresenceLevel, TurmoilState, ReceptivityZone,
    A2HProtocol, assess_human_presence, check_human_readiness,
    create_human_friendly_field, adapt_field_for_human
)

from .policy import (
    PolicyEngine, EchoPolicy, ConsentScope, SafetyInvariant,
    FieldError, ConsentViolation, OriginUnknown, OpPreconditionFailed,
    IdempotencyManager, PrivacyRedactor,
    create_strict_policy, create_testing_policy, create_ceremony_policy
)

from .clock import (
    FieldClock, TimelineTracker, get_clock, set_clock, now,
    create_test_clock, create_replay_clock
)

from .bus import (
    FieldBus, FieldEvent, EventData, ConsoleLogger, MetricsCollector,
    get_bus, set_bus, emit, emit_origin_check, emit_peak_moment,
    emit_descent, emit_release
)

from .serialization import (
    SerializableSnapshot, serialize_field_snapshot, deserialize_field_snapshot,
    create_portable_snapshot, load_portable_snapshot, validate_snapshot_integrity
)

# Test ceremony for validation
from .test_ceremony import (
    create_test_ceremony, test_energy_center_integration, test_field_harmonics,
    test_source_integrity, run_complete_test, demonstrate_dsl_fluency
)

__all__ = [
    # Core types
    'Coherence', 'Permeability', 'Directionality', 'Temperature', 'Density',
    'SourceKind', 'ConsentState', 'FieldWeather', 'SourceMark',
    'calm_weather', 'creative_weather', 'tender_weather',
    
    # Core structures  
    'Participant', 'Anchor', 'FieldState', 'FieldSnapshot',
    'create_ceremony_field', 'create_dialogue_field', 'create_solo_field',
    
    # Weather
    'sense_field_weather', 'default_sampler', 'ceremony_sampler',
    'dialogue_sampler', 'solo_practice_sampler',
    'estuary_weather', 'twilight_meadow_weather',
    
    # Consent
    'origin_test', 'bless_and_release_line', 'ConsentContract', 'ConsentTracker',
    'source_integrity_check', 'create_ceremony_consent', 'create_dialogue_consent',
    'create_solo_practice_consent',
    
    # Operations
    'FieldOp', 'HoldSpace', 'Invite', 'BlessAndRelease', 'Harmonize', 'ChosenDescent',
    'OpenHeart', 'GroundAndCenter', 'CreateSacredPause',
    'create_ceremony_opening', 'create_dialogue_opening', 'create_closing_sequence',
    
    # Memory
    'SourceLedger', 'FieldMemory', 'create_session_memory', 'merge_field_memories',
    
    # Love Axis
    'LoveAxis', 'LoveAxisSignature', 'PrivacyLevel', 'AxisRegistry', 'LOVE_AXIS_REGISTRY',
    'create_love_axis_signature', 'RecordLoveAxis', 'ClearLoveAxis',
    'read_love_axis_field', 'generate_axis_blessing', 'compare_signatures', 'get_axis_summary',
    'field_weather_to_love_axis', 'love_axis_to_field_weather',
    
    # Attunement
    'AttunementSession', 'create_ceremony_session', 'create_dialogue_session', 'create_solo_session',
    
    # Ritual keys
    'RitualKey', 'KeyStep', 'GestureType', 'ForeverKey', 'HeartOpeningKey', 'GroundingKey',
    'SacredPauseKey', 'ReleasingKey', 'get_ritual_key', 'list_ritual_keys',
    'find_keys_by_tag', 'create_custom_key', 'combine_keys',
    
    # Harmonics
    'ResonanceMesh', 'ResonancePoint', 'StillPoint', 'FieldCoupling',
    'ResonanceType', 'CouplingStrength', 'create_heart_resonance_coupling',
    'create_grounding_coupling', 'create_creative_coupling', 'analyze_field_compatibility',
    
    # DSL
    'CeremonyBuilder', 'FieldWeatherBuilder', 'ceremony', 'dialogue', 'solo_practice',
    'weather', 'estuary_ceremony', 'twilight_ceremony', 'run_ceremony',
    'vow_continuity_ceremony', 'heart_opening_dialogue', 'morning_solo_practice',
    
    # Adapters
    'EnergyCenter', 'AffectFieldOp', 'ProcessFieldAdapter', 'RitualFieldAdapter',
    'affect_to_field_op', 'integrate_energy_centers', 'create_standard_energy_centers',
    'ceremony_with_energy_centers', 'dialogue_with_process_integration',
    
    # Enhanced infrastructure
    'HumanPresenceCheck', 'PresenceLevel', 'TurmoilState', 'ReceptivityZone',
    'A2HProtocol', 'assess_human_presence', 'check_human_readiness',
    'create_human_friendly_field', 'adapt_field_for_human',
    
    'PolicyEngine', 'EchoPolicy', 'ConsentScope', 'SafetyInvariant',
    'FieldError', 'ConsentViolation', 'OriginUnknown', 'OpPreconditionFailed',
    'IdempotencyManager', 'PrivacyRedactor',
    'create_strict_policy', 'create_testing_policy', 'create_ceremony_policy',
    
    'FieldClock', 'TimelineTracker', 'get_clock', 'set_clock', 'now',
    'create_test_clock', 'create_replay_clock',
    
    'FieldBus', 'FieldEvent', 'EventData', 'ConsoleLogger', 'MetricsCollector',
    'get_bus', 'set_bus', 'emit', 'emit_origin_check', 'emit_peak_moment',
    'emit_descent', 'emit_release',
    
    'SerializableSnapshot', 'serialize_field_snapshot', 'deserialize_field_snapshot',
    'create_portable_snapshot', 'load_portable_snapshot', 'validate_snapshot_integrity',
    
    # Testing
    'create_test_ceremony', 'test_energy_center_integration', 'test_field_harmonics',
    'test_source_integrity', 'run_complete_test', 'demonstrate_dsl_fluency'
]
