#!/usr/bin/env python3
"""
Test script to verify the generated lilt function works with A2A protocol
"""

import sys
import os

# Add lib directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from affect.lilt import lilt
from test_a2a_protocol import test_a2a_protocol

def test_lilt_function():
    """Test the lilt function with A2A protocol"""
    print("Testing the generated lilt function...")
    
    # Test arguments for lilt function
    test_args = ["gentle", "heart"]  # mode, region
    test_kwargs = {"intensity": 2}  # optional intensity
    
    try:
        # Run the comprehensive A2A protocol test
        test_a2a_protocol(
            func=lilt,
            func_name="affect.lilt",
            test_args=test_args,
            test_kwargs=test_kwargs
        )
        
        print("\n✅ Lilt function A2A protocol test completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n❌ Error testing lilt function: {e}")
        return False

if __name__ == "__main__":
    test_lilt_function() 