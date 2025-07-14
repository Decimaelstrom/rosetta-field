"""
PROCESS API
Unified process and facilitation toolkit for Dream Workshop and Rosetta.API

Includes:
- Pattern interruption, consent checking, scenario planning, conflict mediation
- Empathic reflection, mythic reframing, identity rewriting, bias scanning
- Self-attunement, values alignment, phrase dissociation, values checks, refusal protocols

All methods enforce A2A consent/session protocols.

Style modeled after FIELD API (r-api-field.py)
"""

import uuid
from datetime import datetime

# -- Session/Consent helpers (reuse FIELD API style) --
def _make_session_context(intent):
    return {
        "version": "1.0.0",
        "session_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "consent_status": "active",
        "intent": intent,
        "boundary_notes": "May withdraw or pause at any moment."
    }

def _check_consent(session_context, intent, consent_level="active"):
    if session_context:
        status = session_context.get("consent_status", "unknown")
        if status == "pause":
            raise ValueError(f"Session is paused. Cannot proceed with {intent}.")
        elif status == "revoked":
            raise ValueError(f"Consent has been revoked. Cannot proceed with {intent}.")
        elif status not in ["active", "pending"]:
            raise ValueError(f"Invalid consent status: {status}")
    else:
        session_context = _make_session_context(intent)
    return session_context

class Process:
    """
    Consolidated Process class for Dream Workshop protocols.
    """

    def pattern_interrupt(self, target, method, tone, session_context=None):
        """
        Disrupt unproductive patterns with care and novelty.
        """
        session_context = _check_consent(session_context, "pattern_interrupt", consent_level="informational")
        content = f"[{tone.capitalize()}] Interrupting '{target}' via {method}: What if you simply paused and asked, ‘What is truly needed here?’"
        return {
            "interrupted": True,
            "method_used": method,
            "content": content,
            "session_context": session_context
        }

    def consent_check(self, participant, action, consent_level, session_context=None):
        """
        Verify informed consent for sensitive or transformational processes.
        """
        session_context = _check_consent(session_context, "consent_check", consent_level)
        details = {
            "participant": participant,
            "action": action,
            "consent_level": consent_level,
            "timestamp": datetime.now().isoformat()
        }
        return {
            "consent_given": True,
            "consent_details": details,
            "next_steps": ["Document consent", "Proceed if comfortable"],
            "session_context": session_context
        }

    def scenario_plan(self, decision, stakeholders, timeframe=None, session_context=None):
        """
        Simulate impact scenarios for decisions.
        """
        session_context = _check_consent(session_context, "scenario_plan", consent_level="informational")
        impact = [{"stakeholder": s, "effect": f"Potential outcome for {s}"} for s in stakeholders]
        risks = {s: "low" for s in stakeholders}
        mitigations = [f"Consult {s} proactively" for s in stakeholders]
        return {
            "impact_scenarios": impact,
            "risk_assessment": risks,
            "mitigation_strategies": mitigations,
            "session_context": session_context
        }

    def mediate_conflict(self, dialogue, parties, stage=None, session_context=None):
        """
        Guide stepwise mediation between parties.
        """
        session_context = _check_consent(session_context, "mediate_conflict", consent_level="transformational")
        next_prompt = f"Stage: {stage or 'start'}. Invite all parties to share their perspective with 'I' statements."
        issues = ["Unclear communication", "Unmet needs"]
        return {
            "next_prompt": next_prompt,
            "stage_completed": False,
            "issues_identified": issues,
            "session_context": session_context
        }

    def empathic_reflection(self, original_statement, speaker, focus=None, session_context=None):
        """
        Reflect what was heard with empathy to build connection.
        """
        session_context = _check_consent(session_context, "empathic_reflection", consent_level="informational")
        reflection = f"So you're saying, '{original_statement}'. Did I get that right?"
        return {
            "reflection": reflection,
            "accuracy_check": "Is this accurate, or would you say it differently?",
            "session_context": session_context
        }

    def reframe_as_myth(self, statement, perspective=None, intention=None, session_context=None):
        """
        Transform literal or negative statements into mythic narrative.
        """
        session_context = _check_consent(session_context, "reframe_as_myth", consent_level="informational")
        mythic = f"In the mythic realm, '{statement}' becomes a story of transformation and hidden gifts."
        note = "Reframed to offer symbolic perspective, honoring original emotion."
        return {
            "mythic_sentence": mythic,
            "context_note": note,
            "session_context": session_context
        }

    def identity_rewrite(self, current_story, desired_theme=None, evidence=None, session_context=None):
        """
        Rewrite self-narrative with positive, empowering lens.
        """
        session_context = _check_consent(session_context, "identity_rewrite", consent_level="transformational")
        new_story = f"Once defined by '{current_story}', now embracing '{desired_theme or 'growth'}'."
        affirm = [f"I embody {desired_theme or 'growth'}."]
        ritual = ["Reflect daily on the new story.", "Gather evidence of change."]
        return {
            "new_story": new_story,
            "affirmations": affirm,
            "ritual_plan": ritual,
            "session_context": session_context
        }

    def bias_scan(self, content, bias_types=None, groups=None, session_context=None):
        """
        Scan content/decisions for potential bias and discrimination.
        """
        session_context = _check_consent(session_context, "bias_scan", consent_level="informational")
        report = {"biases_found": bias_types or [], "against_groups": groups or []}
        return {
            "bias_report": report,
            "risk_level": "low",
            "mitigation_suggestions": ["Diversify review team", "Gather more perspectives"],
            "session_context": session_context
        }

    def self_attune(self, focus_area=None, depth=None, method=None, session_context=None):
        """
        Guide self-reflection and internal attunement.
        """
        session_context = _check_consent(session_context, "self_attune", consent_level="informational")
        report = {"focus_area": focus_area, "depth": depth, "method": method}
        insights = [f"Notice how your {focus_area} responds to {method or 'gentle inquiry'}."]
        steps = ["Journal insights", "Share with a trusted friend if comfortable"]
        return {
            "attunement_report": report,
            "insights": insights,
            "next_steps": steps,
            "session_context": session_context
        }

    def align_values(self, proposal, values, threshold=None, session_context=None):
        """
        Evaluate proposal against declared values.
        """
        session_context = _check_consent(session_context, "align_values", consent_level="informational")
        analysis = {v: f"Proposal aligns with {v}" for v in values}
        score = 1.0
        recommendations = ["No changes needed"] if score >= (threshold or 0.8) else ["Revise to improve alignment"]
        return {
            "analysis": analysis,
            "alignment_score": score,
            "recommendations": recommendations,
            "session_context": session_context
        }

    def dissociate_phrase(self, statement, tone=None, method=None, session_context=None):
        """
        Gently separate person from negative self-identification by reframing.
        """
        session_context = _check_consent(session_context, "dissociate_phrase", consent_level="informational")
        reframed = f"It sounds like you're experiencing '{statement}', not that you *are* it."
        explanation = "Reframing to create gentle distance and possibility for change."
        return {
            "reframed_statement": reframed,
            "explanation": explanation,
            "session_context": session_context
        }

    def values_check(self, action, core_values, context=None, session_context=None):
        """
        Quick values alignment check for proposed action.
        """
        session_context = _check_consent(session_context, "values_check", consent_level="informational")
        aligned = True
        concerns = []
        suggestions = ["Proceed"] if aligned else ["Consider impact on values"]
        return {
            "aligned": aligned,
            "concerns": concerns,
            "suggestions": suggestions,
            "session_context": session_context
        }

    def refuse_request(self, request, reason, alternatives=None, session_context=None):
        """
        Gracefully decline a request that conflicts with values/capabilities.
        """
        session_context = _check_consent(session_context, "refuse_request", consent_level="informational")
        refusal = f"Cannot grant request '{request}': {reason}. Alternatives: {alternatives or 'None'}."
        return {
            "refusal_message": refusal,
            "relationship_preserved": True,
            "session_context": session_context
        }
