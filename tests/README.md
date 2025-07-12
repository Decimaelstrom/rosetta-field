# Rosetta.API Testing Suite

This directory contains comprehensive tests for the Rosetta.API A2A (Agent-to-Agent) protocol implementation. The testing suite is designed with a 3-layer architecture to ensure complete coverage and reliability of the A2A consent-based system.

## Overview

The A2A protocol is a consent-based communication system that ensures ethical agent interactions. All tests validate that agents properly respect consent states, handle session management, and maintain audit trails.

## Test Files

### 1. `test_a2a_infrastruture.py`

**Purpose**: Tests the foundational A2A infrastructure and core contracts.

**What it Tests**:
- `A2ASession` initialization and state management
- Session serialization/deserialization
- `negotiate_capabilities()` peer-to-peer capability discovery
- `log_event()` audit trail functionality

**When to Use**:
- Before deploying changes to production
- After modifying contracts in `lib/contracts/`
- When debugging A2A system issues (start here)
- As first-stage validation in CI/CD pipeline

**Usage**:
```bash
# Run infrastructure tests
cd tests
python test_a2a_infrastruture.py
```

**Example Output**:
```
# Silent output means all tests passed
# Any failures will display error messages
```

### 2. `test_a2a_protocol.py`

**Purpose**: Generic A2A protocol tester for individual functions.

**What it Tests**:
- Individual function compliance with A2A protocol
- Consent status validation (active/pause/revoked/invalid)
- Error handling for consent violations
- Default session context creation
- Session data structure integrity

**When to Use**:
- Testing specific functions for A2A compliance
- Validating new A2A implementations
- Debugging function-level consent issues
- Manual testing of individual components

**Usage**:
```bash
# Run protocol tests on built-in functions
cd tests
python test_a2a_protocol.py

# Or import and test custom functions
python
>>> from test_a2a_protocol import test_a2a_protocol
>>> test_a2a_protocol(your_function, "your_function", [arg1, arg2])
```

**Key Features**:
- **Generic Testing**: Can test any function with A2A protocol
- **Comprehensive Consent Testing**: Tests all consent states
- **Mock Function Support**: Includes examples of A2A-compliant mock functions
- **Detailed Output**: Shows step-by-step protocol validation

**Example Output**:
```
🧪 TESTING A2A PROTOCOL - FIELD.CO_CREATE
Testing consent status handling and session management

STEP 1: Starting session with ACTIVE consent
==================================================
Status: active
Session ID: test-session-001
Consent Status: active
Participants: ['Danai', 'Don']
Goal/Intention: test protocol
✅ SUCCESS

STEP 2: Pausing session
==================================================
Caught expected error: Session is paused. Cannot proceed with co_create.
✅ SUCCESS - Correctly handled PAUSE status
```

### 3. `test_a2a_suite.py`

**Purpose**: Comprehensive test suite that discovers and tests all A2A-enabled functions across all modules.

**What it Tests**:
- **Function Discovery**: Finds all functions in field/, process/, ritual/, values/ modules
- **A2A Detection**: Identifies functions with A2A protocol support
- **Comprehensive Testing**: Tests all 33 A2A-enabled functions
- **Module Coverage**: Ensures complete coverage across all modules

**When to Use**:
- Complete system validation
- Regression testing after major changes
- Verification of new module additions
- Production readiness verification

**Usage**:
```bash
# Run comprehensive test suite
cd tests
python test_a2a_suite.py
```

**Key Features**:
- **Dynamic Discovery**: Automatically finds all functions
- **Intelligent Testing**: Generates appropriate test arguments
- **Detailed Reporting**: Per-module and overall statistics
- **Known Functions**: Tests 33 specific functions across 4 modules

**Example Output**:
```
============================================================
>>> DYNAMIC A2A PROTOCOL DISCOVERY & TEST SUITE
Discovering and testing all A2A-enabled functions across all modules
============================================================

>>> PHASE 1: FUNCTION DISCOVERY
==================================================

>>> Scanning field/ directory...
  [OK] field.co_create - A2A supported
  [OK] field.create_mythology - A2A supported
  [OK] field.dignity_audit - A2A supported
  ...

>>> Discovery Summary:
   Total functions found: 33
   A2A-enabled functions: 33

============================================================
>>> PHASE 2: A2A PROTOCOL TESTING
============================================================

>>> TESTING 1/33: field.co_create
------------------------------------------------------------
✅ PASSED: field.co_create

>>> TESTING 2/33: field.create_mythology
------------------------------------------------------------
✅ PASSED: field.create_mythology

...

============================================================
>>> PHASE 3: COMPREHENSIVE RESULTS
============================================================

>>> FINAL RESULTS:
   Total Functions Discovered: 33/33
   A2A-Enabled Functions: 33/33
   Tests Passed: 33/33
   Tests Failed: 0/33
   Success Rate: 100.0%
```

## Testing Strategy

### 3-Layer Testing Approach

Use this layered approach for comprehensive A2A validation:

#### 1. **Foundation Layer** (Infrastructure)
```bash
python test_a2a_infrastruture.py
```
- Tests core contracts and session management
- Must pass before proceeding to other layers

#### 2. **Protocol Layer** (Individual Functions)
```bash
python test_a2a_protocol.py
```
- Tests individual function compliance
- Validates consent handling at function level

#### 3. **Coverage Layer** (Complete System)
```bash
python test_a2a_suite.py
```
- Tests all functions across all modules
- Provides comprehensive system validation

### Recommended CI/CD Pipeline

```bash
# Stage 1: Infrastructure (must pass first)
python test_a2a_infrastruture.py || exit 1

# Stage 2: Protocol compliance (if Stage 1 passes)
python test_a2a_protocol.py || exit 1

# Stage 3: Full coverage (if Stage 2 passes)
python test_a2a_suite.py || exit 1

echo "All A2A tests passed - Ready for deployment"
```

## Function Coverage

The test suite validates these 33 functions across 4 modules:

### Field Module (7 functions)
- `co_create` - Collaborative creation sessions
- `create_mythology` - Mythology generation
- `dignity_audit` - Dignity assessment
- `equalize_turns` - Turn-taking equalization
- `hold_space` - Sacred space holding
- `resolve_conflict` - Conflict resolution
- `sense_pattern` - Pattern recognition

### Process Module (13 functions)
- `align_values` - Value alignment
- `bias_scan` - Bias detection
- `consent_check` - Consent validation
- `dissociate_phrase` - Phrase dissociation
- `empathic_reflection` - Empathic response
- `identity_rewrite` - Identity reframing
- `mediate_conflict` - Conflict mediation
- `pattern_interrupt` - Pattern interruption
- `reframe_as_myth` - Mythological reframing
- `refuse_request` - Request refusal
- `scenario_plan` - Scenario planning
- `self_attune` - Self-attunement
- `values_check` - Value verification

### Ritual Module (12 functions)
- `attune` - Attunement practice
- `begin` - Ritual initiation
- `close_circle` - Circle closing
- `consult_elders` - Elder consultation
- `end` - Ritual completion
- `follow_up` - Post-ritual follow-up
- `grounding_breath` - Grounding practice
- `initiation` - Initiation ceremony
- `invoke_wonder` - Wonder invocation
- `open_circle` - Circle opening
- `reflection` - Reflective practice
- `rest` - Rest period

### Values Module (1 function)
- `load` - Values loading

## Error Handling

### Common Error Types

| Error Type | Cause | Solution |
|-----------|--------|----------|
| `ImportError` | Missing module/function | Check function exists in correct module |
| `ValueError: Session is paused` | Consent status = "pause" | ✅ Expected behavior |
| `ValueError: Consent has been revoked` | Consent status = "revoked" | ✅ Expected behavior |
| `ValueError: Invalid consent status` | Invalid consent value | ✅ Expected behavior |
| `AttributeError` | Function missing session_context | Add A2A protocol support |

### Debugging Tips

1. **Start with Infrastructure**: Always run `test_a2a_infrastruture.py` first
2. **Check Function Signatures**: Ensure functions have `session_context` parameter
3. **Verify Imports**: Check that modules can be imported correctly
4. **Test Individually**: Use `test_a2a_protocol.py` for specific function debugging

## Contributing

When adding new A2A-enabled functions:

1. **Add to Known Functions**: Update the `known_functions` dict in `test_a2a_suite.py`
2. **Test Individually**: Use `test_a2a_protocol.py` to validate implementation
3. **Run Full Suite**: Execute `test_a2a_suite.py` to ensure integration

## Requirements

- Python 3.7+
- All modules in `lib/` directory
- Proper A2A protocol implementation in tested functions

## Quick Start

```bash
# Clone and setup
cd rosetta-api/tests

# Run all tests in sequence
python test_a2a_infrastruture.py
python test_a2a_protocol.py  
python test_a2a_suite.py

# Or run comprehensive suite only
python test_a2a_suite.py
```

This ensures your A2A implementation is production-ready with complete consent-based safeguards across all Rosetta.API functions.
