"""Namespaced access to Rosetta-Field domain modules.

Each subpackage re-exports the legacy implementations from the packaged
``lib`` namespace. This keeps imports stable while supporting discovery.
"""

__all__ = [
    "field",
    "process",
    "ritual",
    "affect",
    "memory",
    "persona",
    "logic",
    "meridian",
]
