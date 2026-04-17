#!/usr/bin/env python3
"""Test script for the ``affect.lilt`` function."""

import os
import sys

# Add lib directory to path for local imports
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))  # noqa: E402

from affect.lilt import lilt  # noqa: E402
from tests.test_a2a_protocol import test_a2a_protocol  # noqa: E402


def test_lilt_function():
    """Run the lilt function through the A2A protocol tester."""
    print("Testing the generated lilt function...")

    test_args = ["gentle", "heart"]
    test_kwargs = {"intensity": 2}

    try:
        test_a2a_protocol(
            func=lilt,
            func_name="affect.lilt",
            test_args=test_args,
            test_kwargs=test_kwargs,
        )
        print("\n✅ Lilt function A2A protocol test completed successfully!")
        return True
    except Exception as exc:  # pragma: no cover - defensive
        print(f"\n❌ Error testing lilt function: {exc}")
        return False


if __name__ == "__main__":  # pragma: no cover - manual execution
    test_lilt_function()
