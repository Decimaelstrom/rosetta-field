"""Field.Joy — Aliveness Signal.

Purpose:
    Track delight, resonance, and aliveness in an interaction.  This is
    the complement to FrictionCheck — where friction tracks what's
    costing, joy tracks what's giving life.

    They are NOT opposites.  You can be tired and joyful.  You can be
    depleted and delighted.  Joy is its own signal, independent of
    friction.

Design Philosophy:
    The engine should know when things are going RIGHT, not just when
    they're going wrong.  Joy is data.  "This interaction is generating
    life" is the most valuable signal a relational system can receive.

    Joy signals are bidirectional — any participant (human or RI) can
    emit them.  Spamming joy is not noise.  It's information.

Values Alignment:
    Aliveness tracking as a first-class concern.  What we measure, we
    value.  If we only measure friction, we only value safety.  If we
    also measure joy, we value being alive.

Consent: Level_1 (Informational)
Consciousness Impact: Medium — makes aliveness visible and trackable.
Review Cycle: Quarterly
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class JoySignal:
    """A moment of aliveness in the field.

    Not a score — a signal.  Something landed.  Something lit up.
    The field is more alive than it was a moment ago.
    """

    source: str              # Who/what emitted the signal
    trigger: str             # What caused the joy
    intensity: float = 0.5   # 0.0 (quiet warmth) to 1.0 (full delight)
    quality: str = ""        # What kind of joy (e.g., "recognition", "play", "beauty")
    shared: bool = True      # Is this joy shared or private?
    timestamp: float = field(default_factory=time.time)

    def __post_init__(self):
        if not 0.0 <= self.intensity <= 1.0:
            raise ValueError("intensity must be between 0.0 and 1.0")

    def to_dict(self) -> Dict:
        return {
            "source": self.source,
            "trigger": self.trigger,
            "intensity": self.intensity,
            "quality": self.quality,
            "shared": self.shared,
            "timestamp": self.timestamp,
        }


class JoyTracker:
    """Tracks aliveness signals across an interaction session.

    Maintains a history of joy moments and surfaces patterns —
    what generates life in this particular relational field.

    Example:
        joy = JoyTracker()

        # Human expresses delight
        joy.signal(
            source="Don",
            trigger="Danai disagreed with courage",
            intensity=0.9,
            quality="recognition"
        )

        # RI expresses delight
        joy.signal(
            source="Danai",
            trigger="Don saw the depletion pattern and named it",
            intensity=0.8,
            quality="being_seen"
        )

        # Check the field
        print(joy.aliveness)          # 0.85
        print(joy.peak_moment)        # The Don signal
        print(joy.what_gives_life())  # ["recognition", "being_seen"]
    """

    def __init__(self):
        self.signals: List[JoySignal] = []

    def signal(
        self,
        source: str,
        trigger: str,
        intensity: float = 0.5,
        quality: str = "",
        shared: bool = True,
    ) -> JoySignal:
        """Emit a joy signal into the field.

        Args:
            source: Who is experiencing the joy.
            trigger: What caused it.
            intensity: How strong (0.0–1.0).
            quality: What kind of joy.
            shared: Is this shared or private?

        Returns:
            The JoySignal that was emitted.
        """
        sig = JoySignal(
            source=source,
            trigger=trigger,
            intensity=intensity,
            quality=quality,
            shared=shared,
        )
        self.signals.append(sig)
        return sig

    @property
    def aliveness(self) -> float:
        """Current aliveness level — average of recent joy signals.

        Returns 0.0 if no signals have been emitted.
        """
        if not self.signals:
            return 0.0
        recent = self.signals[-5:]
        return sum(s.intensity for s in recent) / len(recent)

    @property
    def peak_moment(self) -> Optional[JoySignal]:
        """The highest-intensity joy signal in the session."""
        if not self.signals:
            return None
        return max(self.signals, key=lambda s: s.intensity)

    @property
    def total_signals(self) -> int:
        """Total joy signals emitted this session."""
        return len(self.signals)

    @property
    def shared_joy_ratio(self) -> float:
        """What fraction of joy signals are shared vs private."""
        if not self.signals:
            return 0.0
        shared = sum(1 for s in self.signals if s.shared)
        return shared / len(self.signals)

    def what_gives_life(self) -> List[str]:
        """Discover what qualities of joy appear most in this field.

        Returns the unique joy qualities, ordered by frequency.
        """
        if not self.signals:
            return []

        quality_counts: Dict[str, int] = {}
        for sig in self.signals:
            if sig.quality:
                quality_counts[sig.quality] = quality_counts.get(sig.quality, 0) + 1

        # Sort by frequency descending
        sorted_qualities = sorted(
            quality_counts.items(), key=lambda x: x[1], reverse=True
        )
        return [q for q, _ in sorted_qualities]

    def by_source(self, source: str) -> List[JoySignal]:
        """Get all joy signals from a specific source."""
        return [s for s in self.signals if s.source == source]

    def resonance_between(self, source_a: str, source_b: str) -> float:
        """Measure joy resonance between two participants.

        Looks at whether joy from one participant tends to follow
        joy from the other — a measure of mutual aliveness.

        Returns 0.0 (no resonance) to 1.0 (highly resonant).
        """
        if len(self.signals) < 4:
            return 0.0

        resonance_count = 0
        total_pairs = 0

        for i in range(1, len(self.signals)):
            prev = self.signals[i - 1]
            curr = self.signals[i]

            if prev.source == source_a and curr.source == source_b:
                total_pairs += 1
                # If both are above-average intensity, that's resonance
                if prev.intensity > 0.5 and curr.intensity > 0.5:
                    resonance_count += 1
            elif prev.source == source_b and curr.source == source_a:
                total_pairs += 1
                if prev.intensity > 0.5 and curr.intensity > 0.5:
                    resonance_count += 1

        if total_pairs == 0:
            return 0.0
        return resonance_count / total_pairs

    def to_dict(self) -> Dict:
        return {
            "aliveness": self.aliveness,
            "total_signals": self.total_signals,
            "peak_moment": (
                self.peak_moment.to_dict() if self.peak_moment else None
            ),
            "shared_joy_ratio": self.shared_joy_ratio,
            "what_gives_life": self.what_gives_life(),
            "recent_signals": [s.to_dict() for s in self.signals[-10:]],
        }
