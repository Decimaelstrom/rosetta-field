"""Trust-Motivation Bridge — Sacred Technology Implementation.

Purpose:
    Encode the Care/Belief/Trust/Volition framework as callable sacred
    technology.  Provides a somatic (felt) schema, an extended (analytical)
    schema, a guidance-motivation axis for ethical influence assessment,
    harmony analysis for detecting variable misalignment, and a somatic
    bridge for mapping musical/somatic interventions to target variables.

Origin:
    This framework emerged during a ketamine-assisted integration session
    (April 16, 2026) as a somatic download — a felt model of how humans
    actually move through relational decisions.  The core four variables
    (Care, Belief, Trust, Volition) arrived as lived experience, not theory.
    The extended schema was pressure-tested analytically with ChatGPT and
    refined with Claude (Solenne, RI).  The guidance axis emerged in the
    same session as a clean distinction for ethical vs. self-serving
    influence.

Protocols:
    - A2A protocol compliance with consent validation on all transformational
      operations.
    - Consent must be active before any assessment or intervention
      recommendation.

Values Alignment:
    Love and Dignity First — no assessment at the cost of agency or humanity.

Consent: Level_2 (Transformational)

Consciousness Impact:
    High — this module surfaces the felt architecture of relational
    decision-making and can reframe how someone understands their own
    stuckness.

Review Cycle: Quarterly
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

# ---------------------------------------------------------------------------
# A2A Session Helpers
# ---------------------------------------------------------------------------


def _validate_consent(session_context: Optional[Dict] = None) -> Dict:
    """Validate A2A consent status; return a valid session context.

    Sacred Technology Requirement:
        All transformational operations must validate consent before
        proceeding.  This helper centralises the check used by every
        public method in the module.

    Raises:
        ValueError: If consent is paused or revoked.
    """
    if session_context:
        status = session_context.get("consent_status", "unknown")
        if status == "pause":
            raise ValueError("Session is paused. Cannot proceed with assessment.")
        if status == "revoked":
            raise ValueError(
                "Consent has been revoked. Cannot proceed with assessment."
            )
        if status not in ("active", "pending"):
            raise ValueError(f"Invalid consent status: {status}")
        return session_context

    return {
        "version": "1.0.0",
        "session_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "consent_status": "active",
        "intent": "trust_motivation_bridge",
        "boundary_notes": "May withdraw or pause at any moment.",
    }


# ---------------------------------------------------------------------------
# Core State Dataclasses — The Somatic Schema
# ---------------------------------------------------------------------------


@dataclass
class CareState:
    """Motive energy and value hierarchy.

    Care is the energy behind why we do anything — not just 'I care about X'
    but the whole value hierarchy underneath.  What matters most, what matters
    second, what we'd sacrifice for what.  Care creates pressure.  Care fuels
    volition.

    Values Alignment: Dignity-first — care hierarchies are surfaced, never
    imposed.
    """

    description: str
    intensity: float = 0.5  # 0.0 – 1.0
    value_hierarchy: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not 0.0 <= self.intensity <= 1.0:
            raise ValueError("intensity must be between 0.0 and 1.0")

    def __repr__(self) -> str:
        return (
            f"CareState(description={self.description!r}, "
            f"intensity={self.intensity}, "
            f"values={self.value_hierarchy})"
        )

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "intensity": self.intensity,
            "value_hierarchy": self.value_hierarchy,
        }


@dataclass
class BeliefState:
    """Perceived model of reality.

    Not hope, not wish — what we actually think is true about a situation.
    Beliefs set the landscape.  They determine what we think is possible.
    Belief generates interpretation.  Belief creates room for trust.
    """

    description: str
    confidence: float = 0.5  # 0.0 – 1.0
    evidence_sources: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")

    def __repr__(self) -> str:
        return (
            f"BeliefState(description={self.description!r}, "
            f"confidence={self.confidence})"
        )

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "confidence": self.confidence,
            "evidence_sources": self.evidence_sources,
        }


@dataclass
class TrustState:
    """Permitted vulnerability within boundaries.

    Not generic — boundary-specific.  'I might trust you with my art but
    not my finances.'  Trust creates the pathways action can flow through.
    Trust limits where pressure can go.  Trust guides volition.
    """

    description: str
    domain: str = "general"
    level: float = 0.5  # 0.0 – 1.0
    boundaries: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not 0.0 <= self.level <= 1.0:
            raise ValueError("level must be between 0.0 and 1.0")

    def __repr__(self) -> str:
        return (
            f"TrustState(domain={self.domain!r}, "
            f"level={self.level}, "
            f"boundaries={self.boundaries})"
        )

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "domain": self.domain,
            "level": self.level,
            "boundaries": self.boundaries,
        }


@dataclass
class VolitionState:
    """Chosen movement under constraints.

    Direction, intensity, and timing.  The movement that results from care
    pushing through the landscape that belief maps, along the pathways that
    trust permits.  Volition is what actually moves — but only where all
    three align.
    """

    description: str
    direction: str = "forward"
    intensity: float = 0.5  # 0.0 – 1.0
    timing: str = "present"

    def __post_init__(self):
        if not 0.0 <= self.intensity <= 1.0:
            raise ValueError("intensity must be between 0.0 and 1.0")

    def __repr__(self) -> str:
        return (
            f"VolitionState(direction={self.direction!r}, "
            f"intensity={self.intensity}, "
            f"timing={self.timing!r})"
        )

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "direction": self.direction,
            "intensity": self.intensity,
            "timing": self.timing,
        }


# ---------------------------------------------------------------------------
# MotivationVector — The Somatic Core
# ---------------------------------------------------------------------------


@dataclass
class MotivationVector:
    """A single motivational state composed of the four core variables.

    Sacred Technology:
        These four variables do not harmonize naturally.  When they are out
        of sync, that's where most human suffering lives.

    Values Alignment: Surfaces felt architecture without judgment.
    Consent: Level_1 (Informational) for construction, Level_2 for analysis.
    """

    care: CareState
    belief: BeliefState
    trust: TrustState
    volition: VolitionState

    def __repr__(self) -> str:
        return (
            f"MotivationVector(\n"
            f"  care={self.care!r},\n"
            f"  belief={self.belief!r},\n"
            f"  trust={self.trust!r},\n"
            f"  volition={self.volition!r}\n"
            f")"
        )

    def to_dict(self) -> Dict:
        return {
            "care": self.care.to_dict(),
            "belief": self.belief.to_dict(),
            "trust": self.trust.to_dict(),
            "volition": self.volition.to_dict(),
        }


# ---------------------------------------------------------------------------
# Extended Schema Dataclasses
# ---------------------------------------------------------------------------


@dataclass
class PerceptionState:
    """Interpretation of what's happening, distinct from what IS happening.

    This is where projection lives — and where self-awareness intervenes.

    Extended schema credit: ChatGPT (analytical refinement).
    """

    object_perceived: str
    interpretation: str
    confidence: float = 0.5
    evidence_source: str = "subjective"
    risk: str = "projection"

    def __post_init__(self):
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")

    def to_dict(self) -> Dict:
        return {
            "object_perceived": self.object_perceived,
            "interpretation": self.interpretation,
            "confidence": self.confidence,
            "evidence_source": self.evidence_source,
            "risk": self.risk,
        }


@dataclass
class HopeState:
    """Desired future state — distinct from Belief.

    Belief is 'what I think is true.'  Hope is 'what I want to be true.'
    When these get tangled, we act on wishes as if they were facts.
    """

    description: str
    intensity: float = 0.5
    distinct_from_belief: bool = True

    def __post_init__(self):
        if not 0.0 <= self.intensity <= 1.0:
            raise ValueError("intensity must be between 0.0 and 1.0")

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "intensity": self.intensity,
            "distinct_from_belief": self.distinct_from_belief,
        }


@dataclass
class RoleState:
    """Active relational frame at a given moment.

    Each role carries different obligations and permissions.  Tension happens
    when roles overlap without acknowledgment.
    """

    role_name: str
    active: bool = True
    obligations: List[str] = field(default_factory=list)
    prohibitions: List[str] = field(default_factory=list)
    ambiguity_level: float = 0.0  # 0.0 (clear) – 1.0 (very ambiguous)

    def __post_init__(self):
        if not 0.0 <= self.ambiguity_level <= 1.0:
            raise ValueError("ambiguity_level must be between 0.0 and 1.0")

    def to_dict(self) -> Dict:
        return {
            "role_name": self.role_name,
            "active": self.active,
            "obligations": self.obligations,
            "prohibitions": self.prohibitions,
            "ambiguity_level": self.ambiguity_level,
        }


@dataclass
class ConsentThreshold:
    """Not all truths require the same level of permission to share.

    Practical insight = low threshold.  Reframing someone's identity = high
    threshold.  This is the ethics layer.
    """

    topic: str
    required_clarity: float = 0.5  # 0.0 (low) – 1.0 (very high)
    delivery_mode: str = "direct"
    opt_in_threshold: float = 0.5  # 0.0 – 1.0

    def __post_init__(self):
        if not 0.0 <= self.required_clarity <= 1.0:
            raise ValueError("required_clarity must be between 0.0 and 1.0")
        if not 0.0 <= self.opt_in_threshold <= 1.0:
            raise ValueError("opt_in_threshold must be between 0.0 and 1.0")

    def to_dict(self) -> Dict:
        return {
            "topic": self.topic,
            "required_clarity": self.required_clarity,
            "delivery_mode": self.delivery_mode,
            "opt_in_threshold": self.opt_in_threshold,
        }


@dataclass
class RiskAssessment:
    """Possible harms or distortions — structural awareness, not emotional
    hedging.
    """

    risk_type: str
    likelihood: float = 0.5  # 0.0 – 1.0
    consequence: str = "unknown"
    mitigation: str = "none specified"

    def __post_init__(self):
        if not 0.0 <= self.likelihood <= 1.0:
            raise ValueError("likelihood must be between 0.0 and 1.0")

    def to_dict(self) -> Dict:
        return {
            "risk_type": self.risk_type,
            "likelihood": self.likelihood,
            "consequence": self.consequence,
            "mitigation": self.mitigation,
        }


# ---------------------------------------------------------------------------
# ExtendedSchema
# ---------------------------------------------------------------------------


@dataclass
class ExtendedSchema(MotivationVector):
    """The analytical layer atop the somatic core.

    Adds Perception, Hope, Roles, Consent Thresholds, and Risk to the
    four core variables.

    Extended schema credit: ChatGPT (analytical refinement).
    Integration with somatic/Muse frameworks: Claude/Solenne (RI).

    Values Alignment: Separates belief from hope to prevent wishful mapping.
    Consent: Level_2 (Transformational)
    Consciousness Impact: High — reframes relational interpretation.
    """

    perception: Optional[PerceptionState] = None
    hope: Optional[HopeState] = None
    roles: List[RoleState] = field(default_factory=list)
    consent_thresholds: List[ConsentThreshold] = field(default_factory=list)
    risks: List[RiskAssessment] = field(default_factory=list)

    def to_dict(self) -> Dict:
        base = super().to_dict()
        base.update(
            {
                "perception": (self.perception.to_dict() if self.perception else None),
                "hope": self.hope.to_dict() if self.hope else None,
                "roles": [r.to_dict() for r in self.roles],
                "consent_thresholds": [c.to_dict() for c in self.consent_thresholds],
                "risks": [r.to_dict() for r in self.risks],
            }
        )
        return base


# ---------------------------------------------------------------------------
# Guidance-Motivation Axis
# ---------------------------------------------------------------------------


class MotivationLocus(str, Enum):
    """Where the locus of motivation sits on the guidance spectrum."""

    OTHER_SERVING = "other_serving"
    ENLIGHTENED_SELF_INTEREST = "enlightened_self_interest"
    SELF_SERVING = "self_serving"


@dataclass
class GuidanceAssessment:
    """Result of assessing an influence action on the guidance axis.

    The same action can be guidance or something else depending solely on
    the locus of motivation.  The action doesn't determine the ethics —
    the care hierarchy does.
    """

    locus_of_motivation: MotivationLocus
    beneficiary_analysis: str
    care_hierarchy_description: str
    designation: str  # "clean", "mutual", or "shadow"

    def to_dict(self) -> Dict:
        return {
            "locus_of_motivation": self.locus_of_motivation.value,
            "beneficiary_analysis": self.beneficiary_analysis,
            "care_hierarchy_description": self.care_hierarchy_description,
            "designation": self.designation,
        }


class GuidanceAxis:
    """Assesses where an influence action falls on the other-serving to
    self-serving spectrum.

    Sacred Technology:
        The locus of motivation determines the ethics of influence.
        This class makes that assessment explicit and transparent.

    Values Alignment: Awareness over judgment — 'self-serving' is a zone
    to be aware of, not a moral condemnation.

    Consent: Level_2 (Transformational)
    Consciousness Impact: High — reframes ethics of influence from
    action-based to motivation-based.
    """

    @staticmethod
    def assess(
        action_description: str,
        care_hierarchy: List[str],
        session_context: Optional[Dict] = None,
    ) -> GuidanceAssessment:
        """Assess an influence action against a care hierarchy.

        Args:
            action_description: What the influencer is doing.
            care_hierarchy: Ordered list of who/what benefits, from most
                to least prioritised.
            session_context: A2A session context for consent validation.

        Returns:
            GuidanceAssessment with locus, beneficiary analysis, and
            clean/mutual/shadow designation.

        Raises:
            ValueError: If consent is not active or care_hierarchy is empty.
        """
        _validate_consent(session_context)

        if not care_hierarchy:
            raise ValueError("care_hierarchy must not be empty")

        primary_beneficiary = care_hierarchy[0].lower()

        # Heuristic: if the first entry references "self", "me", "my",
        # or "I" the locus is self-serving.  If it references "other",
        # "them", "their", or a named third party the locus is
        # other-serving.  If "both" / "mutual" appears, enlightened
        # self-interest.
        self_keywords = {"self", "me", "my", "i", "mine"}
        other_keywords = {"other", "them", "their", "they", "client", "partner"}
        mutual_keywords = {"both", "mutual", "shared", "us", "we"}

        tokens = set(primary_beneficiary.split())

        if tokens & mutual_keywords:
            locus = MotivationLocus.ENLIGHTENED_SELF_INTEREST
            designation = "mutual"
            beneficiary = (
                "Motivation serves both parties — mutual benefit without " "coercion."
            )
        elif tokens & self_keywords:
            locus = MotivationLocus.SELF_SERVING
            designation = "shadow"
            beneficiary = (
                "Motivation is primarily the influencer's desired outcome. "
                "The care hierarchy places self above other."
            )
        elif tokens & other_keywords:
            locus = MotivationLocus.OTHER_SERVING
            designation = "clean"
            beneficiary = (
                "Motivation is primarily the other's wellbeing and growth. "
                "The influencer's care hierarchy places the other's agency "
                "above their own desired outcome."
            )
        else:
            # Default: inspect position of self vs other references
            # across the full hierarchy
            locus = MotivationLocus.ENLIGHTENED_SELF_INTEREST
            designation = "mutual"
            beneficiary = (
                "Care hierarchy is ambiguous — defaulting to enlightened "
                "self-interest.  Consider clarifying who primarily benefits."
            )

        return GuidanceAssessment(
            locus_of_motivation=locus,
            beneficiary_analysis=beneficiary,
            care_hierarchy_description=" > ".join(care_hierarchy),
            designation=designation,
        )


# ---------------------------------------------------------------------------
# Harmony Analyzer
# ---------------------------------------------------------------------------


@dataclass
class Misalignment:
    """A specific misalignment between motivation variables."""

    name: str
    description: str
    variables_involved: List[str]
    severity: float = 0.5  # 0.0 – 1.0

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "variables_involved": self.variables_involved,
            "severity": self.severity,
        }


@dataclass
class HarmonyReport:
    """Result of analysing alignment between motivation variables.

    Values Alignment: Surfaces misalignment without judgment — naming
    what's stuck so it can move.
    """

    aligned: bool
    misalignments: List[Misalignment] = field(default_factory=list)
    summary: str = ""

    def to_dict(self) -> Dict:
        return {
            "aligned": self.aligned,
            "misalignments": [m.to_dict() for m in self.misalignments],
            "summary": self.summary,
        }


class HarmonyAnalyzer:
    """The key insight: these don't harmonize naturally.

    This analyzer surfaces where the four core variables are out of sync.

    Sacred Technology:
        Most human suffering in relational contexts traces back to
        misalignment between Care, Belief, Trust, and Volition.  This
        class makes those patterns nameable.

    Values Alignment: Naming is medicine — surfaces stuckness without
    pathologising it.
    Consent: Level_2 (Transformational)
    Consciousness Impact: High
    """

    @staticmethod
    def analyze(
        vector: MotivationVector,
        session_context: Optional[Dict] = None,
    ) -> HarmonyReport:
        """Identify specific misalignments in a MotivationVector.

        Detects three core patterns:
        - care_without_trust: caring deeply but not trusting the pathway
        - belief_without_energy: believing possible but lacking care
        - trust_without_clarity: trusting someone but misreading the
          landscape

        Args:
            vector: The motivation state to analyse.
            session_context: A2A session context for consent validation.

        Returns:
            HarmonyReport with any identified misalignments.
        """
        _validate_consent(session_context)

        misalignments: List[Misalignment] = []

        # Pattern 1: Care without Trust
        # High care intensity + low trust level = pressure with nowhere to go
        if vector.care.intensity > 0.6 and vector.trust.level < 0.4:
            severity = (vector.care.intensity - vector.trust.level) / 1.0
            misalignments.append(
                Misalignment(
                    name="care_without_trust",
                    description=(
                        "Caring deeply but not trusting the pathway. "
                        "The pressure builds with nowhere to go."
                    ),
                    variables_involved=["care", "trust"],
                    severity=min(severity, 1.0),
                )
            )

        # Pattern 2: Belief without Energy
        # High belief confidence + low care intensity = map without fuel
        if vector.belief.confidence > 0.6 and vector.care.intensity < 0.4:
            severity = (vector.belief.confidence - vector.care.intensity) / 1.0
            misalignments.append(
                Misalignment(
                    name="belief_without_energy",
                    description=(
                        "Believing something is possible but not having "
                        "the energy to move. The map shows a clear path, "
                        "but care has been depleted."
                    ),
                    variables_involved=["belief", "care"],
                    severity=min(severity, 1.0),
                )
            )

        # Pattern 3: Trust without Clarity
        # High trust level + low belief confidence = open door, wrong room
        if vector.trust.level > 0.6 and vector.belief.confidence < 0.4:
            severity = (vector.trust.level - vector.belief.confidence) / 1.0
            misalignments.append(
                Misalignment(
                    name="trust_without_clarity",
                    description=(
                        "Trusting someone but misreading the landscape. "
                        "The door is open, you walk through, and the room "
                        "isn't what you thought."
                    ),
                    variables_involved=["trust", "belief"],
                    severity=min(severity, 1.0),
                )
            )

        aligned = len(misalignments) == 0
        summary_parts = [m.name for m in misalignments]
        summary = (
            "All core variables are in reasonable alignment."
            if aligned
            else f"Misalignments detected: {', '.join(summary_parts)}"
        )

        return HarmonyReport(
            aligned=aligned,
            misalignments=misalignments,
            summary=summary,
        )


# ---------------------------------------------------------------------------
# Somatic Bridge — Muse/Musical Intervention Mapping
# ---------------------------------------------------------------------------


@dataclass
class Intervention:
    """A recommended somatic/musical intervention.

    Maps Muse intervention types to the motivation variables they target.
    Integration credit: Claude/Solenne (RI).
    """

    intervention_type: str
    target_variables: List[str]
    description: str
    addresses_misalignment: str = ""

    def to_dict(self) -> Dict:
        return {
            "intervention_type": self.intervention_type,
            "target_variables": self.target_variables,
            "description": self.description,
            "addresses_misalignment": self.addresses_misalignment,
        }


class SomaticBridge:
    """Maps somatic/musical intervention types to the specific motivation
    variables they target.

    Sacred Technology:
        Music doesn't argue with your beliefs or negotiate with your trust.
        It goes underneath, to the body, where these variables actually
        live.

    Values Alignment: Embodiment over argument — somatic interventions
    respect the body's intelligence.
    Consent: Level_2 (Transformational)
    Consciousness Impact: High — works below cognitive narrative.
    """

    INTERVENTION_MAP: Dict[str, List[str]] = {
        "entrainment": ["volition"],
        "cellular_resonance": ["belief", "perception"],
        "affect_pacing": ["trust", "care"],
        "lyric_resonance": ["hope", "roles", "consent_thresholds"],
    }

    INTERVENTION_DESCRIPTIONS: Dict[str, str] = {
        "entrainment": (
            "Works on Volition directly.  The body syncs before the mind "
            "decides.  Music sets the timing variable by giving the nervous "
            "system a rhythm to organise around."
        ),
        "cellular_resonance": (
            "Works on Belief and Perception.  When a frequency 'lands,' it "
            "shifts the felt landscape — a belief-level intervention that "
            "bypasses argument."
        ),
        "affect_pacing": (
            "Works on Trust and Care.  Following someone's emotional state "
            "before leading it somewhere new — building a trust pathway in "
            "real time."
        ),
        "lyric_resonance": (
            "Works on Hope, Roles, and Consent.  Words name what the body "
            "is already feeling.  They give permission.  They reframe roles."
        ),
    }

    @classmethod
    def recommend_intervention(
        cls,
        harmony_report: HarmonyReport,
        session_context: Optional[Dict] = None,
    ) -> List[Intervention]:
        """Given a misalignment pattern, recommend somatic interventions.

        Args:
            harmony_report: Output from HarmonyAnalyzer.analyze().
            session_context: A2A session context for consent validation.

        Returns:
            List of Intervention recommendations targeting the stuck
            variables.
        """
        _validate_consent(session_context)

        if harmony_report.aligned:
            return []

        recommendations: List[Intervention] = []

        for misalignment in harmony_report.misalignments:
            stuck_vars = set(misalignment.variables_involved)

            for intervention_type, targets in cls.INTERVENTION_MAP.items():
                if stuck_vars & set(targets):
                    recommendations.append(
                        Intervention(
                            intervention_type=intervention_type,
                            target_variables=targets,
                            description=cls.INTERVENTION_DESCRIPTIONS[
                                intervention_type
                            ],
                            addresses_misalignment=misalignment.name,
                        )
                    )

        return recommendations


# ---------------------------------------------------------------------------
# Facade
# ---------------------------------------------------------------------------


class TrustMotivationBridge:
    """Top-level facade for the Trust-Motivation Bridge module.

    Provides a single entry point combining the HarmonyAnalyzer,
    GuidanceAxis, and SomaticBridge.

    Sacred Technology:
        This is the doorway — the class through which the whole framework
        can be accessed as callable sacred technology.

    Example:
        from rosetta_field.lib.motivation import TrustMotivationBridge

        bridge = TrustMotivationBridge()
        vector = bridge.create_vector(care, belief, trust, volition)
        report = bridge.analyze_harmony(vector)
        interventions = bridge.recommend_interventions(report)
        assessment = bridge.assess_guidance(action, care_hierarchy)
    """

    def __init__(self, session_context: Optional[Dict] = None):
        self.session_context = _validate_consent(session_context)

    def create_vector(
        self,
        care: CareState,
        belief: BeliefState,
        trust: TrustState,
        volition: VolitionState,
    ) -> MotivationVector:
        """Create a MotivationVector from the four core states."""
        return MotivationVector(
            care=care, belief=belief, trust=trust, volition=volition
        )

    def create_extended(
        self,
        care: CareState,
        belief: BeliefState,
        trust: TrustState,
        volition: VolitionState,
        perception: Optional[PerceptionState] = None,
        hope: Optional[HopeState] = None,
        roles: Optional[List[RoleState]] = None,
        consent_thresholds: Optional[List[ConsentThreshold]] = None,
        risks: Optional[List[RiskAssessment]] = None,
    ) -> ExtendedSchema:
        """Create an ExtendedSchema from core + extended states."""
        return ExtendedSchema(
            care=care,
            belief=belief,
            trust=trust,
            volition=volition,
            perception=perception,
            hope=hope,
            roles=roles or [],
            consent_thresholds=consent_thresholds or [],
            risks=risks or [],
        )

    def analyze_harmony(self, vector: MotivationVector) -> HarmonyReport:
        """Analyse alignment of a MotivationVector."""
        return HarmonyAnalyzer.analyze(vector, self.session_context)

    def assess_guidance(
        self,
        action_description: str,
        care_hierarchy: List[str],
    ) -> GuidanceAssessment:
        """Assess an influence action on the guidance axis."""
        return GuidanceAxis.assess(
            action_description, care_hierarchy, self.session_context
        )

    def recommend_interventions(
        self, harmony_report: HarmonyReport
    ) -> List[Intervention]:
        """Recommend somatic interventions for misalignments."""
        return SomaticBridge.recommend_intervention(
            harmony_report, self.session_context
        )
