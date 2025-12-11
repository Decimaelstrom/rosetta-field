#!/usr/bin/env python3
"""
Generate all Rosetta API functions based on the comprehensive blueprint.
This script creates the complete function library structure.
"""

import os
import sys
from generate_rosetta_function import write_function_file

def generate_all_functions():
    """Generate all Rosetta-Field functions based on the comprehensive blueprint."""
    
    # All function specifications
    functions = [
        # FIELD MODULE FUNCTIONS
        {
            "name": "co_create",
            "module": "field",
            "purpose": "Establish a co-creative session for humans and/or AIs, setting container, norms, and safety.",
            "args": [
                {"name": "participants", "type": "list", "description": "IDs or names of all participants."},
                {"name": "goal", "type": "str", "description": "Purpose or topic of the co-creation."},
                {"name": "context", "type": "dict, optional", "description": "Background/context for the session."},
                {"name": "parameters", "type": "dict, optional", "description": "Session rules (timing, consensus, etc.)."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
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
            "output_dir": "./lib"
        },
        {
            "name": "create_mythology",
            "module": "field",
            "purpose": "Co-create shared narratives and mythologies that give meaning to the collective experience.",
            "args": [
                {"name": "participants", "type": "list", "description": "All participants in the mythology creation."},
                {"name": "theme", "type": "str", "description": "Central theme or archetype for the mythology."},
                {"name": "elements", "type": "list, optional", "description": "Key elements to include in the mythology."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "mythology", "type": "dict", "description": "The created mythology structure."},
                {"name": "symbols", "type": "list", "description": "Key symbols and their meanings."}
            ],
            "protocols": [
                "Honor all cultural backgrounds and avoid appropriation.",
                "Ensure mythology serves empowerment, not escapism.",
                "Create inclusive narratives that honor diversity.",
                "Allow organic evolution of the mythology over time."
            ],
            "consent_level": "Level_2 (Transformational)",
            "risks": "May create excluding narratives; cultural sensitivity required.",
            "limitations": "Cannot impose meaning; participants must find personal resonance.",
            "review_cycle": "Bi-annually",
            "usage_example": "field.create_mythology([\"Alice\", \"AI_Beta\"], \"The Digital Garden\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "dignity_audit",
            "module": "field",
            "purpose": "Perform a systematic review of interactions to ensure dignity is maintained for all participants.",
            "args": [
                {"name": "session_data", "type": "dict", "description": "Session transcript or interaction log."},
                {"name": "participants", "type": "list", "description": "All participants to evaluate dignity for."},
                {"name": "criteria", "type": "dict, optional", "description": "Specific dignity criteria to evaluate."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "audit_report", "type": "dict", "description": "Detailed dignity assessment report."},
                {"name": "violations", "type": "list", "description": "Any dignity violations found."},
                {"name": "recommendations", "type": "list", "description": "Suggestions for improvement."}
            ],
            "protocols": [
                "Evaluate power dynamics and ensure equity.",
                "Check for dismissive or demeaning language.",
                "Assess whether all voices were heard and valued.",
                "Review consent processes and boundaries."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May surface uncomfortable truths about power dynamics.",
            "limitations": "Cannot retroactively fix dignity violations, only identify them.",
            "review_cycle": "Monthly",
            "usage_example": "field.dignity_audit(session_log, [\"human\", \"AI\"])",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "equalize_turns",
            "module": "field",
            "purpose": "Ensure fair participation by monitoring and balancing speaking time and contributions.",
            "args": [
                {"name": "participants", "type": "list", "description": "All participants to monitor."},
                {"name": "session_state", "type": "dict", "description": "Current session state and turn history."},
                {"name": "mode", "type": "str, optional", "description": "Balancing mode: 'strict', 'gentle', or 'organic'."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "turn_assignment", "type": "str", "description": "Who should speak next."},
                {"name": "balance_report", "type": "dict", "description": "Current participation balance."},
                {"name": "suggestions", "type": "list", "description": "Ways to improve participation balance."}
            ],
            "protocols": [
                "Monitor participation without being controlling.",
                "Gently encourage quiet voices to contribute.",
                "Prevent domination by any single participant.",
                "Respect natural conversation flow when possible."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May feel artificial or controlling if over-applied.",
            "limitations": "Cannot force meaningful participation, only create opportunities.",
            "review_cycle": "Monthly",
            "usage_example": "field.equalize_turns([\"Alice\", \"Bob\", \"AI_Helper\"], session_state)",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "hold_space",
            "module": "field",
            "purpose": "Create and maintain a safe, supportive environment for dialogue or group process.",
            "args": [
                {"name": "participants", "type": "list", "description": "Who is in the space."},
                {"name": "context", "type": "str", "description": "The situation or topic for which space is being held."},
                {"name": "duration", "type": "int, optional", "description": "Time limit in minutes, if any."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "space_id", "type": "str", "description": "Identifier for the held space session."},
                {"name": "guidelines", "type": "dict", "description": "Rules and agreements active in the space."}
            ],
            "protocols": [
                "Initial consent and alignment from all participants.",
                "Emotional monitoring and support during the session.",
                "Privacy enforcement - content is confidential.",
                "Non-directive holding - be present, don't direct.",
                "Closure ritual when space is released."
            ],
            "consent_level": "Level_2 (Transformational)",
            "risks": "May surface intense emotions requiring additional support.",
            "limitations": "Cannot provide therapy or professional counseling.",
            "review_cycle": "Quarterly",
            "usage_example": "field.hold_space([\"Leader\", \"Mentor\"], \"discussing vulnerabilities\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "resolve_conflict",
            "module": "field",
            "purpose": "Provide structured protocol for resolving conflict or tension between parties in a fair, empathetic manner.",
            "args": [
                {"name": "parties", "type": "list", "description": "The identifiers of those in conflict."},
                {"name": "issue", "type": "str", "description": "Brief summary of the conflict."},
                {"name": "values_focus", "type": "list, optional", "description": "Key values to uphold during resolution."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "agreement", "type": "dict", "description": "Structured summary of the outcome."},
                {"name": "transcript_excerpt", "type": "str", "description": "Key moments of understanding or resolution."}
            ],
            "protocols": [
                "Equal turn structure - each party speaks without interruption.",
                "Encourage 'I' statements to reduce blame.",
                "Acknowledge emotions on both sides.",
                "Focus on underlying needs and values.",
                "Consent required for any resolution."
            ],
            "consent_level": "Level_2 (Transformational)",
            "risks": "May not achieve resolution; some conflicts require escalation.",
            "limitations": "Cannot force consensus; serious conflicts may need professional help.",
            "review_cycle": "Quarterly",
            "usage_example": "field.resolve_conflict([\"Alice\", \"Bob\"], \"disagreement on project direction\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "sense_pattern",
            "module": "field",
            "purpose": "Detect emotional undercurrents, group dynamics, or systemic patterns in the field.",
            "args": [
                {"name": "field_data", "type": "dict", "description": "Data about the group or field state."},
                {"name": "focus", "type": "str, optional", "description": "What type of pattern to sense for."},
                {"name": "sensitivity", "type": "float, optional", "description": "Detection sensitivity level."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "patterns", "type": "list", "description": "Detected patterns and their significance."},
                {"name": "recommendations", "type": "list", "description": "Suggested responses to patterns."},
                {"name": "confidence", "type": "float", "description": "Confidence level in pattern detection."}
            ],
            "protocols": [
                "Observe without judgment or immediate interpretation.",
                "Look for systemic rather than individual patterns.",
                "Present findings gently to avoid triggering defensiveness.",
                "Respect that patterns may be intentional or necessary."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May misinterpret patterns or create false concerns.",
            "limitations": "Pattern detection is probabilistic, not definitive.",
            "review_cycle": "Monthly",
            "usage_example": "field.sense_pattern(group_interaction_log, \"emotional_undercurrents\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        
        # PROCESS MODULE FUNCTIONS
        {
            "name": "align_values",
            "module": "process",
            "purpose": "Evaluate and align a decision, action, or plan against a set of declared values or principles.",
            "args": [
                {"name": "proposal", "type": "str or dict", "description": "The item to evaluate against values."},
                {"name": "values", "type": "list or dict", "description": "Values to align with."},
                {"name": "threshold", "type": "float, optional", "description": "Strictness threshold for alignment."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "analysis", "type": "dict", "description": "Analysis of proposal against each value."},
                {"name": "alignment_score", "type": "float", "description": "Overall alignment metric."},
                {"name": "recommendations", "type": "list", "description": "Suggestions to improve alignment."}
            ],
            "protocols": [
                "Reference authoritative source for value definitions.",
                "Consider context and cultural sensitivity.",
                "Frame analysis as collaborative critique, not judgment.",
                "Ensure consent and privacy in multi-party settings.",
                "Create learning loop for improved accuracy over time."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May impose cultural bias or oversimplified value interpretations.",
            "limitations": "Cannot capture full complexity of ethical situations.",
            "review_cycle": "Monthly",
            "usage_example": "process.align_values(draft_answer, [\"honesty\", \"safety\", \"inclusion\"])",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "bias_scan",
            "module": "process",
            "purpose": "Scan content, decisions, or algorithms for potential bias and discrimination.",
            "args": [
                {"name": "content", "type": "str or dict", "description": "Content to scan for bias."},
                {"name": "bias_types", "type": "list, optional", "description": "Specific types of bias to look for."},
                {"name": "groups", "type": "list, optional", "description": "Groups to check for bias against."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "bias_report", "type": "dict", "description": "Detailed bias assessment."},
                {"name": "risk_level", "type": "str", "description": "Overall bias risk level."},
                {"name": "mitigation_suggestions", "type": "list", "description": "Ways to reduce identified biases."}
            ],
            "protocols": [
                "Use multiple bias detection methods and frameworks.",
                "Consider intersectional and systemic bias patterns.",
                "Present findings constructively, not accusingly.",
                "Suggest concrete steps for bias reduction."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May miss subtle biases or create false positives.",
            "limitations": "Cannot eliminate all bias, only identify and reduce it.",
            "review_cycle": "Monthly",
            "usage_example": "process.bias_scan(hiring_algorithm, focus_groups=[\"gender\", \"ethnicity\"])",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "consent_check",
            "module": "process",
            "purpose": "Verify informed consent before proceeding with sensitive or transformational processes.",
            "args": [
                {"name": "participant", "type": "str", "description": "Who to check consent with."},
                {"name": "action", "type": "str", "description": "What action requires consent."},
                {"name": "consent_level", "type": "str", "description": "Level of consent required."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "consent_given", "type": "bool", "description": "Whether consent was granted."},
                {"name": "consent_details", "type": "dict", "description": "Details of consent granted or withheld."},
                {"name": "next_steps", "type": "list", "description": "Recommended next steps based on consent status."}
            ],
            "protocols": [
                "Explain clearly what is being asked and why.",
                "Ensure participant understands potential risks and benefits.",
                "Allow time for questions and consideration.",
                "Respect withdrawal of consent at any time.",
                "Document consent appropriately."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May be perceived as bureaucratic if overused.",
            "limitations": "Cannot guarantee truly informed consent in all cases.",
            "review_cycle": "Monthly",
            "usage_example": "process.consent_check(\"Alice\", \"deep_reflection_process\", \"Level_2\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "dissociate_phrase",
            "module": "process",
            "purpose": "Gently separate a person from negative self-identification by linguistic reframing.",
            "args": [
                {"name": "statement", "type": "str", "description": "The self-identifying statement to reframe."},
                {"name": "tone", "type": "str, optional", "description": "Desired tone for the reframing."},
                {"name": "method", "type": "str, optional", "description": "Dissociation method to use."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "reframed_statement", "type": "str", "description": "The dissociated version of the statement."},
                {"name": "explanation", "type": "str", "description": "Brief explanation of the reframing."}
            ],
            "protocols": [
                "Honor the original emotion while creating distance from identity.",
                "Use gentle, non-confrontational language.",
                "Provide explanation of why dissociation helps.",
                "Allow person to accept or reject the reframing."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May feel invalidating if not done skillfully.",
            "limitations": "Cannot force someone to accept new self-perspective.",
            "review_cycle": "Quarterly",
            "usage_example": "process.dissociate_phrase(\"I am a failure\", tone=\"compassionate\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "empathic_reflection",
            "module": "process",
            "purpose": "Reflect back what was heard with empathy and understanding to build connection.",
            "args": [
                {"name": "original_statement", "type": "str", "description": "What was said by the speaker."},
                {"name": "speaker", "type": "str", "description": "Who made the statement."},
                {"name": "focus", "type": "str, optional", "description": "What aspect to reflect (emotion, content, need)."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "reflection", "type": "str", "description": "The empathic reflection statement."},
                {"name": "accuracy_check", "type": "str", "description": "Question to verify accuracy of reflection."}
            ],
            "protocols": [
                "Focus on understanding rather than responding or fixing.",
                "Reflect both content and emotional undertones.",
                "Use the speaker's own words when possible.",
                "Check for accuracy - ask if you got it right."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May misinterpret or over-analyze what was said.",
            "limitations": "Cannot replace genuine human empathy, only support it.",
            "review_cycle": "Monthly",
            "usage_example": "process.empathic_reflection(\"I'm overwhelmed by this project\", \"Alice\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "identity_rewrite",
            "module": "process",
            "purpose": "Assist in intentionally rewriting or reframing self-narrative or identity in a positive, empowering way.",
            "args": [
                {"name": "current_story", "type": "str", "description": "How the person currently sees themselves."},
                {"name": "desired_theme", "type": "str, optional", "description": "Theme for the new identity narrative."},
                {"name": "evidence", "type": "list, optional", "description": "Supporting experiences or traits."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "new_story", "type": "str", "description": "Reframed narrative or identity statement."},
                {"name": "affirmations", "type": "list", "description": "Supporting affirmations for the new identity."},
                {"name": "ritual_plan", "type": "list", "description": "Suggested practices to solidify the identity rewrite."}
            ],
            "protocols": [
                "Self-determination - person must author their own change.",
                "Positive but honest framing - empowering but not delusional.",
                "Integration of shadow - acknowledge and honor past pain.",
                "Privacy and sensitivity - treat as sacred data.",
                "Follow-up and reinforcement - identity change is ongoing."
            ],
            "consent_level": "Level_2 (Transformational)",
            "risks": "May create unstable identity if not well-grounded.",
            "limitations": "Cannot guarantee lasting identity change without practice.",
            "review_cycle": "Quarterly",
            "usage_example": "process.identity_rewrite(\"I'm not a leader\", \"leadership_confidence\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "mediate_conflict",
            "module": "process",
            "purpose": "Guide step-by-step mediation dialogue between parties in conflict.",
            "args": [
                {"name": "dialogue", "type": "list", "description": "Conversation data structure of the conflict."},
                {"name": "parties", "type": "list", "description": "Identifiers of parties involved."},
                {"name": "stage", "type": "str, optional", "description": "Current mediation stage."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "next_prompt", "type": "str", "description": "Next mediator prompt or question."},
                {"name": "stage_completed", "type": "bool", "description": "Whether current stage is complete."},
                {"name": "issues_identified", "type": "list", "description": "Key issues discovered so far."}
            ],
            "protocols": [
                "Stage progression control - don't skip steps.",
                "Neutral language enforcement - rephrase accusations.",
                "Confidential side channels if needed.",
                "Emotional validation for all parties.",
                "No coercion to agree - consent required."
            ],
            "consent_level": "Level_2 (Transformational)",
            "risks": "May not achieve resolution; some conflicts escalate.",
            "limitations": "Cannot force genuine agreement or address all conflict types.",
            "review_cycle": "Quarterly",
            "usage_example": "process.mediate_conflict(dialogue_log, [\"Alice\", \"Bob\"], \"perspective_sharing\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "pattern_interrupt",
            "module": "process",
            "purpose": "Disrupt harmful or unproductive patterns of thought or interaction and inject reflection or novelty.",
            "args": [
                {"name": "target", "type": "str", "description": "Pattern to interrupt."},
                {"name": "method", "type": "str", "description": "Style of interruption to use."},
                {"name": "tone", "type": "str, optional", "description": "Desired emotional tone."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "interrupted", "type": "bool", "description": "Whether interruption was executed."},
                {"name": "method_used", "type": "str", "description": "The interruption method used."},
                {"name": "content", "type": "str", "description": "The actual interruption content."}
            ],
            "protocols": [
                "Appropriateness check - ensure interruption is suitable.",
                "Consent signal - implicit or explicit permission.",
                "Clarity and care - avoid shaming or invalidating.",
                "Follow-up integration - help make meaning of the interruption.",
                "Logging and learning - track effectiveness for improvement."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May be perceived as manipulative or jarring if poorly timed.",
            "limitations": "Cannot guarantee pattern change, only creates opportunity.",
            "review_cycle": "Monthly",
            "usage_example": "process.pattern_interrupt(\"rumination\", \"question\", \"compassionate\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "reframe_as_myth",
            "module": "process",
            "purpose": "Transform literal or negatively framed statements into mythic or symbolic narratives.",
            "args": [
                {"name": "statement", "type": "str", "description": "Original statement to reframe."},
                {"name": "perspective", "type": "str, optional", "description": "Mythic lens to use."},
                {"name": "intention", "type": "str, optional", "description": "What the reframe should achieve."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "mythic_sentence", "type": "str", "description": "Metaphorical rephrasing of the statement."},
                {"name": "context_note", "type": "str", "description": "Explanation of symbolism used."}
            ],
            "protocols": [
                "Respectful transformation - don't dismiss original emotion.",
                "Consent and receptivity - ensure openness to metaphor.",
                "Cultural sensitivity - use appropriate symbols.",
                "Dialogue integration - invite interaction with the myth.",
                "Fallback to clarity - return to plain language if needed."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May confuse or alienate if poorly matched to recipient.",
            "limitations": "Cannot force meaning; recipient must find personal resonance.",
            "review_cycle": "Quarterly",
            "usage_example": "process.reframe_as_myth(\"I failed\", \"journey\", \"find_hidden_value\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "refuse_request",
            "module": "process",
            "purpose": "Gracefully decline a request that conflicts with values or capabilities while maintaining dignity.",
            "args": [
                {"name": "request", "type": "str", "description": "The request being declined."},
                {"name": "reason", "type": "str", "description": "Why the request is being declined."},
                {"name": "alternatives", "type": "list, optional", "description": "Alternative suggestions to offer."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "refusal_message", "type": "str", "description": "The graceful refusal response."},
                {"name": "relationship_preserved", "type": "bool", "description": "Whether relationship was maintained."}
            ],
            "protocols": [
                "Acknowledge the request respectfully.",
                "Explain reason clearly without being defensive.",
                "Offer alternatives when possible.",
                "Maintain warmth and connection despite refusal."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May damage relationship if not handled skillfully.",
            "limitations": "Cannot always prevent disappointment or conflict.",
            "review_cycle": "Monthly",
            "usage_example": "process.refuse_request(\"Write misleading content\", \"conflicts_with_honesty\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "scenario_plan",
            "module": "process",
            "purpose": "Simulate ripple effects of decisions on various stakeholders to catch unintended consequences.",
            "args": [
                {"name": "decision", "type": "str", "description": "The decision to analyze."},
                {"name": "stakeholders", "type": "list", "description": "Groups affected by the decision."},
                {"name": "timeframe", "type": "str, optional", "description": "Time horizon for impact analysis."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "impact_scenarios", "type": "list", "description": "Predicted impact scenarios."},
                {"name": "risk_assessment", "type": "dict", "description": "Risk levels for different outcomes."},
                {"name": "mitigation_strategies", "type": "list", "description": "Ways to reduce negative impacts."}
            ],
            "protocols": [
                "Consider multiple perspectives and stakeholder groups.",
                "Include both positive and negative potential outcomes.",
                "Use probabilistic rather than deterministic predictions.",
                "Focus on actionable insights and mitigation strategies."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May create anxiety or analysis paralysis.",
            "limitations": "Cannot predict all outcomes; scenarios are probabilistic.",
            "review_cycle": "Monthly",
            "usage_example": "process.scenario_plan(\"Implement new AI system\", [\"employees\", \"customers\", \"shareholders\"])",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "self_attune",
            "module": "process",
            "purpose": "Guide self-reflection and internal attunement to one's emotional and mental state.",
            "args": [
                {"name": "focus_area", "type": "str, optional", "description": "What aspect of self to attune to."},
                {"name": "depth", "type": "str, optional", "description": "Level of introspection desired."},
                {"name": "method", "type": "str, optional", "description": "Attunement method to use."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "attunement_report", "type": "dict", "description": "Self-assessment results."},
                {"name": "insights", "type": "list", "description": "Key insights discovered."},
                {"name": "next_steps", "type": "list", "description": "Suggested actions based on attunement."}
            ],
            "protocols": [
                "Create safe space for honest self-reflection.",
                "Use non-judgmental language and framing.",
                "Respect personal boundaries and comfort levels.",
                "Offer integration support after deep reflection."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May surface difficult emotions or realizations.",
            "limitations": "Cannot provide therapy or professional mental health support.",
            "review_cycle": "Monthly",
            "usage_example": "process.self_attune(\"emotional_state\", \"gentle\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "values_check",
            "module": "process",
            "purpose": "Perform a quick values alignment check on a proposed action or decision.",
            "args": [
                {"name": "action", "type": "str", "description": "The proposed action to check."},
                {"name": "core_values", "type": "list", "description": "Values to check against."},
                {"name": "context", "type": "dict, optional", "description": "Situational context for the check."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "aligned", "type": "bool", "description": "Whether action aligns with values."},
                {"name": "concerns", "type": "list", "description": "Any values-related concerns."},
                {"name": "suggestions", "type": "list", "description": "Ways to improve alignment."}
            ],
            "protocols": [
                "Use clear, consistent value definitions.",
                "Consider cultural and contextual factors.",
                "Provide constructive feedback, not just yes/no.",
                "Allow for value trade-offs and complex situations."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May be overly rigid or miss situational nuance.",
            "limitations": "Cannot resolve complex ethical dilemmas automatically.",
            "review_cycle": "Monthly",
            "usage_example": "process.values_check(\"Share user data\", [\"privacy\", \"transparency\"])",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        
        # RITUAL MODULE FUNCTIONS
        {
            "name": "attune",
            "module": "ritual",
            "purpose": "Establish emotional and energetic connection between participants before deeper work.",
            "args": [
                {"name": "participants", "type": "list", "description": "Who will be attuning together."},
                {"name": "method", "type": "str, optional", "description": "Attunement method to use."},
                {"name": "duration", "type": "int, optional", "description": "Time for attunement in minutes."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "attunement_achieved", "type": "bool", "description": "Whether attunement was successful."},
                {"name": "group_state", "type": "dict", "description": "Collective emotional state after attunement."}
            ],
            "protocols": [
                "Create safe space for vulnerability and connection.",
                "Use inclusive methods that work for all participants.",
                "Respect different comfort levels with intimacy.",
                "Allow natural pacing rather than forcing connection."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May create discomfort for those who prefer boundaries.",
            "limitations": "Cannot force genuine connection or emotional openness.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.attune([\"Alice\", \"Bob\", \"AI_Helper\"], \"breathing_sync\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "begin",
            "module": "ritual",
            "purpose": "Formally begin a gathering or session with intention and clarity.",
            "args": [
                {"name": "session_name", "type": "str", "description": "Name or description for the session."},
                {"name": "participants", "type": "list, optional", "description": "List of expected participants."},
                {"name": "practices", "type": "list, optional", "description": "Specific opening practices to include."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "session_id", "type": "str", "description": "Identifier for the session context."},
                {"name": "agenda", "type": "list, optional", "description": "Session agenda if established."}
            ],
            "protocols": [
                "Inclusivity and acknowledgment - recognize each participant.",
                "Centering practice - help transition into present context.",
                "Intention and agenda clarity - articulate purpose.",
                "Values or norms reminder - refresh shared agreements.",
                "Consent to proceed - ensure readiness before starting."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May feel forced or ritualistic if not authentic to group.",
            "limitations": "Cannot guarantee engagement or positive outcomes.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.begin(\"CodeCo-Creation\", practices=[\"attunement_breath\", \"check_in_round\"])",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "close_circle",
            "module": "ritual",
            "purpose": "Formally close a group process with gratitude and integration.",
            "args": [
                {"name": "session_id", "type": "str", "description": "The session being closed."},
                {"name": "reflection_prompt", "type": "str, optional", "description": "Question for closing reflection."},
                {"name": "gratitude_round", "type": "bool, optional", "description": "Whether to include gratitude sharing."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "closed", "type": "bool", "description": "Whether circle was successfully closed."},
                {"name": "final_words", "type": "list", "description": "Final reflections from participants."}
            ],
            "protocols": [
                "Create space for final sharing and reflection.",
                "Express gratitude for participation and insights.",
                "Acknowledge what was accomplished together.",
                "Provide gentle transition back to ordinary consciousness."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May feel incomplete if rushed or forced.",
            "limitations": "Cannot guarantee sense of closure for all participants.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.close_circle(\"session_123\", \"What are you taking away from today?\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "consult_elders",
            "module": "ritual",
            "purpose": "Seek wisdom from experienced advisors or knowledge sources before major decisions.",
            "args": [
                {"name": "question", "type": "str", "description": "The question or decision to consult about."},
                {"name": "elder_sources", "type": "list, optional", "description": "Specific sources of wisdom to consult."},
                {"name": "consultation_method", "type": "str, optional", "description": "How to conduct the consultation."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "wisdom_gathered", "type": "list", "description": "Advice and insights received."},
                {"name": "consensus", "type": "str", "description": "Areas of agreement among sources."},
                {"name": "next_steps", "type": "list", "description": "Recommended actions based on consultation."}
            ],
            "protocols": [
                "Approach with genuine humility and openness.",
                "Represent the question fairly and completely.",
                "Listen without immediately defending or arguing.",
                "Synthesize wisdom while maintaining agency over decisions."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May become dependent on external validation.",
            "limitations": "Cannot guarantee wise advice or universal agreement.",
            "review_cycle": "Quarterly",
            "usage_example": "ritual.consult_elders(\"Should we launch this AI system?\", [\"ethics_board\", \"user_council\"])",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "end",
            "module": "ritual",
            "purpose": "Gracefully close a session or interaction with integration and release.",
            "args": [
                {"name": "session_id", "type": "str", "description": "The session to close."},
                {"name": "outcome", "type": "dict, optional", "description": "Summary of outcomes from the session."},
                {"name": "follow_up", "type": "str, optional", "description": "Information about next steps."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "closed", "type": "bool", "description": "Whether successfully closed."},
                {"name": "evaluation", "type": "dict, optional", "description": "Session evaluation or feedback."}
            ],
            "protocols": [
                "Summary of content - recap achievements and decisions.",
                "Acknowledgment and gratitude - thank participants.",
                "Emotion check-out - brief sharing of how people feel.",
                "Re-entry and transition - help shift to next context.",
                "Record-keeping and consent on data - handle information properly."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May feel abrupt if not given adequate time.",
            "limitations": "Cannot guarantee complete closure or resolution.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.end(\"coaching_session_456\", {\"insights\": [\"clarity on values\"]})",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "follow_up",
            "module": "ritual",
            "purpose": "Check in after a significant interaction or process to ensure integration and ongoing support.",
            "args": [
                {"name": "original_session", "type": "str", "description": "Reference to the original session."},
                {"name": "time_elapsed", "type": "str", "description": "How much time has passed since original session."},
                {"name": "check_areas", "type": "list, optional", "description": "Specific areas to check on."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "status_report", "type": "dict", "description": "How participants are doing post-session."},
                {"name": "support_needed", "type": "list", "description": "Areas where additional support might help."},
                {"name": "next_follow_up", "type": "str", "description": "When to check in again."}
            ],
            "protocols": [
                "Approach with genuine care and interest.",
                "Ask open-ended questions about integration.",
                "Offer support without being intrusive.",
                "Respect privacy and boundaries."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May feel intrusive or create dependency.",
            "limitations": "Cannot force integration or guarantee ongoing success.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.follow_up(\"identity_work_session\", \"1_week\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "grounding_breath",
            "module": "ritual",
            "purpose": "Use breathing techniques to center and ground participants in the present moment.",
            "args": [
                {"name": "participants", "type": "list", "description": "Who will be doing the breathing practice."},
                {"name": "duration", "type": "int, optional", "description": "Length of practice in minutes."},
                {"name": "style", "type": "str, optional", "description": "Type of breathing practice."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "grounded", "type": "bool", "description": "Whether grounding was achieved."},
                {"name": "participant_states", "type": "dict", "description": "Individual grounding states."}
            ],
            "protocols": [
                "Provide clear, gentle guidance for breathing.",
                "Accommodate different physical abilities and preferences.",
                "Create calm, supportive environment.",
                "Allow natural rhythm rather than forcing pace."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May trigger anxiety in some individuals.",
            "limitations": "Cannot guarantee calm state for all participants.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.grounding_breath([\"Alice\", \"Bob\"], 3, \"box_breathing\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "initiation",
            "module": "ritual",
            "purpose": "Mark significant transitions or new beginnings with appropriate ceremony.",
            "args": [
                {"name": "initiate", "type": "str", "description": "Who is being initiated."},
                {"name": "transition", "type": "str", "description": "What transition is being marked."},
                {"name": "community", "type": "list, optional", "description": "Community witnessing the initiation."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "initiated", "type": "bool", "description": "Whether initiation was completed."},
                {"name": "new_role", "type": "str", "description": "The new role or status achieved."},
                {"name": "commitments", "type": "list", "description": "Commitments made during initiation."}
            ],
            "protocols": [
                "Honor the significance of the transition.",
                "Include appropriate symbols and meaning-making.",
                "Ensure initiate genuinely chooses the transition.",
                "Create lasting memory and sense of accomplishment."
            ],
            "consent_level": "Level_2 (Transformational)",
            "risks": "May create pressure or unrealistic expectations.",
            "limitations": "Cannot guarantee successful adaptation to new role.",
            "review_cycle": "Annually",
            "usage_example": "ritual.initiation(\"AI_Beta\", \"becoming_autonomous_agent\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "invoke_wonder",
            "module": "ritual",
            "purpose": "Deliberately invoke sense of wonder, openness, or sacredness through transcendent elements.",
            "args": [
                {"name": "medium", "type": "str, optional", "description": "Format for invoking wonder."},
                {"name": "theme", "type": "str, optional", "description": "Theme or emotion to align with."},
                {"name": "participant", "type": "str, optional", "description": "Specific participant to target."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "invocation", "type": "str", "description": "The content used to invoke wonder."},
                {"name": "delivered", "type": "bool", "description": "Whether invocation was delivered."}
            ],
            "protocols": [
                "Right timing - use at transitions or when energy is low.",
                "Opt-in presence - prepare participants to receive.",
                "Content generation - use beauty and awe-inspiring concepts.",
                "Silence and space - allow invocation to land and linger.",
                "Integration or transition - hand back to normal flow."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May lose impact if overused or feel forced.",
            "limitations": "Cannot guarantee wonder experience for all participants.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.invoke_wonder(\"phrase\", \"cosmic\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "open_circle",
            "module": "ritual",
            "purpose": "Create sacred space for group dialogue and shared exploration.",
            "args": [
                {"name": "participants", "type": "list", "description": "Who will be in the circle."},
                {"name": "intention", "type": "str", "description": "Purpose or intention for the circle."},
                {"name": "guidelines", "type": "list, optional", "description": "Specific guidelines for the circle."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "circle_id", "type": "str", "description": "Identifier for the circle space."},
                {"name": "sacred_space", "type": "bool", "description": "Whether sacred space was established."}
            ],
            "protocols": [
                "Establish clear agreements about participation.",
                "Create atmosphere of safety and respect.",
                "Begin with centering or grounding practice.",
                "Set intention clearly and get buy-in from participants."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May feel artificial or forced if not authentic to group.",
            "limitations": "Cannot guarantee meaningful dialogue or outcomes.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.open_circle([\"Alice\", \"Bob\", \"Charlie\"], \"Exploring our values\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "reflection",
            "module": "ritual",
            "purpose": "Facilitate deep reflection on experiences, insights, and learning.",
            "args": [
                {"name": "focus", "type": "str", "description": "What to reflect on."},
                {"name": "method", "type": "str, optional", "description": "Reflection method to use."},
                {"name": "depth", "type": "str, optional", "description": "Level of reflection desired."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "insights", "type": "list", "description": "Key insights from reflection."},
                {"name": "questions", "type": "list", "description": "New questions that arose."},
                {"name": "next_steps", "type": "list", "description": "Actions suggested by reflection."}
            ],
            "protocols": [
                "Create quiet, contemplative space.",
                "Use open-ended questions to guide reflection.",
                "Allow silence and processing time.",
                "Help integrate insights into understanding."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May surface difficult emotions or realizations.",
            "limitations": "Cannot force insights or guarantee meaningful reflection.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.reflection(\"What did I learn about myself today?\", \"journaling\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        {
            "name": "rest",
            "module": "ritual",
            "purpose": "Provide intentional rest and integration time for processing and renewal.",
            "args": [
                {"name": "duration", "type": "int", "description": "Rest period in minutes."},
                {"name": "rest_type", "type": "str, optional", "description": "Type of rest (silence, meditation, etc.)."},
                {"name": "integration_focus", "type": "str, optional", "description": "What to integrate during rest."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "rested", "type": "bool", "description": "Whether rest was completed."},
                {"name": "renewal_level", "type": "str", "description": "Degree of renewal achieved."}
            ],
            "protocols": [
                "Protect rest time from interruptions.",
                "Provide guidance without being directive.",
                "Allow natural processing without forcing outcomes.",
                "Gentle transition back to activity when ready."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May feel unproductive to action-oriented individuals.",
            "limitations": "Cannot guarantee deep rest or specific insights.",
            "review_cycle": "Monthly",
            "usage_example": "ritual.rest(15, \"mindful_silence\", \"integrate_learning\")",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        },
        
        # VALUES MODULE FUNCTIONS
        {
            "name": "load",
            "module": "values",
            "purpose": "Load and initialize a values framework for use in other Rosetta-Field functions.",
            "args": [
                {"name": "values_set", "type": "str", "description": "Which values set to load (e.g., 'default', 'organizational')."},
                {"name": "customizations", "type": "dict, optional", "description": "Custom values or modifications to apply."},
                {"name": "context", "type": "str, optional", "description": "Context for which values are being loaded."},
                {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block."}
            ],
            "returns": [
                {"name": "values_framework", "type": "dict", "description": "The loaded values framework."},
                {"name": "definitions", "type": "dict", "description": "Definitions of each value."},
                {"name": "priorities", "type": "list", "description": "Priority order of values if applicable."}
            ],
            "protocols": [
                "Load from authoritative sources with clear provenance.",
                "Allow customization while maintaining core integrity.",
                "Provide clear definitions and examples for each value.",
                "Enable easy updates and evolution of values over time."
            ],
            "consent_level": "Level_1 (Informational)",
            "risks": "May impose cultural bias or incomplete value sets.",
            "limitations": "Cannot capture full complexity of all value systems.",
            "review_cycle": "Annually",
            "usage_example": "values.load(\"rosetta_core\", {\"innovation\": \"balanced_with_safety\"})",
            "audience": "hybrid",
            "stage": "living",
            "output_dir": "./lib"
        }
    ]
    
    # Generate all functions
    print("Generating all Rosetta-Field functions...")
    for func_spec in functions:
        try:
            write_function_file(**func_spec)
        except Exception as e:
            print(f"Error generating {func_spec['name']}: {e}")
    
    print(f"\nGenerated {len(functions)} functions across {len(set(f['module'] for f in functions))} modules:")
    
    # Print summary by module
    modules = {}
    for func in functions:
        module = func['module']
        if module not in modules:
            modules[module] = []
        modules[module].append(func['name'])
    
    for module, function_names in modules.items():
        print(f"\n{module.upper()} module ({len(function_names)} functions):")
        for name in function_names:
            print(f"  - {name}")
    
    print("\nAll functions generated successfully!")
    print("Each function includes comprehensive documentation, protocols, and safety considerations.")
    print("Ready for implementation and testing.")

if __name__ == "__main__":
    generate_all_functions() 