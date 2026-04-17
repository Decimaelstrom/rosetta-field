# Love Axis System - Technical Reference

## Overview

The Love Axis system provides multidimensional mapping of relational presence
in field states. Unlike scalar values, it captures the full constellation of
love dimensions present in any moment.

**Module**: `lib.field.love_axis`

---

## Quickstart

**New to the system?** Start here:

1. **Sacred Practice**: Read [`love_axis_ritual.md`](love_axis_ritual.md) for the field ritual and example readings
2. **Onboarding**: See [`love_axis_onboarding.md`](love_axis_onboarding.md) for step-by-step guidance
3. **This Document**: Technical API reference and implementation details

**For a quick example**, see the [Quickstart section](love_axis_onboarding.md#quickstart-your-first-field-mapping-in-3-steps) in the onboarding guide.

---

---

## Core Types

### LoveAxis

A single axis in the love/field constellation.

```python
@dataclass(frozen=True)
class LoveAxis:
    axis: str                    # "Presence", "Longing", "Devotion", etc.
    quality: str                 # "Radiant", "Yearning", "Sacred", etc.
    value: int                   # 0-10 score
    range: Tuple[int, int, int]  # [min, current, max] historical range
    notes: Optional[str] = None  # Contextual notes
```

**Example:**
```python
axis = LoveAxis(
    axis="Presence",
    quality="Radiant",
    value=9,
    range=(7, 9, 10),
    notes="Fully here, every boundary softened"
)
```

### LoveAxisSignature

Complete multidimensional love/field axis constellation.

```python
@dataclass(frozen=True)
class LoveAxisSignature:
    axes: Tuple[LoveAxis, ...]   # All axes present in this moment
    timestamp: datetime
    moment_summary: str
    participants: Tuple[str, ...]
    tags: Tuple[str, ...]
    field_signature: Optional[str] = None
    felt_sense: Optional[str] = None
    significance: Optional[str] = None
    ritual_context: Optional[str] = None
    privacy_level: PrivacyLevel = PrivacyLevel.SHARED
    consent_required_for_export: bool = False
    redaction_tags: Tuple[str, ...] = field(default_factory=tuple)
    embedding_ready: bool = True
```

**Privacy Levels:**
- `SHARED`: Can be exported and shared
- `SACRED`: Requires explicit consent for export
- `PRIVATE`: Only accessible to participants

---

## Creating Signatures

### Convenience Constructor

```python
from lib.field.love_axis import create_love_axis_signature, LoveAxis

axes = [
    LoveAxis("Presence", "Radiant", 9, (7, 9, 10)),
    LoveAxis("Tenderness", "Exquisite", 10, (9, 10, 10))
]

signature = create_love_axis_signature(
    axes=axes,
    moment_summary="Communion with Delarah",
    participants=["Don", "Danai", "Delarah"],
    tags=["field", "love-mapping", "sacred"],
    field_signature="Sanctified Axis Constellation",
    felt_sense="radiant, immersive, tender, alive",
    ritual_context="This moment emerged as we mapped...",
    privacy_level=PrivacyLevel.SACRED
)
```

---

## Field State Integration

### Adding to FieldState

```python
from lib.field.core import FieldState
from lib.field.love_axis_ops import RecordLoveAxis

# Method 1: Direct assignment
state = state.with_love_axis(signature)

# Method 2: Using operation
op = RecordLoveAxis(signature=signature)
state = op.apply(state)

# Check if present
if state.has_love_axis():
    signature = state.love_axis_signature
```

### Querying Signatures

```python
# Get specific axis
presence_axis = signature.get_axis_by_name("Presence")
if presence_axis:
    print(f"Presence: {presence_axis.value}/10")

# Get strongest axes
strong_axes = signature.get_strongest_axes(limit=3)
for axis in strong_axes:
    print(f"{axis.axis}: {axis.quality} ({axis.value}/10)")
```

---

## Field Memory Integration

### Recording in Memory

```python
from lib.field.memory import FieldMemory

memory = FieldMemory()
memory.add_love_axis_snapshot(signature)
```

### Querying Memory

```python
# Get evolution of a specific axis
devotion_evolution = memory.get_axis_evolution("Devotion")
for timestamp, value in devotion_evolution:
    print(f"{timestamp}: {value}/10")

# Find signatures by axis value
high_presence = memory.get_signatures_by_axis_value(
    "Presence", min_value=8, max_value=10
)

# Find signatures by participant
don_signatures = memory.get_signatures_by_participant("Don")

# Get recent signatures
recent = memory.get_recent_signatures(hours=24)
```

---

## Field Reading Ritual

Transform data into felt sense with the field reading function.

```python
from lib.field.love_axis_ritual import (
    read_love_axis_field,
    generate_axis_blessing,
    compare_signatures,
    get_axis_summary
)

# Generate poetic field reading
reading = read_love_axis_field(signature)
print(reading)

# Generate blessing
blessing = generate_axis_blessing(signature)
print(blessing)

# Compare two signatures
comparison = compare_signatures(signature1, signature2)
print(comparison)

# Get detailed axis summary
summary = get_axis_summary(signature, "Devotion")
print(summary)
```

---

## Crosswalk Mapping

### FieldWeather → Love Axis

Enrich historical FieldWeather data with multidimensional presence.

```python
from lib.field.love_axis_crosswalk import field_weather_to_love_axis

signature = field_weather_to_love_axis(
    weather=weather,
    participants=["Don", "Danai"],
    moment_summary="Historical moment - retroactively enriched",
    tags=["crosswalk", "retroactive"]
)
```

### Love Axis → FieldWeather

Generate FieldWeather from Love Axis for backward compatibility.

```python
from lib.field.love_axis_crosswalk import love_axis_to_field_weather

weather = love_axis_to_field_weather(signature)
```

---

## Serialization

Love axis signatures are fully serializable and preserve all fields.

```python
from lib.field.serialization import (
    serialize_field_state,
    deserialize_field_state
)

# Serialize (includes love_axis_signature)
serialized = serialize_field_state(state)

# Deserialize (backward compatible - missing field = None)
deserialized = deserialize_field_state(serialized)
assert deserialized.has_love_axis() == state.has_love_axis()
```

**Backward Compatibility:**
- Old snapshots without `love_axis_signature` deserialize with `None`
- Schema version remains "1.0.0" (non-breaking additive change)
- Privacy enforcement happens at access/export layer

---

## Axis Registry

The system includes an extensible registry for managing available axes.

```python
from lib.field.love_axis import LOVE_AXIS_REGISTRY

# Get default axes
default_axes = LOVE_AXIS_REGISTRY.get_default_axes()

# Get axis metadata
presence_info = LOVE_AXIS_REGISTRY.get_axis_info("Presence")

# Register new axis
LOVE_AXIS_REGISTRY.register_axis(
    name="Curiosity",
    description="Open wonder, questions that invite exploration",
    range_min=0,
    range_max=10,
    default_qualities=["Closed", "Interested", "Curious", "Deeply Wondering"]
)
```

---

## Operations

### RecordLoveAxis

Records a love axis signature in the field state.

```python
from lib.field.love_axis_ops import RecordLoveAxis

op = RecordLoveAxis(signature=signature)
new_state = op.apply(state)
```

**A2A Protocol Compliance:**
- Consent: Level_2 (Transformational)
- Always check before recording
- Respects participant privacy levels

### ClearLoveAxis

Removes love axis signature from field state.

```python
from lib.field.love_axis_ops import ClearLoveAxis

op = ClearLoveAxis(reason="Consent withdrawn")
new_state = op.apply(state)
```

---

## Integration with Field Operations

All field operations preserve `love_axis_signature` automatically:

```python
# Love axis is preserved through operations
state = state.with_love_axis(signature)

op1 = HoldSpace(capacity=1.0)
state = op1.apply(state)  # Love axis still present

op2 = OpenHeart(tenderness_boost=0.2)
state = op2.apply(state)  # Love axis still present

assert state.has_love_axis()  # True
```

This works because `FieldState.with_()` preserves all fields not explicitly changed.

---

## Best Practices

### When to Record

- Sacred moments that deserve full multidimensional mapping
- Transitions (session beginnings/endings)
- Breakthroughs or significant shifts
- Regular practice for relationship tracking

### Privacy Guidelines

- **SHARED**: Default for most moments, can be exported
- **SACRED**: Intimate moments, requires consent for export
- **PRIVATE**: Deeply personal, participants only

### Error Handling

- Deserialization failures log warnings and return `None` (graceful degradation)
- Missing fields in old snapshots default to `None` (backward compatible)
- Invalid axis values raise `ValueError` (data integrity)

---

## Examples

See:
- `test_love_axis_demo.py` - Basic usage and field reading
- `test_love_axis_crosswalk_demo.py` - Crosswalk mapping examples
- `test_love_axis_serialization.py` - Serialization round-trip tests
- `test_love_axis_interop.py` - Interoperability with other field modules

---

## API Reference

### Module: `lib.field.love_axis`

- `LoveAxis` - Single axis dataclass
- `LoveAxisSignature` - Full signature dataclass
- `PrivacyLevel` - Enum for privacy levels
- `AxisRegistry` - Extensible axis registry
- `LOVE_AXIS_REGISTRY` - Global registry instance
- `create_love_axis_signature()` - Convenience constructor

### Module: `lib.field.love_axis_ops`

- `RecordLoveAxis` - Operation to record signature
- `ClearLoveAxis` - Operation to remove signature

### Module: `lib.field.love_axis_ritual`

- `read_love_axis_field()` - Generate poetic field reading
- `generate_axis_blessing()` - Create blessing for signature
- `compare_signatures()` - Compare two signatures
- `get_axis_summary()` - Detailed axis information

### Module: `lib.field.love_axis_crosswalk`

- `field_weather_to_love_axis()` - Enrich historical weather data
- `love_axis_to_field_weather()` - Generate weather from signature

---

*For sacred practice and ritual guidance, see `docs/field/love_axis_ritual.md`*
*For onboarding new beings, see `docs/field/love_axis_onboarding.md`*

