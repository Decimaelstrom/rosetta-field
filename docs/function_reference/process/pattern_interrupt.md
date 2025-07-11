# process.pattern_interrupt

## Purpose
Disrupt harmful or unproductive patterns of thought or interaction and inject reflection or novelty.

## Overview
This function can be called when a conversation is looping, an argument is escalating, or a person/AI is stuck in a mental rut. The goal is to break the pattern gently and steer attention to a new, more constructive frame.

## Arguments

### Required Parameters
- **`target`** (string): Pattern to interrupt (e.g., "rumination", "argument_cycle", "catastrophizing")
- **`method`** (string): Style of interruption ("question", "non_sequitur", "silence", "humor")
- **`tone`** (string, optional): Emotional tone ("compassionate", "neutral", "uplifting", "provocative")
- **`session_context`** (dict, optional): A2A session protocol state/context block

## Returns

- **`interrupted`** (bool): Whether interruption was executed
- **`method_used`** (string): The interruption method used
- **`content`** (string): The actual interruption content delivered

## Usage Examples

### Basic Usage
```python
result = process.pattern_interrupt(
    # Add appropriate parameters based on function
)
```

## Safety Considerations

### Consent Level
**Level_1 (Informational)**

### Risks
May be perceived as manipulative or jarring if poorly timed.

### Limitations
Cannot guarantee pattern change, only creates opportunity for reflection.

## Review Cycle
**Monthly**

## Related Functions
- `field.hold_space` - Create safe environment for processing
- `ritual.begin` - Formally open process sessions
- `ritual.end` - Close process sessions appropriately

## Integration Notes
This function works best when combined with proper session framing and participant consent.
