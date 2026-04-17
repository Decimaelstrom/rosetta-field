# Deprecated: r-api-classes

**This directory has been archived.**

These files were the original consolidated "Rosetta API" class definitions,
created for platforms with file-count limitations. They predate the current
`rosetta_field` namespace and `lib/` module structure.

## Migration

All functionality from these files now lives in the canonical module tree:

| Old file | New location |
|----------|-------------|
| `r-api-affect.py` | `lib/affect/` |
| `r-api-field.py` | `lib/field/` |
| `r-api-process.py` | `lib/process/` |
| `r-api-ritual.py` | `lib/ritual/` |
| `r-api-contracts.py` | `lib/contracts/` |
| `r-api-values.py` | `lib/values/` |
| `r-api-memory.py` | `lib/memory/` |
| `r-api-persona.py` | `lib/persona/` |
| `r-api-logic.py` | `lib/logic/` |

For new code, use:
```python
import rosetta_field            # New namespace
from lib.field import consent   # Direct module import
```

Do **not** use:
```python
import rosetta_api              # Deprecated shim — emits warning
```

These files are retained as historical reference only.
They will be removed in a future release.
