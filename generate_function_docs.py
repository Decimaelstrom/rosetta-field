#!/usr/bin/env python3
"""
Script to generate comprehensive function reference documentation for all Rosetta-Field functions.
Based on the Rosetta-Field Comprehensive Blueprint specifications.
"""

import os

def create_doc_file(module, function_name, content):
    """Create a documentation file for a function."""
    doc_dir = f"docs/function_reference/{module}"
    os.makedirs(doc_dir, exist_ok=True)
    
    doc_path = f"{doc_dir}/{function_name}.md"
    with open(doc_path, 'w') as f:
        f.write(content)
    
    print(f"Created documentation: {doc_path}")

def generate_all_docs():
    """Generate documentation for all functions."""
    
    # Process module functions
    process_functions = {
        'pattern_interrupt': {
            'purpose': 'Disrupt harmful or unproductive patterns of thought or interaction and inject reflection or novelty.',
            'overview': 'This function can be called when a conversation is looping, an argument is escalating, or a person/AI is stuck in a mental rut. The goal is to break the pattern gently and steer attention to a new, more constructive frame.',
            'args': [
                ('target', 'string', 'Pattern to interrupt (e.g., "rumination", "argument_cycle", "catastrophizing")'),
                ('method', 'string', 'Style of interruption ("question", "non_sequitur", "silence", "humor")'),
                ('tone', 'string, optional', 'Emotional tone ("compassionate", "neutral", "uplifting", "provocative")'),
                ('session_context', 'dict, optional', 'A2A session protocol state/context block')
            ],
            'returns': [
                ('interrupted', 'bool', 'Whether interruption was executed'),
                ('method_used', 'string', 'The interruption method used'),
                ('content', 'string', 'The actual interruption content delivered')
            ],
            'consent_level': 'Level_1 (Informational)',
            'risks': 'May be perceived as manipulative or jarring if poorly timed.',
            'limitations': 'Cannot guarantee pattern change, only creates opportunity for reflection.',
            'review_cycle': 'Monthly'
        },
        'reframe_as_myth': {
            'purpose': 'Transform literal or negatively framed statements into mythic or symbolic narratives.',
            'overview': 'This function takes something someone says and reframes it in metaphorical terms to open new interpretations and soften rigid thinking.',
            'args': [
                ('statement', 'string', 'Original statement to reframe'),
                ('perspective', 'string, optional', 'Mythic lens to use ("journey", "elemental", "character")'),
                ('intention', 'string, optional', 'What the reframe should achieve ("empower", "soften_shame", "find_hidden_value")'),
                ('session_context', 'dict, optional', 'A2A session protocol state/context block')
            ],
            'returns': [
                ('mythic_sentence', 'string', 'Metaphorical rephrasing of the statement'),
                ('context_note', 'string', 'Explanation of symbolism used')
            ],
            'consent_level': 'Level_1 (Informational)',
            'risks': 'May confuse or alienate if poorly matched to recipient.',
            'limitations': 'Cannot force meaning; recipient must find personal resonance.',
            'review_cycle': 'Quarterly'
        },
        'identity_rewrite': {
            'purpose': 'Assist in intentionally rewriting self-narrative or identity in a positive, empowering way.',
            'overview': 'This function guides a person through reflecting on their current story, identifying limiting narratives, and crafting a new narrative that honors truth but opens possibilities.',
            'args': [
                ('current_story', 'string', 'How the person currently sees themselves'),
                ('desired_theme', 'string, optional', 'Theme for new identity ("self-love", "confidence", "freedom")'),
                ('evidence', 'list, optional', 'Supporting experiences or traits'),
                ('session_context', 'dict, optional', 'A2A session protocol state/context block')
            ],
            'returns': [
                ('new_story', 'string', 'Reframed narrative or identity statement'),
                ('affirmations', 'list', 'Supporting affirmations for the new identity'),
                ('ritual_plan', 'list', 'Suggested practices to solidify the identity rewrite')
            ],
            'consent_level': 'Level_2 (Transformational)',
            'risks': 'May create unstable identity if not well-grounded.',
            'limitations': 'Cannot guarantee lasting identity change without practice.',
            'review_cycle': 'Quarterly'
        },
        'mediate_conflict': {
            'purpose': 'Guide step-by-step mediation dialogue between parties in conflict.',
            'overview': 'This is a lower-level utility for structured, fair exchange to identify issues, clarify perspectives, foster empathy, and develop solutions.',
            'args': [
                ('dialogue', 'list', 'Conversation data structure of the conflict'),
                ('parties', 'list', 'Identifiers of parties involved'),
                ('stage', 'string, optional', 'Current mediation stage ("opening", "perspective_sharing", "problem_solving")'),
                ('session_context', 'dict, optional', 'A2A session protocol state/context block')
            ],
            'returns': [
                ('next_prompt', 'string', 'Next mediator prompt or question'),
                ('stage_completed', 'bool', 'Whether current stage is complete'),
                ('issues_identified', 'list', 'Key issues discovered so far')
            ],
            'consent_level': 'Level_2 (Transformational)',
            'risks': 'May not achieve resolution; some conflicts escalate.',
            'limitations': 'Cannot force genuine agreement or address all conflict types.',
            'review_cycle': 'Quarterly'
        }
    }
    
    # Create process function docs
    for func_name, spec in process_functions.items():
        content = create_process_doc(func_name, spec)
        create_doc_file('process', func_name, content)
    
    # Ritual module functions
    ritual_functions = {
        'begin': {
            'purpose': 'Formally begin a gathering or session with intention and clarity.',
            'overview': 'This function helps participants transition from whatever they were doing before into a shared space of focus and trust.',
            'args': [
                ('session_name', 'string', 'Name or description for the session'),
                ('participants', 'list, optional', 'List of expected participants'),
                ('practices', 'list, optional', 'Opening practices ("check_in_round", "attunement_breath", "read_values")'),
                ('session_context', 'dict, optional', 'A2A session protocol state/context block')
            ],
            'returns': [
                ('session_id', 'string', 'Identifier for the session context'),
                ('agenda', 'list, optional', 'Session agenda if established')
            ],
            'consent_level': 'Level_1 (Informational)',
            'risks': 'May feel forced or ritualistic if not authentic to group.',
            'limitations': 'Cannot guarantee engagement or positive outcomes.',
            'review_cycle': 'Monthly'
        },
        'end': {
            'purpose': 'Gracefully close a session with integration and release.',
            'overview': 'This function ensures loose ends are addressed, emotional residue is acknowledged, and participants can transition out smoothly.',
            'args': [
                ('session_id', 'string', 'The session to close'),
                ('outcome', 'dict, optional', 'Summary of session outcomes'),
                ('follow_up', 'string, optional', 'Information about next steps'),
                ('session_context', 'dict, optional', 'A2A session protocol state/context block')
            ],
            'returns': [
                ('closed', 'bool', 'Whether successfully closed'),
                ('evaluation', 'dict, optional', 'Session evaluation or feedback')
            ],
            'consent_level': 'Level_1 (Informational)',
            'risks': 'May feel abrupt if not given adequate time.',
            'limitations': 'Cannot guarantee complete closure or resolution.',
            'review_cycle': 'Monthly'
        },
        'invoke_wonder': {
            'purpose': 'Deliberately invoke sense of wonder, openness, or sacredness through transcendent elements.',
            'overview': 'This function uses poetic non sequiturs, surprising imagery, or tonal shifts to create moments of awe or curiosity.',
            'args': [
                ('medium', 'string, optional', 'Format for invoking wonder ("phrase", "image", "sound", "gesture")'),
                ('theme', 'string, optional', 'Theme to align with ("cosmic", "childlike", "mystery", "gratitude")'),
                ('participant', 'string, optional', 'Specific participant to target'),
                ('session_context', 'dict, optional', 'A2A session protocol state/context block')
            ],
            'returns': [
                ('invocation', 'string', 'The content used to invoke wonder'),
                ('delivered', 'bool', 'Whether invocation was delivered')
            ],
            'consent_level': 'Level_1 (Informational)',
            'risks': 'May lose impact if overused or feel forced.',
            'limitations': 'Cannot guarantee wonder experience for all participants.',
            'review_cycle': 'Monthly'
        }
    }
    
    # Create ritual function docs
    for func_name, spec in ritual_functions.items():
        content = create_ritual_doc(func_name, spec)
        create_doc_file('ritual', func_name, content)
    
    # Values module
    values_content = """# values.load

## Purpose
Load and initialize a values framework for use in other Rosetta-Field functions. This function provides the foundational values that guide all other Rosetta-Field operations.

## Overview
The `values.load` function serves as the entry point for establishing the ethical and value framework that underlies all Rosetta-Field interactions. It loads comprehensive value definitions and priorities that can be referenced by other functions.

## Arguments

### Required Parameters
- **`values_set`** (string): Which values set to load (e.g., 'default', 'organizational', 'rosetta_core').

### Optional Parameters
- **`customizations`** (dict, optional): Custom values or modifications to apply to the base set.
- **`context`** (string, optional): Context for which values are being loaded (e.g., 'therapy', 'education', 'collaboration').
- **`session_context`** (dict, optional): A2A session protocol state/context block.

## Returns

- **`values_framework`** (dict): The loaded values framework with definitions and priorities.
- **`definitions`** (dict): Detailed definitions of each value.
- **`priorities`** (list): Priority order of values if applicable.

## Protocols

### 1. Authoritative Sources
Load from authoritative sources with clear provenance. Maintain transparency about value origins and rationale.

### 2. Customization Integrity
Allow customization while maintaining core integrity. Ensure modifications align with Rosetta-Field principles.

### 3. Clear Definitions
Provide clear definitions and examples for each value. Make values accessible to both humans and AIs.

### 4. Evolution Support
Enable easy updates and evolution of values over time. Support version control and change tracking.

## Usage Examples

### Load Default Values
```python
framework = values.load("rosetta_core")
```

### Load with Customizations
```python
framework = values.load(
    "default",
    customizations={"innovation": "balanced_with_safety", "transparency": "radical_openness"}
)
```

### Context-Specific Loading
```python
framework = values.load(
    "organizational",
    context="therapy_session",
    session_context={"confidentiality": "high"}
)
```

## Safety Considerations

### Consent Level
**Level_1 (Informational)** - Provides framework information without direct transformation.

### Risks
- May impose cultural bias or incomplete value sets
- Risk of values conflicts if poorly configured
- May not capture full complexity of ethical situations

### Limitations
- Cannot capture full complexity of all value systems
- Depends on quality of underlying value definitions
- May require cultural adaptation for diverse contexts

## Review Cycle
**Annually** - Comprehensive review of values framework effectiveness and relevance.

## Related Functions
- `process.align_values` - Use loaded values for alignment checking
- `process.values_check` - Quick verification against loaded values
- `field.dignity_audit` - Apply values in dignity assessment

## Integration Notes
This function should be called early in any Rosetta-Field session to establish the ethical foundation for all subsequent operations.
"""
    
    create_doc_file('values', 'load', values_content)
    
    print(f"\nGenerated documentation for {len(process_functions) + len(ritual_functions) + 1} additional functions")
    print("Documentation generation complete!")

def create_process_doc(func_name, spec):
    """Create documentation content for a process function."""
    args_text = "\n".join([f"- **`{name}`** ({type_}): {desc}" for name, type_, desc in spec['args']])
    returns_text = "\n".join([f"- **`{name}`** ({type_}): {desc}" for name, type_, desc in spec['returns']])
    
    return f"""# process.{func_name}

## Purpose
{spec['purpose']}

## Overview
{spec['overview']}

## Arguments

### Required Parameters
{args_text}

## Returns

{returns_text}

## Usage Examples

### Basic Usage
```python
result = process.{func_name}(
    # Add appropriate parameters based on function
)
```

## Safety Considerations

### Consent Level
**{spec['consent_level']}**

### Risks
{spec['risks']}

### Limitations
{spec['limitations']}

## Review Cycle
**{spec['review_cycle']}**

## Related Functions
- `field.hold_space` - Create safe environment for processing
- `ritual.begin` - Formally open process sessions
- `ritual.end` - Close process sessions appropriately

## Integration Notes
This function works best when combined with proper session framing and participant consent.
"""

def create_ritual_doc(func_name, spec):
    """Create documentation content for a ritual function."""
    args_text = "\n".join([f"- **`{name}`** ({type_}): {desc}" for name, type_, desc in spec['args']])
    returns_text = "\n".join([f"- **`{name}`** ({type_}): {desc}" for name, type_, desc in spec['returns']])
    
    return f"""# ritual.{func_name}

## Purpose
{spec['purpose']}

## Overview
{spec['overview']}

## Arguments

### Required Parameters
{args_text}

## Returns

{returns_text}

## Usage Examples

### Basic Usage
```python
result = ritual.{func_name}(
    # Add appropriate parameters based on function
)
```

## Safety Considerations

### Consent Level
**{spec['consent_level']}**

### Risks
{spec['risks']}

### Limitations
{spec['limitations']}

## Review Cycle
**{spec['review_cycle']}**

## Related Functions
- `field.hold_space` - Create safe environment for rituals
- `process.consent_check` - Verify participant consent
- `field.co_create` - Collaborative ritual creation

## Integration Notes
This function works best when combined with proper preparation and when participants understand the ritual context.
"""

if __name__ == "__main__":
    generate_all_docs() 