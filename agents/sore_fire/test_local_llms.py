#!/usr/bin/env python3
"""
Test script for local LLM integrations (Ollama and LMStudio)
"""

import sys
import os
import asyncio

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))
sys.path.append(os.path.dirname(__file__))

from sore_fire_llm_bot import SoreFireLLMBot, LLMConfig


async def test_ollama():
    """Test Ollama integration"""
    print("🦙 Testing Ollama Integration")
    print("-" * 40)
    
    config = LLMConfig(
        provider="ollama",
        model="llama2",  # Assumes llama2 is installed
        base_url="http://localhost:11434",
        max_tokens=512,
        temperature=0.7
    )
    
    bot = SoreFireLLMBot(config, debug=True)
    
    try:
        # Test field sensing (this should work without LLM)
        field_result = bot._tool_sense_field("I'm feeling lost today")
        print(f"✅ Field sensing works: {field_result.result.get('primary_anatomy')}")
        
        # Test LLM call (this requires Ollama to be running)
        print("\n🧪 Testing LLM call (requires Ollama server running)...")
        response = await bot.process_message("Hello, can you sense my field?")
        print(f"🔥 Response: {response[:100]}...")
        
    except Exception as e:
        print(f"❌ Ollama test failed: {e}")
        print("💡 Make sure Ollama is running: ollama serve")
        print("💡 And model is installed: ollama pull llama2")


async def test_lmstudio():
    """Test LMStudio integration"""
    print("\n🎭 Testing LMStudio Integration")
    print("-" * 40)
    
    config = LLMConfig(
        provider="lmstudio",
        model="test-model",  # Replace with your actual model name
        base_url="http://localhost:1234",
        max_tokens=512,
        temperature=0.7
    )
    
    bot = SoreFireLLMBot(config, debug=True)
    
    try:
        # Test field sensing
        field_result = bot._tool_sense_field("I need help with something")
        print(f"✅ Field sensing works: {field_result.result.get('primary_anatomy')}")
        
        # Test LLM call (this requires LMStudio server running)
        print("\n🧪 Testing LLM call (requires LMStudio server running)...")
        response = await bot.process_message("Can you help me understand the Amara framework?")
        print(f"🔥 Response: {response[:100]}...")
        
    except Exception as e:
        print(f"❌ LMStudio test failed: {e}")
        print("💡 Make sure LMStudio local server is running")
        print("💡 And a model is loaded in the interface")


async def test_library_integration():
    """Test library integration without LLM calls"""
    print("\n📚 Testing Library Integration (No LLM Required)")
    print("-" * 50)
    
    # Create a dummy config
    config = LLMConfig(provider="test", model="test")
    bot = SoreFireLLMBot(config, debug=True)
    
    test_messages = [
        "I'm feeling sad and alone",
        "I'm angry about injustice", 
        "I want to create something beautiful",
        "Help me understand deeply"
    ]
    
    for message in test_messages:
        print(f"\n💬 Input: \"{message}\"")
        
        # Test field sensing
        field_result = bot._tool_sense_field(message)
        amara_mode = field_result.result.get('primary_anatomy', 'Unknown')
        print(f"   🎯 Amara Mode: {amara_mode}")
        
        # Test story activation
        if amara_mode != 'Unknown':
            story_result = bot._tool_activate_story_memory(amara_mode)
            archetype = story_result.result.get('archetype', 'Unknown')
            print(f"   🎭 Archetype: {archetype}")
            
            # Test micro practice
            practice_result = bot._tool_suggest_micro_practice(amara_mode)
            practice = practice_result.result.get('micro_act', 'Unknown')
            print(f"   🌱 Practice: {practice[:50]}...")
        
        # Test system prompt building
        system_prompt = bot._build_system_prompt([field_result])
        print(f"   📝 System Prompt: {len(system_prompt)} chars")


async def main():
    """Run all tests"""
    print("🔥 SORE FIRE LOCAL LLM TESTING")
    print("=" * 60)
    
    # Always test library integration
    await test_library_integration()
    
    # Test local LLMs if available
    print(f"\n{'='*60}")
    print("🏠 LOCAL LLM TESTS (require servers to be running)")
    
    choice = input("\nTest Ollama? (y/n): ").strip().lower()
    if choice == 'y':
        await test_ollama()
    
    choice = input("\nTest LMStudio? (y/n): ").strip().lower()
    if choice == 'y':
        await test_lmstudio()
    
    print(f"\n{'='*60}")
    print("✅ Testing complete!")
    print("\n🚀 To run the full chatbot:")
    print("   python sore_fire_llm_bot.py")


if __name__ == "__main__":
    asyncio.run(main())
