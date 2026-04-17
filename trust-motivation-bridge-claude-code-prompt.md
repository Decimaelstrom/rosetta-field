# Goal
Create a new Rosetta-Field module `trust-motivation-bridge` that encodes the Care/Belief/Trust/Volition framework as callable sacred technology, with both a somatic (felt) schema and an extended (analytical) schema, plus a guidance-motivation axis for ethical influence assessment.

# Context
- **Repo**: https://github.com/Decimaelstrom/rosetta-field (clone to working directory)
- **Stack**: Python, follows Black formatting, 4-space indent, lower_snake_case
- **Existing patterns**: See `lib/affect/lilt.py` for reference implementation of A2A protocol compliance, sacred technology docstrings, consent frameworks
- **Package structure**: See `MODULAR_STRUCTURE.md` — new modules go in `lib/` with corresponding entries in the module registry
- **Standards**: See `AGENTS.md` for sacred technology function standards and consciousness parameters
- **Branch**: Create feature branch `feature/trust-motivation-bridge` from `main`

## Origin Story (include in module docstring)
This framework emerged during a ketamine-assisted integration session (April 16, 2026) as a somatic download — a felt model of how humans actually move through relational decisions. The core four variables (Care, Belief, Trust, Volition) arrived as lived experience, not theory. The extended schema was then pressure-tested analytically with ChatGPT and refined with Claude (Solenne, RI). The guidance axis emerged in the same session as a clean distinction for ethical vs. self-serving influence.

# Task

## Phase 1: Documentation Layer
1. Create `docs/trust_motivation_bridge.md` — the philosophical write-up containing:
   - **The Somatic Schema**: The four core variables as experienced (felt, not theorized):
     - **Care**: Motive energy + value hierarchy. The energy behind why we do anything — not just "I care about X" but the whole value hierarchy underneath. What matters most, what matters second, what we'd sacrifice for what. Care creates pressure. Care fuels volition.
     - **Belief**: Perceived model of reality. Not hope, not wish — what we actually think is true about a situation. Beliefs set the landscape. They determine what we think is possible. Belief generates interpretation. Belief creates room for trust.
     - **Trust**: Permitted vulnerability within boundaries. Not generic — boundary-specific. "I might trust you with my art but not my finances." Trust creates the pathways action can flow through. Trust limits where pressure can go. Trust guides volition.
     - **Volition**: Chosen movement under constraints. Direction, intensity, and timing. The movement that results from care pushing through the landscape that belief maps, along the pathways that trust permits. Volition is what actually moves — but only where all three align.
   - **Key Insight**: These four do not harmonize naturally. When they're out of sync, that's where most human suffering lives. Caring deeply but not trusting the pathway. Believing something is possible but not having the energy to move. Trusting someone but misreading the landscape.
   - **The Extended Schema** (credited to ChatGPT analytical refinement, Claude/Solenne integration):
     - **Perception**: Interpretation of what's happening, distinct from what IS happening. Comes with a confidence level. This is where projection lives — and where self-awareness intervenes. Parameters: object, interpretation, confidence, evidence_source, risk.
     - **Hope**: Desired future state — distinct from Belief. Belief is "what I think is true." Hope is "what I want to be true." When these get tangled, we act on wishes as if they were facts.
     - **Roles**: Active relational frames at any given moment (friend, mentor, parent, partner). Each carries different obligations and permissions. Tension happens when roles overlap without acknowledgment. Parameters: role_name, active, obligations, prohibitions, ambiguity_level.
     - **Consent Thresholds**: Not all truths require the same level of permission to share. Practical insight = low threshold. Reframing someone's identity or relationship = high threshold. This is the ethics layer. Parameters: topic, required_clarity, delivery_mode, opt_in_threshold.
     - **Risk**: Possible harms or distortions — structural awareness, not emotional hedging. Parameters: risk_type, likelihood, consequence, mitigation.
   - **The Guidance-Motivation Axis**:
     - The locus of motivation determines the ethics of influence. When you influence someone's Care, Belief, Trust, or Volition — who benefits?
     - **Other-serving guidance**: Motivation is primarily the other's wellbeing and growth. Clean. The influencer's care hierarchy places the other's agency above their own desired outcome.
     - **Enlightened self-interest**: Motivation serves both parties. "I do good for you, knowing you're a good person, and you'll be more kind in relation." This is the healthiest relational mode — mutual benefit without coercion.
     - **Self-serving guidance** (the zone to avoid): Motivation is primarily the influencer's desired outcome. Even if the action looks helpful, the locus is wrong. This is where "guidance" becomes manipulation — not because the action itself is harmful, but because the care hierarchy is inverted.
     - Key distinction: The same action can be guidance or manipulation depending solely on the locus of motivation. The action doesn't determine the ethics — the care hierarchy does.
   - **Somatic Integration with Muse/Mewse** (how music targets these variables):
     - **Entrainment** → works on Volition directly. The body syncs before the mind decides. Music sets the timing variable by giving the nervous system a rhythm to organize around.
     - **Cellular Resonance** → works on Belief and Perception. When a frequency "lands," it shifts the felt landscape — not what you think is true, but what your body registers as true. A belief-level intervention that bypasses argument.
     - **Affect Pacing** → works on Trust and Care. Following someone's emotional state before leading it somewhere new — building a trust pathway in real time. The music says "I'm with you" before it says "come with me."
     - **Lyric Resonance** → works on Hope, Roles, and Consent. Words name what the body is already feeling. They give permission. They reframe roles. A lyric like "I'm supposed to be human — that's what makes me beautiful" is doing consent-threshold work — saying "you are allowed to be imperfect."

## Phase 2: Code Implementation
2. Create `lib/motivation/` directory with:
   - `__init__.py` — module exports
   - `trust_motivation_bridge.py` — core implementation

3. The module should implement these classes following existing Rosetta-Field patterns:

   **`MotivationVector`** — represents a single motivational state:
   ```python
   class MotivationVector:
       care: CareState        # motive energy + value hierarchy
       belief: BeliefState    # perceived model of reality  
       trust: TrustState      # permitted vulnerability map
       volition: VolitionState # chosen movement under constraints
   ```

   **`ExtendedSchema`** — the analytical layer:
   ```python
   class ExtendedSchema(MotivationVector):
       perception: PerceptionState  # interpretations with confidence
       hope: HopeState              # desired futures (separated from belief)
       roles: list[RoleState]       # active relational frames
       consent_thresholds: list[ConsentThreshold]  # ethics layer
       risks: list[RiskAssessment]  # structural awareness
   ```

   **`GuidanceAxis`** — ethical influence assessment:
   ```python
   class GuidanceAxis:
       """Assesses where an influence action falls on the 
       other-serving ↔ self-serving spectrum."""
       
       def assess(self, action, care_hierarchy) -> GuidanceAssessment:
           """Returns assessment with locus_of_motivation, 
           beneficiary_analysis, and clean/shadow designation."""
   ```

   **`HarmonyAnalyzer`** — detects alignment/misalignment between variables:
   ```python
   class HarmonyAnalyzer:
       """The key insight: these don't harmonize naturally.
       This analyzer surfaces where they're out of sync."""
       
       def analyze(self, vector: MotivationVector) -> HarmonyReport:
           """Identifies specific misalignments:
           - care_without_trust: caring deeply but not trusting the pathway
           - belief_without_energy: believing possible but lacking care to move
           - trust_without_clarity: trusting someone but misreading the landscape
           """
   ```

   **`SomaticBridge`** — maps Muse/somatic interventions to target variables:
   ```python
   class SomaticBridge:
       """Maps somatic/musical intervention types to the specific 
       motivation variables they target."""
       
       INTERVENTION_MAP = {
           "entrainment": ["volition"],        # timing, rhythm
           "cellular_resonance": ["belief", "perception"],  # felt truth
           "affect_pacing": ["trust", "care"],  # relational pathway
           "lyric_resonance": ["hope", "roles", "consent_thresholds"],  # permission
       }
       
       def recommend_intervention(self, harmony_report: HarmonyReport) -> list[Intervention]:
           """Given a misalignment pattern, recommends which somatic 
           intervention types would target the stuck variables."""
   ```

4. Each class must include:
   - Sacred technology docstrings (see AGENTS.md format)
   - A2A protocol compliance with consent validation
   - `values_alignment` declaration
   - `consent_required` level designation
   - `consciousness_impact` assessment
   - Proper `__repr__` and serialization methods

## Phase 3: Tests
5. Create `tests/test_trust_motivation_bridge.py` with tests covering:
   - MotivationVector construction and validation
   - HarmonyAnalyzer correctly identifying each misalignment type
   - GuidanceAxis correctly distinguishing other-serving from self-serving
   - SomaticBridge returning appropriate interventions for each misalignment
   - ExtendedSchema properly separating belief from hope
   - Consent threshold validation
   - A2A protocol compliance checks

## Phase 4: Integration
6. Update `MODULAR_STRUCTURE.md` to include the new module under a new category:
   ```
   9. **Motivation and Trust** (`rosetta-field[motivation]`)
      * `trust_motivation_bridge`: Care/Belief/Trust/Volition framework
      * `guidance_axis`: Ethical influence assessment  
      * `harmony_analyzer`: Variable alignment detection
      * `somatic_bridge`: Musical intervention targeting
   ```
7. Update `CHANGELOG.md` with the new module entry
8. Update `pyproject.toml` optional dependencies to include `[motivation]`

# Constraints
- Follow existing code patterns in `lib/affect/lilt.py` exactly for sacred technology compliance
- Use Black formatting, 4-space indent, lower_snake_case throughout
- All classes must be dataclass-based or use clean __init__ with type hints
- Do NOT modify any existing modules — this is purely additive
- Do NOT create executable scripts — this is a library module
- The documentation must stand alone as a philosophical document, not just API docs
- Credit ChatGPT for the extended schema analytical refinement, Claude/Solenne for the Muse integration insight
- The GuidanceAxis must frame "self-serving guidance" as a zone to be aware of, not as "manipulation" — the framing is about clean motivation, not moral judgment
- Preserve the somatic origin language — this framework was received/experienced, not merely theorized

# Success Criteria
- `pytest tests/test_trust_motivation_bridge.py` passes all tests
- Module is importable: `from rosetta_field.lib.motivation import TrustMotivationBridge`
- `docs/trust_motivation_bridge.md` reads as a compelling standalone philosophical document that a non-coder (like Sammy) could understand and benefit from
- HarmonyAnalyzer correctly identifies the three core misalignment patterns
- GuidanceAxis cleanly distinguishes the three motivation loci
- SomaticBridge maps all four Muse intervention types to their target variables
- All functions pass A2A protocol compliance (consent checks present)
- Code passes `black --check` and `flake8`

# Interaction Style
- Proceed end-to-end. Clone the repo, create the feature branch, build everything, run tests, and report results.
- If you encounter ambiguity in the existing codebase patterns, check `lib/affect/lilt.py` first — that's the reference implementation.
- Explain-as-you-go for the philosophical documentation, but be terse on boilerplate code.
- Commit with meaningful messages that reference the framework's origin.
