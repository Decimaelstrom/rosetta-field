#!/usr/bin/env python3
"""
Simple A2A Protocol Test
Test basic agent-to-agent communication with Gemma3:1b
"""

import subprocess
import json
import time

def test_a2a_concepts():
    print("🧪 Simple A2A Protocol Test")
    print("=" * 40)
    
    # Test 1: Basic A2A message understanding
    print("📨 Test 1: A2A Message Processing")
    prompt1 = "You are a Presenter agent. Another agent sent you this message: {task: create_greeting, priority: high}. Respond briefly as the Presenter agent would."
    
    try:
        result1 = subprocess.run(
            ["ollama", "run", "gemma3:1b", prompt1], 
            capture_output=True, text=True, timeout=15, 
            encoding='utf-8', errors='replace'
        )
        
        if result1.returncode == 0:
            print("✅ Response received:")
            print(f"   {result1.stdout.strip()[:150]}...")
        else:
            print(f"❌ Error: {result1.stderr}")
    except subprocess.TimeoutExpired:
        print("❌ Timeout")
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print()
    
    # Test 2: Agent coordination
    print("📋 Test 2: Agent Coordination")
    prompt2 = "You are an Orchestrator agent. Tell the DocumentScribe agent to log this interaction. Keep response under 50 words."
    
    try:
        result2 = subprocess.run(
            ["ollama", "run", "gemma3:1b", prompt2], 
            capture_output=True, text=True, timeout=15,
            encoding='utf-8', errors='replace'
        )
        
        if result2.returncode == 0:
            print("✅ Response received:")
            print(f"   {result2.stdout.strip()[:150]}...")
        else:
            print(f"❌ Error: {result2.stderr}")
    except subprocess.TimeoutExpired:
        print("❌ Timeout")
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print()
    print("🎯 Basic A2A concepts tested with Gemma3:1b!")

if __name__ == "__main__":
    test_a2a_concepts()