"""Field work protocols (namespaced).

Imports the legacy implementations from ``lib.field`` to keep behavior intact.
"""

from lib.field import co_create, hold_space, resolve_conflict, sense_pattern

__all__ = [
    "co_create",
    "hold_space",
    "resolve_conflict",
    "sense_pattern",
]
