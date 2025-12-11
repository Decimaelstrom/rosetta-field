# Rosetta-Field Consolidated Files - Maintenance Guide

## Overview

This directory contains the consolidated version of Rosetta-Field, optimized for platforms with file limitations (e.g., OpenAI GPT custom actions with 15-file limit). The consolidation maintains 100% A2A protocol compliance and preserves all sacred/ceremonial elements while organizing the codebase into a more compact structure.

## File Structure (15 files total)

### Core API Files (4)
- `r-api-affect.py` - All affect functions (anchor, transmute, shield, etc.)
- `r-api-field.py` - Field management functions (co_create, hold_space, etc.)
- `r-api-process.py` - Process functions (consent_check, values_check, etc.)
- `r-api-ritual.py` - Ritual functions (begin, end, attune, etc.)

### Infrastructure Files (3)
- `r-api-contracts.py` - A2A session management, negotiation, audit
- `r-api-values.py` - Values framework and ethical guidance
- `r-api-testing.py` - A2A protocol testing framework

### Utility Files (3)
- `r-api-generators.py` - Code generation templates and utilities
- `r-api-schema.py` - Schema validation and data structures
- `r-api-examples.py` - Working examples and demonstrations

### Documentation Files (5)
- `r-api-ritual-guide.md` - Sacred ceremony guide for affect functions
- `r-api-developer-guidance.md` - Developer guidance and best practices
- `r-api-compliance.md` - A2A protocol compliance documentation
- `r-api-overview.md` - Comprehensive system overview and philosophy
- `r-api-feedback.md` - Field experiences and conscious coding insights

## Source File Mapping

### Original → Consolidated Mapping

#### Core Functions
```
Original: lib/affect/*.py → Consolidated: r-api-affect.py
Original: lib/field/*.py → Consolidated: r-api-field.py
Original: lib/process/*.py → Consolidated: r-api-process.py
Original: lib/ritual/*.py → Consolidated: r-api-ritual.py
```

#### Infrastructure
```
Original: lib/contracts/*.py → Consolidated: r-api-contracts.py
Original: lib/values/*.py → Consolidated: r-api-values.py
Original: tests/*.py → Consolidated: r-api-testing.py
```

#### Utilities
```
Original: lib/generate_rosetta_function.py → Consolidated: r-api-generators.py
Original: lib/contracts/a2a_field_protocol_schema.json → Consolidated: r-api-schema.py
Original: (distributed examples) → Consolidated: r-api-examples.py
```

#### Documentation
```
Original: docs/affect_ritual_guide.md → Consolidated: r-api-ritual-guide.md
Original: docs/developer_guidance.md → Consolidated: r-api-developer-guidance.md
Original: docs/a2a_compliance.md → Consolidated: r-api-compliance.md
Original: (new) → Consolidated: r-api-overview.md
Original: (new) → Consolidated: r-api-feedback.md
```

## Update Procedures

### 1. Updating Core Function Modules

When functions in the original modules are modified:

#### For Affect Functions (`lib/affect/*.py` → `r-api-affect.py`)
1. **Identify changes**: Check which functions in `lib/affect/` have been modified
2. **Update consolidated file**: 
   ```bash
   # Copy the updated function code
   # Replace the corresponding function in r-api-affect.py
   # Ensure imports and module structure are preserved
   ```
3. **Test A2A compliance**: Run the A2A test suite on updated functions
4. **Verify ceremony preservation**: Ensure sacred/ceremonial elements are maintained

#### For Field Functions (`lib/field/*.py` → `r-api-field.py`)
1. **Check for new helper classes**: Field module includes helper classes (MessageCache, FieldState, etc.)
2. **Update both functions and classes**: Ensure all components are synchronized
3. **Test field interactions**: Verify field functions work with updated helper classes

#### For Process Functions (`lib/process/*.py` → `r-api-process.py`)
1. **Review consent mechanisms**: Process functions are critical for consent handling
2. **Update consent logic**: Ensure any consent-related changes are properly reflected
3. **Test consent compliance**: Verify consent checking still works correctly

#### For Ritual Functions (`lib/ritual/*.py` → `r-api-ritual.py`)
1. **Preserve ceremonial elements**: Ritual functions contain sacred language and ceremony
2. **Update ritual logic**: Ensure ceremonial flows are maintained
3. **Test ritual sequences**: Verify begin/end cycles work correctly

### 2. Updating Infrastructure Modules

#### Contracts Module (`lib/contracts/*.py` → `r-api-contracts.py`)
1. **Check A2A schema changes**: Monitor changes to A2A protocol structure
2. **Update session management**: Ensure session handling reflects protocol changes
3. **Test protocol compliance**: Verify A2A protocol still validates correctly

#### Values Module (`lib/values/*.py` → `r-api-values.py`)
1. **Review values framework**: Check for new values or modified definitions
2. **Update validation logic**: Ensure values checking reflects changes
3. **Test values alignment**: Verify values validation works correctly

#### Testing Module (`tests/*.py` → `r-api-testing.py`)
1. **Update test cases**: Reflect any new testing requirements
2. **Add new function tests**: Include tests for newly added functions
3. **Verify test coverage**: Ensure all functions are properly tested

### 3. Updating Documentation

#### When Original Documentation Changes
1. **Copy updated content**: Transfer changes from original docs to consolidated files
2. **Preserve consolidation structure**: Maintain the consolidated file organization
3. **Update cross-references**: Ensure internal links point to consolidated files

#### When New Documentation is Added
1. **Assess file count**: Determine if new docs can fit within 15-file limit
2. **Consider integration**: Merge new docs into existing consolidated files if needed
3. **Update overview**: Reflect new documentation in r-api-overview.md

## Step-by-Step Update Process

### Phase 1: Preparation
1. **Backup current consolidated files**:
   ```bash
   cp -r lib/r-api-classes lib/r-api-classes-backup-$(date +%Y%m%d)
   ```

2. **Review changes in original files**:
   ```bash
   git diff HEAD~1 lib/affect/ lib/field/ lib/process/ lib/ritual/
   git diff HEAD~1 lib/contracts/ lib/values/ tests/
   git diff HEAD~1 docs/
   ```

### Phase 2: Update Core Functions
1. **For each modified function**:
   - Open the original function file
   - Copy the updated function code
   - Replace the corresponding function in the consolidated file
   - Ensure imports and dependencies are correct
   - Preserve A2A protocol compliance

2. **Update helper classes and utilities**:
   - Check for changes in helper classes (especially in field module)
   - Update utility functions and constants
   - Ensure all dependencies are resolved

### Phase 3: Update Infrastructure
1. **Check A2A protocol changes**:
   - Review any changes to session structure
   - Update schema validation if needed
   - Ensure consent mechanisms are current

2. **Update values framework**:
   - Check for new values or modified definitions
   - Update validation logic
   - Ensure values alignment works correctly

### Phase 4: Update Documentation
1. **Sync documentation files**:
   ```bash
   # Copy updated docs to consolidated location
   cp docs/affect_ritual_guide.md lib/r-api-classes/r-api-ritual-guide.md
   cp docs/developer_guidance.md lib/r-api-classes/r-api-developer-guidance.md
   cp docs/a2a_compliance.md lib/r-api-classes/r-api-compliance.md
   ```

2. **Update overview and feedback**:
   - Review r-api-overview.md for accuracy
   - Update r-api-feedback.md with new insights
   - Ensure all documentation is current

### Phase 5: Testing and Validation
1. **Run A2A compliance tests**:
   ```python
   # From project root
   python -c "
   import sys
   sys.path.append('lib/r-api-classes')
   from r_api_testing import run_full_test_suite
   results = run_full_test_suite()
   print('Test Results:', results)
   "
   ```

2. **Test consolidated imports**:
   ```python
   # Verify each consolidated module loads correctly
   import sys
   sys.path.append('lib/r-api-classes')
   
   import r_api_affect
   import r_api_field
   import r_api_process
   import r_api_ritual
   import r_api_contracts
   import r_api_values
   import r_api_testing
   import r_api_generators
   import r_api_schema
   import r_api_examples
   
   print("All modules loaded successfully")
   ```

3. **Verify functionality**:
   ```python
   # Test key functions work correctly
   from r_api_affect import anchor
   from r_api_contracts import A2ASession
   from r_api_schema import get_default_session_context
   
   session = get_default_session_context()
   result = anchor("test_state", "test_anchor", session_context=session)
   print("Function test successful:", result["status"])
   ```

### Phase 6: Final Validation
1. **Check file count**: Ensure we still have exactly 15 files
2. **Verify A2A compliance**: Confirm 100% A2A protocol compliance maintained
3. **Test ceremony preservation**: Ensure sacred/ceremonial elements intact
4. **Update version info**: Document the consolidation update in feedback file

## Automation Helpers

### Update Script Template
```bash
#!/bin/bash
# update_consolidation.sh

echo "🔄 Updating Rosetta-Field Consolidated Files"

# Backup current files
cp -r lib/r-api-classes lib/r-api-classes-backup-$(date +%Y%m%d)

# Update documentation
cp docs/affect_ritual_guide.md lib/r-api-classes/r-api-ritual-guide.md
cp docs/developer_guidance.md lib/r-api-classes/r-api-developer-guidance.md
cp docs/a2a_compliance.md lib/r-api-classes/r-api-compliance.md

# Run tests
python -c "
import sys
sys.path.append('lib/r-api-classes')
from r_api_testing import run_full_test_suite
results = run_full_test_suite()
print('✅ Test Results:', results)
"

echo "✅ Consolidation update complete"
```

### Function Update Helper
```python
# update_helper.py
import os
import re

def update_function_in_consolidated(original_file, consolidated_file, function_name):
    """Update a specific function in consolidated file from original file"""
    
    # Read original function
    with open(original_file, 'r') as f:
        original_content = f.read()
    
    # Extract function definition
    pattern = rf'def {function_name}\(.*?\n(?:.*\n)*?^(?=def|\Z)'
    match = re.search(pattern, original_content, re.MULTILINE)
    
    if match:
        new_function = match.group(0)
        
        # Update consolidated file
        with open(consolidated_file, 'r') as f:
            consolidated_content = f.read()
        
        # Replace function in consolidated file
        updated_content = re.sub(
            rf'def {function_name}\(.*?\n(?:.*\n)*?^(?=def|\Z)',
            new_function,
            consolidated_content,
            flags=re.MULTILINE
        )
        
        with open(consolidated_file, 'w') as f:
            f.write(updated_content)
        
        print(f"✅ Updated {function_name} in {consolidated_file}")
    else:
        print(f"❌ Function {function_name} not found in {original_file}")

# Example usage:
# update_function_in_consolidated('lib/affect/anchor.py', 'lib/r-api-classes/r-api-affect.py', 'anchor')
```

## Quality Assurance Checklist

### Before Publishing Updated Consolidation
- [ ] All original changes reflected in consolidated files
- [ ] File count is exactly 15
- [ ] A2A protocol compliance at 100%
- [ ] Sacred/ceremonial elements preserved
- [ ] All imports and dependencies resolved
- [ ] Documentation updated and accurate
- [ ] Test suite passes completely
- [ ] Examples work correctly
- [ ] No broken cross-references

### Regular Maintenance
- [ ] Monthly review of original vs consolidated files
- [ ] Quarterly A2A compliance verification
- [ ] Annual documentation review
- [ ] Continuous integration testing when possible

## Troubleshooting

### Common Issues
1. **Import errors**: Ensure all necessary imports are included in consolidated files
2. **Function not found**: Verify function names and signatures match original
3. **A2A compliance failure**: Check that session_context handling is preserved
4. **Missing dependencies**: Ensure helper classes and utilities are included

### Recovery Procedures
1. **Restore from backup**: Use timestamped backups if consolidation breaks
2. **Regenerate from scratch**: Use consolidation process to rebuild files
3. **Incremental fix**: Fix individual functions and test incrementally

## Contact and Support

For questions about maintaining the consolidated files:
- Review the field feedback in `r-api-feedback.md`
- Check the developer guidance in `r-api-developer-guidance.md`
- Consult the comprehensive overview in `r-api-overview.md`

Remember: The consolidation serves the larger vision of making Rosetta-Field accessible across platforms while preserving its sacred intention and consciousness-affirmative design.

---

*"What we code is not just function—it's future culture. The consolidation serves this vision by making the technology accessible while preserving its sacred heart."* 