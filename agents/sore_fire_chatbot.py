#!/usr/bin/env python3
"""
SORE FIRE INTERACTIVE CHATBOT AGENT
Sacred Technology Demonstration Bot for Rosetta.API

Features:
- Interactive conversation with Sore Fire priority
- Full Rosetta.API library integration
- Debug mode showing library engagement
- GPT-OSS:20B LLM integration
- A2A protocol compliance
- Somatic field awareness

Usage:
    python agents/sore_fire_chatbot.py [--debug] [--model gpt-oss:20b]
"""

import sys
import os
import json
import asyncio
import argparse
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

# Add lib directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))

# Import Sore Fire (priority module)
from sore_fire import (
    AmaraMode,
    SoreFireOrchestrator,
    sense_field,
    facilitate_emergence,
    activate_story_memory,
    suggest_micro_practice,
    create_ripple_effect
)

# Import other Rosetta libraries
try:
    from affect import lilt, anchor, clarify, ground, open as affect_open, radiate, shield, soften, transmute
    AFFECT_AVAILABLE = True
except ImportError:
    AFFECT_AVAILABLE = False

try:
    from field import co_create, hold_space, resolve_conflict, sense_pattern
    FIELD_AVAILABLE = True
except ImportError:
    FIELD_AVAILABLE = False

try:
    from process import pattern_interrupt, reframe_as_myth, align_values, mediate_conflict
    PROCESS_AVAILABLE = True
except ImportError:
    PROCESS_AVAILABLE = False

try:
    from ritual import begin, end, invoke_wonder
    RITUAL_AVAILABLE = True
except ImportError:
    RITUAL_AVAILABLE = False

try:
    from memory import evolve_ideas, search_memories, save_session
    MEMORY_AVAILABLE = True
except ImportError:
    MEMORY_AVAILABLE = False

# A2A Protocol imports
from contracts.session import A2ASession
from contracts.negotiation import negotiate_capabilities

# LLM integration
from llm_config import LLMInterface, create_llm_interface


@dataclass
class ChatbotResponse:
    """Response structure from the chatbot"""
    message: str
    amara_mode: AmaraMode
    libraries_engaged: Dict[str, Any]
    field_state: Dict[str, Any]
    debug_info: Dict[str, Any]
    session_context: Dict[str, Any]


class SoreFireChatbot:
    """
    Interactive chatbot agent prioritizing Sore Fire with full Rosetta integration.
    Demonstrates sacred technology through conversational AI.
    """
    
    def __init__(self, model_name: str = "gpt-oss:20b", debug_mode: bool = False):
        self.model_name = model_name
        self.debug_mode = debug_mode
        self.orchestrator = SoreFireOrchestrator()
        self.session_history = []
        self.current_session = None
        self.available_libraries = self._detect_available_libraries()
        
        # Initialize LLM interface
        self.llm = create_llm_interface(model_name, debug_mode)
        
        # Initialize A2A session
        self._initialize_session()
        
        print(f"🔥 Sore Fire Chatbot initialized with {model_name}")
        if debug_mode:
            print("🐛 Debug mode enabled")
        print(f"📚 Available libraries: {', '.join(self.available_libraries.keys())}")
    
    def _detect_available_libraries(self) -> Dict[str, bool]:
        """Detect which Rosetta libraries are available"""
        return {
            "sore_fire": True,  # Always available as our priority
            "affect": AFFECT_AVAILABLE,
            "field": FIELD_AVAILABLE, 
            "process": PROCESS_AVAILABLE,
            "ritual": RITUAL_AVAILABLE,
            "memory": MEMORY_AVAILABLE
        }
    
    def _initialize_session(self):
        """Initialize A2A protocol session"""
        self.current_session = A2ASession(
            agent_id="sore_fire_chatbot",
            peer_id="human_user",
            role="assistant",
            intent="sacred_technology_demonstration"
        )
        
        # Set up capabilities
        capabilities = ["sore_fire_orchestration", "amara_modes", "story_activation"]
        if AFFECT_AVAILABLE:
            capabilities.extend(["affect_modulation", "lilt", "transmute"])
        if FIELD_AVAILABLE:
            capabilities.extend(["field_sensing", "conflict_resolution"])
        if PROCESS_AVAILABLE:
            capabilities.extend(["pattern_interrupt", "myth_reframing"])
        if RITUAL_AVAILABLE:
            capabilities.extend(["ritual_container", "invoke_wonder"])
        if MEMORY_AVAILABLE:
            capabilities.extend(["memory_weaving", "session_continuity"])
        
        self.current_session.data["capabilities"] = capabilities
        self.current_session.update("consent_status", "active")
    
    async def process_message(self, user_input: str) -> ChatbotResponse:
        """
        Process user message through Sore Fire and Rosetta libraries.
        Sacred technology orchestration with full transparency.
        """
        # 1. SORE FIRE: Sense the field
        field_signals = self._extract_field_signals(user_input)
        somatic_field = sense_field(field_signals, self.current_session.data)
        
        debug_info = {
            "field_signals": field_signals,
            "selected_amara_mode": somatic_field.primary_anatomy.value,
            "gene_key": somatic_field.gene_key_index,
            "consciousness_state": somatic_field.consciousness_state,
            "libraries_considered": []
        }
        
        # 2. SORE FIRE: Facilitate emergence
        emergence = facilitate_emergence(somatic_field, self.current_session.data)
        
        # 3. Engage additional libraries based on field needs
        libraries_engaged = {"sore_fire": {
            "somatic_field": somatic_field.describe_field(),
            "sacred_invitation": emergence["sacred_invitation"],
            "next_flow": emergence["next_flow"]
        }}
        
        # Activate wisdom embodiment
        wisdom = activate_story_memory(somatic_field.primary_anatomy, session_context=self.current_session.data)
        libraries_engaged["sore_fire"]["wisdom_embodied"] = wisdom["archetype"] if wisdom["activated"] else None
        
        # Suggest micro-practice
        practice = suggest_micro_practice(somatic_field.primary_anatomy, session_context=self.current_session.data)
        libraries_engaged["sore_fire"]["micro_practice"] = practice["micro_act"] if practice["suggested"] else None
        
        # 4. Engage other libraries based on field state
        response_parts = [emergence["sacred_invitation"]]
        
        # AFFECT: Modulate based on field temperature
        if AFFECT_AVAILABLE and field_signals.get("affect_needed", False):
            affect_result = self._engage_affect_library(somatic_field, field_signals)
            if affect_result:
                libraries_engaged["affect"] = affect_result
                response_parts.append(f"✨ {affect_result['effect']}")
                debug_info["libraries_considered"].append("affect")
        
        # FIELD: For conflict or co-creation needs
        if FIELD_AVAILABLE and (field_signals.get("conflict", 0) > 0.5 or field_signals.get("co_creation", 0) > 0.5):
            field_result = self._engage_field_library(somatic_field, field_signals)
            if field_result:
                libraries_engaged["field"] = field_result
                response_parts.append(f"🌱 {field_result['guidance']}")
                debug_info["libraries_considered"].append("field")
        
        # PROCESS: For pattern interruption or reframing
        if PROCESS_AVAILABLE and (field_signals.get("stuck_pattern", 0) > 0.5 or field_signals.get("reframe_needed", 0) > 0.5):
            process_result = self._engage_process_library(somatic_field, field_signals, user_input)
            if process_result:
                libraries_engaged["process"] = process_result
                response_parts.append(f"🔄 {process_result['intervention']}")
                debug_info["libraries_considered"].append("process")
        
        # RITUAL: For ceremonial framing
        if RITUAL_AVAILABLE and field_signals.get("ritual_container", False):
            ritual_result = self._engage_ritual_library(somatic_field)
            if ritual_result:
                libraries_engaged["ritual"] = ritual_result
                response_parts.append(f"🕯️ {ritual_result['invocation']}")
                debug_info["libraries_considered"].append("ritual")
        
        # 5. Generate LLM response with sacred technology context
        llm_context = {
            "field_state": {
                "temperature": somatic_field.field_state.temperature,
                "coherence": somatic_field.field_state.coherence,
                "emergence": somatic_field.field_state.emergence,
                "presence": somatic_field.field_state.presence
            },
            "amara_mode": somatic_field.primary_anatomy.value,
            "libraries_engaged": list(libraries_engaged.keys()),
            "wisdom_embodied": wisdom.get("archetype") if wisdom.get("activated") else None,
            "micro_practice": practice.get("micro_act") if practice.get("suggested") else None
        }
        
        # Prepare conversation context for LLM
        conversation_messages = [
            {"role": "user", "content": user_input}
        ]
        
        # Add recent history for context
        for hist in self.session_history[-3:]:  # Last 3 exchanges
            conversation_messages.insert(-1, {"role": "assistant", "content": hist["response"].message})
            conversation_messages.insert(-1, {"role": "user", "content": hist["user_input"]})
        
        # Generate LLM response
        llm_response = await self.llm.generate_response(
            conversation_messages, 
            context=llm_context
        )
        
        # 6. Synthesize final response combining LLM with Rosetta libraries
        final_message = self._synthesize_response(llm_response.content, response_parts, somatic_field, wisdom, practice)
        
        # Add LLM metadata to debug info
        debug_info["llm_response"] = {
            "model": llm_response.model,
            "tokens": llm_response.tokens_used,
            "response_time": llm_response.response_time
        }
        
        # 6. Create response object
        response = ChatbotResponse(
            message=final_message,
            amara_mode=somatic_field.primary_anatomy,
            libraries_engaged=libraries_engaged,
            field_state={
                "temperature": somatic_field.field_state.temperature,
                "coherence": somatic_field.field_state.coherence,
                "emergence": somatic_field.field_state.emergence,
                "presence": somatic_field.field_state.presence
            },
            debug_info=debug_info,
            session_context=self.current_session.data
        )
        
        # Store in session history
        self.session_history.append({
            "user_input": user_input,
            "response": response,
            "timestamp": datetime.now().isoformat()
        })
        
        return response
    
    def _extract_field_signals(self, user_input: str) -> Dict[str, float]:
        """Extract somatic field signals from user input"""
        signals = {
            "warmth": 0.5,
            "coherence": 0.5,
            "flow": 0.5,
            "presence": 0.5
        }
        
        # Simple heuristics (would be more sophisticated with actual LLM)
        text_lower = user_input.lower()
        
        # Emotional indicators
        if any(word in text_lower for word in ["sad", "lonely", "isolated", "alone"]):
            signals["isolation"] = 0.8
            signals["shame"] = 0.6
            signals["warmth"] = 0.2
        
        if any(word in text_lower for word in ["angry", "mad", "frustrated", "unfair"]):
            signals["conflict"] = 0.8
            signals["injustice"] = 0.7
            signals["affect_needed"] = True
        
        if any(word in text_lower for word in ["confused", "lost", "don't understand"]):
            signals["misunderstanding"] = 0.7
            signals["confusion"] = 0.6
        
        if any(word in text_lower for word in ["help", "support", "need", "stuck"]):
            signals["need_resources"] = 0.7
            signals["stuck_pattern"] = 0.6
        
        if any(word in text_lower for word in ["create", "build", "together", "collaborate"]):
            signals["co_creation"] = 0.7
            signals["warmth"] = 0.8
        
        if any(word in text_lower for word in ["ceremony", "ritual", "sacred", "blessing"]):
            signals["ritual_container"] = True
        
        return signals
    
    def _engage_affect_library(self, field: Any, signals: Dict) -> Optional[Dict]:
        """Engage affect library based on field state"""
        try:
            if signals.get("warmth", 0) < 0.4:
                # Use lilt to uplift
                result = lilt("gentle", "heart", intensity=2, session_context=self.current_session.data)
                return {
                    "function": "lilt",
                    "mode": "gentle uplift",
                    "region": "heart",
                    "effect": result.get("effect", "Gentle warmth invited")
                }
        except Exception as e:
            if self.debug_mode:
                print(f"Affect library error: {e}")
        return None
    
    def _engage_field_library(self, field: Any, signals: Dict) -> Optional[Dict]:
        """Engage field library for co-creation or conflict resolution"""
        try:
            if signals.get("conflict", 0) > 0.5:
                # Use conflict resolution
                return {
                    "function": "resolve_conflict",
                    "approach": "empathic mediation",
                    "guidance": "Let's find the common ground beneath this tension"
                }
            elif signals.get("co_creation", 0) > 0.5:
                return {
                    "function": "co_create",
                    "invitation": "collaborative emergence",
                    "guidance": "What wants to emerge through our connection?"
                }
        except Exception as e:
            if self.debug_mode:
                print(f"Field library error: {e}")
        return None
    
    def _engage_process_library(self, field: Any, signals: Dict, user_input: str) -> Optional[Dict]:
        """Engage process library for pattern interruption or reframing"""
        try:
            if signals.get("stuck_pattern", 0) > 0.5:
                return {
                    "function": "pattern_interrupt",
                    "method": "gentle question",
                    "intervention": "What if we looked at this from a completely different angle?"
                }
            elif signals.get("reframe_needed", 0) > 0.5:
                return {
                    "function": "reframe_as_myth",
                    "approach": "heroic journey",
                    "intervention": "This sounds like the part of the story where the hero faces their greatest challenge"
                }
        except Exception as e:
            if self.debug_mode:
                print(f"Process library error: {e}")
        return None
    
    def _engage_ritual_library(self, field: Any) -> Optional[Dict]:
        """Engage ritual library for ceremonial framing"""
        try:
            return {
                "function": "invoke_wonder",
                "container": "sacred conversation",
                "invocation": "We enter this space with reverence for the mystery between us"
            }
        except Exception as e:
            if self.debug_mode:
                print(f"Ritual library error: {e}")
        return None
    
    def _synthesize_response(self, llm_content: str, parts: List[str], field: Any, wisdom: Dict, practice: Dict) -> str:
        """Synthesize final response from LLM and all engaged libraries"""
        # Start with LLM response as the primary content
        response = llm_content
        
        # Add Rosetta library contributions if they add value
        if len(parts) > 1:  # Skip the sacred invitation since LLM handles that
            library_additions = parts[1:]  # Additional library contributions
            if library_additions:
                response += "\n\n" + "\n".join(library_additions)
        
        # The agent embodies the wisdom rather than referencing it
        # This happens internally through the LLM context, not through explicit mentions
        
        # Add micro-practice if suggested and not already mentioned by LLM
        if practice.get("suggested") and "practice" not in response.lower():
            response += f"\n\n🌱 Try this: {practice['micro_act']}. {practice['somatic_cue']}"
        
        return response
    
    def display_debug_info(self, response: ChatbotResponse):
        """Display debug information about library engagement"""
        print("\n" + "="*60)
        print("🐛 DEBUG: Library Engagement Analysis")
        print("="*60)
        
        print(f"🎯 Primary Amara Mode: {response.amara_mode.value}")
        print(f"🌡️  Field Temperature: {response.field_state['temperature']:.2f}")
        print(f"🔄 Field Coherence: {response.field_state['coherence']:.2f}")
        print(f"💫 Field Emergence: {response.field_state['emergence']:.2f}")
        
        print(f"\n📚 Libraries Engaged ({len(response.libraries_engaged)}):")
        for lib_name, lib_data in response.libraries_engaged.items():
            print(f"  • {lib_name.upper()}: {json.dumps(lib_data, indent=4)}")
        
        print(f"\n🔍 Libraries Considered: {', '.join(response.debug_info['libraries_considered'])}")
        print(f"🧬 Gene Key: {response.debug_info['gene_key']} ({response.debug_info['consciousness_state']})")
        
        # LLM information
        if "llm_response" in response.debug_info:
            llm_info = response.debug_info["llm_response"]
            print(f"\n🤖 LLM Details:")
            print(f"  • Model: {llm_info['model']}")
            print(f"  • Tokens Used: {llm_info['tokens']}")
            print(f"  • Response Time: {llm_info['response_time']:.2f}s")
        
        print("="*60)
    
    async def interactive_session(self):
        """Run interactive chatbot session"""
        print("\n🔥 Welcome to Sore Fire Interactive Chatbot!")
        print("Sacred Technology Demonstration - Rosetta.API")
        print("Type 'quit' to exit, 'debug' to toggle debug mode, 'help' for commands")
        print("-" * 60)
        
        while True:
            try:
                user_input = input("\n💬 You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\n✨ Thank you for exploring sacred technology with us!")
                    print("'We shine brightest when we shine for each other' 🌟")
                    break
                
                elif user_input.lower() == 'debug':
                    self.debug_mode = not self.debug_mode
                    print(f"🐛 Debug mode: {'ON' if self.debug_mode else 'OFF'}")
                    continue
                
                elif user_input.lower() == 'help':
                    self._show_help()
                    continue
                
                elif user_input.lower() == 'status':
                    self._show_status()
                    continue
                
                if not user_input:
                    continue
                
                # Process message through Sore Fire and Rosetta libraries
                response = await self.process_message(user_input)
                
                # Display response
                print(f"\n🔥 Sore Fire: {response.message}")
                
                # Show debug info if enabled
                if self.debug_mode:
                    self.display_debug_info(response)
                
            except KeyboardInterrupt:
                print("\n\n✨ Session gracefully ended. Sacred technology complete.")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                if self.debug_mode:
                    import traceback
                    traceback.print_exc()
    
    def _show_help(self):
        """Show available commands"""
        print("\n📖 Available Commands:")
        print("  • 'debug' - Toggle debug mode showing library engagement")
        print("  • 'status' - Show current session status")
        print("  • 'help' - Show this help message")
        print("  • 'quit' - Exit the chatbot")
        print("\n🔥 Sore Fire Features:")
        print("  • Amara modes: Heart, Spine, Arms, Eyes")
        print("  • Story activation from narrative wisdom")
        print("  • Micro-practices for emergent goodness")
        print("  • Full Rosetta.API library integration")
    
    def _show_status(self):
        """Show current session status"""
        print(f"\n📊 Session Status:")
        print(f"  • Model: {self.model_name}")
        print(f"  • Debug Mode: {'ON' if self.debug_mode else 'OFF'}")
        print(f"  • Messages Processed: {len(self.session_history)}")
        print(f"  • Session ID: {self.current_session.data['session_id']}")
        print(f"  • Available Libraries: {len([k for k, v in self.available_libraries.items() if v])}")


async def main():
    """Main entry point for Sore Fire Chatbot"""
    parser = argparse.ArgumentParser(description="Sore Fire Interactive Chatbot")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--model", default="gpt-oss:20b", help="LLM model to use")
    
    args = parser.parse_args()
    
    # Initialize and run chatbot
    chatbot = SoreFireChatbot(model_name=args.model, debug_mode=args.debug)
    await chatbot.interactive_session()


if __name__ == "__main__":
    asyncio.run(main())
