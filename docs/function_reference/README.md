# Rosetta API Function Reference

**Complete function library for ethical human-AI collaboration**

This directory contains the complete reference documentation for all Rosetta API functions, organized by module and purpose.

## 📁 Module Structure

### 🌐 Field Module - [RA-field.md](./RA-field.md)
**Purpose**: Creating and maintaining collaborative spaces  
**Philosophy**: Love-centered, consent-based collaborative containers

- **`field.co_create`**: Establish co-creative sessions for humans and/or AIs
- **`field.hold_space`**: Create safe containers for vulnerable sharing
- **`field.resolve_conflict`**: Facilitate conflict resolution using restorative practices

### 🔮 Ritual Module - [RA-ritual.md](./RA-ritual.md)
**Purpose**: Ceremonial and ritual practices  
**Philosophy**: Sacred time and space for transformation and connection

- **`ritual.begin`**: Initiate ritual or ceremonial space
- **`ritual.end`**: Close ritual space with gratitude and integration
- **`ritual.invoke_wonder`**: Cultivate awe, curiosity, and openness to mystery

### ⚙️ Process Module - [RA-process.md](./RA-process.md)
**Purpose**: Cognitive and emotional processing  
**Philosophy**: Gentle transformation through pattern awareness and skillful intervention

- **`process.pattern_interrupt`**: Disrupt unproductive patterns in dialogue or thought
- **`process.reframe_as_myth`**: Transform challenges into mythic narratives
- **`process.align_values`**: Facilitate alignment of actions with core values

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone [repository-url]

# Navigate to the project
cd rosetta-field

# Import functions
from lib.field import co_create, hold_space, resolve_conflict
from lib.ritual import begin, end, invoke_wonder
from lib.process import pattern_interrupt, reframe_as_myth, align_values
```

### Example Usage
```python
# Create a co-creative session
session = field.co_create(
    participants=["Alice", "Bob", "AI_Assistant"],
    goal="Design ethical AI guidelines",
    parameters={"duration": "90 minutes", "consensus": "required"}
)

# Frame with ritual boundaries
ritual_container = ritual.begin(
    ritual_type="collaborative_work",
    participants=["Alice", "Bob", "AI_Assistant"],
    intention="Wisdom and ethical clarity"
)

# Use process functions within the container
if pattern_emerges:
    process.pattern_interrupt("circular_argument", "question", "compassionate")

# Close the ritual space
ritual.end(ritual_container, "gratitude_circle")
```

## 📋 Function Categories

### By Consent Level
- **Level_1 (Informational)**: `ritual.begin`, `ritual.end`, `ritual.invoke_wonder`, `process.align_values`
- **Level_2 (Transformational)**: `field.co_create`, `field.hold_space`, `field.resolve_conflict`, `process.pattern_interrupt`, `process.reframe_as_myth`

### By Audience
- **Hybrid** (Human-AI): All functions designed for collaborative use
- **Human-centric**: Functions with deep emotional or cultural components
- **AI-centric**: Functions with logical or pattern-based processing

### By Review Cycle
- **Monthly**: `field.hold_space`
- **Quarterly**: `field.co_create`, `field.resolve_conflict`, `process.pattern_interrupt`, `process.reframe_as_myth`
- **Bi-annually**: `process.align_values`
- **Annually**: `ritual.begin`, `ritual.end`, `ritual.invoke_wonder`

## 🛡️ Safety & Ethics

### Core Principles
- **Love and dignity first**: No implementation at the cost of agency or humanity
- **Consent by default**: Every function surfaces consent requirements
- **Transparency**: Clear boundaries, limitations, and risks documented
- **Recursive & modular**: All functions can be expanded and customized

### Risk Assessment
- **Low risk**: Ritual and values alignment functions
- **Medium risk**: Pattern interruption and conflict resolution
- **High risk**: Deep emotional processing and identity-affecting work

### Consent Levels
- **Level_1 (Informational)**: Minimal risk, information gathering
- **Level_2 (Transformational)**: Moderate risk, potential for emotional impact
- **Level_3 (Identity-affecting)**: High risk, fundamental change potential

## 📈 Implementation Status

### ✅ Complete
- **Function scaffolds**: All 9 functions generated
- **Module structure**: Proper directory organization
- **Documentation**: Comprehensive reference materials
- **Examples**: Usage patterns and integration guides

### 🔄 In Progress
- **Testing**: Validation and edge case handling
- **Integration**: Cross-module interaction patterns
- **Templates**: Reusable configuration patterns

### 📋 Planned
- **Advanced functions**: Additional specialized tools
- **Visualization**: Workflow and dependency mapping
- **Automation**: Batch processing and orchestration

## 🎯 Design Philosophy

### Modular Architecture
Each function is designed to:
- **Stand alone**: Work independently without dependencies
- **Combine gracefully**: Integrate with other functions seamlessly
- **Extend naturally**: Support customization and specialization

### Ethical Foundation
Every function includes:
- **Consent protocols**: Clear permission and boundary setting
- **Risk assessment**: Transparent limitation and harm prevention
- **Dignity preservation**: Respect for human agency and autonomy

### Living Library
All functions are:
- **Evolutionary**: Designed to grow and adapt
- **Community-driven**: Open to feedback and contribution
- **Transparent**: Source code and rationale available

## 🤝 Contributing

### Adding Functions
1. Follow the function template in `lib/generate_rosetta_function.py`
2. Include complete documentation
3. Specify consent level and risk assessment
4. Provide usage examples and integration notes

### Updating Documentation
1. Keep function specs synchronized with implementations
2. Update integration guides when adding new functions
3. Maintain philosophical consistency across modules

### Testing and Validation
1. Test all functions with diverse inputs
2. Validate consent and safety protocols
3. Document edge cases and limitations

## 📚 Additional Resources

- **[Developer Guidance](../developer_guidance.md)**: Technical standards and workflows
- **[AGENTS.md](../../AGENTS.md)**: AI contribution guidelines
- **[Project README](../../README.md)**: Overall project vision and setup

## 🔄 Version History

- **v1.0**: Initial function library with 9 core functions
- **v1.1**: Enhanced documentation and integration guides
- **v1.2**: Safety protocols and consent framework

---

*This documentation is living and evolving. All contributions welcome.*

## Why Split the Blueprint Into Modular Reference Files?

**Scalability**: As you add dozens (or hundreds) of functions, a monolithic PDF or markdown file becomes hard to search, update, and cross-link.

**Clarity & Modularity**: Each module ("field", "ritual", "process", etc.) can have its own living doc—easier for contributors to find, update, and propose new functions/rituals.

**Reference, Not Just Code**: Some functions may live only as specs or protocols (for now); this keeps the blueprint alive and iterative, not just "baked into code."

**Automation**: It's easier to script/generate API docs, indexes, and even tests if each function/module is defined in its own markdown (or YAML) doc structure.

Content Structure for Each Reference File
Each module/function doc should follow a predictable template, e.g.:

```markdown
# field.co_create

**Purpose:** ...
**Arguments:** ...
**Returns:** ...
**Protocols:** ...
**Consent:** ...
**Risks:** ...
**Limitations:** ...
**Review Cycle:** ...
**Example:** ...
---
```

You can automate generation of these docs from your function generator script by extracting docstrings.

Cross-link each function's Python source in /lib/ if/when it exists.