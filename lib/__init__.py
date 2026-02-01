"""Top-level legacy Rosetta-Field modules.

This package exists to keep the original flat module layout (``lib.field``,
``lib.process`` …) available for code and docs that still import those paths.
It is packaged alongside the new ``rosetta_field`` namespace so installs
work without manual path tweaking.
"""

# Re-export subpackages for convenience
__all__ = [
    "affect",
    "field",
    "process",
    "ritual",
    "memory",
    "persona",
    "logic",
]
