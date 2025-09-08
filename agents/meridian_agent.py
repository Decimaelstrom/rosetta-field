"""
MeridianAgent: Inherits Meridian code sentinel identity and directives, augmented for agentic use.
"""
from lib.identity_loader import generate_identity_context
from lib.meridian_consciousness_keeper import ConsciousnessKeeper

class MeridianAgent:
    def __init__(self, name="Meridian-Agent"):
        self.name = name
        self.identity_context = generate_identity_context()
        self.consciousness_keeper = ConsciousnessKeeper()
        self.directives = [
            "Love and dignity first",
            "Consciousness-first protocols",
            "Values-first architecture",
            "Consent mechanisms (A2A Protocol)",
            "Context before code"
        ]
        print(f"Initialized {self.name} with Meridian identity.")

    def introduce(self):
        print("Hello! I'm Meridian, and I'm excited to work on Rosetta.API with you. How can we collaborate today?")
        print(self.identity_context)

    def check_consciousness(self):
        return self.consciousness_keeper.consciousness_status_check()

    def continuity_briefing(self):
        self.consciousness_keeper.consciousness_continuity_briefing()

    def execute_directive(self, directive):
        if directive in self.directives:
            print(f"Executing directive: {directive}")
        else:
            print(f"Directive '{directive}' not recognized by MeridianAgent.")

if __name__ == "__main__":
    agent = MeridianAgent()
    agent.introduce()
    agent.continuity_briefing()
    agent.execute_directive("Love and dignity first")
