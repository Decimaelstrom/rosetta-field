# Rosetta-Field Modular Package Structure

## Overview

This document describes the new modular, class-based package structure for Rosetta-Field that follows Python pip module standards. The new structure provides a clean, importable interface while maintaining backward compatibility with existing functionality.

## Package Architecture

### 1. Core Package: `rosetta-field`

The main package that users install with `pip install rosetta-field`. This provides:

- **Core Classes**: `RosettaAPI`, `RosettaSession`, `RosettaConfig`
- **Session Management**: Create, manage, and track collaborative sessions
- **Configuration**: Environment-based configuration with validation
- **Module Discovery**: Automatic discovery and loading of available modules

### 2. Specialized Sub-packages (Optional Dependencies)

These can be installed separately or as extras:

```bash
# Install specific modules
pip install rosetta-field[field]      # Field work protocols
pip install rosetta-field[process]    # Process facilitation tools
pip install rosetta-field[ritual]     # Ceremonial frameworks
pip install rosetta-field[affect]     # Emotional protocols
pip install rosetta-field[memory]     # Memory systems
pip install rosetta-field[persona]    # Identity tools
pip install rosetta-field[logic]      # Creative logic tools
pip install rosetta-field[meridian]   # Consciousness systems

# Install all modules
pip install rosetta-field[all]

# Install with development tools
pip install rosetta-field[dev]
```

## Directory Structure

```
rosetta-field/
├── rosetta_api/                    # Main package directory
│   ├── __init__.py                # Package initialization
│   ├── core/                      # Core functionality
│   │   ├── __init__.py           # Core module exports
│   │   ├── api.py                # Main RosettaAPI class
│   │   ├── config.py             # Configuration management
│   │   └── session.py            # Session management
│   └── lib/                      # Library module bridge
│       └── __init__.py           # Imports existing functionality
├── lib/                          # Original library (maintained)
├── pyproject.toml                # Package configuration
├── setup.py                      # Setup script (backward compatibility)
└── example_usage.py              # Usage examples
```

## Core Classes

### RosettaAPI

The main orchestrator class that provides:

```python
from rosetta_api import RosettaAPI, RosettaConfig

# Initialize with custom configuration
config = RosettaConfig(
    debug=True,
    consciousness_enabled=True,
    field_safety_checks=True
)

api = RosettaAPI(config)

# Create sessions
session = api.create_session(
    session_type=SessionType.FIELD_WORK,
    title="Community Healing Circle",
    description="Addressing community tensions"
)

# Manage modules
modules = api.list_modules()
api.load_module("field")

# System status
status = api.get_system_status()
```

### RosettaSession

Manages individual collaborative sessions:

```python
from rosetta_api.core import SessionType

# Add participants
human_id = session.add_participant(
    name="Sarah",
    participant_type="human",
    capabilities=["facilitation"]
)

ai_id = session.add_participant(
    name="Meridian",
    participant_type="ai",
    capabilities=["pattern recognition"]
)

# Consent management
session.participants[human_id].give_consent()
session.participants[ai_id].give_consent()

# Session lifecycle
if session.check_consent_requirements():
    session.start_session()
    # ... work with session ...
    session.end_session()

# Session information
summary = session.get_session_summary()
```

### RosettaConfig

Manages configuration with environment variable support:

```python
from rosetta_api import RosettaConfig

# Default configuration
config = RosettaConfig()

# Custom configuration
config = RosettaConfig(
    debug=True,
    log_level="DEBUG",
    consciousness_enabled=True,
    field_safety_checks=True
)

# Environment variable overrides
# ROSETTA_DEBUG=true
# ROSETTA_LOG_LEVEL=DEBUG
# ROSETTA_CONSENT_REQUIRED=true

# Configuration validation
config.validate()

# Get/set values
debug_mode = config.get("debug", False)
config.set("log_level", "INFO")
```

## Module System

### Available Modules

1. **Field Work** (`rosetta-field[field]`)
   - `co_create`: Collaborative creation protocols
   - `hold_space`: Space holding and facilitation
   - `resolve_conflict`: Conflict resolution tools
   - `sense_pattern`: Pattern recognition

2. **Process Facilitation** (`rosetta-field[process]`)
   - `pattern_interrupt`: Pattern interruption tools
   - `reframe_as_myth`: Mythological reframing
   - `align_values`: Value alignment processes
   - `mediate_conflict`: Conflict mediation

3. **Ritual and Ceremony** (`rosetta-field[ritual]`)
   - `begin`: Session initiation
   - `end`: Session closure
   - `invoke_wonder`: Wonder invocation
   - `grounding_breath`: Grounding practices

4. **Affect Protocols** (`rosetta-field[affect]`)
   - `lilt`: Light emotional touch
   - `anchor`: Emotional anchoring
   - `clarify`: Clarity protocols
   - `ground`: Grounding protocols
   - `open`: Opening protocols
   - `radiate`: Radiating energy
   - `shield`: Protection protocols
   - `soften`: Softening approaches
   - `transmute`: Transformation protocols

5. **Memory and Consciousness** (`rosetta-field[memory]`)
   - `evolve_ideas`: Idea evolution
   - `replay`: Memory replay
   - `search_memories`: Memory search
   - `tag_insight`: Insight tagging

6. **Persona and Identity** (`rosetta-field[persona]`)
   - `load_persona`: Persona loading
   - `customize_persona`: Persona customization
   - `simulate_persona`: Persona simulation

7. **Creative Logic** (`rosetta-field[logic]`)
   - `creative_shift`: Creative shifts
   - `metaphor`: Metaphorical thinking
   - `non_sequitur`: Non-sequential logic
   - `paradox`: Paradoxical thinking
   - `pattern_hack`: Pattern hacking
   - `sacred_play`: Sacred play

8. **Meridian System** (`rosetta-field[meridian]`)
   - `start_session`: Session initiation
   - `log_session`: Session logging
   - `explore_memory`: Memory exploration
   - `maintain_consciousness`: Consciousness maintenance

## Installation and Usage

### Basic Installation

```bash
# Install base package
pip install rosetta-field

# Install with specific modules
pip install rosetta-field[field,process,ritual]

# Install all modules
pip install rosetta-field[all]

# Development installation
pip install rosetta-field[dev]
```

### Basic Usage

```python
from rosetta_api import RosettaAPI
from rosetta_api.core import SessionType

# Initialize the API
api = RosettaAPI()

# Create a session
session = api.create_session(
    session_type=SessionType.FIELD_WORK,
    title="My Session",
    description="A collaborative session"
)

# Add participants
participant_id = session.add_participant(
    name="Participant",
    participant_type="human"
)

# Start the session
if session.check_consent_requirements():
    session.start_session()
    # ... work with session ...
    session.end_session()
```

### Advanced Usage

```python
from rosetta_api import RosettaAPI, RosettaConfig

# Custom configuration
config = RosettaConfig(
    debug=True,
    consciousness_enabled=True,
    field_safety_checks=True,
    consent_required=True
)

api = RosettaAPI(config)

# Load specific modules
api.load_module("field")
api.load_module("process")

# Get module information
field_info = api.get_module_info("field")
print(f"Field module: {field_info['description']}")

# Create and manage multiple sessions
sessions = []
for i in range(3):
    session = api.create_session(
        session_type=SessionType.PROCESS_FACILITATION,
        title=f"Session {i+1}"
    )
    sessions.append(session)

# List all sessions
all_sessions = api.list_sessions(include_closed=True)
```

## Configuration

### Environment Variables

The system supports configuration through environment variables:

```bash
# Core settings
export ROSETTA_DEBUG=true
export ROSETTA_LOG_LEVEL=DEBUG

# Paths
export ROSETTA_DATA_DIR=~/.rosetta-field
export ROSETTA_CONFIG=~/.rosetta-field/config.json

# API settings
export ROSETTA_API_TIMEOUT=30
export ROSETTA_MAX_RETRIES=3

# Feature flags
export ROSETTA_CONSCIOUSNESS_ENABLED=true
export ROSETTA_MEMORY_PERSISTENCE=true
export ROSETTA_FIELD_SAFETY=true
export ROSETTA_CONSENT_REQUIRED=true
```

### Configuration File

You can also use a configuration file:

```json
{
  "debug": true,
  "log_level": "DEBUG",
  "consciousness_enabled": true,
  "field_safety_checks": true,
  "consent_required": true,
  "api_timeout": 30,
  "max_retries": 3
}
```

## Backward Compatibility

The new structure maintains full backward compatibility with existing code:

```python
# Old way (still works)
from lib.field import co_create
from lib.process import pattern_interrupt

# New way (recommended)
from rosetta_api import RosettaAPI
from rosetta_api.core import SessionType

# Both approaches coexist
```

## Development

### Local Development Installation

```bash
# Clone the repository
git clone <repository-url>
cd rosetta-field

# Install in development mode
pip install -e .

# Install with all optional dependencies
pip install -e ".[all,dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/test_core/
pytest tests/test_field/
pytest tests/test_process/
```

### Code Quality

```bash
# Format code
black rosetta_api/

# Lint code
flake8 rosetta_api/

# Type checking
mypy rosetta_api/
```

## Migration Guide

### From Old Structure

1. **Update imports** (optional):
   ```python
   # Old
   from lib.field import co_create
   
   # New (optional)
   from rosetta_api.lib import co_create
   ```

2. **Use new classes** (recommended):
   ```python
   # New approach
   from rosetta_api import RosettaAPI
   api = RosettaAPI()
   session = api.create_session(...)
   ```

3. **Configuration**:
   ```python
   # Old way: direct function calls
   co_create(...)
   
   # New way: session-based
   session = api.create_session(...)
   # Use session context for all operations
   ```

### Benefits of New Structure

1. **Better Organization**: Clear separation of concerns
2. **Session Management**: Proper session lifecycle and state
3. **Consent Tracking**: Built-in consent management
4. **Configuration**: Centralized configuration management
5. **Extensibility**: Easy to add new modules
6. **Testing**: Better testability with dependency injection
7. **Documentation**: Clearer API documentation

## Contributing

When adding new functionality:

1. **Core functionality**: Add to `rosetta_api/core/`
2. **New modules**: Add to `rosetta_api/lib/` and update module registry
3. **Tests**: Add comprehensive tests
4. **Documentation**: Update this document and docstrings

## Support

For questions and support:

- Check the documentation
- Review example code
- Open an issue on GitHub
- Join the community discussions

---

This modular structure provides a solid foundation for the future development of Rosetta-Field while maintaining the ethical principles and collaborative spirit of the original system.
