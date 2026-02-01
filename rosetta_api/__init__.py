"""
Compatibility shim for legacy imports.

Using ``import rosetta_api`` is deprecated; prefer ``import rosetta_field``.
This module re-exports the primary interfaces while emitting a deprecation
warning on import to encourage migration.
"""

import warnings
import os

message = "Deprecated: use `import rosetta_field` instead of `rosetta_api`."
if os.environ.get("ROSETTA_API_DEPRECATED_STRICT"):
    raise ImportError(message)
warnings.warn(message, DeprecationWarning, stacklevel=2)

from rosetta_field import RosettaAPI, RosettaSession, RosettaConfig  # noqa: F401

__all__ = ["RosettaAPI", "RosettaSession", "RosettaConfig"]
