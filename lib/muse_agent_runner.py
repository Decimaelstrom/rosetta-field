#!/usr/bin/env python3
"""
Muse Agent Runner
Deploys and manages the Muse agent constellation with A2A protocol integration
"""

import asyncio
import json
import time
import threading
import queue
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import subprocess
import requests
from pathlib import Path

# Import our Rosetta.API A2A infrastructure
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from muse_local_orchestrator import MuseLocalOrchestrator, AgentConfig

@dataclass
class A2AMessage:
    """A2A protocol message structure"""
    sender: str
    recipient: str
    message_type: str  # "request", "response", "notification"
    content: Any
    session_context: Dict
    timestamp: str
    message_id: str

@dataclass
class AgentState:
    """Current state of a running agent"""
    name: str
    model: str
    status: str  # "starting", "running", "paused", "stopped", "error"
    process_id: Optional[int]
    last_activity: str
    message_queue: queue.Queue
    consent_status: str  # A2A consent status
    session_context: Dict

class MuseAgent:
    """Individual agent with A2A protocol support"""
    
    def __init__(self, config: AgentConfig, runner_instance):
        self.config = config
        self.runner = runner_instance
        self.state = AgentState(
            name=config.name,
            model=config.model.name,
            status="stopped",
            process_id=None,
            last_activity=datetime.now().isoformat(),
            message_queue=queue.Queue(),
            consent_status="pending",
            session_context={
                "agent_id": config.name.lower().replace(" ", "_"),
                "consent_status": "pending",
                "session_start": datetime.now().isoformat(),
                "interaction_count": 0,
                "a2a_enabled": True
            }
        )
        self.ollama_process = None
        
    def start(self):
        """Start the agent with A2A protocol initialization"""
        print(f"🚀 Starting {self.config.name} with model {self.config.model.name}")
        
        try:
            # Initialize A2A session context with active consent
            self.state.consent_status = "active"  # Set consent to active
            self.state.session_context.update({
                "consent_status": "active",
                "model_loaded": self.config.model.name,
                "capabilities": ["text_generation", "a2a_protocol"],
                "resource_allocation": {
                    "vram_gb": self.config.model.vram_gb,
                    "ram_gb": self.config.model.ram_gb
                }
            })
            
            # Test model availability with Ollama
            result = subprocess.run(
                ["ollama", "run", self.config.model.name, "Hello, I am initializing as an A2A-enabled agent. Please confirm you can respond."],
                capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace'
            )
            
            if result.returncode == 0:
                self.state.status = "running"
                self.state.last_activity = datetime.now().isoformat()
                self.state.session_context["interaction_count"] += 1
                
                print(f"✅ {self.config.name} initialized successfully")
                print(f"   Model response: {result.stdout.strip()[:100]}...")
                return True
            else:
                self.state.status = "error"
                print(f"❌ {self.config.name} failed to initialize: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            self.state.status = "error"
            print(f"❌ {self.config.name} timeout during initialization")
            return False
        except Exception as e:
            self.state.status = "error"
            print(f"❌ {self.config.name} error: {e}")
            return False
    
    def send_a2a_message(self, recipient: str, message_type: str, content: Any) -> A2AMessage:
        """Send A2A protocol message to another agent"""
        if self.state.consent_status != "active":
            raise ValueError(f"Agent {self.config.name} does not have active consent for A2A interactions")
        
        message = A2AMessage(
            sender=self.config.name,
            recipient=recipient,
            message_type=message_type,
            content=content,
            session_context=self.state.session_context.copy(),
            timestamp=datetime.now().isoformat(),
            message_id=f"{self.config.name}_{int(time.time() * 1000)}"
        )
        
        # Route message through runner
        return self.runner.route_a2a_message(message)
    
    def process_a2a_message(self, message: A2AMessage) -> Optional[A2AMessage]:
        """Process incoming A2A message with consent checks"""
        print(f"📨 {self.config.name} received A2A message from {message.sender}")
        
        # A2A Protocol Step 1: Consent Check
        if self.state.consent_status != "active":
            print(f"⚠️  {self.config.name} rejecting message - consent not active")
            return A2AMessage(
                sender=self.config.name,
                recipient=message.sender,
                message_type="response",
                content={"error": "consent_required", "current_status": self.state.consent_status},
                session_context=self.state.session_context,
                timestamp=datetime.now().isoformat(),
                message_id=f"error_{int(time.time() * 1000)}"
            )
        
        # A2A Protocol Step 2: Context Validation
        if not message.session_context.get("a2a_enabled", False):
            print(f"⚠️  {self.config.name} rejecting message - A2A not enabled in sender context")
            return None
        
        # Process the message content based on type and role
        try:
            if message.message_type == "request":
                response_content = self._generate_response(message.content)
            elif message.message_type == "notification":
                response_content = {"acknowledged": True, "timestamp": datetime.now().isoformat()}
            else:
                response_content = {"received": True}
            
            # Update session context
            self.state.session_context["interaction_count"] += 1
            self.state.last_activity = datetime.now().isoformat()
            
            # Create A2A response
            return A2AMessage(
                sender=self.config.name,
                recipient=message.sender,
                message_type="response",
                content=response_content,
                session_context=self.state.session_context,
                timestamp=datetime.now().isoformat(),
                message_id=f"response_{int(time.time() * 1000)}"
            )
            
        except Exception as e:
            print(f"❌ {self.config.name} error processing message: {e}")
            return None
    
    def _generate_response(self, content: Any) -> Dict:
        """Generate role-appropriate response using Ollama"""
        try:
            # Create role-specific prompt
            role_prompts = {
                "Orchestrator": "As the Orchestrator agent, coordinate and manage this request:",
                "Presenter": "As the Presenter agent, create user-friendly content for this request:",
                "DocumentScribe": "As the DocumentScribe agent, analyze and document this information:",
                "Firefly_Image": "As the Firefly Image agent, help with image-related prompts for this request:",
                "Firefly_Video": "As the Firefly Video agent, help with video-related prompts for this request:",
                "Firefly_Music": "As the Firefly Music agent, help with music-related prompts for this request:",
                "ExportHandler": "As the Export Handler agent, manage data export for this request:",
                "ErrorMonitor": "As the Error Monitor agent, check for issues in this request:"
            }
            
            prompt = f"{role_prompts.get(self.config.name, 'As an AI agent')}\n\nRequest: {json.dumps(content, indent=2)}\n\nProvide a helpful response in JSON format."
            
            result = subprocess.run(
                ["ollama", "run", self.config.model.name, prompt],
                capture_output=True, text=True, timeout=15, encoding='utf-8', errors='replace'
            )
            
            if result.returncode == 0:
                response_text = result.stdout.strip()
                return {
                    "status": "success",
                    "agent_role": self.config.name,
                    "response": response_text[:500],  # Limit response length
                    "processing_time": "< 15s"
                }
            else:
                return {
                    "status": "error",
                    "error": result.stderr.strip()[:200]
                }
                
        except subprocess.TimeoutExpired:
            return {
                "status": "timeout",
                "error": "Response generation timed out"
            }
        except Exception as e:
            return {
                "status": "error", 
                "error": str(e)
            }
    
    def stop(self):
        """Stop the agent gracefully"""
        print(f"🛑 Stopping {self.config.name}")
        self.state.status = "stopped"
        self.state.consent_status = "revoked"

class MuseAgentRunner:
    """Manages the complete Muse agent constellation"""
    
    def __init__(self, deployment_mode: str = "ultra_efficient"):
        self.orchestrator_sys = MuseLocalOrchestrator()
        self.deployment_mode = deployment_mode
        self.agents: Dict[str, MuseAgent] = {}
        self.message_log: List[A2AMessage] = []
        self.running = False
        
        # Validate deployment feasibility
        validation = self.orchestrator_sys.validate_system_resources(deployment_mode)
        if not validation["can_deploy"]:
            raise RuntimeError(f"Cannot deploy in {deployment_mode} mode: {validation['issues']}")
        
        print(f"✅ Muse Agent Runner initialized for {deployment_mode} deployment")
    
    def initialize_agents(self):
        """Initialize all agents for the deployment mode"""
        print(f"🏗️  Initializing Muse agent constellation...")
        
        # Get agent configurations based on deployment mode
        agent_configs = self.orchestrator_sys.agents
        
        if self.deployment_mode == "minimal":
            agent_configs = {k: v for k, v in agent_configs.items() if v.priority == "critical"}
        elif self.deployment_mode == "essential":
            agent_configs = {k: v for k, v in agent_configs.items() if v.priority in ["critical", "high"]}
        elif self.deployment_mode == "minimal_test":
            # Just orchestrator and presenter for basic A2A testing
            agent_configs = {
                k: v for k, v in agent_configs.items() 
                if k in ["orchestrator", "presenter"]
            }
        
        # Create agent instances
        for agent_id, config in agent_configs.items():
            agent = MuseAgent(config, self)
            self.agents[agent_id] = agent
            print(f"   📦 Created {config.name} agent")
        
        print(f"✅ {len(self.agents)} agents created")
    
    def start_constellation(self):
        """Start all agents in the constellation"""
        print(f"🚀 Starting Muse constellation in {self.deployment_mode} mode...")
        
        started_count = 0
        for agent_id, agent in self.agents.items():
            if agent.start():
                started_count += 1
            time.sleep(1)  # Brief delay between starts
        
        if started_count == len(self.agents):
            self.running = True
            print(f"✅ All {started_count} agents started successfully!")
            return True
        else:
            print(f"⚠️  Only {started_count}/{len(self.agents)} agents started")
            return False
    
    def route_a2a_message(self, message: A2AMessage) -> Optional[A2AMessage]:
        """Route A2A message between agents"""
        print(f"🔀 Routing A2A message: {message.sender} → {message.recipient}")
        
        # Log the message
        self.message_log.append(message)
        
        # Find recipient agent
        recipient_agent = None
        for agent in self.agents.values():
            if agent.config.name == message.recipient:
                recipient_agent = agent
                break
        
        if not recipient_agent:
            print(f"❌ Recipient agent {message.recipient} not found")
            return None
        
        # Route message to recipient
        response = recipient_agent.process_a2a_message(message)
        if response:
            self.message_log.append(response)
        
        return response
    
    def test_a2a_interactions(self):
        """Test A2A protocol interactions between agents"""
        print(f"\n🧪 Testing A2A Protocol Interactions")
        print("=" * 50)
        
        if not self.running:
            print("❌ Constellation not running - start agents first")
            return False
        
        test_scenarios = [
            {
                "name": "Orchestrator → Presenter",
                "sender": "orchestrator", 
                "recipient": "Presenter",
                "content": {"task": "Create user greeting", "priority": "high"}
            },
            {
                "name": "Presenter → DocumentScribe", 
                "sender": "presenter",
                "recipient": "DocumentScribe", 
                "content": {"action": "document_user_session", "data": {"user_id": "test_user"}}
            },
            {
                "name": "Orchestrator → Firefly_Image",
                "sender": "orchestrator",
                "recipient": "Firefly_Image", 
                "content": {"generate": "landscape prompt", "style": "photorealistic"}
            }
        ]
        
        successful_tests = 0
        
        for scenario in test_scenarios:
            print(f"\n📋 Test: {scenario['name']}")
            
            try:
                # Find sender agent
                sender_agent = None
                for agent in self.agents.values():
                    if agent.config.name.lower().replace(" ", "_") == scenario["sender"] or agent.config.name == scenario["recipient"]:
                        if agent.config.name.lower().replace(" ", "_") == scenario["sender"]:
                            sender_agent = agent
                            break
                
                if not sender_agent:
                    print(f"   ❌ Sender agent not found")
                    continue
                
                # Send A2A message
                start_time = time.time()
                response = sender_agent.send_a2a_message(
                    scenario["recipient"],
                    "request", 
                    scenario["content"]
                )
                end_time = time.time()
                
                if response:
                    print(f"   ✅ Success ({end_time - start_time:.2f}s)")
                    print(f"      Response: {str(response.content)[:100]}...")
                    successful_tests += 1
                else:
                    print(f"   ❌ No response received")
                    
            except Exception as e:
                print(f"   ❌ Error: {e}")
        
        print(f"\n📊 A2A Test Results: {successful_tests}/{len(test_scenarios)} successful")
        return successful_tests == len(test_scenarios)
    
    def get_constellation_status(self) -> Dict:
        """Get current status of all agents"""
        status = {
            "deployment_mode": self.deployment_mode,
            "constellation_running": self.running,
            "agents": {},
            "a2a_message_count": len(self.message_log),
            "timestamp": datetime.now().isoformat()
        }
        
        for agent_id, agent in self.agents.items():
            status["agents"][agent_id] = {
                "name": agent.config.name,
                "model": agent.state.model,
                "status": agent.state.status,
                "consent_status": agent.state.consent_status,
                "interaction_count": agent.state.session_context.get("interaction_count", 0),
                "last_activity": agent.state.last_activity
            }
        
        return status
    
    def stop_constellation(self):
        """Stop all agents gracefully"""
        print(f"🛑 Stopping Muse constellation...")
        
        for agent_id, agent in self.agents.items():
            agent.stop()
        
        self.running = False
        print(f"✅ Constellation stopped")

def main():
    """Main runner interface"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        deployment_mode = sys.argv[2] if len(sys.argv) > 2 else "ultra_efficient"
        
        try:
            runner = MuseAgentRunner(deployment_mode)
            
            if command == "start":
                runner.initialize_agents()
                success = runner.start_constellation()
                if success:
                    print(f"\n🎯 Muse constellation ready for A2A interactions!")
                    print(f"Use 'python muse_agent_runner.py test {deployment_mode}' to test A2A protocols")
                    
            elif command == "test":
                runner.initialize_agents()
                if runner.start_constellation():
                    time.sleep(2)  # Let agents stabilize
                    runner.test_a2a_interactions()
                    runner.stop_constellation()
                    
            elif command == "status":
                runner.initialize_agents()
                if runner.start_constellation():
                    status = runner.get_constellation_status()
                    print(json.dumps(status, indent=2))
                    runner.stop_constellation()
                    
            else:
                print("Usage: python muse_agent_runner.py [start|test|status] [deployment_mode]")
                
        except RuntimeError as e:
            print(f"❌ {e}")
            
    else:
        # Default: run test
        try:
            runner = MuseAgentRunner("ultra_efficient")
            runner.initialize_agents()
            if runner.start_constellation():
                time.sleep(2)
                runner.test_a2a_interactions()
                runner.stop_constellation()
        except RuntimeError as e:
            print(f"❌ {e}")

if __name__ == "__main__":
    main()