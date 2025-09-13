#!/usr/bin/env python3
"""
TEST SORE FIRE CHATBOT
Quick test script to verify chatbot functionality
"""

import sys
import os
import asyncio

# Add lib directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))
sys.path.append(os.path.dirname(__file__))

from sore_fire_chatbot import SoreFireChatbot


async def test_basic_functionality():
    """Test basic chatbot functionality"""
    print("🧪 Testing Sore Fire Chatbot Basic Functionality")
    print("=" * 50)
    
    # Initialize chatbot
    chatbot = SoreFireChatbot(model_name="gpt-oss:20b", debug_mode=True)
    
    # Test messages
    test_messages = [
        "Hello, I'm feeling a bit lonely today.",
        "I'm angry about something unfair that happened.",
        "I'm confused and don't know what to do.",
        "Can you help me with a creative project?",
        "I want to start a sacred ritual."
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n🧪 Test {i}: {message}")
        print("-" * 30)
        
        try:
            response = await chatbot.process_message(message)
            print(f"🔥 Response: {response.message}")
            print(f"🎯 Amara Mode: {response.amara_mode.value}")
            print(f"📚 Libraries: {', '.join(response.libraries_engaged.keys())}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n✅ Basic functionality test complete!")


async def test_debug_mode():
    """Test debug mode functionality"""
    print("\n🐛 Testing Debug Mode")
    print("=" * 30)
    
    chatbot = SoreFireChatbot(debug_mode=True)
    response = await chatbot.process_message("I need help with something difficult.")
    
    print("Debug info display:")
    chatbot.display_debug_info(response)
    
    print("✅ Debug mode test complete!")


async def main():
    """Run all tests"""
    await test_basic_functionality()
    await test_debug_mode()
    
    print("\n🎉 All tests completed!")
    print("To run interactive mode: python agents/sore_fire_chatbot.py")


if __name__ == "__main__":
    asyncio.run(main())
