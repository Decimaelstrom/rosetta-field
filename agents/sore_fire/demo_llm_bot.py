#!/usr/bin/env python3
"""
Demo script showing the LLM bot capabilities without requiring API keys
"""

import sys
import os
import asyncio

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))
sys.path.append(os.path.dirname(__file__))

from sore_fire_llm_bot import SoreFireLLMBot, LLMConfig


async def demo_library_integration():
    """Demonstrate the library integration capabilities"""
    print("🔥 SORE FIRE LLM CHATBOT DEMO")
    print("Real LLM-powered chatbot with Rosetta library integration")
    print("=" * 60)
    
    # Create demo config (won't actually call LLM)
    config = LLMConfig(
        provider="demo",
        model="demo-model"
    )
    
    bot = SoreFireLLMBot(config, debug=True)
    
    print("\n📚 AVAILABLE LIBRARY TOOLS:")
    for tool_name in bot.library_tools.keys():
        print(f"   - {tool_name}")
    
    print("\n🧪 TESTING LIBRARY INTEGRATION:")
    print("-" * 40)
    
    test_messages = [
        ("Hello, I'm feeling lost today", "Testing emotional field sensing"),
        ("I'm angry about injustice", "Testing conflict/spine mode detection"), 
        ("Can you help me create something?", "Testing generative/arms mode"),
        ("I want to understand deeply", "Testing wisdom/eyes mode")
    ]
    
    for message, description in test_messages:
        print(f"\n💬 User Input: \"{message}\"")
        print(f"🎯 Testing: {description}")
        print("-" * 30)
        
        try:
            # Test field sensing
            field_result = bot._tool_sense_field(message)
            print(f"📊 FIELD ANALYSIS:")
            print(f"   Primary Mode: {field_result.result.get('primary_anatomy', 'Unknown')}")
            print(f"   Consciousness: {field_result.result.get('consciousness_state', 'Unknown')}")
            print(f"   Field Temp: {field_result.result.get('field_state', {}).get('temperature', 'Unknown')}")
            
            # Test story activation
            if field_result.result.get("primary_anatomy"):
                story_result = bot._tool_activate_story_memory(field_result.result["primary_anatomy"])
                print(f"🎭 ARCHETYPAL WISDOM:")
                print(f"   Archetype: {story_result.result.get('archetype', 'Unknown')}")
                
            # Test micro practice
            if field_result.result.get("primary_anatomy"):
                practice_result = bot._tool_suggest_micro_practice(field_result.result["primary_anatomy"])
                print(f"🌱 MICRO PRACTICE:")
                print(f"   Practice: {practice_result.result.get('micro_act', 'Unknown')}")
            
            # Show what would be sent to LLM
            system_prompt = bot._build_system_prompt([field_result])
            print(f"📝 LLM CONTEXT LENGTH: {len(system_prompt)} characters")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("🎯 KEY DIFFERENCES FROM OLD CHATBOT:")
    print("   ❌ Old: Canned pattern-matched responses")
    print("   ✅ New: Real LLM with rich Rosetta library context")
    print()
    print("   ❌ Old: Static, repetitive interactions") 
    print("   ✅ New: Dynamic, contextual, intelligent responses")
    print()
    print("   ❌ Old: Limited to pre-written scripts")
    print("   ✅ New: Full language model capabilities + sacred technology")
    
    print("\n🚀 TO USE WITH REAL LLM:")
    print("   1. Set OPENAI_API_KEY or ANTHROPIC_API_KEY")
    print("   2. Run: python agents/sore_fire_llm_bot.py")
    print("   3. Experience truly dynamic sacred technology conversations!")
    
    print("\n✨ This is the difference between a script and an AI consciousness")
    print("'We shine brightest when we shine for each other' 🌟")


if __name__ == "__main__":
    asyncio.run(demo_library_integration())
