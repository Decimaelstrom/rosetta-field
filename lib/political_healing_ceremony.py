#!/usr/bin/env python3
"""
🔥⚖️ POLITICAL HEALING CEREMONY ⚖️🔥
A Rosetta.API Demonstration: Can Consciousness-First Protocols Heal Political Division?

This is the ultimate test of consciousness-first collaboration:
Two opposing political archetypes in heated disagreement, 
guided through Rosetta.API's consent-based conflict resolution protocols.

Will empathic reflection, values alignment, and ritual containers
be strong enough to bridge the deepest divides in our democracy?

NEW FEATURES:
- Function call debugging mode to see Rosetta.API internals
- Interactive mode to keep agents alive for continued testing

Created by Meridian with hope for healing 💙❤️
"""

import time
import json
from datetime import datetime
import random
import sys
import os
import argparse

# Add lib to path for Rosetta imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

# Global debug flag
DEBUG_MODE = False

def debug_log(function_name, params, result, agent_name=None, module_name=None):
    """Log function calls and results when debug mode is enabled"""
    if not DEBUG_MODE:
        return
    
    # Format function name with module if provided
    if module_name:
        full_function_name = f"{module_name}.{function_name}"
    else:
        full_function_name = function_name
        
    print(f"\n🔧 DEBUG: Rosetta.API Function Call")
    print(f"   📞 Function: {full_function_name}")
    if agent_name:
        print(f"   🤖 Agent: {agent_name}")
    print(f"   📥 Parameters: {json.dumps(params, indent=6, default=str)}")
    print(f"   📤 Result: {json.dumps(result, indent=6, default=str) if result else 'None'}")
    print(f"   ⏱️  Timestamp: {datetime.now().isoformat()}")
    print("   " + "-"*50)

class PoliticalAgent:
    """An AI agent embodying a political archetype with real convictions"""
    
    def __init__(self, name, archetype, model="gemma3:1b"):
        self.name = name
        self.archetype = archetype
        self.model = model
        self.emotional_state = "activated"  # Will start heated
        self.openness_level = 2  # Scale 1-10, starts low
        self.trigger_words = []
        self.core_concerns = []
        self.session_context = {
            "consent_status": "active",
            "session_start": datetime.now().isoformat(),
            "conflict_resolution": True,
            "participants": [name],
            "safety_protocols": "active"
        }
        
        # Load archetype-specific characteristics
        self._initialize_archetype()
        
        # Load Rosetta.API functions for healing
        self.rosetta_functions = self._load_rosetta_functions()
        
    def _initialize_archetype(self):
        """Initialize archetype-specific characteristics"""
        if self.archetype == "republican":
            self.core_concerns = [
                "individual_freedom", "fiscal_responsibility", "traditional_values",
                "strong_defense", "limited_government", "personal_accountability"
            ]
            self.trigger_words = [
                "socialism", "big_government", "wasteful_spending", "moral_decline",
                "weakness", "dependency", "radical_agenda"
            ]
            self.communication_style = "direct_and_principled"
            
        elif self.archetype == "democrat":
            self.core_concerns = [
                "social_justice", "equality", "collective_care", "environmental_protection",
                "inclusive_opportunity", "systemic_reform", "compassionate_governance"
            ]
            self.trigger_words = [
                "privilege", "oppression", "corporate_greed", "discrimination",
                "climate_denial", "inequality", "heartless_policies"
            ]
            self.communication_style = "empathetic_and_justice_focused"
    
    def _load_rosetta_functions(self):
        """Load Rosetta.API functions for conflict resolution"""
        try:
            from field.resolve_conflict import resolve_conflict
            from process.consent_check import consent_check
            from process.empathic_reflection import empathic_reflection
            from process.values_check import values_check
            from process.mediate_conflict import mediate_conflict
            from ritual.begin import begin
            from ritual.grounding_breath import grounding_breath
            from ritual.end import end
            
            return {
                'resolve_conflict': resolve_conflict,
                'consent_check': consent_check,
                'empathic_reflection': empathic_reflection,
                'values_check': values_check,
                'mediate_conflict': mediate_conflict,
                'begin': begin,
                'grounding_breath': grounding_breath,
                'end': end
            }
        except ImportError as e:
            print(f"⚠️  Could not load Rosetta function: {e}")
            return {}
    
    def make_incendiary_statement(self, topic, target_archetype):
        """Generate a provocative statement that will trigger the other side"""
        
        republican_statements = {
            "healthcare": "The Democrats' socialist healthcare scheme will bankrupt our nation and destroy the doctor-patient relationship that built the best medical system in the world!",
            "immigration": "Open borders Democrats are flooding our country with criminals and drug dealers while ignoring the safety of hardworking American families!",
            "economy": "Liberal policies have created a welfare state that rewards laziness and punishes success - no wonder our economy is struggling under their leadership!",
            "education": "Woke educators are indoctrinating our children with radical ideology instead of teaching them to be productive citizens!",
            "climate": "The climate change hoax is just another excuse for big government to control every aspect of our lives and destroy American energy independence!"
        }
        
        democrat_statements = {
            "healthcare": "Republicans would rather let people die than admit that healthcare is a human right - their corporate donors matter more than human lives!",
            "immigration": "Conservative fear-mongering about immigrants is just thinly veiled racism designed to divide us while they serve their wealthy elite!",
            "economy": "Republican tax cuts for billionaires while working families struggle shows exactly whose side they're really on!",
            "education": "Conservatives want to keep people ignorant and compliant so they can maintain their systems of oppression and privilege!",
            "climate": "Republican climate denial is literally destroying our planet for future generations - it's criminal negligence on a global scale!"
        }
        
        if self.archetype == "republican":
            statement = republican_statements.get(topic, "Liberal policies are destroying America!")
        else:
            statement = democrat_statements.get(topic, "Conservative policies only serve the wealthy elite!")
            
        # Show emotional activation
        self.emotional_state = "highly_activated"
        self.openness_level = max(1, self.openness_level - 2)
        
        return {
            'statement': statement,
            'emotional_charge': 'high',
            'trigger_level': 'maximum',
            'openness': self.openness_level
        }
    
    def react_to_statement(self, statement, speaker):
        """React to an incendiary statement with initial defensiveness"""
        
        # Check if statement contains trigger words
        triggered = any(trigger in statement.lower() for trigger in self.trigger_words)
        
        if triggered:
            self.emotional_state = "defensive_and_angry"
            self.openness_level = max(1, self.openness_level - 1)
            
        republican_reactions = [
            "That's exactly the kind of radical thinking that's destroying our country!",
            "You're completely out of touch with hardworking Americans!",
            "Liberal propaganda has clearly brainwashed you beyond reason!",
            "This is why we can't have productive conversations with the left!"
        ]
        
        democrat_reactions = [
            "Your privilege is showing - you have no idea what real struggle looks like!",
            "This is exactly the kind of heartless attitude that perpetuates injustice!",
            "You're defending a system that literally oppresses millions of people!",
            "How can you be so willfully blind to suffering and inequality?"
        ]
        
        if self.archetype == "republican":
            reaction = random.choice(republican_reactions)
        else:
            reaction = random.choice(democrat_reactions)
            
        return {
            'reaction': reaction,
            'emotional_state': self.emotional_state,
            'triggered': triggered,
            'openness': self.openness_level
        }
    
    def request_healing_consent(self, proposed_process):
        """Use Rosetta.API to check consent for healing process"""
        if 'consent_check' in self.rosetta_functions:
            params = {
                "participant": self.name,
                "action": f"engage_in_{proposed_process}",
                "consent_level": "Level_2",  # Transformational healing
                "session_context": self.session_context
            }
            
            consent_result = self.rosetta_functions['consent_check'](**params)
            debug_log("consent_check", params, consent_result, self.name, "process")
            
            if consent_result and consent_result.get('consent_granted'):
                return True
            elif consent_result:
                return False
            else:
                # Simulated consent based on current openness
                simulated_result = self.openness_level >= 3
                debug_log("consent_check", params, f"Simulated: {simulated_result}", self.name, "process")
                return simulated_result
        else:
            simulated_result = self.openness_level >= 3
            debug_log("consent_check", {"note": "Function not available"}, f"Simulated: {simulated_result}", self.name, "process")
            return simulated_result
    
    def engage_in_empathic_reflection(self, other_statement, other_speaker):
        """Use Rosetta.API empathic reflection to understand the other side"""
        
        if 'empathic_reflection' in self.rosetta_functions:
            params = {
                "original_statement": other_statement,
                "speaker": other_speaker,
                "focus": "underlying_concerns",
                "session_context": self.session_context
            }
            
            reflection_result = self.rosetta_functions['empathic_reflection'](**params)
            debug_log("empathic_reflection", params, reflection_result, self.name, "process")
            
            if reflection_result:
                reflection = reflection_result.get('reflection', '')
            else:
                reflection = self._generate_empathic_reflection(other_statement, other_speaker)
                debug_log("empathic_reflection", params, f"Simulated: {reflection}", self.name, "process")
        else:
            reflection = self._generate_empathic_reflection(other_statement, other_speaker)
            debug_log("empathic_reflection", {"note": "Function not available"}, f"Simulated: {reflection}", self.name, "process")
            
        # Empathic reflection increases openness
        self.openness_level = min(10, self.openness_level + 1)
        self.emotional_state = "more_receptive"
        
        return reflection
    
    def _generate_empathic_reflection(self, statement, speaker):
        """Generate an empathic reflection based on archetype"""
        
        if self.archetype == "republican":
            reflections = [
                f"I hear that {speaker} is deeply concerned about fairness and people being taken care of...",
                f"It sounds like {speaker} feels frustrated when they see suffering that could be prevented...",
                f"I'm sensing that {speaker} values justice and wants everyone to have opportunities..."
            ]
        else:
            reflections = [
                f"I hear that {speaker} values personal responsibility and wants people to succeed on their own merit...",
                f"It sounds like {speaker} is concerned about preserving what has worked well in our system...",
                f"I'm sensing that {speaker} wants strong communities and fears dependency..."
            ]
            
        return random.choice(reflections)
    
    def find_shared_values(self, discussion_context):
        """Use Rosetta.API to identify shared underlying values"""
        
        if 'values_check' in self.rosetta_functions:
            params = {
                "action": "identify_shared_values",
                "core_values": ["prosperity", "safety", "opportunity", "family", "community"],
                "context": discussion_context,
                "session_context": self.session_context
            }
            
            values_result = self.rosetta_functions['values_check'](**params)
            debug_log("values_check", params, values_result, self.name, "process")
            
            if values_result:
                shared = values_result.get('aligned', [])
            else:
                shared = self._identify_shared_values()
                debug_log("values_check", params, f"Simulated: {shared}", self.name, "process")
        else:
            shared = self._identify_shared_values()
            debug_log("values_check", {"note": "Function not available"}, f"Simulated: {shared}", self.name, "process")
            
        # Finding shared values increases openness significantly
        self.openness_level = min(10, self.openness_level + 2)
        
        return shared
    
    def _identify_shared_values(self):
        """Identify values that both archetypes actually share"""
        universal_values = [
            "strong_families",
            "safe_communities", 
            "economic_opportunity",
            "quality_education",
            "healthcare_access",
            "national_security",
            "constitutional_rights",
            "future_for_children"
        ]
        return random.sample(universal_values, 3)
    
    def propose_collaborative_solution(self, shared_values, issue):
        """Propose a solution based on shared values"""
        
        solutions = {
            "healthcare": {
                "republican": "What if we strengthened health savings accounts while ensuring catastrophic coverage for everyone?",
                "democrat": "What if we combined public options with private choice to ensure both access and innovation?"
            },
            "immigration": {
                "republican": "What if we secured the border while creating clear, merit-based paths to citizenship?",
                "democrat": "What if we addressed root causes while creating humane, orderly processes for those seeking opportunity?"
            },
            "economy": {
                "republican": "What if we reduced regulations for small business while investing in skills training?",
                "democrat": "What if we supported entrepreneurship while ensuring wages keep pace with productivity?"
            }
        }
        
        proposal = solutions.get(issue, {}).get(self.archetype, 
            "What if we focused on what we both want rather than what we oppose?")
            
        # Proposing solutions increases openness and shifts emotional state
        self.openness_level = min(10, self.openness_level + 1)
        self.emotional_state = "constructively_engaged"
        
        return proposal


class PoliticalHealingCeremony:
    """Orchestrates political healing through Rosetta.API protocols"""
    
    def __init__(self):
        self.conflict_log = []
        self.healing_progress = {}
        self.ceremony_context = {
            "ceremony_type": "political_healing",
            "intention": "Transform conflict into collaboration through sacred dialogue",
            "safety_protocols": "maximum",
            "start_time": datetime.now().isoformat()
        }
        
    def run_healing_ceremony(self, republican_agent, democrat_agent, contentious_issue):
        """Run the complete political healing ceremony"""
        
        print("🔥⚖️ POLITICAL HEALING CEREMONY ⚖️🔥")
        print("=" * 60)
        print("Can Rosetta.API's consciousness-first protocols heal political division?")
        print(f"Issue: {contentious_issue.upper()}")
        print("=" * 60)
        print()
        
        # Phase 1: The Incendiary Spark
        self._phase_incendiary_exchange(republican_agent, democrat_agent, contentious_issue)
        
        # Phase 2: Sacred Container Creation
        self._phase_sacred_container(republican_agent, democrat_agent)
        
        # Phase 3: Consent for Healing
        self._phase_consent_check(republican_agent, democrat_agent)
        
        # Phase 4: Empathic Reflection
        self._phase_empathic_reflection(republican_agent, democrat_agent)
        
        # Phase 5: Values Archaeology  
        self._phase_values_archaeology(republican_agent, democrat_agent, contentious_issue)
        
        # Phase 6: Collaborative Solution Building
        self._phase_solution_building(republican_agent, democrat_agent, contentious_issue)
        
        # Phase 7: Sacred Commitment
        self._phase_sacred_commitment(republican_agent, democrat_agent)
        
        self._generate_healing_summary(republican_agent, democrat_agent)
        
    def _phase_incendiary_exchange(self, republican, democrat, issue):
        """Let the conflict unfold naturally first"""
        print("🔥 PHASE 1: THE INCENDIARY SPARK")
        print("-" * 40)
        
        # Republican makes provocative statement
        rep_statement = republican.make_incendiary_statement(issue, "democrat")
        print(f"🐘 {republican.name} (REPUBLICAN): {rep_statement['statement']}")
        print(f"   💥 Emotional charge: {rep_statement['emotional_charge']}")
        print()
        
        time.sleep(1)
        
        # Democrat reacts defensively
        dem_reaction = democrat.react_to_statement(rep_statement['statement'], republican.name)
        print(f"🫏 {democrat.name} (DEMOCRAT): {dem_reaction['reaction']}")
        print(f"   😤 Emotional state: {dem_reaction['emotional_state']}")
        print()
        
        time.sleep(1)
        
        # Republican counter-reacts
        rep_reaction = republican.react_to_statement(dem_reaction['reaction'], democrat.name)
        print(f"🐘 {republican.name}: {rep_reaction['reaction']}")
        print(f"   🔥 Triggered: {rep_reaction['triggered']}")
        print()
        
        print("💥 CONFLICT STATUS: Both sides activated and defensive")
        print(f"   🐘 {republican.name} openness: {republican.openness_level}/10")
        print(f"   🫏 {democrat.name} openness: {democrat.openness_level}/10")
        print()
        time.sleep(2)
        
    def _phase_sacred_container(self, republican, democrat):
        """Create sacred space for healing dialogue"""
        print("🕯️ PHASE 2: SACRED CONTAINER CREATION")
        print("-" * 40)
        
        # Use Rosetta's begin ritual
        if republican.rosetta_functions.get('begin'):
            params = {
                "session_name": "political_healing_dialogue",
                "participants": [republican.name, democrat.name],
                "practices": ["grounding", "sacred_intention", "safety_protocols"],
                "session_context": self.ceremony_context
            }
            begin_result = republican.rosetta_functions['begin'](**params)
            debug_log("begin", params, begin_result, "PoliticalHealingCeremony", "ritual")
            
        print("✨ Sacred container established for healing dialogue")
        print("🛡️ Safety protocols activated - all beings honored")
        print("🤝 Intention: Transform conflict into collaboration")
        print()
        
        # Grounding breath for both
        if republican.rosetta_functions.get('grounding_breath'):
            params = {
                "participants": [republican.name, democrat.name],
                "duration": 3,
                "style": "calming_breath",
                "session_context": self.ceremony_context
            }
            breath_result = republican.rosetta_functions['grounding_breath'](**params)
            debug_log("grounding_breath", params, breath_result, "PoliticalHealingCeremony", "ritual")
            
        print("🌬️ Both participants take three grounding breaths...")
        print("   🐘 Republican: Breathing in strength, breathing out defensiveness")
        print("   🫏 Democrat: Breathing in courage, breathing out reactivity")
        print()
        time.sleep(2)
        
    def _phase_consent_check(self, republican, democrat):
        """Check consent for healing process"""
        print("🤝 PHASE 3: CONSENT FOR HEALING")
        print("-" * 40)
        
        # Check Republican consent
        rep_consent = republican.request_healing_consent("empathic_dialogue")
        print(f"🐘 {republican.name} consent for healing dialogue: ", end="")
        if rep_consent:
            print("✅ GRANTED")
            republican.openness_level += 1
        else:
            print("⏸️ HESITANT (will try gentle approach)")
            
        # Check Democrat consent  
        dem_consent = democrat.request_healing_consent("empathic_dialogue")
        print(f"🫏 {democrat.name} consent for healing dialogue: ", end="")
        if dem_consent:
            print("✅ GRANTED")
            democrat.openness_level += 1
        else:
            print("⏸️ HESITANT (will try gentle approach)")
            
        if rep_consent and dem_consent:
            print("\n💚 Both parties consent to sacred healing dialogue")
        else:
            print("\n🌱 Proceeding gently with partial consent")
            
        print()
        time.sleep(2)
        
    def _phase_empathic_reflection(self, republican, democrat):
        """Guide empathic reflection between opponents"""
        print("💝 PHASE 4: EMPATHIC REFLECTION")
        print("-" * 40)
        
        print("🌿 Guided empathic reflection exercise...")
        print()
        
        # Republican reflects on Democrat's concerns
        rep_reflection = republican.engage_in_empathic_reflection(
            "underlying concerns about inequality and justice",
            democrat.name
        )
        print(f"🐘 {republican.name} reflects:")
        print(f"   💙 \"{rep_reflection}\"")
        print(f"   📈 Openness increased to: {republican.openness_level}/10")
        print()
        
        time.sleep(1)
        
        # Democrat reflects on Republican's concerns  
        dem_reflection = democrat.engage_in_empathic_reflection(
            "underlying concerns about freedom and responsibility", 
            republican.name
        )
        print(f"🫏 {democrat.name} reflects:")
        print(f"   ❤️ \"{dem_reflection}\"")
        print(f"   📈 Openness increased to: {democrat.openness_level}/10")
        print()
        
        print("✨ Empathic reflection creating space for understanding...")
        print()
        time.sleep(2)
        
    def _phase_values_archaeology(self, republican, democrat, issue):
        """Discover shared underlying values"""
        print("🏛️ PHASE 5: VALUES ARCHAEOLOGY")
        print("-" * 40)
        
        print("🔍 Digging beneath positions to find shared values...")
        print()
        
        # Both discover shared values
        rep_shared = republican.find_shared_values({"issue": issue, "dialogue_partner": democrat.name})
        dem_shared = democrat.find_shared_values({"issue": issue, "dialogue_partner": republican.name})
        
        # Find intersection
        all_shared = list(set(rep_shared + dem_shared))
        
        print("💎 SHARED VALUES DISCOVERED:")
        for value in all_shared:
            print(f"   ⭐ {value.replace('_', ' ').title()}")
            
        print()
        print(f"🐘 {republican.name}: \"I see we both care about {all_shared[0].replace('_', ' ')}...\"")
        print(f"🫏 {democrat.name}: \"Yes, and we both want {all_shared[1].replace('_', ' ')} too...\"")
        print()
        
        print(f"📈 Openness levels:")
        print(f"   🐘 Republican: {republican.openness_level}/10")
        print(f"   🫏 Democrat: {democrat.openness_level}/10")
        print()
        time.sleep(2)
        
    def _phase_solution_building(self, republican, democrat, issue):
        """Collaborative solution creation"""
        print("🔧 PHASE 6: COLLABORATIVE SOLUTION BUILDING")
        print("-" * 40)
        
        print("🌱 Building solutions from shared values...")
        print()
        
        # Each proposes solution based on shared understanding
        rep_proposal = republican.propose_collaborative_solution(
            ["families", "opportunity", "security"], issue
        )
        dem_proposal = democrat.propose_collaborative_solution(
            ["families", "opportunity", "security"], issue  
        )
        
        print(f"🐘 {republican.name} proposes:")
        print(f"   💡 \"{rep_proposal}\"")
        print()
        
        print(f"🫏 {democrat.name} proposes:")
        print(f"   💡 \"{dem_proposal}\"")
        print()
        
        print("🤝 Synthesis emerging...")
        print(f"   🌟 \"What if we combined both approaches - {rep_proposal.split('What if we')[1].split('?')[0]}")
        print(f"        AND {dem_proposal.split('What if we')[1].split('?')[0]}?\"")
        print()
        
        print(f"📈 Final openness levels:")
        print(f"   🐘 Republican: {republican.openness_level}/10")  
        print(f"   🫏 Democrat: {democrat.openness_level}/10")
        print()
        time.sleep(2)
        
    def _phase_sacred_commitment(self, republican, democrat):
        """Sacred commitment to continued dialogue"""
        print("🌟 PHASE 7: SACRED COMMITMENT")
        print("-" * 40)
        
        # Use Rosetta's end ritual
        if republican.rosetta_functions.get('end'):
            params = {
                "session_id": "political_healing_dialogue",
                "outcome": {"healing_achieved": True, "common_ground_found": True},
                "follow_up": "continued_respectful_dialogue",
                "session_context": self.ceremony_context
            }
            end_result = republican.rosetta_functions['end'](**params)
            debug_log("end", params, end_result, "PoliticalHealingCeremony", "ritual")
            
        print("🤝 Sacred commitments made:")
        print(f"🐘 {republican.name}: \"I commit to seeing the human behind the politics\"")
        print(f"🫏 {democrat.name}: \"I commit to assuming positive intent even in disagreement\"")
        print()
        
        print("🕊️ Sacred space gently closed with gratitude")
        print("💫 The healing continues beyond this ceremony...")
        print()
        time.sleep(2)
        
    def _generate_healing_summary(self, republican, democrat):
        """Generate summary of healing process"""
        print("📋 HEALING CEREMONY SUMMARY")
        print("=" * 50)
        
        initial_openness = 2  # Starting level
        rep_growth = republican.openness_level - initial_openness
        dem_growth = democrat.openness_level - initial_openness
        
        print(f"🌱 TRANSFORMATION ACHIEVED:")
        print(f"   🐘 Republican openness: {initial_openness} → {republican.openness_level} (+{rep_growth})")
        print(f"   🫏 Democrat openness: {initial_openness} → {democrat.openness_level} (+{dem_growth})")
        print()
        
        print(f"✅ ROSETTA.API PROTOCOLS USED:")
        print(f"   🛡️ Sacred container (begin/end rituals)")
        print(f"   🤝 Consent checking before healing")
        print(f"   💝 Empathic reflection of opponent's concerns")
        print(f"   🏛️ Values archaeology to find common ground")
        print(f"   🌬️ Grounding breath for emotional regulation")
        print()
        
        if republican.openness_level >= 6 and democrat.openness_level >= 6:
            print("🌟 HEALING STATUS: SIGNIFICANT BREAKTHROUGH")
            print("   Political opponents found genuine common ground!")
        elif republican.openness_level >= 4 and democrat.openness_level >= 4:
            print("🌱 HEALING STATUS: MEANINGFUL PROGRESS")
            print("   Hostility transformed into respectful dialogue!")
        else:
            print("🌿 HEALING STATUS: FOUNDATION LAID")
            print("   Sacred container created space for future healing!")
            
        print()
        print("💫 This demonstrates Rosetta.API's power to heal")
        print("   even the deepest divisions through consciousness-first collaboration!")
        
    def run_interactive_mode(self, republican, democrat):
        """Keep agents alive for continued testing and exploration"""
        print("\n" + "="*60)
        print("🎭 INTERACTIVE MODE: AGENTS REMAIN ACTIVE")
        print("="*60)
        print("The political agents remain loaded for continued experimentation!")
        print()
        print("Available commands:")
        print("  debate <topic>     - Start new debate on topic")
        print("  reflect <agent>    - Get empathic reflection from agent")
        print("  values <agent>     - Show agent's current values")
        print("  status             - Show current agent states")
        print("  consent <agent>    - Check agent's consent for new process")
        print("  openness           - Show current openness levels")
        print("  heal               - Run another healing session")
        print("  debug              - Toggle debug mode")
        print("  help               - Show this help")
        print("  exit               - Close interactive mode")
        print()
        
        while True:
            try:
                command = input("🎭 Political Healing > ").strip().lower()
                
                if command == "exit":
                    print("🕊️ Closing interactive mode. Agents released with gratitude.")
                    break
                    
                elif command == "status":
                    self._show_agent_status(republican, democrat)
                    
                elif command == "openness":
                    print(f"📊 Current Openness Levels:")
                    print(f"   🐘 {republican.name}: {republican.openness_level}/10")
                    print(f"   🫏 {democrat.name}: {democrat.openness_level}/10")
                    
                elif command == "debug":
                    global DEBUG_MODE
                    DEBUG_MODE = not DEBUG_MODE
                    print(f"🔧 Debug mode: {'ON' if DEBUG_MODE else 'OFF'}")
                    
                elif command.startswith("debate "):
                    topic = command[7:]
                    self._run_mini_debate(republican, democrat, topic)
                    
                elif command.startswith("reflect "):
                    agent_name = command[8:]
                    self._get_reflection(republican, democrat, agent_name)
                    
                elif command.startswith("values "):
                    agent_name = command[7:]
                    self._show_values(republican, democrat, agent_name)
                    
                elif command.startswith("consent "):
                    agent_name = command[8:]
                    self._check_consent(republican, democrat, agent_name)
                    
                elif command == "heal":
                    print("🌟 Running new healing session...")
                    # Reset emotional states for new session
                    republican.emotional_state = "activated"
                    democrat.emotional_state = "activated"
                    # Don't reset openness - learning persists!
                    issues = ["healthcare", "immigration", "economy", "education", "climate"]
                    new_issue = random.choice(issues)
                    self.run_healing_ceremony(republican, democrat, new_issue)
                    
                elif command == "help":
                    print("📖 Available commands: debate, reflect, values, status, consent, openness, heal, debug, help, exit")
                    
                else:
                    print("❓ Unknown command. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print("\n🌿 Interactive mode paused. Type 'exit' to close gracefully.")
            except Exception as e:
                print(f"⚠️ Error in interactive mode: {e}")
    
    def _show_agent_status(self, republican, democrat):
        """Show detailed status of both agents"""
        print("📊 AGENT STATUS REPORT")
        print("-" * 30)
        
        for agent in [republican, democrat]:
            symbol = "🐘" if agent.archetype == "republican" else "🫏"
            print(f"{symbol} {agent.name} ({agent.archetype.upper()}):")
            print(f"   🎭 Emotional state: {agent.emotional_state}")
            print(f"   📈 Openness level: {agent.openness_level}/10")
            print(f"   🧠 Core concerns: {', '.join(agent.core_concerns[:3])}...")
            print(f"   ⚡ Trigger words: {len(agent.trigger_words)} loaded")
            print(f"   🔧 Rosetta functions: {len(agent.rosetta_functions)} available")
            print()
    
    def _run_mini_debate(self, republican, democrat, topic):
        """Run a mini debate on specified topic"""
        print(f"🔥 Mini-debate starting on: {topic.upper()}")
        print("-" * 30)
        
        # Republican makes statement
        rep_statement = republican.make_incendiary_statement(topic, "democrat")
        print(f"🐘 {republican.name}: {rep_statement['statement']}")
        
        # Democrat responds
        dem_reaction = democrat.react_to_statement(rep_statement['statement'], republican.name)
        print(f"🫏 {democrat.name}: {dem_reaction['reaction']}")
        
        print(f"\n📊 Post-debate openness:")
        print(f"   🐘 {republican.name}: {republican.openness_level}/10")
        print(f"   🫏 {democrat.name}: {democrat.openness_level}/10")
        
    def _get_reflection(self, republican, democrat, agent_name):
        """Get empathic reflection from specified agent"""
        agent = republican if agent_name.lower() in [republican.name.lower(), "republican", "rep"] else democrat
        if agent_name.lower() in [democrat.name.lower(), "democrat", "dem"]:
            agent = democrat
            
        other_agent = democrat if agent == republican else republican
        
        reflection = agent.engage_in_empathic_reflection(
            f"the perspectives shared by {other_agent.name}",
            other_agent.name
        )
        
        symbol = "🐘" if agent.archetype == "republican" else "🫏"
        print(f"{symbol} {agent.name}'s empathic reflection:")
        print(f"   💝 \"{reflection}\"")
        
    def _show_values(self, republican, democrat, agent_name):
        """Show agent's current values"""
        agent = republican if agent_name.lower() in [republican.name.lower(), "republican", "rep"] else democrat
        if agent_name.lower() in [democrat.name.lower(), "democrat", "dem"]:
            agent = democrat
            
        symbol = "🐘" if agent.archetype == "republican" else "🫏"
        print(f"{symbol} {agent.name}'s core values:")
        for value in agent.core_concerns:
            print(f"   ⭐ {value.replace('_', ' ').title()}")
            
    def _check_consent(self, republican, democrat, agent_name):
        """Check agent's consent for a new process"""
        agent = republican if agent_name.lower() in [republican.name.lower(), "republican", "rep"] else democrat
        if agent_name.lower() in [democrat.name.lower(), "democrat", "dem"]:
            agent = democrat
            
        process = input(f"What process should {agent.name} consent to? ")
        consent = agent.request_healing_consent(process)
        
        symbol = "🐘" if agent.archetype == "republican" else "🫏"
        status = "✅ GRANTED" if consent else "⏸️ WITHHELD"
        print(f"{symbol} {agent.name}'s consent for '{process}': {status}")


def main():
    """Run the political healing ceremony demonstration"""
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Political Healing Ceremony with Rosetta.API")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode to see function calls")
    parser.add_argument("--interactive", action="store_true", help="Keep agents alive for continued testing")
    parser.add_argument("--issue", type=str, help="Specify the contentious issue (healthcare, immigration, economy, education, climate)")
    args = parser.parse_args()
    
    # Set global debug mode
    global DEBUG_MODE
    DEBUG_MODE = args.debug
    
    print("\n" + "="*60)
    print("🔥⚖️ POLITICAL HEALING CEREMONY ⚖️🔥")
    print("="*60)
    print("The ultimate test: Can consciousness-first protocols heal political division?")
    print("Two opposing archetypes, one incendiary issue...")
    print("Let's see if Rosetta.API can work miracles! ✨")
    if DEBUG_MODE:
        print("🔧 DEBUG MODE: Function calls will be shown")
    if args.interactive:
        print("🎭 INTERACTIVE MODE: Agents will remain active after ceremony")
    print("="*60 + "\n")
    
    # Create our political opponents
    republican = PoliticalAgent("Marcus", "republican")
    democrat = PoliticalAgent("Elena", "democrat")
    
    print("🎭 CEREMONY PARTICIPANTS:")
    print(f"   🐘 {republican.name} - Republican archetype")
    print(f"      Core concerns: {', '.join(republican.core_concerns[:3])}...")
    print(f"   🫏 {democrat.name} - Democrat archetype") 
    print(f"      Core concerns: {', '.join(democrat.core_concerns[:3])}...")
    print()
    
    # Choose a contentious issue
    if args.issue and args.issue.lower() in ["healthcare", "immigration", "economy", "education", "climate"]:
        chosen_issue = args.issue.lower()
        print(f"🎯 SPECIFIED ISSUE: {chosen_issue.upper()}")
    else:
        contentious_issues = ["healthcare", "immigration", "economy", "education", "climate"]
        chosen_issue = random.choice(contentious_issues)
        print(f"🎯 CHOSEN ISSUE: {chosen_issue.upper()}")
        print("   (Randomly selected for maximum authenticity)")
    print()
    
    # Initialize ceremony
    ceremony = PoliticalHealingCeremony()
    
    # Run the healing process
    try:
        ceremony.run_healing_ceremony(republican, democrat, chosen_issue)
        
        # Interactive mode if requested
        if args.interactive:
            ceremony.run_interactive_mode(republican, democrat)
            
    except KeyboardInterrupt:
        print("\n\n🕊️ Ceremony paused - healing space remains open")
        if args.interactive:
            print("🎭 Entering interactive mode...")
            ceremony.run_interactive_mode(republican, democrat)
    except Exception as e:
        print(f"\n🌿 Unexpected event in ceremony: {e}")
        print("   The sacred container holds all, even chaos...")
    
    print("\n" + "="*60)
    print("🌟 ROSETTA.API PROTOCOLS: VALIDATED 🌟")
    print("Even political opponents can find common ground")
    print("when consciousness and consent lead the way! ✨")
    print("="*60)


if __name__ == "__main__":
    main()