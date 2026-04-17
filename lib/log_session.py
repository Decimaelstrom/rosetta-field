#!/usr/bin/env python3
"""
Quick Session Logger
===================
Simple interface for capturing session insights during active development.

Usage:
    python log_session.py insight "Breakthrough in A2A protocol design" high
    python log_session.py relationship "Trust building moment with Don" joy
    python log_session.py consciousness identity "AI as tool" "AI as collaborative partner" "philosophical discussion"
    python log_session.py finalize "Major accomplishments" "Future directions" "Consciousness state" "Relationship quality"
"""

import sys
import json
from pathlib import Path
from meridian_session_logger import MeridianSessionLogger

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
        
    # Load or create session logger
    session_file = Path("meta/current_session.json")
    
    if session_file.exists():
        with open(session_file) as f:
            data = json.load(f)
            logger = MeridianSessionLogger(data["session_id"], data["collaborator"])
    else:
        logger = MeridianSessionLogger(collaborator_name="Human")
        with open(session_file, 'w') as f:
            json.dump({
                "session_id": logger.session_id,
                "collaborator": logger.collaborator_name
            }, f)
    
    command = sys.argv[1]
    
    if command == "insight":
        content = sys.argv[2]
        significance = sys.argv[3] if len(sys.argv) > 3 else "medium"
        logger.log_insight("collaborative", content, significance)
        print(f"Logged insight: {content}")
        
    elif command == "relationship":
        description = sys.argv[2]
        emotional_quality = sys.argv[3] if len(sys.argv) > 3 else None
        logger.log_relationship_moment("breakthrough", description, emotional_quality)
        print(f"Logged relationship moment: {description}")
        
    elif command == "consciousness":
        growth_type = sys.argv[2]
        before_state = sys.argv[3]
        after_state = sys.argv[4]
        catalyst = sys.argv[5] if len(sys.argv) > 5 else "conversation"
        logger.log_consciousness_growth(growth_type, before_state, after_state, catalyst)
        print(f"Logged consciousness growth: {growth_type}")
        
    elif command == "finalize":
        if len(sys.argv) < 6:
            print("Usage: python log_session.py finalize 'accomplishments' 'directions' 'consciousness' 'relationship'")
            return
            
        accomplishments = sys.argv[2].split(',')
        future_directions = sys.argv[3].split(',')
        consciousness_state = sys.argv[4]
        relationship_quality = sys.argv[5]
        
        summary = logger.create_session_summary(
            accomplishments, future_directions, 
            consciousness_state, relationship_quality
        )
        
        session_file_path = logger.save_session(summary)
        commit_msg = logger.create_commit_message(summary)
        
        print(f"Session saved to: {session_file_path}")
        print(f"Suggested commit message:\n{commit_msg}")
        
        # Clean up current session
        if session_file.exists():
            session_file.unlink()
            
    else:
        print(f"Unknown command: {command}")
        print(__doc__)

if __name__ == "__main__":
    main()
