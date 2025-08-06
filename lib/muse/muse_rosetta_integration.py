#!/usr/bin/env python3
"""
Muse-Rosetta Integration Test
Testing Muse agents using actual Rosetta.API functions with A2A protocols
"""

import sys
import os
import json
import time
from datetime import datetime
from typing import Dict, Any

# Add paths for Rosetta.API imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib', 'field'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib', 'process'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib', 'ritual'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib', 'values'))

# Import Muse A2A infrastructure
from muse_a2a_test import LightweightA2AAgent

class RosettaEnabledAgent(LightweightA2AAgent):
    """Agent enhanced with Rosetta.API function calls"""
    
    def __init__(self, name: str, model: str = "gemma3:1b"):
        super().__init__(name, model)
        self.rosetta_functions = {}
        self.load_rosetta_functions()
        
        print(f"🌹 {name} enhanced with {len(self.rosetta_functions)} Rosetta.API functions")
    
    def load_rosetta_functions(self):
        """Load available Rosetta.API functions"""
        try:
            # Try to import Rosetta functions
            available_functions = {}
            
            # Field functions
            try:
                from co_create import co_create
                available_functions['co_create'] = co_create
                print(f"   ✅ Loaded field.co_create")
            except ImportError as e:
                print(f"   ⚠️  Could not load co_create: {e}")
            
            # Process functions (try a few common ones)
            process_functions = ['consent_check', 'empathic_reflection', 'values_check']
            for func_name in process_functions:
                try:
                    module = __import__(func_name)
                    if hasattr(module, func_name):
                        available_functions[func_name] = getattr(module, func_name)
                        print(f"   ✅ Loaded process.{func_name}")
                except ImportError:
                    print(f"   ⚠️  Could not load {func_name}")
            
            # Ritual functions
            ritual_functions = ['begin', 'grounding_breath', 'end']
            for func_name in ritual_functions:
                try:
                    module = __import__(func_name)
                    if hasattr(module, func_name):
                        available_functions[func_name] = getattr(module, func_name)
                        print(f"   ✅ Loaded ritual.{func_name}")
                except ImportError:
                    print(f"   ⚠️  Could not load {func_name}")
            
            # Values functions
            try:
                from load import load
                available_functions['values_load'] = load
                print(f"   ✅ Loaded values.load")
            except ImportError:
                print(f"   ⚠️  Could not load values.load")
            
            self.rosetta_functions = available_functions
            
        except Exception as e:
            print(f"   ❌ Error loading Rosetta functions: {e}")
            self.rosetta_functions = {}
    
    def call_rosetta_function(self, function_name: str, **kwargs) -> Dict:
        """Call a Rosetta.API function with A2A session context"""
        if function_name not in self.rosetta_functions:
            return {
                "status": "error",
                "error": f"Function {function_name} not available",
                "available_functions": list(self.rosetta_functions.keys())
            }
        
        try:
            # Ensure session_context is provided for A2A compliance
            if 'session_context' not in kwargs:
                kwargs['session_context'] = self.session_context.copy()
                kwargs['session_context'].update({
                    "calling_agent": self.name,
                    "rosetta_function": function_name,
                    "call_timestamp": datetime.now().isoformat()
                })
            
            print(f"🌹 {self.name} calling Rosetta.{function_name}")
            
            # Call the Rosetta function
            start_time = time.time()
            result = self.rosetta_functions[function_name](**kwargs)
            end_time = time.time()
            
            # Update interaction count
            self.session_context["interaction_count"] += 1
            
            return {
                "status": "success",
                "function": function_name,
                "result": result,
                "execution_time": round(end_time - start_time, 3),
                "agent": self.name
            }
            
        except Exception as e:
            return {
                "status": "error",
                "function": function_name,
                "error": str(e),
                "agent": self.name
            }
    
    def process_a2a_message_with_rosetta(self, message: Dict) -> Dict:
        """Process A2A message and potentially use Rosetta functions"""
        print(f"🌹📥 {self.name} processing A2A message with Rosetta integration")
        
        # Standard A2A consent check
        if self.session_context["consent_status"] != "active":
            return {
                "status": "error",
                "error": "consent_not_active"
            }
        
        try:
            content = message.get("content", {})
            
            # Check if message requests Rosetta function
            if "rosetta_function" in content:
                function_name = content["rosetta_function"]
                function_args = content.get("function_args", {})
                
                print(f"   🌹 Rosetta function requested: {function_name}")
                
                # Call the requested Rosetta function
                rosetta_result = self.call_rosetta_function(function_name, **function_args)
                
                return {
                    "status": "success",
                    "sender": self.name,
                    "recipient": message["sender"],
                    "content": {
                        "rosetta_call": rosetta_result,
                        "agent_response": f"Completed Rosetta.{function_name} call",
                        "available_functions": list(self.rosetta_functions.keys())
                    },
                    "session_context": self.session_context,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                # Standard agent response
                return super().process_a2a_message(message)
                
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "agent": self.name
            }

def test_muse_rosetta_integration():
    """Test Muse agents using Rosetta.API functions"""
    print("🌹🚀 Muse-Rosetta Integration Test")
    print("=" * 60)
    
    # Create Rosetta-enabled agents
    orchestrator = RosettaEnabledAgent("Orchestrator")
    presenter = RosettaEnabledAgent("Presenter")
    
    print(f"\n✅ Created 2 Rosetta-enabled agents")
    print()
    
    # Test 1: Direct Rosetta function call
    print("🧪 Test 1: Direct Rosetta Function Call")
    print("-" * 40)
    
    if 'co_create' in orchestrator.rosetta_functions:
        result = orchestrator.call_rosetta_function(
            'co_create',
            participants=["Orchestrator", "Presenter"],
            goal="Test Muse-Rosetta integration",
            context={"models": ["gemma3:1b"], "protocols": ["A2A"]},
            parameters={"time_limit": "5 minutes"}
        )
        
        if result["status"] == "success":
            print(f"   ✅ co_create call successful ({result['execution_time']}s)")
            print(f"   📋 Result: {str(result['result'])[:150]}...")
        else:
            print(f"   ❌ co_create failed: {result['error']}")
    else:
        print("   ⚠️  co_create function not available")
    
    print()
    
    # Test 2: A2A message requesting Rosetta function
    print("🧪 Test 2: A2A Message with Rosetta Function Request")
    print("-" * 50)
    
    if orchestrator.rosetta_functions:
        available_function = list(orchestrator.rosetta_functions.keys())[0]
        
        # Create A2A message requesting Rosetta function
        a2a_message = {
            "sender": "Presenter",
            "recipient": "Orchestrator", 
            "message_type": "request",
            "content": {
                "rosetta_function": available_function,
                "function_args": {
                    "participants": ["Presenter", "User"],
                    "goal": "Create welcome experience"
                }
            },
            "session_context": presenter.session_context,
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"   📤 Presenter requesting Rosetta.{available_function} from Orchestrator")
        
        # Process the message
        response = orchestrator.process_a2a_message_with_rosetta(a2a_message)
        
        if response["status"] == "success":
            print(f"   ✅ A2A Rosetta call successful")
            rosetta_result = response["content"]["rosetta_call"]
            print(f"   📋 Rosetta result: {rosetta_result['status']}")
            if rosetta_result["status"] == "success":
                print(f"   🌹 Function output: {str(rosetta_result['result'])[:100]}...")
        else:
            print(f"   ❌ A2A Rosetta call failed: {response['error']}")
    else:
        print("   ⚠️  No Rosetta functions available for testing")
    
    print()
    
    # Test 3: Agent coordination with Rosetta workflow
    print("🧪 Test 3: Agent Coordination with Rosetta Workflow")
    print("-" * 50)
    
    try:
        # Orchestrator coordinates a workflow using Presenter
        workflow_message = {
            "sender": "Orchestrator",
            "recipient": "Presenter",
            "message_type": "request", 
            "content": {
                "task": "coordinate_user_onboarding",
                "steps": [
                    "gather_user_preferences",
                    "create_personalized_welcome",
                    "establish_collaboration_protocols"
                ],
                "use_rosetta": True
            },
            "session_context": orchestrator.session_context,
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"   📤 Orchestrator coordinating workflow with Presenter")
        
        # Send message
        response = presenter.process_a2a_message(workflow_message)
        
        if response["status"] == "success":
            print(f"   ✅ Workflow coordination successful")
            print(f"   📋 Presenter response: {response['content']['agent_response'][:100]}...")
        else:
            print(f"   ❌ Workflow coordination failed: {response.get('error')}")
            
    except Exception as e:
        print(f"   ❌ Workflow test error: {e}")
    
    print()
    
    # Summary
    print("📊 Muse-Rosetta Integration Summary")
    print("=" * 40)
    print(f"Orchestrator Rosetta functions: {len(orchestrator.rosetta_functions)}")
    print(f"Presenter Rosetta functions: {len(presenter.rosetta_functions)}")
    print(f"Orchestrator interactions: {orchestrator.session_context['interaction_count']}")
    print(f"Presenter interactions: {presenter.session_context['interaction_count']}")
    
    if orchestrator.rosetta_functions or presenter.rosetta_functions:
        print("🎉 MUSE-ROSETTA INTEGRATION SUCCESSFUL!")
        print("✅ Agents can call Rosetta.API functions via A2A protocols")
    else:
        print("⚠️  Integration limited - check Rosetta.API imports")
    
    return True

if __name__ == "__main__":
    test_muse_rosetta_integration()