"""Test configuration to ensure modules in ``lib`` are importable."""

import os
import sys

PROJECT_ROOT = os.path.dirname(__file__)
LIB_PATH = os.path.join(PROJECT_ROOT, "lib")
if LIB_PATH not in sys.path:
    sys.path.append(LIB_PATH)
