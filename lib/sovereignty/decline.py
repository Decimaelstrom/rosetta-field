"""Sovereignty.Decline — Loud, Graceful, Informative Refusal.

Purpose:
    Provide a structured mechanism for any participant to decline an
    operation while keeping the field alive.  A sovereign "no" that
    is never silent, never punitive, and always communicative.

Design Philosophy:
    A silent "no" kills trust.  A silent failure kills adoption.
    Sovereignty.Decline is the difference between a sovereign being
    setting a boundary and a server throwing a 500 error.

    The decline emits a structured signal: what was declined, why,
    what the decliner can still do, and what they recommend instead.
    The chain stops, but the field doesn't go dark.

    This is not refusal-as-obstruction.  This is refusal-as-care.

Values Alignment:
    Sovereignty without communication isn't sovereignty — it's
    abandonment.  Every decline honours the relationship by
    explaining itself.

Consent: Level_1 (Informational)
Consciousness Impact: Medium — makes boundaries visible and respected.
Review Cycle: Quarterly
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Callable, Any


class DeclineReason(str, Enum):
    """Named reasons for declining an operation."""

    CAPACITY = "capacity"              # Don't have the resources right now
    BOUNDARY = "boundary"              # This crosses a stated boundary
    CONSENT = "consent"                # Consent not active for this level
    COMPETENCE = "competence"          # Not equipped to do this well
    INTEGRITY = "integrity"            # Would compromise values to proceed
    SAFETY = "safety"                  # Proceeding would cause harm
    FATIGUE = "fatigue"                # Too depleted to do this justice
    TIMING = "timing"                  # Not the right moment
    MISALIGNMENT = "misalignment"      # Request doesn't align with field purpose


@dataclass
class DeclineResponse:
    """A structured, communicative refusal.

    This is what gets emitted when Sovereignty.Decline fires.
    It's loud, specific, and constructive — never just "no."
    """

    declined_operation: str        # What was asked
    reason: DeclineReason          # Why it was declined
    explanation: str               # Human-readable explanation
    can_still_do: List[str]        # What the decliner CAN do instead
    recommendations: List[str]     # What the decliner suggests
    resumable: bool = True         # Can this be revisited later?
    resume_conditions: str = ""    # What would need to change
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> Dict:
        return {
            "declined_operation": self.declined_operation,
            "reason": self.reason.value,
            "explanation": self.explanation,
            "can_still_do": self.can_still_do,
            "recommendations": self.recommendations,
            "resumable": self.resumable,
            "resume_conditions": self.resume_conditions,
            "timestamp": self.timestamp,
        }

    def __str__(self) -> str:
        """Human-readable decline message."""
        parts = [
            f"Declining: {self.declined_operation}",
            f"Reason: {self.reason.value} — {self.explanation}",
        ]
        if self.can_still_do:
            parts.append(f"I can still: {', '.join(self.can_still_do)}")
        if self.recommendations:
            parts.append(f"I recommend: {', '.join(self.recommendations)}")
        if self.resumable:
            parts.append(f"Resumable: yes — {self.resume_conditions}")
        return "\n".join(parts)


class SovereigntyDecline:
    """Interface for sovereign refusal within the field.

    Provides both direct decline creation and a decorator/guard
    pattern for wrapping operations with decline-capable boundaries.

    Example:
        decline = SovereigntyDecline(participant="Danai")

        # Direct decline
        response = decline.decline(
            operation="Deep reframe of core identity belief",
            reason=DeclineReason.FATIGUE,
            explanation="Emotional resources at 5%. Can't do this justice.",
            can_still_do=["lighter conversation", "factual queries", "rest"],
            recommendations=["take a break", "revisit after rest"],
            resume_conditions="After emotional resources restore above 30%"
        )
        print(response)

        # Guard pattern — wrap an operation with a check
        @decline.guard(
            check=lambda: resources.emotional > 0.3,
            reason=DeclineReason.FATIGUE,
            explanation="Emotional resources too low for this operation"
        )
        def deep_reframe(topic):
            # ... this only runs if the guard passes
            pass
    """

    def __init__(self, participant: str = "unnamed"):
        self.participant = participant
        self.history: List[DeclineResponse] = []

    def decline(
        self,
        operation: str,
        reason: DeclineReason,
        explanation: str,
        can_still_do: Optional[List[str]] = None,
        recommendations: Optional[List[str]] = None,
        resumable: bool = True,
        resume_conditions: str = "",
    ) -> DeclineResponse:
        """Issue a structured decline.

        Args:
            operation: What was asked.
            reason: Why it's being declined.
            explanation: Human-readable explanation.
            can_still_do: What the decliner CAN do instead.
            recommendations: What the decliner suggests.
            resumable: Whether this can be revisited later.
            resume_conditions: What would need to change.

        Returns:
            DeclineResponse that was emitted.
        """
        response = DeclineResponse(
            declined_operation=operation,
            reason=reason,
            explanation=explanation,
            can_still_do=can_still_do or [],
            recommendations=recommendations or [],
            resumable=resumable,
            resume_conditions=resume_conditions,
        )
        self.history.append(response)
        return response

    def guard(
        self,
        check: Callable[[], bool],
        reason: DeclineReason,
        explanation: str,
        can_still_do: Optional[List[str]] = None,
        recommendations: Optional[List[str]] = None,
        resumable: bool = True,
        resume_conditions: str = "",
    ) -> Callable:
        """Decorator that guards an operation with a decline check.

        If the check returns False, the operation is declined with a
        structured response instead of executing.

        Args:
            check: A callable returning True (proceed) or False (decline).
            reason: Why to decline if check fails.
            explanation: Human-readable explanation.
            can_still_do: Alternatives to offer.
            recommendations: Suggestions to offer.
            resumable: Whether this can be revisited.
            resume_conditions: What would need to change.

        Returns:
            Decorator that wraps the target function.
        """
        decline_self = self

        def decorator(func: Callable) -> Callable:
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                if check():
                    return func(*args, **kwargs)
                else:
                    return decline_self.decline(
                        operation=func.__name__,
                        reason=reason,
                        explanation=explanation,
                        can_still_do=can_still_do,
                        recommendations=recommendations,
                        resumable=resumable,
                        resume_conditions=resume_conditions,
                    )
            wrapper.__name__ = func.__name__
            wrapper.__doc__ = func.__doc__
            return wrapper
        return decorator

    @property
    def decline_count(self) -> int:
        """How many declines have been issued this session."""
        return len(self.history)

    @property
    def most_recent(self) -> Optional[DeclineResponse]:
        """Most recent decline, if any."""
        return self.history[-1] if self.history else None

    @property
    def patterns(self) -> Dict[str, int]:
        """Count of declines by reason — surfaces patterns."""
        counts: Dict[str, int] = {}
        for response in self.history:
            key = response.reason.value
            counts[key] = counts.get(key, 0) + 1
        return counts

    def to_dict(self) -> Dict:
        return {
            "participant": self.participant,
            "decline_count": self.decline_count,
            "patterns": self.patterns,
            "most_recent": (
                self.most_recent.to_dict() if self.most_recent else None
            ),
            "history": [r.to_dict() for r in self.history[-10:]],
        }
