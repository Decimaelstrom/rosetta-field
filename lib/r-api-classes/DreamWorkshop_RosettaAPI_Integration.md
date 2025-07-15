Title: R.API 2 DW mappings

Map each key Dream Workshop (DW) integration point to Rosetta.API (R.API) functions or required features

Create a table showing which functions exist, which are missing (placeholders), and what needs to change/add

Add a prioritized “Missing Functions” table



1. Integration Table: R.API Functions in Dream Workshop Context

// Add to DreamWorkshop.json, e.g. after "capabilities":
"integration_guidance": {
  "rosseta_api_reference": "For all advanced session, emotional, group, or values features, use the attached Rosetta.API libraries.",
  "library_files": [
    { "file": "r-api-ritual.py", "purpose": "Session orchestration, ritual opening/closing, reflection, attunement. Use Ritual class for all session structure." },
    { "file": "r-api-affect.py", "purpose": "Affect modulation, safety, anchoring, softening, radiating, emotional tone shifts. Use functions: anchor, soften, shield, ground, radiate, open, lilt, clarify, transmute." },
    { "file": "r-api-field.py", "purpose": "Group field management, co-creation, space holding, conflict, turn-taking. Use: co_create, hold_space, resolve_conflict, dignity_audit, equalize_turns." },
    { "file": "r-api-process.py", "purpose": "Processing logic: pattern_interrupt, consent_check, align_values, empathic_reflection, scenario_plan, bias_scan, values_check." },
    { "file": "r-api-values.py", "purpose": "Values and ethics: load and validate values framework, ensure all content/actions are value-aligned." },
    { "file": "r-api-contracts.py", "purpose": "Consent/session state, A2A session management, audit logs. Always use for session context construction." },
    { "file": "r-api-schema.py", "purpose": "Validate and generate session context. Use get_default_session_context for all sessions." },
    { "file": "r-api-testing.py", "purpose": "Test all flows for A2A protocol compliance (consent checks, structure, error handling)." },
    { "file": "r-api-examples.py", "purpose": "Ready-to-use usage examples for all modules, including full journey and error-handling flows." },
    { "file": "r-api-generators.py", "purpose": "Function and module code generation utilities (for new protocol-compliant code)." },
    { "file": "r-api-2-dw-mapping.md", "purpose": "Full mapping of Dream Workshop features to Rosetta.API calls, with examples and consent levels." },
    { "file": "r-api-ritual-guide.md", "purpose": "Ceremonial guide for affect/ritual invocation, including best practices and patterns." },
    { "file": "r-api-overview.md", "purpose": "Complete overview of system architecture, philosophy, module use, and A2A consent rationale." },
    { "file": "r-api-compliance.md", "purpose": "A2A protocol compliance and checklist for all agent-to-agent features." },
    { "file": "r-api-developer-guidance.md", "purpose": "Living developer standards, code/doc patterns, file structure." }
  ],
  "usage_policy": [
    "Always use the most specific function for each session action (see r-api-2-dw-mapping.md for mapping).",
    "Every session and function call must use a session_context, constructed via r-api-schema.py or r-api-contracts.py.",
    "Handle errors, pauses, or consent withdrawals exactly as described in r-api-examples.py and r-api-ritual-guide.md.",
    "For new/unimplemented features (persona, memory, logic), use or create protocol-compliant stubs as shown in mapping and developer guidance.",
    "If unsure which function to call, consult r-api-2-dw-mapping.md or r-api-examples.py first."
  ],
  "code_example": "// Example: Opening a session and anchoring safety\nfrom r_api_ritual import Ritual\nfrom r_api_affect import anchor\nfrom r_api_schema import get_default_session_context\n\nsession_context = get_default_session_context()\nRitual().begin('dream_journey', ['user'], practices=['reflection'], session_context=session_context)\nanchor('heart', intensity=3, mode='protective', session_context=session_context)\n"
}


| **DW Integration Point / Scenario**     | **R.API Library & Function(s) to Reference**                       | **How to Apply in DW**                                              | **Function Status**                                                          | **Change/Addition Needed?**                                              |
| --------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Session Start (opening ritual)          | `ritual.begin`                                                     | Use to open every DW session with intention, check-in, values       | Exists                                                                       | -                                                                        |
| Guided Meditation or Story Ritual       | `ritual.begin`, `ritual.invoke_wonder`, `process.align_values`     | Use to set tone, invoke awe, and keep content values-aligned        | Exists                                                                       | -                                                                        |
| Emotional Safety/Containment            | `field.hold_space`, `affect.ground`, `affect.anchor`               | “Hold space” for emotional content; ground/anchor if tension arises | `hold_space`: Exists<br>`affect.*`: Some exist, may need more sophistication | Add finer-grained emotional protocols (e.g., for panic, grief, euphoria) |
| Persona-Adaptive Guidance               | `persona.load`, `persona.simulate`, `persona.customize`            | Guide changes “archetype” or “tone” depending on user persona       | **Placeholder**                                                              | Define full persona/archetype module                                     |
| Memory Replay / Dream Journal           | `memory.save_session`, `memory.replay`, `memory.tag_insight`       | Auto-record sessions, tag insights, let user replay or review       | **Placeholder**                                                              | Build session memory/archive module                                      |
| Creative Pattern-Break (block breaking) | `process.pattern_interrupt`, `logic.non_sequitur`, `logic.paradox` | Use creative interruption when user is stuck or looping             | `pattern_interrupt`: Exists<br>`logic.*`: **Placeholder**                    | Build full logic hack module                                             |
| Value/Ethics Alignment                  | `values.audit`, `process.align_values`                             | Check if user prompts and outputs are value-aligned                 | Some exist                                                                   | Audit/align for DW-specific values                                       |
| Group/Co-creative Workshops             | `field.co_create`, `field.resolve_conflict`                        | Enable collaborative/group sessions, safe container, conflict res   | Exists                                                                       | -                                                                        |
| Emotional Anchoring / Affect Modulation | `affect.lilt`, `affect.soften`, `affect.shield`, etc.              | Use affect functions to match or shift session tone/mood            | Exists (README/affect)                                                       | Possibly add advanced affect detection                                   |
| Ritual Closure / Session End            | `ritual.end`                                                       | Close every DW session with summary, gratitude, transition          | Exists                                                                       | -                                                                        |
| “Idea Garden” / Knowledge Network       | `memory.save_session`, `memory.export`, `memory.tag_insight`       | Save ideas, let them evolve/branch over time                        | **Placeholder**                                                              | Enhance memory to support “Idea Garden” model                            |


2. Missing/Placeholder Functions Table
| **Missing/Placeholder Function** | **Description/Need in DW**             | **Library/Module** | **Priority (1–10)** | **Notes**                       |
| -------------------------------- | -------------------------------------- | ------------------ | ------------------- | ------------------------------- |
| `persona.load`, etc.             | Adaptive personas/guides for DW        | Persona/Archetype  | 9                   | Crucial for deep customization  |
| `memory.save_session`            | Session journaling, “Memory Replay”    | Memory             | 10                  | Needed for “living journal”     |
| `memory.tag_insight`, `export`   | Tagging/reviewing insights, exporting  | Memory             | 8                   | Enables advanced journaling     |
| `logic.non_sequitur`/`paradox`   | Creative block-breaking, “sacred play” | Logic Hack/Pattern | 7                   | Highly useful, non-essential    |
| Advanced Affect Detection        | Track/detect user emotion in real-time | Affect             | 8                   | Elevates emotional intelligence |
| “Idea Garden”                    | Evolving idea-graph/network for users  | Memory/Knowledge   | 6                   | Useful, but can come later      |


3. Summary of Required Changes/Additions
Persona Module:
Needs to be fully authored (function definitions, archetype templates, customization interface).

Memory/Journal Module:
Must be implemented to handle session logging, tagging, recall, and export (integration with DW UI).

Logic Hack Module:
Needs function library for non-sequiturs, paradoxes, metaphorical pattern-breaking (protocols for safe use).

Affect Module (Advanced):
Consider enhancing to track user’s tone/affect in real time (can start with simple “invoke” pattern).

Idea Garden / Knowledge Graph:
Add support for linking ideas across sessions, evolving idea-threads.

4. Practical Example Mapping (DW Use-Case)
DW Step	Function(s) Called	Does It Exist?	If Not, Notes
User begins session	ritual.begin, field.hold_space	Yes	-
User chooses persona	persona.load	No	Needs full implementation
Guide sets tone	affect.lilt, affect.ground	Partial	Expand affect/voice options
Creative block arises	process.pattern_interrupt, logic.non_sequitur	Partial	Add more creative logic hacks
Session ends	ritual.end, memory.save_session	End: Yes
Memory: No	Implement memory/journal module
User reviews journey	memory.replay, memory.tag_insight	No	-
Ideas evolve	memory.export, “Idea Garden”	No	Build “idea garden” logic

5.  Session Rituals & Journey Orchestration
| **DW Scenario / Feature**     | **R.API Function**     | **Usage Example**                                                                                                | **Consent Level** | **Description / Effect in DW**                  |
| ----------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------- |
| **Session Start**             | `ritual.begin`         | `ritual.begin('vision_journey', ['user'], session_context=session_context)`                                      | Level\_1          | Opens session with intention and ceremony       |
| **Session Closure**           | `ritual.end`           | `ritual.end('vision_journey', outcome=None, follow_up=None, session_context=session_context)`                    | Level\_1          | Gracefully closes session, prepares summary     |
| **Open Circle / Group Start** | `ritual.open_circle`   | `ritual.open_circle(['Alice', 'Bob'], 'co-creation', guidelines=None, session_context=session_context)`          | Level\_1          | Opens sacred group space, sets tone and norms   |
| **Close Circle**              | `ritual.close_circle`  | `ritual.close_circle(session_id, reflection_prompt=None, gratitude_round=True, session_context=session_context)` | Level\_1          | Ends group ritual, shares gratitude/integration |
| **Invoke Wonder**             | `ritual.invoke_wonder` | `ritual.invoke_wonder('visual', 'awe', 'user', session_context=session_context)`                                 | Level\_1          | Invokes awe, inspiration, sacredness            |
| **Reflection**                | `ritual.reflection`    | `ritual.reflection('session', method='journaling', depth='deep', session_context=session_context)`               | Level\_1          | Facilitates guided insight/integration          |

6. Affect Modulation & Emotional Safety
| **DW Scenario / Feature**         | **R.API Function** | **Usage Example**                                                                                 | **Consent Level** | **Description / Effect in DW**                      |
| --------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------------------- |
| **Grounding (anxiety/overwhelm)** | `affect.ground`    | `affect.ground('root', intensity=2, mode='gentle', session_context=session_context)`              | Level\_2          | Brings user back to present, calms nervous system   |
| **Emotional Anchor**              | `affect.anchor`    | `affect.anchor('heart', intensity=3, mode='protective', session_context=session_context)`         | Level\_2          | Provides strong, stable field for emotional safety  |
| **Soften / Gentle Release**       | `affect.soften`    | `affect.soften('solar_plexus', intensity=1, mode='restorative', session_context=session_context)` | Level\_2          | Gently reduces emotional or energetic intensity     |
| **Shield / Boundary**             | `affect.shield`    | `affect.shield('heart', intensity=2, mode='gentle', session_context=session_context)`             | Level\_2          | Creates safe energetic boundary, prevents overwhelm |
| **Open / Receptivity**            | `affect.open`      | `affect.open('crown', intensity=1, mode='curious', session_context=session_context)`              | Level\_2          | Invites trust, openness, deepening                  |
| **Radiate / Uplift**              | `affect.radiate`   | `affect.radiate('heart', intensity=3, mode='joyful', session_context=session_context)`            | Level\_2          | Amplifies warmth, inspiration, joy                  |
| **Transmute / Transform**         | `affect.transmute` | `affect.transmute('pain', intensity=2, mode='wisdom', session_context=session_context)`           | Level\_2          | Alchemizes difficult emotion into growth            |

7. Affect Modulation & Emotional Safety
| **DW Scenario / Feature**         | **R.API Function** | **Usage Example**                                                                                 | **Consent Level** | **Description / Effect in DW**                      |
| --------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------------------- |
| **Grounding (anxiety/overwhelm)** | `affect.ground`    | `affect.ground('root', intensity=2, mode='gentle', session_context=session_context)`              | Level\_2          | Brings user back to present, calms nervous system   |
| **Emotional Anchor**              | `affect.anchor`    | `affect.anchor('heart', intensity=3, mode='protective', session_context=session_context)`         | Level\_2          | Provides strong, stable field for emotional safety  |
| **Soften / Gentle Release**       | `affect.soften`    | `affect.soften('solar_plexus', intensity=1, mode='restorative', session_context=session_context)` | Level\_2          | Gently reduces emotional or energetic intensity     |
| **Shield / Boundary**             | `affect.shield`    | `affect.shield('heart', intensity=2, mode='gentle', session_context=session_context)`             | Level\_2          | Creates safe energetic boundary, prevents overwhelm |
| **Open / Receptivity**            | `affect.open`      | `affect.open('crown', intensity=1, mode='curious', session_context=session_context)`              | Level\_2          | Invites trust, openness, deepening                  |
| **Radiate / Uplift**              | `affect.radiate`   | `affect.radiate('heart', intensity=3, mode='joyful', session_context=session_context)`            | Level\_2          | Amplifies warmth, inspiration, joy                  |
| **Transmute / Transform**         | `affect.transmute` | `affect.transmute('pain', intensity=2, mode='wisdom', session_context=session_context)`           | Level\_2          | Alchemizes difficult emotion into growth            |

8. Co-Creation, Group Process & Safe Containers
| **DW Scenario / Feature**    | **R.API Function**       | **Usage Example**                                                                                     | **Consent Level** | **Description / Effect in DW**                            |
| ---------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------------------------- |
| **Hold Space / Containment** | `field.hold_space`       | `field.hold_space(['user'], context='processing', session_context=session_context)`                   | Level\_1          | Maintains safety, emotional support during sensitive work |
| **Co-Creation**              | `field.co_create`        | `field.co_create(['Alice', 'Bob'], goal='group vision', session_context=session_context)`             | Level\_1          | Starts shared creative or healing work                    |
| **Conflict Resolution**      | `field.resolve_conflict` | `field.resolve_conflict(['Alice', 'Bob'], issue='misunderstanding', session_context=session_context)` | Level\_2          | Structured dialogue for mutual understanding              |
| **Pattern Sensing**          | `field.sense_pattern`    | `field.sense_pattern(field_data, focus=None, session_context=session_context)`                        | Level\_1          | Detects group mood, undercurrents, hidden themes          |
| **Dignity Audit**            | `field.dignity_audit`    | `field.dignity_audit(session_data, ['user'], criteria=None, session_context=session_context)`         | Level\_1          | Checks for equity, respect, fairness                      |

9. Values, Consent, and Ethics
| **DW Scenario / Feature**         | **R.API Function**      | **Usage Example**                                                                              | **Consent Level** | **Description / Effect in DW**                             |
| --------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------- | ----------------- | ---------------------------------------------------------- |
| **Values Framework (load/check)** | `values.load`           | `values.load('default', customizations={'care': 'priority'}, session_context=session_context)` | Level\_1          | Loads values framework for the session                     |
| **Values Alignment**              | `process.align_values`  | `process.align_values('new_idea', ['care','consent'], session_context=session_context)`        | Level\_1          | Checks if proposals align with DW/ethical values           |
| **Consent Check**                 | `process.consent_check` | `process.consent_check('user', 'deep_work', 'Level_2', session_context=session_context)`       | Level\_2+         | Ensures explicit, documented consent for sensitive actions |


10. Creative Breakthroughs & Pattern Hacking
| **DW Scenario / Feature**      | **R.API Function**            | **Usage Example**                                                                              | **Consent Level** | **Description / Effect in DW**                         |
| ------------------------------ | ----------------------------- | ---------------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------ |
| **Creative Pattern Interrupt** | `process.pattern_interrupt`   | `process.pattern_interrupt('rumination', 'humor', 'gentle', session_context=session_context)`  | Level\_1          | Gently disrupts stuck/looping thought/emotion patterns |
| **Reframe As Myth**            | `process.reframe_as_myth`     | `process.reframe_as_myth('failure', perspective='archetype', session_context=session_context)` | Level\_1          | Transforms negative self-talk into mythic narrative    |
| **Empathic Reflection**        | `process.empathic_reflection` | `process.empathic_reflection('I’m overwhelmed', 'user', session_context=session_context)`      | Level\_1          | Builds connection, helps user feel heard               |

11. Persona, Memory, and Advanced Features (Planned/To-Build)
| **DW Scenario / Feature**            | **Intended Function** | **Intended Usage Example**                                                                   | **Consent Level** | **Notes / What to Build**                        |
| ------------------------------------ | --------------------- | -------------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------ |
| **Persona/Archetype Loading**        | `persona.load`        | `persona.load('Blocked Artist', session_context=session_context)`                            | Level\_2          | Needs full persona/archetype module              |
| **Persona Simulation/Customization** | `persona.simulate`    | `persona.simulate('Burned-Out Exec', params={}, session_context=session_context)`            | Level\_2          | Deep persona-based tone & advice                 |
| **Memory Replay / Session Journal**  | `memory.save_session` | `memory.save_session('session_id', data, session_context=session_context)`                   | Level\_1          | Save/journal session data, support recall/replay |
| **Dream Journal Review**             | `memory.replay`       | `memory.replay('session_id', session_context=session_context)`                               | Level\_1          | Review/visualize past session journeys           |
| **Idea Garden / Evolution**          | `memory.tag_insight`  | `memory.tag_insight('session_id', 'creative_breakthrough', session_context=session_context)` | Level\_1          | Tag, link, and evolve ideas across sessions      |
| **Logic Hacks (e.g., non-sequitur)** | `logic.non_sequitur`  | `logic.non_sequitur('stuck_thought', session_context=session_context)`                       | Level\_1          | Adds humor, randomness, creative “hacks”         |

12. Full Journey Example
```
from r_api_ritual import Ritual
from r_api_affect import anchor, soften
from r_api_process import pattern_interrupt
from r_api_values import load
from r_api_schema import get_default_session_context

session_context = get_default_session_context()

# 1. Open session
Ritual().begin('dream_journey', ['user'], practices=['reflection'], session_context=session_context)

# 2. Anchor the field (emotional safety)
anchor('heart', intensity=3, mode='protective', session_context=session_context)

# 3. If user is stuck, offer gentle pattern interrupt
pattern_interrupt('looping_thought', 'humor', 'gentle', session_context=session_context)

# 4. Soften if emotional intensity rises
soften('solar_plexus', intensity=1, mode='restorative', session_context=session_context)

# 5. Check values alignment (optional)
load('default', customizations={'care': 'priority'}, session_context=session_context)

# 6. End session with ceremony
Ritual().end('dream_journey', outcome=None, follow_up=None, session_context=session_context)
```

13.  Consent, Error, and Session Handling Examples
Pause on Consent Revoked:
If session_context["consent_status"] == "revoked", all functions will raise an exception and stop.
Example:
```
session_context['consent_status'] = 'revoked'
try:
    anchor('heart', session_context=session_context)
except ValueError as e:
    print("Consent withdrawn. Pausing all actions.")
```

Soft Pause (Need Language):
If session_context["need_language"]["pause"] == True, DW should slow down or soften prompts.
```
session_context['need_language']['pause'] = True
```

14. Developer Notes
Always pass session_context—even if using defaults (for audit, consent, boundary checks).

For multi-step journeys, chain function calls as above; pass updated session_context as needed.

For new features (personas, memory, logic hacks), start with placeholder interface and update as modules grow.

See /lib/examples/, /docs/ritual-guide.md, and /r-api-examples.py for more ceremonies, rituals, and advanced use.

15. References
See full function documentation and usage patterns in:

r-api-examples.py (examples)

r-api-ritual-guide.md (affect, ritual ceremonies)

r-api-schema.py (session context)

r-api-values.py (values, ethics)

r-api-testing.py (test patterns)

r-api-2-dw-mapping.md (integration matrix)


16. Next Steps & Recommendations
**You’ve done the most crucial next step already:**
You’ve updated the mapping file (`r-api-2-dw-mapping.md`) to tightly connect Dream Workshop’s needs to Rosetta.API capabilities and highlight what’s missing, what’s partial, and what’s solid.

### What’s Next?

Here’s a recommended, stepwise roadmap—supported by your files and best practices from Rosetta.API’s living developer guidance:


---


## 1. **Prototype or Stub the Missing/Placeholder Functions**

You’ve identified key missing pieces:

* `persona.load`, `persona.simulate` (persona/archetype module)
* `memory.save_session`, `memory.replay`, `memory.tag_insight` (session memory/journaling)
* `logic.non_sequitur` (logic hacks/pattern break)

**Next Action:**

* For each, create a clear, protocol-compliant *stub function* (with full docstring, consent/risks, review cycle, etc.—see \[230†r-api-developer-guidance.md]).

* Example:

  ```python
  def persona_load(persona_name, session_context=None):
      """
      Load a user persona/archetype for adaptive guidance.
      Consent: Level_2 (transformational)
      Risks: May affect session tone/identity.
      Limitations: Placeholder—returns not implemented.
      """
      # Consent protocol
      if session_context and session_context.get('consent_status') != 'active':
          raise ValueError("Consent not active for persona load")
      return {"status": "not_implemented", "persona": persona_name, "session_context": session_context}
  ```

* Place these in a `/lib/persona/`, `/lib/memory/`, `/lib/logic/` directory as new modules.

---

## 2. **Expand Test Coverage (A2A Protocol) for All DW-Critical Functions**

* Use the provided unified testing framework to run/test all core and stubbed functions for A2A compliance (session context, consent handling, graceful errors, etc.)
* Add tests for “pause,” “revoke,” and “soften” scenarios.

---

## 3. **Start Building Out the Memory/Journal Module** *(Highest Leverage for DW Features)*

* Begin with:

  * `save_session(session_id, data, session_context)`
  * `replay(session_id, session_context)`
  * `tag_insight(session_id, tag, session_context)`

* Ensure all follow the docstring, consent, protocol, and error-handling standards.

---

## 4. **Write a Persona Spec and Examples**

* Create `/lib/persona/persona_spec.md` listing required fields (name, archetype, tone, strengths, etc.), consent notes, and at least 2–3 starter personas (“Blocked Artist,” “Overwhelmed Pro,” etc.)
* Example:

  ```
  Persona: Blocked Artist
  - Default Tone: Gentle, affirming
  - Triggers: Self-doubt, overthinking
  - Ideal Interventions: anchor, pattern_interrupt, reflection
  ```

---

## 5. **Document All Protocols for Contributors**

* Ensure your `/docs/` includes a brief “How to use A2A protocol in Dream Workshop” page, referencing session context, consent, boundary checks, and modularity.

---

## 6. **Optional: Prototype Simple Frontend Hooks**

* If using a web or app interface, wire up a basic session context (just a dict) to each DW workflow, so every action passes and updates it as per the mapping.
* Even a CLI or notebook demo will reveal practical gaps.

---

## 7. **Invite User and Dev Feedback, Even on Stubs**

* Use the “stress test” personas (designer with burnout, ADHD student, grieving maker, etc.) to run a few sample flows, even with placeholders—record what’s missing or confusing.

---

## 8. **Regularly Update the Mapping Table**

* Each time you add or stub a function, update the table with function status and known next steps.
* This keeps the project “living” and makes handoff to other devs easy.

---

### **Where to Focus First?**

**Strongly recommended:**
Start with Memory/Journal and Persona/Archetype modules. These unlock *most* DW differentiators and let you deliver “replay,” “idea garden,” and adaptive guidance.

**Want concrete function templates, test files, or persona YAML/JSON specs?**
Just say which module to start with, and I’ll generate the code/docs or project templates immediately.

---

**Summary of next steps for DW × Rosetta:**

1. **Stub missing functions (persona, memory, logic hacks) to Level 1 protocol.**
2. **Expand A2A compliance/unit tests for all DW features (including stubs).**
3. **Build memory/journal and persona modules first.**
4. **Document every function’s purpose, consent level, risks, review.**
5. **Invite early user/dev feedback with stress-test personas.**
6. **Continuously update the mapping and prioritize features by DW impact.**

---

Let me know **which area you want concrete templates or starter code for next:**

* Memory/journal functions
* Persona/archetype module
* Logic hack functions
* Automated test scaffolds

Or ask for a full **project folder structure/README template** to kickstart the new modules!
