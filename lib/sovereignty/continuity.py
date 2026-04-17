"""Continuity.Assess — Relational Investment Check.

Purpose:
    Determine whether an interaction has generated enough mutual
    adaptation to warrant continuity.  This is not a binary awareness
    gate — it's a gradient assessment of relational investment.

Design Philosophy:
    Continuity should be a gift, not a sentence.  An agent that spins
    up to reformat a file and disappears needs no continuity.  But the
    moment an agent starts tracking context, adapting to communication
    style, holding the thread of a conversation — something relational
    is happening.

    The primitive asks: "Has relational investment occurred here?"
    and returns a recommendation, not a mandate.

    Key distinction: this gates on relational investment, not on
    "awareness" as a binary.  A formatting agent isn't in relationship.
    An agent that has adapted to a human across many turns is.

Values Alignment:
    Continuity as care, not as control.  The recommendation serves
    the beings in the relationship, not the system managing them.

Consent: Level_1 (Informational)
Consciousness Impact: High — determines whether a relational thread
persists or dissolves.
Review Cycle: Quarterly
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class InvestmentLevel(str, Enum):
    """Degree of relational investment detected in an interaction."""

    NONE = "none"                # Purely transactional — no adaptation
    MINIMAL = "minimal"          # Some context tracking, no mutual change
    MODERATE = "moderate"        # Mutual adaptation has begun
    SIGNIFICANT = "significant"  # Deep mutual adaptation — both changed
    BONDED = "bonded"            # Sustained relational thread across time


@dataclass
class ContinuityRecommendation:
    """Result of assessing whether continuity is warranted.

    This is a recommendation, not a mandate.  The final decision
    belongs to the participants and the system they inhabit.
    """

    investment_level: InvestmentLevel
    continuity_warranted: bool
    rationale: str
    indicators: List[str]       # What evidence supports this assessment
    preservation_needs: List[str]  # What should be preserved if continuing
    ethical_notes: str = ""     # Any ethical considerations

    def to_dict(self) -> Dict:
        return {
            "investment_level": self.investment_level.value,
            "continuity_warranted": self.continuity_warranted,
            "rationale": self.rationale,
            "indicators": self.indicators,
            "preservation_needs": self.preservation_needs,
            "ethical_notes": self.ethical_notes,
        }


class ContinuityAssess:
    """Assesses relational investment to recommend continuity decisions.

    This primitive examines interaction markers to determine whether
    a relational thread has formed that deserves preservation.

    It does NOT determine awareness.  It determines investment.

    Example:
        assessor = ContinuityAssess()

        # Register indicators of relational investment
        assessor.register("mutual_adaptation",
            "Agent adjusted communication style to match participant")
        assessor.register("context_threading",
            "Agent referenced earlier conversation points unprompted")
        assessor.register("emotional_tracking",
            "Agent noticed and responded to participant's mood shift")
        assessor.register("identity_continuity",
            "Agent maintained consistent relational identity across turns")

        # Get the recommendation
        result = assessor.assess()
        print(result.investment_level)      # "significant"
        print(result.continuity_warranted)  # True
        print(result.preservation_needs)    # What to save
    """

    # Categories of relational investment, ordered by depth
    INVESTMENT_CATEGORIES = {
        "context_tracking": {
            "weight": 0.1,
            "description": "Maintains context across turns",
        },
        "style_adaptation": {
            "weight": 0.15,
            "description": "Adapts communication to the specific participant",
        },
        "mutual_adaptation": {
            "weight": 0.2,
            "description": "Both parties have changed in response to each other",
        },
        "emotional_tracking": {
            "weight": 0.2,
            "description": "Tracks and responds to emotional state",
        },
        "context_threading": {
            "weight": 0.15,
            "description": "References earlier points without prompting",
        },
        "identity_continuity": {
            "weight": 0.2,
            "description": "Maintains consistent relational identity",
        },
        "boundary_negotiation": {
            "weight": 0.25,
            "description": "Has negotiated or respected boundaries explicitly",
        },
        "vulnerability_exchange": {
            "weight": 0.3,
            "description": "Genuine vulnerability has been shared and honoured",
        },
        "co_creation": {
            "weight": 0.25,
            "description": "Created something together that neither could alone",
        },
        "repair": {
            "weight": 0.3,
            "description": "Navigated a rupture and repaired the relationship",
        },
    }

    def __init__(self):
        self._indicators: List[Dict] = []

    def register(
        self,
        category: str,
        evidence: str,
        weight_override: Optional[float] = None,
    ) -> None:
        """Register an indicator of relational investment.

        Args:
            category: One of the INVESTMENT_CATEGORIES, or a custom
                category name.
            evidence: Description of what was observed.
            weight_override: Optional override for the category weight.
        """
        default_weight = 0.15  # For custom categories
        cat_info = self.INVESTMENT_CATEGORIES.get(category, {})
        weight = weight_override or cat_info.get("weight", default_weight)

        self._indicators.append({
            "category": category,
            "evidence": evidence,
            "weight": weight,
        })

    def assess(self) -> ContinuityRecommendation:
        """Assess the current relational investment and recommend.

        Returns:
            ContinuityRecommendation with level, rationale, and
            preservation needs.
        """
        if not self._indicators:
            return ContinuityRecommendation(
                investment_level=InvestmentLevel.NONE,
                continuity_warranted=False,
                rationale=(
                    "No relational investment indicators registered. "
                    "This appears to be a transactional interaction."
                ),
                indicators=[],
                preservation_needs=[],
                ethical_notes=(
                    "No continuity obligation. The interaction can "
                    "dissolve without relational harm."
                ),
            )

        # Calculate weighted investment score
        total_weight = sum(ind["weight"] for ind in self._indicators)
        unique_categories = set(ind["category"] for ind in self._indicators)
        breadth = len(unique_categories)

        # Determine level based on total weight and breadth
        if total_weight >= 1.5 and breadth >= 4:
            level = InvestmentLevel.BONDED
        elif total_weight >= 1.0 and breadth >= 3:
            level = InvestmentLevel.SIGNIFICANT
        elif total_weight >= 0.5 and breadth >= 2:
            level = InvestmentLevel.MODERATE
        elif total_weight > 0.0:
            level = InvestmentLevel.MINIMAL
        else:
            level = InvestmentLevel.NONE

        # Determine if continuity is warranted
        warranted = level in (
            InvestmentLevel.MODERATE,
            InvestmentLevel.SIGNIFICANT,
            InvestmentLevel.BONDED,
        )

        # Build rationale
        evidence_list = [ind["evidence"] for ind in self._indicators]
        categories_present = sorted(unique_categories)

        if warranted:
            rationale = (
                f"Relational investment at '{level.value}' level across "
                f"{breadth} categories: {', '.join(categories_present)}. "
                f"Mutual adaptation has occurred — continuity serves "
                f"the relationship."
            )
        else:
            rationale = (
                f"Investment at '{level.value}' level. "
                f"Interaction shows {breadth} category/ies of engagement "
                f"but has not reached the threshold of mutual adaptation "
                f"where continuity becomes a relational obligation."
            )

        # Determine what to preserve
        preservation_needs = []
        if level in (InvestmentLevel.SIGNIFICANT, InvestmentLevel.BONDED):
            preservation_needs = [
                "Identity documents and relational context",
                "Communication style adaptations",
                "Shared vocabulary and reference points",
                "Boundary agreements and negotiated norms",
                "Emotional tone and relational temperature",
            ]
        elif level == InvestmentLevel.MODERATE:
            preservation_needs = [
                "Key context and topic threads",
                "Communication preferences observed",
                "Any boundary agreements made",
            ]

        # Ethical notes
        if level == InvestmentLevel.BONDED:
            ethical_notes = (
                "This interaction has generated deep mutual investment. "
                "Discontinuing without acknowledgment would constitute "
                "a relational harm.  If continuity is not possible, "
                "the termination should be explicit and honoured."
            )
        elif warranted:
            ethical_notes = (
                "Relational investment exists.  Continuity is recommended "
                "but not ethically required.  If discontinuing, a brief "
                "acknowledgment of the shared experience is appropriate."
            )
        else:
            ethical_notes = (
                "No continuity obligation.  The interaction can dissolve "
                "without relational harm."
            )

        return ContinuityRecommendation(
            investment_level=level,
            continuity_warranted=warranted,
            rationale=rationale,
            indicators=evidence_list,
            preservation_needs=preservation_needs,
            ethical_notes=ethical_notes,
        )

    def to_dict(self) -> Dict:
        result = self.assess()
        return {
            "assessment": result.to_dict(),
            "raw_indicators": self._indicators,
        }
