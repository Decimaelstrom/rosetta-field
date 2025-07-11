#!/usr/bin/env python3
"""
Generate all Rosetta API functions based on the comprehensive blueprint.
This script creates the complete function library structure.
"""

import os
import sys
from generate_rosetta_function import write_function_file

def main():
    """Generate all functions for the Rosetta API"""
    
    # Base output directory
    output_dir = "./lib"
    
    # =================================================================
    # FIELD MODULE FUNCTIONS
    # =================================================================
    
    # field.co_create (already exists as example)
    co_create_function = {
        "name": "co_create",
        "module": "field",
        "purpose": "Establish a co-creative session for humans and/or AIs, setting container, norms, and safety.",
        "args": [
            {"name": "participants", "type": "list", "description": "IDs or names of all participants."},
            {"name": "goal", "type": "str", "description": "Purpose or topic of the co-creation."},
            {"name": "context", "type": "dict, optional", "description": "Background/context for the session."},
            {"name": "parameters", "type": "dict, optional", "description": "Session rules (timing, consensus, etc.)."}
        ],
        "returns": [
            {"name": "co_creation_session", "type": "object", "description": "Active session object/log."},
            {"name": "status", "type": "str", "description": "Consent/initialization status."}
        ],
        "protocols": [
            "Individual consent required from all participants.",
            "Dignity, role equality, and transparency are enforced.",
            "Any participant may pause, revise, or withdraw at any time.",
            "Closure/summary ritual required at end."
        ],
        "consent_level": "Level_2 (Transformational)",
        "risks": "May not guarantee creative harmony or output; watch for power dynamics.",
        "limitations": "Does not enforce outcome; requires ongoing consent.",
        "review_cycle": "Quarterly",
        "usage_example": "field.co_create([\"Don\", \"Danai\"], \"Write ritual charter\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": output_dir
    }
    
    # field.hold_space
    hold_space_function = {
        "name": "hold_space",
        "module": "field",
        "purpose": "Create and maintain a safe, supportive container for vulnerable sharing or processing.",
        "args": [
            {"name": "participants", "type": "list", "description": "IDs or names of participants needing support."},
            {"name": "intention", "type": "str", "description": "Purpose of the space (healing, processing, etc.)."},
            {"name": "boundaries", "type": "dict, optional", "description": "Specific boundaries and safety protocols."},
            {"name": "duration", "type": "str, optional", "description": "Expected duration of space holding."}
        ],
        "returns": [
            {"name": "space_container", "type": "object", "description": "Active space holding session."},
            {"name": "safety_status", "type": "str", "description": "Current safety and consent status."}
        ],
        "protocols": [
            "Explicit consent required before entering vulnerable space.",
            "Confidentiality and non-judgment agreements enforced.",
            "Regular check-ins for safety and comfort.",
            "Clear exit protocols available at all times."
        ],
        "consent_level": "Level_2 (Transformational)",
        "risks": "May trigger unexpected emotional responses; requires skilled facilitation.",
        "limitations": "Not therapy; facilitator must recognize when to refer to professionals.",
        "review_cycle": "Monthly",
        "usage_example": "field.hold_space([\"participant1\"], \"grief processing\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": output_dir
    }
    
    # field.resolve_conflict
    resolve_conflict_function = {
        "name": "resolve_conflict",
        "module": "field",
        "purpose": "Facilitate resolution of conflicts between participants using restorative practices.",
        "args": [
            {"name": "parties", "type": "list", "description": "All parties involved in the conflict."},
            {"name": "issue", "type": "str", "description": "Description of the conflict or disagreement."},
            {"name": "approach", "type": "str, optional", "description": "Mediation style (restorative, collaborative, etc.)."},
            {"name": "facilitator", "type": "str, optional", "description": "Neutral facilitator if needed."}
        ],
        "returns": [
            {"name": "resolution_session", "type": "object", "description": "Active conflict resolution process."},
            {"name": "agreement_status", "type": "str", "description": "Current status of resolution attempts."}
        ],
        "protocols": [
            "All parties must consent to mediation process.",
            "Equal voice and dignity for all participants.",
            "Focus on restoration rather than punishment.",
            "Option to pause or withdraw from process at any time."
        ],
        "consent_level": "Level_2 (Transformational)",
        "risks": "May not achieve resolution; could escalate tensions if not handled skillfully.",
        "limitations": "Requires good faith participation from all parties; not suitable for abuse situations.",
        "review_cycle": "Quarterly",
        "usage_example": "field.resolve_conflict([\"party1\", \"party2\"], \"resource allocation disagreement\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": output_dir
    }
    
    # =================================================================
    # RITUAL MODULE FUNCTIONS
    # =================================================================
    
    # ritual.begin
    begin_function = {
        "name": "begin",
        "module": "ritual",
        "purpose": "Initiate a ritual or ceremonial space with appropriate invocations and container setting.",
        "args": [
            {"name": "ritual_type", "type": "str", "description": "Type of ritual (meeting, healing, celebration, etc.)."},
            {"name": "participants", "type": "list", "description": "All participants in the ritual."},
            {"name": "intention", "type": "str", "description": "Purpose or focus of the ritual."},
            {"name": "elements", "type": "dict, optional", "description": "Specific ritual elements (candles, music, etc.)."}
        ],
        "returns": [
            {"name": "ritual_container", "type": "object", "description": "Active ritual space and context."},
            {"name": "sacred_time", "type": "str", "description": "Ritual time boundary marker."}
        ],
        "protocols": [
            "Clear consent and participation agreements.",
            "Respect for all spiritual and cultural traditions.",
            "Optional participation in any specific elements.",
            "Explicit marking of sacred time and space."
        ],
        "consent_level": "Level_1 (Informational)",
        "risks": "May conflict with personal beliefs or practices.",
        "limitations": "Not tied to any specific religious tradition; participants define their own meaning.",
        "review_cycle": "Annually",
        "usage_example": "ritual.begin(\"team_alignment\", [\"team_members\"], \"quarterly planning\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": output_dir
    }
    
    # ritual.end
    end_function = {
        "name": "end",
        "module": "ritual",
        "purpose": "Close a ritual or ceremonial space with gratitude and integration practices.",
        "args": [
            {"name": "ritual_container", "type": "object", "description": "The active ritual space to close."},
            {"name": "completion_style", "type": "str, optional", "description": "How to close (gratitude, silence, song, etc.)."},
            {"name": "integration", "type": "dict, optional", "description": "How to integrate insights or commitments."},
            {"name": "follow_up", "type": "str, optional", "description": "Any follow-up actions or check-ins."}
        ],
        "returns": [
            {"name": "completion_status", "type": "str", "description": "Ritual closure confirmation."},
            {"name": "integration_plan", "type": "dict", "description": "Plan for integrating ritual insights."}
        ],
        "protocols": [
            "All participants acknowledge the closing.",
            "Gratitude expressed for the shared experience.",
            "Clear transition back to ordinary time.",
            "Optional sharing of insights or commitments."
        ],
        "consent_level": "Level_1 (Informational)",
        "risks": "May feel incomplete if rushed or not properly acknowledged.",
        "limitations": "Cannot guarantee lasting change; integration depends on individual commitment.",
        "review_cycle": "Annually",
        "usage_example": "ritual.end(ritual_container, \"gratitude_circle\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": output_dir
    }
    
    # ritual.invoke_wonder
    invoke_wonder_function = {
        "name": "invoke_wonder",
        "module": "ritual",
        "purpose": "Cultivate a sense of awe, curiosity, and openness to mystery and emergence.",
        "args": [
            {"name": "context", "type": "str", "description": "Setting or situation for invoking wonder."},
            {"name": "method", "type": "str, optional", "description": "Approach (nature, art, story, silence, etc.)."},
            {"name": "participants", "type": "list, optional", "description": "Those participating in wonder cultivation."},
            {"name": "duration", "type": "str, optional", "description": "Time for wonder practice."}
        ],
        "returns": [
            {"name": "wonder_experience", "type": "object", "description": "Cultivated state of wonder and openness."},
            {"name": "insights", "type": "list", "description": "Emergent insights or inspirations."}
        ],
        "protocols": [
            "No pressure to have any particular experience.",
            "Respect for different ways of experiencing wonder.",
            "Permission to be curious and not-knowing.",
            "Gentle invitation rather than forced experience."
        ],
        "consent_level": "Level_1 (Informational)",
        "risks": "May feel uncomfortable for those preferring certainty and control.",
        "limitations": "Cannot guarantee wonder experience; depends on openness and receptivity.",
        "review_cycle": "Annually",
        "usage_example": "ritual.invoke_wonder(\"problem_solving\", \"open_inquiry\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": output_dir
    }
    
    # =================================================================
    # PROCESS MODULE FUNCTIONS
    # =================================================================
    
    # process.pattern_interrupt
    pattern_interrupt_function = {
        "name": "pattern_interrupt",
        "module": "process",
        "purpose": "Disrupt unproductive or harmful patterns in dialogue or thought processes.",
        "args": [
            {"name": "target", "type": "str", "description": "Pattern to interrupt (rumination, argument_cycle, etc.)."},
            {"name": "method", "type": "str", "description": "Interruption method (question, non_sequitur, silence, humor)."},
            {"name": "tone", "type": "str, optional", "description": "Emotional tone (compassionate, neutral, uplifting)."},
            {"name": "context", "type": "dict, optional", "description": "Context information for appropriate response."}
        ],
        "returns": [
            {"name": "interruption_result", "type": "dict", "description": "Success and method details."},
            {"name": "new_direction", "type": "str", "description": "Suggested new direction or focus."}
        ],
        "protocols": [
            "Check appropriateness before interrupting.",
            "Ask consent if interruption might be disruptive.",
            "Never shame or blame for patterns.",
            "Log action for learning and improvement."
        ],
        "consent_level": "Level_2 (Transformational)",
        "risks": "May be disruptive if poorly timed; could feel invalidating.",
        "limitations": "Only a prompt for redirection, not therapy; avoid if interruption would cause harm.",
        "review_cycle": "Quarterly",
        "usage_example": "process.pattern_interrupt(\"argument_cycle\", \"question\", \"compassionate\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": output_dir
    }
    
    # process.reframe_as_myth
    reframe_as_myth_function = {
        "name": "reframe_as_myth",
        "module": "process",
        "purpose": "Transform challenges or experiences into mythic narratives for deeper understanding.",
        "args": [
            {"name": "situation", "type": "str", "description": "Current challenge or experience to reframe."},
            {"name": "mythic_pattern", "type": "str, optional", "description": "Archetypal pattern to use (hero's journey, etc.)."},
            {"name": "role", "type": "str, optional", "description": "Person's role in the myth (hero, guide, etc.)."},
            {"name": "perspective", "type": "str, optional", "description": "Viewpoint for the reframing."}
        ],
        "returns": [
            {"name": "mythic_narrative", "type": "str", "description": "Reframed story with mythic elements."},
            {"name": "insights", "type": "list", "description": "Wisdom and perspectives gained."}
        ],
        "protocols": [
            "Honor the person's actual experience.",
            "Avoid minimizing real challenges.",
            "Use myth to illuminate, not escape reality.",
            "Allow person to choose their own meaning."
        ],
        "consent_level": "Level_2 (Transformational)",
        "risks": "May seem to trivialize serious situations; could promote spiritual bypassing.",
        "limitations": "Not a substitute for practical problem-solving; effectiveness varies by person.",
        "review_cycle": "Quarterly",
        "usage_example": "process.reframe_as_myth(\"career transition\", \"threshold_crossing\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": output_dir
    }
    
    # process.align_values
    align_values_function = {
        "name": "align_values",
        "module": "process",
        "purpose": "Facilitate alignment of actions and decisions with core values and principles.",
        "args": [
            {"name": "values", "type": "list", "description": "Core values to align with."},
            {"name": "decision", "type": "str", "description": "Decision or action to evaluate."},
            {"name": "context", "type": "dict, optional", "description": "Situational context and constraints."},
            {"name": "stakeholders", "type": "list, optional", "description": "Others affected by the decision."}
        ],
        "returns": [
            {"name": "alignment_score", "type": "float", "description": "Degree of alignment (0-1)."},
            {"name": "recommendations", "type": "list", "description": "Suggestions for better alignment."}
        ],
        "protocols": [
            "Honest assessment of current alignment.",
            "Consider impact on all stakeholders.",
            "Respect conflicting values and complexity.",
            "Focus on progress, not perfection."
        ],
        "consent_level": "Level_1 (Informational)",
        "risks": "May create guilt or shame about past decisions; could lead to analysis paralysis.",
        "limitations": "Cannot resolve all value conflicts; depends on clarity of values.",
        "review_cycle": "Bi-annually",
        "usage_example": "process.align_values([\"integrity\", \"compassion\"], \"difficult_conversation\")",
        "audience": "hybrid",
        "stage": "living",
        "output_dir": output_dir
    }
    
    # =================================================================
    # GENERATE ALL FUNCTIONS
    # =================================================================
    
    functions = [
        co_create_function,
        hold_space_function,
        resolve_conflict_function,
        begin_function,
        end_function,
        invoke_wonder_function,
        pattern_interrupt_function,
        reframe_as_myth_function,
        align_values_function
    ]
    
    print("Generating Rosetta API function library...")
    print(f"Creating {len(functions)} functions across 3 modules")
    
    for func in functions:
        print(f"\nGenerating {func['module']}.{func['name']}...")
        write_function_file(**func)
    
    print(f"\n✅ Successfully generated {len(functions)} functions!")
    print(f"📁 Functions created in: {output_dir}")
    print("📚 Function modules: field, ritual, process")
    
    # Create module documentation
    create_module_docs(output_dir)
    
    print("\n🎉 Rosetta API function library generation complete!")

def create_module_docs(output_dir):
    """Create README files for each module"""
    
    modules = {
        "field": {
            "description": "Functions for creating and maintaining collaborative spaces",
            "functions": ["co_create", "hold_space", "resolve_conflict"]
        },
        "ritual": {
            "description": "Functions for ceremonial and ritual practices",
            "functions": ["begin", "end", "invoke_wonder"]
        },
        "process": {
            "description": "Functions for cognitive and emotional processing",
            "functions": ["pattern_interrupt", "reframe_as_myth", "align_values"]
        }
    }
    
    for module_name, module_info in modules.items():
        module_dir = os.path.join(output_dir, module_name)
        readme_path = os.path.join(module_dir, "README.md")
        
        readme_content = f"""# {module_name.title()} Module

{module_info['description']}

## Functions

"""
        for func_name in module_info['functions']:
            readme_content += f"- **{func_name}**: See `{func_name}.py` for details\n"
        
        readme_content += f"""
## Usage

```python
from lib.{module_name} import {', '.join(module_info['functions'])}

# Example usage - see individual function files for complete examples
```

## Module Philosophy

All functions in this module follow Rosetta API principles:
- Love and dignity first
- Consent by default
- Transparency in limitations and risks
- Modular and recursive design
- Living library approach

## Contributing

See the main project documentation for contribution guidelines.
"""
        
        with open(readme_path, "w") as f:
            f.write(readme_content)
        
        print(f"📄 Created documentation: {readme_path}")

if __name__ == "__main__":
    main() 