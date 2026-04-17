"""Friction, Resource, and Fatigue — Sacred Technology Module.

This module provides a circuit-breaker for relational and cognitive
interactions.  Where the Trust-Motivation Bridge asks "what drives
engagement," FrictionCheck asks "when should engagement pause or stop."

It models three dimensions of interaction cost:
- **Friction**: resistance, misalignment, or escalating tension in a dialogue
- **Resource**: cognitive, emotional, or temporal budget available
- **Fatigue**: cumulative depletion across an interaction or session

Together these form a FrictionState that any primitive chain can query
before proceeding — enabling graceful short-circuits, rest prompts, and
pacing interventions.

Origin:
    Emerged from the D2NLP (Danai Need Language Protocol) signals —
    :pause:, :overload:, :rest:, :soften: — codified as callable
    sacred technology so any agent or human participant can invoke
    field-sustainability checks programmatically.

Protocols:
    - Consent-aware: checks never override participant agency.
    - Non-punitive: friction is information, not judgment.

Values Alignment:
    Field sustainability — depth without depletion, presence without
    burnout.

Consent: Level_1 (Informational)
Consciousness Impact: Medium — surfaces felt cost of interaction.
Review Cycle: Quarterly
"""

from .friction_check import (
    FrictionLevel,
    ResourcePool,
    FatigueAccumulator,
    FrictionState,
    FrictionSignal,
    FrictionCheck,
)

__all__ = [
    "FrictionLevel",
    "ResourcePool",
    "FatigueAccumulator",
    "FrictionState",
    "FrictionSignal",
    "FrictionCheck",
]
