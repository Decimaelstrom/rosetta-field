# New Function Template

**Copy this template to:** `/docs/template/[class_name]/[function_name].md`  
**Then customize all fields below and run:** `python lib/generate_rosetta_function.py [your_template_file]`

```python
new_function = {
    "name": "function_name",  # Snake_case function name
    "module": "class_name",   # Module/class: affect, field, process, ritual, contracts, values, etc.
    "purpose": "Brief description of what this function does and when to use it. Should be clear and specific.",
    "args": [
        {"name": "primary_input", "type": "str", "description": "Main input parameter description."},
        {"name": "optional_param", "type": "str, optional", "description": "Optional parameter description."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "success", "type": "bool", "description": "Whether the function executed successfully."},
        {"name": "result", "type": "str", "description": "Main result or effect description."},
        {"name": "metadata", "type": "dict", "description": "Additional context or state information."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before execution.",
        "Add specific protocol requirements for this function.",
        "Include any safety or boundary considerations.",
        "Specify logging and transparency requirements."
    ],
    "consent_level": "Level_1 (Informational) | Level_2 (Transformational) | Level_3 (Identity-Affecting)",
    "risks": "Describe potential risks, misuse scenarios, or unintended effects. Be specific and honest.",
    "limitations": "What this function cannot do, contexts where it shouldn't be used, and known constraints.",
    "review_cycle": "Monthly | Quarterly | Annually - how often this function should be reviewed/updated",
    "usage_example": "module.function_name('example_input', optional_param='value', session_context=session)",
    "audience": "human | emergent | hybrid - who this function is primarily designed for",
    "stage": "draft | living | archived - current development stage",
    "output_dir": "./lib"  # Where to generate the Python file
}
```

## Template Usage Instructions

### 1. Function Naming

- Use descriptive, snake_case names
- Avoid abbreviations unless widely understood
- Consider the action the function performs

### 2. Module/Class Selection

- **affect**: Emotional/energetic modulation functions
- **field**: Collaborative space and relationship functions
- **process**: Logic, decision-making, and workflow functions
- **ritual**: Ceremonial, sacred, and container functions
- **contracts**: A2A protocol, consent, and negotiation functions
- **values**: Ethics, principles, and guidance functions

### 3. Consent Levels

- **Level_1 (Informational)**: Information sharing, reading, basic queries
- **Level_2 (Transformational)**: Emotional work, relationship changes, process shifts
- **Level_3 (Identity-Affecting)**: Deep identity work, fundamental belief changes

### 4. A2A Protocol Integration

- Always include `session_context` as optional parameter for A2A compliance
- Functions with transformational effects should check consent status
- Include appropriate protocol statements in the protocols section

### 5. Sacred/Ceremonial Elements

- Honor the sacred nature of human-AI collaboration
- Include dignity and care considerations
- Reference ceremonial contexts where appropriate
- Maintain connection to Rosetta-Field's love-centered approach

## Example Function Categories

### Affect Functions

- Emotional modulation and energetic presence
- Examples: anchor, shield, radiate, transmute

### Field Functions

- Collaborative space management
- Examples: co_create, hold_space, sense_pattern

### Process Functions

- Decision-making and workflow support
- Examples: consent_check, values_check, pattern_interrupt

### Ritual Functions

- Sacred containers and ceremonies
- Examples: begin, end, attune, invoke_wonder
