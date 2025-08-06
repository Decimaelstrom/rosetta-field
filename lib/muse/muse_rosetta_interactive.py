#!/usr/bin/env python3
"""
Interactive Muse-Rosetta Session
Live demonstration with persistent agents and real-time usage information
"""

import sys
import os
import json
import time
import threading
from datetime import datetime
from typing import Dict, Any

# Add paths for Rosetta.API imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib', 'field'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib', 'process'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib', 'ritual'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib', 'values'))

from muse_rosetta_integration import RosettaEnabledAgent

class InteractiveMuseSession:
    """Interactive session manager for Muse-Rosetta agents"""
    
    def __init__(self):
        self.agents = {}
        self.session_active = False
        self.session_start_time = None
        self.command_history = []
        self.usage_stats = {
            "total_a2a_messages": 0,
            "total_rosetta_calls": 0,
            "successful_operations": 0,
            "failed_operations": 0,
            "session_duration": 0
        }
        
    def initialize_agents(self):
        """Initialize the Muse agents with Rosetta integration"""
        print("🌹🚀 Initializing Interactive Muse-Rosetta Session")
        print("=" * 60)
        
        # Create agents
        self.agents['orchestrator'] = RosettaEnabledAgent("Orchestrator", "gemma3:1b")
        self.agents['presenter'] = RosettaEnabledAgent("Presenter", "gemma3:1b")
        
        self.session_active = True
        self.session_start_time = time.time()
        
        print(f"\n✅ Session initialized with {len(self.agents)} agents")
        print("📡 Models are loaded and ready for interaction")
        print()
        
    def show_usage_info(self):
        """Display current usage statistics"""
        if not self.session_active:
            print("❌ Session not active")
            return
            
        current_time = time.time()
        self.usage_stats["session_duration"] = round(current_time - self.session_start_time, 1)
        
        print("📊 LIVE USAGE INFORMATION")
        print("=" * 40)
        print(f"Session Duration: {self.usage_stats['session_duration']}s")
        print(f"A2A Messages Sent: {self.usage_stats['total_a2a_messages']}")
        print(f"Rosetta Function Calls: {self.usage_stats['total_rosetta_calls']}")
        print(f"Successful Operations: {self.usage_stats['successful_operations']}")
        print(f"Failed Operations: {self.usage_stats['failed_operations']}")
        
        if self.usage_stats['total_a2a_messages'] > 0:
            success_rate = (self.usage_stats['successful_operations'] / 
                          (self.usage_stats['successful_operations'] + self.usage_stats['failed_operations'])) * 100
            print(f"Success Rate: {success_rate:.1f}%")
        
        print()
        
        # Agent-specific stats
        print("🤖 AGENT STATUS")
        print("-" * 20)
        for name, agent in self.agents.items():
            interactions = agent.session_context.get("interaction_count", 0)
            consent = agent.session_context.get("consent_status", "unknown")
            functions = len(agent.rosetta_functions)
            print(f"{agent.name}:")
            print(f"  Interactions: {interactions}")
            print(f"  Consent Status: {consent}")
            print(f"  Rosetta Functions: {functions}")
            print(f"  Model: {agent.model}")
        print()
    
    def list_available_commands(self):
        """Show available interactive commands"""
        print("🎮 AVAILABLE COMMANDS")
        print("=" * 30)
        print("1. 'status' - Show current usage information")
        print("2. 'agents' - List available agents and their functions")
        print("3. 'test_a2a' - Send a test A2A message between agents")
        print("4. 'test_rosetta <function>' - Test a specific Rosetta function")
        print("5. 'workflow' - Run a complex workflow demonstration")
        print("6. 'history' - Show command history")
        print("7. 'help' - Show this command list")
        print("8. 'close' - Close the session and stop models")
        print()
        
    def list_agents_and_functions(self):
        """List all agents and their available Rosetta functions"""
        print("🤖 AGENTS & ROSETTA FUNCTIONS")
        print("=" * 40)
        
        for name, agent in self.agents.items():
            print(f"\n{agent.name} ({agent.model}):")
            print(f"  Available Rosetta Functions:")
            for func_name in agent.rosetta_functions.keys():
                print(f"    - {func_name}")
        print()
    
    def test_a2a_message(self):
        """Send a test A2A message between agents"""
        print("📤 TESTING A2A MESSAGE")
        print("-" * 25)
        
        orchestrator = self.agents['orchestrator']
        presenter = self.agents['presenter']
        
        # Create test message
        test_message = {
            "sender": "Orchestrator",
            "recipient": "Presenter",
            "message_type": "request",
            "content": {
                "task": "create_status_report",
                "priority": "medium",
                "details": "Generate a brief status report for the current session"
            },
            "session_context": orchestrator.session_context,
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"Sending: {orchestrator.name} → {presenter.name}")
        print(f"Content: {test_message['content']['task']}")
        
        try:
            start_time = time.time()
            response = presenter.process_a2a_message(test_message)
            end_time = time.time()
            
            self.usage_stats["total_a2a_messages"] += 1
            
            if response.get("status") == "success":
                self.usage_stats["successful_operations"] += 1
                print(f"✅ A2A message successful ({end_time - start_time:.2f}s)")
                agent_response = response.get("content", {}).get("agent_response", "")
                print(f"📝 Response preview: {agent_response[:150]}...")
            else:
                self.usage_stats["failed_operations"] += 1
                print(f"❌ A2A message failed: {response.get('error', 'unknown')}")
                
        except Exception as e:
            self.usage_stats["failed_operations"] += 1
            print(f"❌ Exception during A2A test: {e}")
        
        print()
        
    def test_rosetta_function(self, function_name: str):
        """Test a specific Rosetta function"""
        print(f"🌹 TESTING ROSETTA FUNCTION: {function_name}")
        print("-" * 40)
        
        orchestrator = self.agents['orchestrator']
        
        if function_name not in orchestrator.rosetta_functions:
            print(f"❌ Function '{function_name}' not available")
            print(f"Available functions: {list(orchestrator.rosetta_functions.keys())}")
            return
        
        # Prepare test arguments based on function
        test_args = {}
        if function_name == "co_create":
            test_args = {
                "participants": ["Orchestrator", "Presenter", "User"],
                "goal": f"Test {function_name} function in interactive session",
                "context": {"session_type": "interactive_demo"},
                "parameters": {"demo_mode": True}
            }
        elif function_name == "consent_check":
            test_args = {
                "participant": "User",
                "action": "function_testing",
                "consent_level": "Level_1"
            }
        else:
            # Generic test args
            test_args = {
                "participants": ["Orchestrator", "Presenter"]
            }
        
        print(f"Calling: {orchestrator.name}.{function_name}()")
        print(f"Arguments: {json.dumps(test_args, indent=2)}")
        
        try:
            start_time = time.time()
            result = orchestrator.call_rosetta_function(function_name, **test_args)
            end_time = time.time()
            
            self.usage_stats["total_rosetta_calls"] += 1
            
            if result.get("status") == "success":
                self.usage_stats["successful_operations"] += 1
                print(f"✅ Rosetta call successful ({result.get('execution_time', 0):.3f}s)")
                print(f"📋 Result: {json.dumps(result['result'], indent=2)}")
            else:
                self.usage_stats["failed_operations"] += 1
                print(f"❌ Rosetta call failed: {result.get('error', 'unknown')}")
                
        except Exception as e:
            self.usage_stats["failed_operations"] += 1
            print(f"❌ Exception during Rosetta test: {e}")
        
        print()
        
    def run_workflow_demo(self):
        """Run a complex workflow demonstration"""
        print("🎭 COMPLEX WORKFLOW DEMONSTRATION")
        print("=" * 45)
        
        orchestrator = self.agents['orchestrator']
        presenter = self.agents['presenter']
        
        workflow_steps = [
            {
                "step": 1,
                "action": "Initialize co-creation session",
                "type": "rosetta_call",
                "function": "co_create",
                "agent": orchestrator
            },
            {
                "step": 2, 
                "action": "Request status report from Presenter",
                "type": "a2a_message",
                "sender": orchestrator,
                "recipient": presenter
            },
            {
                "step": 3,
                "action": "Validate consent for workflow",
                "type": "rosetta_call", 
                "function": "consent_check",
                "agent": presenter
            }
        ]
        
        successful_steps = 0
        
        for step_info in workflow_steps:
            print(f"Step {step_info['step']}: {step_info['action']}")
            
            try:
                if step_info['type'] == 'rosetta_call':
                    # Rosetta function call
                    agent = step_info['agent']
                    func_name = step_info['function']
                    
                    if func_name == "co_create":
                        args = {
                            "participants": ["Orchestrator", "Presenter"],
                            "goal": "Workflow demonstration",
                            "context": {"demo": True}
                        }
                    elif func_name == "consent_check":
                        args = {
                            "participant": "User", 
                            "action": "workflow_validation",
                            "consent_level": "Level_1"
                        }
                    else:
                        args = {"participants": ["Orchestrator", "Presenter"]}
                    
                    result = agent.call_rosetta_function(func_name, **args)
                    self.usage_stats["total_rosetta_calls"] += 1
                    
                    if result.get("status") == "success":
                        print(f"   ✅ {func_name} completed successfully")
                        successful_steps += 1
                        self.usage_stats["successful_operations"] += 1
                    else:
                        print(f"   ❌ {func_name} failed: {result.get('error')}")
                        self.usage_stats["failed_operations"] += 1
                        
                elif step_info['type'] == 'a2a_message':
                    # A2A message
                    message = {
                        "sender": step_info['sender'].name,
                        "recipient": step_info['recipient'].name,
                        "message_type": "request",
                        "content": {
                            "task": "workflow_status_check",
                            "step": step_info['step']
                        },
                        "session_context": step_info['sender'].session_context,
                        "timestamp": datetime.now().isoformat()
                    }
                    
                    response = step_info['recipient'].process_a2a_message(message)
                    self.usage_stats["total_a2a_messages"] += 1
                    
                    if response.get("status") == "success":
                        print(f"   ✅ A2A message delivered successfully")
                        successful_steps += 1
                        self.usage_stats["successful_operations"] += 1
                    else:
                        print(f"   ❌ A2A message failed: {response.get('error')}")
                        self.usage_stats["failed_operations"] += 1
                
                time.sleep(0.5)  # Brief pause between steps
                
            except Exception as e:
                print(f"   ❌ Step {step_info['step']} exception: {e}")
                self.usage_stats["failed_operations"] += 1
        
        print(f"\n📊 Workflow Results: {successful_steps}/{len(workflow_steps)} steps completed")
        print()
        
    def show_command_history(self):
        """Show command history"""
        print("📜 COMMAND HISTORY")
        print("-" * 20)
        if not self.command_history:
            print("No commands executed yet")
        else:
            for i, cmd in enumerate(self.command_history, 1):
                print(f"{i}. {cmd}")
        print()
        
    def close_session(self):
        """Close the session and cleanup"""
        print("🛑 CLOSING MUSE-ROSETTA SESSION")
        print("=" * 40)
        
        if self.session_active:
            final_duration = time.time() - self.session_start_time
            self.usage_stats["session_duration"] = round(final_duration, 1)
            
            print("📊 FINAL SESSION STATISTICS")
            print("-" * 30)
            self.show_usage_info()
            
            # Reset agent states
            for agent in self.agents.values():
                agent.session_context["consent_status"] = "revoked"
            
            self.session_active = False
            print("✅ Session closed successfully")
            print("🔴 Models are no longer active")
        else:
            print("❌ No active session to close")
        
        print()
        
    def run_interactive_session(self):
        """Main interactive session loop"""
        self.initialize_agents()
        self.list_available_commands()
        
        print("🎮 INTERACTIVE MODE ACTIVE")
        print("Type commands below ('help' for options, 'close' to exit)")
        print("=" * 55)
        
        while self.session_active:
            try:
                command = input("🌹 Muse-Rosetta> ").strip().lower()
                
                if not command:
                    continue
                    
                self.command_history.append(command)
                
                if command == "status":
                    self.show_usage_info()
                    
                elif command == "agents":
                    self.list_agents_and_functions()
                    
                elif command == "test_a2a":
                    self.test_a2a_message()
                    
                elif command.startswith("test_rosetta"):
                    parts = command.split()
                    if len(parts) > 1:
                        function_name = parts[1]
                        self.test_rosetta_function(function_name)
                    else:
                        print("Usage: test_rosetta <function_name>")
                        print("Available functions:", list(self.agents['orchestrator'].rosetta_functions.keys()))
                        
                elif command == "workflow":
                    self.run_workflow_demo()
                    
                elif command == "history":
                    self.show_command_history()
                    
                elif command == "help":
                    self.list_available_commands()
                    
                elif command == "close":
                    self.close_session()
                    break
                    
                else:
                    print(f"Unknown command: '{command}'. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print("\n🔴 Session interrupted by user")
                self.close_session()
                break
            except Exception as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    session = InteractiveMuseSession()
    session.run_interactive_session()