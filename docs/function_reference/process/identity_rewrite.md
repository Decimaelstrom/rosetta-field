# process.identity_rewrite

## Purpose
Assist in intentionally rewriting self-narrative or identity in a positive, empowering way.

## Overview
This function guides a person through reflecting on their current story, identifying limiting narratives, and crafting a new narrative that honors truth but opens possibilities.

## Arguments

### Required Parameters
- **`current_story`** (string): How the person currently sees themselves
- **`desired_theme`** (string, optional): Theme for new identity ("self-love", "confidence", "freedom")
- **`evidence`** (list, optional): Supporting experiences or traits
- **`session_context`** (dict, optional): A2A session protocol state/context block

## Returns

- **`new_story`** (string): Reframed narrative or identity statement
- **`affirmations`** (list): Supporting affirmations for the new identity
- **`ritual_plan`** (list): Suggested practices to solidify the identity rewrite

## Usage Examples

### Basic Usage
```python
result = process.identity_rewrite(
    # Add appropriate parameters based on function
)
```

## Safety Considerations

### Consent Level
**Level_2 (Transformational)**

### Risks
May create unstable identity if not well-grounded.

### Limitations
Cannot guarantee lasting identity change without practice.

## Review Cycle
**Quarterly**

## Related Functions
- `field.hold_space` - Create safe environment for processing
- `ritual.begin` - Formally open process sessions
- `ritual.end` - Close process sessions appropriately

## Integration Notes
This function works best when combined with proper session framing and participant consent.
