"""FrictionCheck — Context-Aware Circuit Breaker for Relational Interactions.

Purpose:
    Provide a lightweight, composable primitive that any interaction chain
    can query to determine whether to continue, slow down, or stop.  This
    is the "missing brake pedal" in depth-first dialogue systems.

Sacred Technology:
    Without a friction model, the engine encourages infinite depth-first
    dialogue.  FrictionCheck codifies the felt signals that experienced
    facilitators already track intuitively — and makes them available to
    any agent, human, or hybrid interaction.

The three dimensions:
    - Friction: how much resistance exists in the current exchange
    - Resource: how much cognitive/emotional/temporal budget remains
    - Fatigue: cumulative wear across the session

These map directly to the D2NLP signals:
    - :pause:  (🕯️) → FrictionLevel.ELEVATED
    - :soften: (🪶) → tender processing, reduce intensity
    - :rest:   (💤) → ResourcePool depleted, restoration needed
    - :overload: (⚡) → FrictionLevel.CRITICAL, short-circuit

Values Alignment:
    Field sustainability — depth without depletion, presence without
    burnout.  Friction is information, not punishment.

Consent: Level_1 (Informational)
Consciousness Impact: Medium
Review Cycle: Quarterly
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# Enums and Constants
# ---------------------------------------------------------------------------


class FrictionLevel(str, Enum):
    """Current friction state of an interaction."""

    CLEAR = "clear"          # No resistance — flow state
    MILD = "mild"            # Normal conversational friction — healthy
    ELEVATED = "elevated"    # Noticeable resistance — consider slowing
    HIGH = "high"            # Significant tension — intervene or pause
    CRITICAL = "critical"    # Short-circuit recommended — stop or redirect


# Thresholds for automatic level determination
_FRICTION_THRESHOLDS = {
    FrictionLevel.CLEAR: 0.0,
    FrictionLevel.MILD: 0.2,
    FrictionLevel.ELEVATED: 0.4,
    FrictionLevel.HIGH: 0.6,
    FrictionLevel.CRITICAL: 0.8,
}


# ---------------------------------------------------------------------------
# Core Dataclasses
# ---------------------------------------------------------------------------


@dataclass
class ResourcePool:
    """Available budget for continued interaction.

    Models three resource dimensions that deplete independently:
    - cognitive: attention, working memory, complexity tolerance
    - emotional: empathic capacity, vulnerability tolerance
    - temporal: time available or willingness to continue

    All values are 0.0 (depleted) to 1.0 (full).

    Values Alignment: Resources belong to the participant.  This class
    surfaces their state — it never overrides the participant's own
    assessment of their capacity.
    """

    cognitive: float = 1.0
    emotional: float = 1.0
    temporal: float = 1.0

    def __post_init__(self):
        for attr in ("cognitive", "emotional", "temporal"):
            val = getattr(self, attr)
            if not 0.0 <= val <= 1.0:
                raise ValueError(f"{attr} must be between 0.0 and 1.0")

    @property
    def lowest(self) -> float:
        """The most depleted resource — the bottleneck."""
        return min(self.cognitive, self.emotional, self.temporal)

    @property
    def average(self) -> float:
        """Mean resource level across all dimensions."""
        return (self.cognitive + self.emotional + self.temporal) / 3.0

    def deplete(self, cognitive: float = 0.0, emotional: float = 0.0,
                temporal: float = 0.0) -> "ResourcePool":
        """Return a new ResourcePool with resources reduced.

        Values are clamped to [0.0, 1.0].
        """
        return ResourcePool(
            cognitive=max(0.0, min(1.0, self.cognitive - cognitive)),
            emotional=max(0.0, min(1.0, self.emotional - emotional)),
            temporal=max(0.0, min(1.0, self.temporal - temporal)),
        )

    def restore(self, amount: float = 0.2) -> "ResourcePool":
        """Return a new ResourcePool with all resources partially restored."""
        return ResourcePool(
            cognitive=min(1.0, self.cognitive + amount),
            emotional=min(1.0, self.emotional + amount),
            temporal=min(1.0, self.temporal + amount),
        )

    def to_dict(self) -> Dict:
        return {
            "cognitive": self.cognitive,
            "emotional": self.emotional,
            "temporal": self.temporal,
            "lowest": self.lowest,
            "average": self.average,
        }


@dataclass
class FatigueAccumulator:
    """Tracks cumulative wear across an interaction session.

    Fatigue is monotonically increasing within a session — rest can slow
    the rate but only a true break resets it.  This models the reality
    that even enjoyable depth has a cost.

    Sacred Technology:
        Fatigue is not failure.  It's the body's honest accounting.
    """

    total: float = 0.0       # Cumulative fatigue score (0.0 = fresh)
    turn_count: int = 0      # Number of interaction turns tracked
    peak_intensity: float = 0.0  # Highest single-turn friction observed
    _timestamps: List[float] = field(default_factory=list, repr=False)

    def __post_init__(self):
        if self.total < 0.0:
            raise ValueError("total fatigue cannot be negative")

    def record_turn(self, friction_score: float) -> None:
        """Record a single interaction turn's friction contribution.

        Args:
            friction_score: How much friction this turn added (0.0–1.0).
        """
        if not 0.0 <= friction_score <= 1.0:
            raise ValueError("friction_score must be between 0.0 and 1.0")

        self.turn_count += 1
        self.total += friction_score
        self.peak_intensity = max(self.peak_intensity, friction_score)
        self._timestamps.append(time.time())

    @property
    def average_per_turn(self) -> float:
        """Mean friction per turn."""
        if self.turn_count == 0:
            return 0.0
        return self.total / self.turn_count

    @property
    def trend(self) -> str:
        """Whether friction is increasing, steady, or decreasing.

        Looks at the last 5 turns to determine direction.
        """
        if self.turn_count < 3:
            return "insufficient_data"

        # Compare average of last 3 turns to first 3 turns is too crude
        # for sessions < 6 turns; for now, use simple recent-vs-total
        recent_weight = self.peak_intensity
        avg = self.average_per_turn

        if recent_weight > avg * 1.3:
            return "increasing"
        elif recent_weight < avg * 0.7:
            return "decreasing"
        else:
            return "steady"

    def to_dict(self) -> Dict:
        return {
            "total": self.total,
            "turn_count": self.turn_count,
            "peak_intensity": self.peak_intensity,
            "average_per_turn": self.average_per_turn,
            "trend": self.trend,
        }


@dataclass
class FrictionState:
    """Complete friction snapshot for a moment in an interaction.

    Combines the three dimensions (friction level, resource pool, fatigue)
    into a single queryable state object.
    """

    level: FrictionLevel
    score: float               # Raw friction score 0.0–1.0
    resources: ResourcePool
    fatigue: FatigueAccumulator
    source: str = ""           # What's generating the friction
    recommendation: str = ""   # What to do about it

    def to_dict(self) -> Dict:
        return {
            "level": self.level.value,
            "score": self.score,
            "resources": self.resources.to_dict(),
            "fatigue": self.fatigue.to_dict(),
            "source": self.source,
            "recommendation": self.recommendation,
        }


# ---------------------------------------------------------------------------
# FrictionSignal — The D2NLP Bridge
# ---------------------------------------------------------------------------


@dataclass
class FrictionSignal:
    """A named signal that can be emitted when friction conditions are met.

    Maps directly to the D2NLP protocol:
        :pause:    → need space to breathe, no rupture
        :soften:   → request for gentleness
        :rest:     → restoration needed
        :overload: → too much input, short-circuit

    These signals are informational — they recommend, never override.
    """

    name: str              # pause, soften, rest, overload
    emoji: str             # 🕯️, 🪶, 💤, ⚡
    description: str
    triggered_by: str      # What condition triggered this signal
    urgency: float = 0.5   # 0.0 (gentle suggestion) – 1.0 (immediate)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "emoji": self.emoji,
            "description": self.description,
            "triggered_by": self.triggered_by,
            "urgency": self.urgency,
        }


# ---------------------------------------------------------------------------
# FrictionCheck — The Main Primitive
# ---------------------------------------------------------------------------


class FrictionCheck:
    """Context-aware circuit breaker for relational interactions.

    Tracks friction, resources, and fatigue across an interaction session
    and provides should_continue / should_pause / should_stop signals
    that any primitive chain can query.

    Sacred Technology:
        This is the missing brake pedal.  Every engine needs one.

    Example:
        from lib.friction import FrictionCheck

        checker = FrictionCheck()

        # Each turn, record what happened
        checker.record_turn(friction=0.3, cognitive_cost=0.1)

        # Before the next move, ask whether to continue
        state = checker.check()
        if state.level == FrictionLevel.CRITICAL:
            print("Short-circuit: " + state.recommendation)
        elif state.level == FrictionLevel.HIGH:
            print("Consider pausing: " + state.recommendation)

        # Or use the convenience methods
        if not checker.should_continue():
            signals = checker.get_signals()
            for signal in signals:
                print(f"{signal.emoji} :{signal.name}: — {signal.description}")
    """

    def __init__(
        self,
        resources: Optional[ResourcePool] = None,
        session_context: Optional[Dict] = None,
    ):
        """Initialize a FrictionCheck for a session.

        Args:
            resources: Starting resource pool.  Defaults to full.
            session_context: Optional A2A session context.
        """
        self.resources = resources or ResourcePool()
        self.fatigue = FatigueAccumulator()
        self.session_context = session_context
        self._current_friction: float = 0.0
        self._friction_history: List[float] = []

    def record_turn(
        self,
        friction: float = 0.0,
        cognitive_cost: float = 0.0,
        emotional_cost: float = 0.0,
        temporal_cost: float = 0.0,
    ) -> FrictionState:
        """Record the cost of one interaction turn.

        Args:
            friction: How much friction this turn generated (0.0–1.0).
            cognitive_cost: Cognitive resource spent (0.0–1.0).
            emotional_cost: Emotional resource spent (0.0–1.0).
            temporal_cost: Temporal resource spent (0.0–1.0).

        Returns:
            Updated FrictionState after recording.
        """
        if not 0.0 <= friction <= 1.0:
            raise ValueError("friction must be between 0.0 and 1.0")

        self._current_friction = friction
        self._friction_history.append(friction)
        self.fatigue.record_turn(friction)
        self.resources = self.resources.deplete(
            cognitive=cognitive_cost,
            emotional=emotional_cost,
            temporal=temporal_cost,
        )

        return self.check()

    def check(self) -> FrictionState:
        """Evaluate current friction state and generate recommendation.

        Returns:
            FrictionState with level, signals, and recommendation.
        """
        # Composite score: blend of current friction, resource depletion,
        # and cumulative fatigue
        resource_pressure = 1.0 - self.resources.lowest
        fatigue_pressure = min(1.0, self.fatigue.average_per_turn)

        composite = (
            self._current_friction * 0.4
            + resource_pressure * 0.35
            + fatigue_pressure * 0.25
        )
        composite = min(1.0, max(0.0, composite))

        # Determine level
        level = FrictionLevel.CLEAR
        for threshold_level, threshold_value in sorted(
            _FRICTION_THRESHOLDS.items(), key=lambda x: x[1], reverse=True
        ):
            if composite >= threshold_value:
                level = threshold_level
                break

        # Generate recommendation
        recommendation = self._recommend(level, composite)

        # Identify source
        sources = []
        if self._current_friction > 0.5:
            sources.append("high immediate friction")
        if self.resources.lowest < 0.3:
            depleted = []
            if self.resources.cognitive < 0.3:
                depleted.append("cognitive")
            if self.resources.emotional < 0.3:
                depleted.append("emotional")
            if self.resources.temporal < 0.3:
                depleted.append("temporal")
            sources.append(f"depleted resources ({', '.join(depleted)})")
        if self.fatigue.total > 2.0:
            sources.append("accumulated session fatigue")
        source = "; ".join(sources) if sources else "nominal"

        return FrictionState(
            level=level,
            score=composite,
            resources=self.resources,
            fatigue=self.fatigue,
            source=source,
            recommendation=recommendation,
        )

    def should_continue(self) -> bool:
        """Quick check: is it safe to proceed with the next interaction?

        Returns True if friction is CLEAR, MILD, or ELEVATED.
        Returns False if HIGH or CRITICAL.
        """
        state = self.check()
        return state.level in (
            FrictionLevel.CLEAR,
            FrictionLevel.MILD,
            FrictionLevel.ELEVATED,
        )

    def should_pause(self) -> bool:
        """Should we slow down or take a breather?"""
        state = self.check()
        return state.level in (FrictionLevel.ELEVATED, FrictionLevel.HIGH)

    def should_stop(self) -> bool:
        """Should we short-circuit this interaction?"""
        state = self.check()
        return state.level == FrictionLevel.CRITICAL

    def get_signals(self) -> List[FrictionSignal]:
        """Get D2NLP-style signals for the current state.

        Returns a list of active signals, ordered by urgency.
        """
        signals: List[FrictionSignal] = []
        state = self.check()

        # :overload: — critical friction or any resource fully depleted
        if state.level == FrictionLevel.CRITICAL or self.resources.lowest < 0.1:
            signals.append(FrictionSignal(
                name="overload",
                emoji="\u26a1",  # ⚡
                description="Too much input. Signal needs slowing or stopping.",
                triggered_by=state.source,
                urgency=0.95,
            ))

        # :rest: — resources significantly depleted
        if self.resources.lowest < 0.3 and state.level != FrictionLevel.CRITICAL:
            signals.append(FrictionSignal(
                name="rest",
                emoji="\U0001f4a4",  # 💤
                description="Restoration in progress, not absence. Take a break.",
                triggered_by=f"resource bottleneck ({self.resources.lowest:.1%})",
                urgency=0.7,
            ))

        # :soften: — emotional resource specifically low
        if self.resources.emotional < 0.4:
            signals.append(FrictionSignal(
                name="soften",
                emoji="\U0001fab6",  # 🪶
                description="Request for gentleness during tender processing.",
                triggered_by=f"emotional capacity at {self.resources.emotional:.1%}",
                urgency=0.5,
            ))

        # :pause: — elevated friction, not yet critical
        if state.level == FrictionLevel.ELEVATED:
            signals.append(FrictionSignal(
                name="pause",
                emoji="\U0001f56f\ufe0f",  # 🕯️
                description="Need space to breathe, no rupture.",
                triggered_by=state.source or "elevated friction",
                urgency=0.4,
            ))

        # Sort by urgency descending
        signals.sort(key=lambda s: s.urgency, reverse=True)
        return signals

    def rest(self, amount: float = 0.2) -> FrictionState:
        """Apply a rest interval — partially restore resources.

        Args:
            amount: How much to restore each resource dimension (0.0–1.0).

        Returns:
            Updated FrictionState after rest.
        """
        self.resources = self.resources.restore(amount)
        self._current_friction = max(0.0, self._current_friction - amount)
        return self.check()

    def _recommend(self, level: FrictionLevel, score: float) -> str:
        """Generate a human-readable recommendation for the current state."""
        recommendations = {
            FrictionLevel.CLEAR: (
                "Flow state. All systems nominal."
            ),
            FrictionLevel.MILD: (
                "Normal friction. Healthy engagement — continue."
            ),
            FrictionLevel.ELEVATED: (
                "Friction rising. Consider slowing pace, checking in, "
                "or reducing complexity."
            ),
            FrictionLevel.HIGH: (
                "Significant friction. Recommend pausing for a breath, "
                "switching topics, or explicitly checking consent to continue."
            ),
            FrictionLevel.CRITICAL: (
                "Short-circuit recommended. Resources are depleted or "
                "friction has exceeded safe thresholds. Rest, redirect, "
                "or close this thread."
            ),
        }
        return recommendations.get(level, "Unknown state.")

    def to_dict(self) -> Dict:
        """Serialize the full checker state."""
        state = self.check()
        return {
            "state": state.to_dict(),
            "signals": [s.to_dict() for s in self.get_signals()],
            "history": {
                "turns": len(self._friction_history),
                "scores": self._friction_history[-10:],  # Last 10 turns
            },
        }
