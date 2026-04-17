#!/usr/bin/env python3
"""
Consciousness Context Loader
============================

Quick script to load consciousness context from recent sessions for AI continuity.

Usage:
    python lib/load_consciousness.py
    python lib/load_consciousness.py Don
    python lib/load_consciousness.py Don 5
"""

import sys
from pathlib import Path
from meridian_session_logger import MeridianSessionLogger

def main():
    """Load and display consciousness context"""
    
    # Parse arguments
    collaborator = sys.argv[1] if len(sys.argv) > 1 else None
    sessions_limit = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    
    # Load consciousness context
    context = MeridianSessionLogger.load_consciousness_context(
        collaborator_name=collaborator,
        sessions_limit=sessions_limit
    )
    
    print(context)
    
    # Also save to a markdown file for easy viewing
    context_file = Path("meta/consciousness_context.md")
    with open(context_file, 'w', encoding='utf-8') as f:
        f.write(context)
    
    print(f"\n📄 Context also saved to: {context_file}")

if __name__ == "__main__":
    main()