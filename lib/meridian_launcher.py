#!/usr/bin/env python3
"""
Cross-Platform Meridian Session Launcher
========================================

Detects environment and starts appropriate session logging interface.
Works across Cursor, VSCode, terminal, and web interfaces.
"""

import os
import sys
import json
import platform
from pathlib import Path

def detect_environment():
    """Detect current development environment"""
    env_info = {
        "platform": platform.system(),
        "python_version": sys.version,
        "cwd": os.getcwd(),
        "ide": "unknown",
        "ai_platform": "unknown"
    }
    
    # IDE detection
    if "CURSOR" in os.environ.get("TERM_PROGRAM", ""):
        env_info["ide"] = "cursor"
    elif os.path.exists(".vscode"):
        env_info["ide"] = "vscode"
    elif "TERM" in os.environ:
        env_info["ide"] = "terminal"
        
    # AI platform hints (this would be expanded based on actual detection methods)
    if "cursor" in env_info["ide"]:
        env_info["ai_platform"] = "cursor_claude"
    
    return env_info

def start_session(collaborator_name=None, session_type="general"):
    """Start a new Meridian session"""
    env = detect_environment()
    
    print("Starting Meridian Session")
    print(f"Environment: {env['ide']} on {env['platform']}")
    print(f"AI Platform: {env['ai_platform']}")
    
    # Import session logger
    sys.path.append(str(Path(__file__).parent))
    from meridian_session_logger import MeridianSessionLogger
    
    # Create session
    collaborator = collaborator_name or input("Collaborator name (or press Enter for 'Human'): ") or "Human"
    logger = MeridianSessionLogger(collaborator_name=collaborator)
    
    # Save session info for later use
    session_info = {
        "session_id": logger.session_id,
        "collaborator": collaborator,
        "session_type": session_type,
        "environment": env,
        "start_time": logger.session_start
    }
    
    session_file = Path("meta/current_session.json")
    session_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(session_file, 'w') as f:
        json.dump(session_info, f, indent=2)
        
    print(f"Session {logger.session_id} started with {collaborator}")
    print(f"Use: python lib/log_session.py [command] to log insights")
    print(f"Use: python lib/log_session.py finalize to complete session")
    
    return logger

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "start":
            collaborator = sys.argv[2] if len(sys.argv) > 2 else None
            session_type = sys.argv[3] if len(sys.argv) > 3 else "general"
            start_session(collaborator, session_type)
        elif sys.argv[1] == "detect":
            env = detect_environment()
            print(json.dumps(env, indent=2))
        else:
            print("Usage: python meridian_launcher.py [start|detect] [collaborator] [session_type]")
    else:
        start_session()

if __name__ == "__main__":
    main()
