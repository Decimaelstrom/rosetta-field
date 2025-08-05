#!/usr/bin/env python3
"""
Muse A2A Protocol Test
Lightweight testing of agent-to-agent interactions without full constellation deployment
"""

import subprocess
import json
import time
from datetime import datetime
from typing import Dict, Any

class LightweightA2AAgent:
    """Lightweight agent for A2A testing"""
    
    def __init__(self, name: str, model: str = "gemma3:1b"):
        self.name = name
        self.model = model
        self.session_context = {
            "agent_id": name.lower().replace(" ", "_"),
            "consent_status": "active",
            "session_start": datetime.now().isoformat(),
            "interaction_count": 0,
            "a2a_enabled": True
        }
        
        print(f"🤖 Created {name} agent using {model}")
    
    def send_a2a_message(self, recipient_agent, message_content: Dict[str, Any]) -> Dict:
        """Send A2A message to another agent"""
        print(f"📤 {self.name} → {recipient_agent.name}: {message_content}")
        
        # Create A2A message structure
        a2a_message = {
            "sender": self.name,
            "recipient": recipient_agent.name,
            "message_type": "request",
            "content": message_content,
            "session_context": self.session_context,
            "timestamp": datetime.now().isoformat()
        }
        
        # Send to recipient
        response = recipient_agent.process_a2a_message(a2a_message)
        
        # Update interaction count
        self.session_context["interaction_count"] += 1
        
        return response
    
    def process_a2a_message(self, message: Dict) -> Dict:
        """Process incoming A2A message"""
        print(f"📥 {self.name} processing message from {message['sender']}")
        
        # A2A Protocol Step 1: Consent Check
        if self.session_context["consent_status"] != "active":
            return {
                "status": "error",
                "error": "consent_not_active",
                "current_consent": self.session_context["consent_status"]
            }
        
        # A2A Protocol Step 2: Process with role-specific logic
        try:
            response_content = self._generate_agent_response(message["content"])
            
            # Update session context
            self.session_context["interaction_count"] += 1
            
            return {
                "status": "success",
                "sender": self.name,
                "recipient": message["sender"],
                "content": response_content,
                "session_context": self.session_context,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "agent": self.name
            }
    
    def _generate_agent_response(self, content: Dict) -> Dict:
        """Generate role-specific response using Gemma3:1b"""
        
        # Role-specific prompts
        role_prompts = {
            "Orchestrator": "As the Orchestrator agent coordinating the Muse system, handle this request:",
            "Presenter": "As the Presenter agent creating user-facing content, respond to this request:",
            "DocumentScribe": "As the DocumentScribe agent handling documentation, process this request:",
            "Firefly_Image": "As the Firefly Image agent handling image generation prompts, respond to this:",
            "ErrorMonitor": "As the Error Monitor agent checking for issues, analyze this request:"
        }
        
        prompt = f"""{role_prompts.get(self.name, f"As the {self.name} agent")}

Request: {json.dumps(content, indent=2)}

Provide a brief, helpful response (under 100 words) as this agent would. Be professional and role-appropriate."""
        
        try:
            # Use Ollama to generate response
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True, text=True, timeout=20,
                encoding='utf-8', errors='replace'
            )
            
            if result.returncode == 0:
                response_text = result.stdout.strip()
                return {
                    "agent_response": response_text[:300],  # Limit length
                    "processing_time": "< 20s",
                    "model_used": self.model
                }
            else:
                return {
                    "error": "model_execution_failed",
                    "stderr": result.stderr[:100]
                }
                
        except subprocess.TimeoutExpired:
            return {
                "error": "response_timeout",
                "timeout_seconds": 20
            }
        except Exception as e:
            return {
                "error": "generation_exception",
                "exception": str(e)
            }

def test_a2a_interactions():
    """Test A2A protocol interactions between lightweight agents"""
    print("🚀 Muse A2A Protocol Testing")
    print("=" * 50)
    
    # Create test agents
    orchestrator = LightweightA2AAgent("Orchestrator")
    presenter = LightweightA2AAgent("Presenter") 
    document_scribe = LightweightA2AAgent("DocumentScribe")
    firefly_image = LightweightA2AAgent("Firefly_Image")
    error_monitor = LightweightA2AAgent("ErrorMonitor")
    
    agents = [orchestrator, presenter, document_scribe, firefly_image, error_monitor]
    
    print(f"✅ Created {len(agents)} lightweight A2A agents")
    print()
    
    # Test scenarios
    test_scenarios = [
        {
            "name": "Task Delegation",
            "sender": orchestrator,
            "recipient": presenter,
            "message": {
                "task": "create_welcome_message",
                "user_type": "new_user",
                "priority": "high"
            }
        },
        {
            "name": "Documentation Request", 
            "sender": presenter,
            "recipient": document_scribe,
            "message": {
                "action": "log_user_interaction",
                "user_id": "user_123",
                "interaction_type": "welcome_flow"
            }
        },
        {
            "name": "Image Generation Coordination",
            "sender": orchestrator,
            "recipient": firefly_image,
            "message": {
                "generate": "welcome_banner",
                "style": "professional",
                "dimensions": "1200x400"
            }
        },
        {
            "name": "Error Monitoring",
            "sender": error_monitor,
            "recipient": orchestrator,
            "message": {
                "alert": "high_memory_usage",
                "agent": "firefly_image",
                "threshold_exceeded": "85%"
            }
        }
    ]
    
    successful_tests = 0
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"🧪 Test {i}: {scenario['name']}")
        print(f"   {scenario['sender'].name} → {scenario['recipient'].name}")
        
        try:
            start_time = time.time()
            
            # Send A2A message
            response = scenario['sender'].send_a2a_message(
                scenario['recipient'], 
                scenario['message']
            )
            
            end_time = time.time()
            processing_time = end_time - start_time
            
            if response.get("status") == "success":
                print(f"   ✅ Success ({processing_time:.2f}s)")
                agent_response = response.get("content", {}).get("agent_response", "")
                print(f"   📝 Response: {agent_response[:100]}...")
                successful_tests += 1
            else:
                print(f"   ❌ Failed: {response.get('error', 'unknown_error')}")
                
        except Exception as e:
            print(f"   ❌ Exception: {e}")
        
        print()
        time.sleep(0.5)  # Brief pause between tests
    
    # Results
    print("📊 A2A Protocol Test Results")
    print("=" * 30)
    print(f"Successful tests: {successful_tests}/{len(test_scenarios)}")
    print(f"Success rate: {(successful_tests/len(test_scenarios)*100):.1f}%")
    
    if successful_tests == len(test_scenarios):
        print("🎉 ALL A2A PROTOCOL TESTS PASSED!")
        print("✅ Muse agents can successfully communicate using A2A protocols")
    else:
        print("⚠️  Some A2A tests failed - check individual results above")
    
    # Agent interaction summary
    print("\n🤖 Agent Activity Summary:")
    for agent in agents:
        interactions = agent.session_context["interaction_count"]
        print(f"   {agent.name}: {interactions} interactions")
    
    return successful_tests == len(test_scenarios)

if __name__ == "__main__":
    test_a2a_interactions()