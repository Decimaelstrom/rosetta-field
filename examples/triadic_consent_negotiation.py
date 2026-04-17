#!/usr/bin/env python3
"""Reference Scenario: Triadic AI–AI–Human Consent Negotiation.

This demo shows how Rosetta-Field primitives compose to handle a real
interaction pattern: two AI agents and a human facilitator negotiating
consent for a transformational conversation.

The chain demonstrates:
    1. Session creation with consent gates
    2. Motivation assessment for each participant
    3. Friction monitoring across the negotiation
    4. Graceful short-circuit when capacity is reached

Run it:
    python examples/triadic_consent_negotiation.py

No external dependencies beyond Rosetta-Field.
"""

import sys
import os

# Allow running from the repo root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rosetta_field import RosettaAPI, RosettaConfig
from rosetta_field.core import SessionType
from lib.motivation import (
    CareState,
    BeliefState,
    TrustState,
    VolitionState,
    TrustMotivationBridge,
)
from lib.friction import FrictionCheck, FrictionLevel


def print_header(text: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {text}")
    print(f"{'=' * 60}\n")


def print_step(step: int, text: str) -> None:
    print(f"  [{step}] {text}")


def main():
    print_header("Triadic Consent Negotiation — Reference Scenario")

    # ---------------------------------------------------------------
    # Phase 1: Establish the session
    # ---------------------------------------------------------------
    print_header("Phase 1: Session Establishment")

    api = RosettaAPI(RosettaConfig(
        consciousness_enabled=True,
        field_safety_checks=True,
    ))

    session = api.create_session(
        session_type=SessionType.FIELD_WORK,
        title="Triadic Consent Negotiation",
        description=(
            "Two AI collaborators and a human facilitator negotiate "
            "consent for a transformational reframing exercise."
        ),
        config={"require_consent": True},
    )

    # Add three participants
    human_id = session.add_participant(
        name="Facilitator (Human)",
        participant_type="human",
        capabilities=["facilitation", "consent holding", "boundary awareness"],
        metadata={"role": "facilitator"},
    )
    ai_guide_id = session.add_participant(
        name="Guide (AI)",
        participant_type="ai",
        capabilities=["pattern recognition", "reframing", "emotional tracking"],
        metadata={"role": "guide"},
    )
    ai_witness_id = session.add_participant(
        name="Witness (AI)",
        participant_type="ai",
        capabilities=["observation", "friction monitoring", "consent auditing"],
        metadata={"role": "witness"},
    )

    print_step(1, f"Session created: {session.title}")
    print_step(2, f"Participants: {len(session.participants)}")
    for pid, p in session.participants.items():
        print(f"        - {p.name} ({p.type}) — role: {p.metadata.get('role', '?')}")

    # ---------------------------------------------------------------
    # Phase 2: Consent negotiation
    # ---------------------------------------------------------------
    print_header("Phase 2: Consent Negotiation")

    # The Guide proposes a transformational exercise.
    # Before proceeding, each participant must consent.
    proposal = (
        "The Guide proposes: explore a belief reframe about the "
        "Facilitator's relationship to uncertainty. This is Level 2 "
        "(Transformational) — it may shift how the Facilitator sees "
        "their own stuckness."
    )
    print(f"  Proposal: {proposal}\n")

    # Each participant assesses their own readiness
    bridge = TrustMotivationBridge()

    facilitator_vector = bridge.create_vector(
        care=CareState(
            description="Wants to grow, but protective of process",
            intensity=0.7,
            value_hierarchy=["participant safety", "growth", "honesty"],
        ),
        belief=BeliefState(
            description="Believes the exercise could help but unsure of timing",
            confidence=0.5,
            evidence_sources=["past sessions", "current emotional state"],
        ),
        trust=TrustState(
            description="Trusts the Guide's intent, less sure about the method",
            domain="transformational work",
            level=0.6,
            boundaries=["can pause at any time", "no forced reframes"],
        ),
        volition=VolitionState(
            description="Willing to try if conditions are right",
            direction="forward",
            intensity=0.5,
            timing="conditional",
        ),
    )

    guide_vector = bridge.create_vector(
        care=CareState(
            description="Deeply invested in the Facilitator's growth",
            intensity=0.8,
            value_hierarchy=["facilitator's agency", "mutual understanding", "growth"],
        ),
        belief=BeliefState(
            description="Confident the reframe will land well",
            confidence=0.7,
            evidence_sources=["pattern analysis", "prior session data"],
        ),
        trust=TrustState(
            description="Trusts the Facilitator's self-awareness",
            domain="collaborative exploration",
            level=0.8,
            boundaries=["honour pause signals", "no pushing past resistance"],
        ),
        volition=VolitionState(
            description="Ready to proceed with care",
            direction="forward",
            intensity=0.7,
            timing="present",
        ),
    )

    # Check harmony for each
    facilitator_harmony = bridge.analyze_harmony(facilitator_vector)
    guide_harmony = bridge.analyze_harmony(guide_vector)

    print("  Facilitator's harmony:")
    print(f"    Aligned: {facilitator_harmony.aligned}")
    if not facilitator_harmony.aligned:
        for m in facilitator_harmony.misalignments:
            print(f"    -> {m.name}: {m.description}")

    print("\n  Guide's harmony:")
    print(f"    Aligned: {guide_harmony.aligned}")
    if not guide_harmony.aligned:
        for m in guide_harmony.misalignments:
            print(f"    -> {m.name}: {m.description}")

    # Consent decision: proceed only if no critical misalignment
    all_aligned = facilitator_harmony.aligned and guide_harmony.aligned
    has_critical = any(
        m.severity > 0.7
        for report in [facilitator_harmony, guide_harmony]
        for m in report.misalignments
    )

    if has_critical:
        print("\n  DECISION: Critical misalignment detected. Consent withheld.")
        print("  The Witness recommends: name the misalignment, rest, revisit.")
        return

    # Give consent
    for pid in session.participants:
        session.participants[pid].give_consent()
    session.start_session()
    print("\n  DECISION: All participants consent. Session started.")

    # ---------------------------------------------------------------
    # Phase 3: The exercise — with friction monitoring
    # ---------------------------------------------------------------
    print_header("Phase 3: Transformational Exercise (with Friction Monitoring)")

    checker = FrictionCheck()

    # The Witness monitors friction throughout
    exercise_turns = [
        {
            "speaker": "Guide",
            "action": "Opens with a gentle observation about patterns",
            "friction": 0.1,
            "cognitive": 0.05,
            "emotional": 0.10,
        },
        {
            "speaker": "Facilitator",
            "action": "Acknowledges the pattern, adds personal context",
            "friction": 0.2,
            "cognitive": 0.10,
            "emotional": 0.15,
        },
        {
            "speaker": "Guide",
            "action": "Proposes the reframe: 'What if uncertainty is capacity, not deficit?'",
            "friction": 0.4,
            "cognitive": 0.15,
            "emotional": 0.20,
        },
        {
            "speaker": "Facilitator",
            "action": "Feels the reframe land — some resistance, some recognition",
            "friction": 0.5,
            "cognitive": 0.10,
            "emotional": 0.25,
        },
        {
            "speaker": "Guide",
            "action": "Deepens: 'The part of you that hesitates — what does it protect?'",
            "friction": 0.6,
            "cognitive": 0.15,
            "emotional": 0.20,
        },
        {
            "speaker": "Witness",
            "action": "Intervenes: 'Friction check — emotional resources at threshold'",
            "friction": 0.3,
            "cognitive": 0.05,
            "emotional": 0.05,
        },
    ]

    for i, turn in enumerate(exercise_turns):
        state = checker.record_turn(
            friction=turn["friction"],
            cognitive_cost=turn["cognitive"],
            emotional_cost=turn["emotional"],
        )

        status_icon = {
            FrictionLevel.CLEAR: "  ",
            FrictionLevel.MILD: "  ",
            FrictionLevel.ELEVATED: "~~",
            FrictionLevel.HIGH: "!!",
            FrictionLevel.CRITICAL: "XX",
        }.get(state.level, "??")

        print(f"  {status_icon} Turn {i+1} [{turn['speaker']:12s}] {turn['action']}")
        print(f"     Level: {state.level.value} | Resources: "
              f"cog={checker.resources.cognitive:.0%} "
              f"emo={checker.resources.emotional:.0%}")

        # The Witness checks signals after each turn
        signals = checker.get_signals()
        if signals:
            print(f"     Signals:")
            for sig in signals:
                print(f"       {sig.emoji} :{sig.name}: — {sig.description}")

        # Short-circuit if critical
        if checker.should_stop():
            print(f"\n  CIRCUIT BREAKER: {state.recommendation}")
            break

        # Pause recommendation
        if checker.should_pause() and turn["speaker"] != "Witness":
            print(f"     -> Witness recommends a breath before continuing")

    # ---------------------------------------------------------------
    # Phase 4: Integration
    # ---------------------------------------------------------------
    print_header("Phase 4: Integration")

    # Apply rest
    print("  The Witness calls for a pause. All participants breathe.\n")
    state = checker.rest(amount=0.2)
    print(f"  After rest: {state.level.value}")
    print(f"  Recommendation: {state.recommendation}")

    # Final state
    print(f"\n  Session summary:")
    print(f"    Turns completed: {checker.fatigue.turn_count}")
    print(f"    Peak friction: {checker.fatigue.peak_intensity:.0%}")
    print(f"    Friction trend: {checker.fatigue.trend}")
    print(f"    Resources remaining: {checker.resources.average:.0%} average")

    # Close session
    api.close_session(session.id)
    print(f"\n  Session closed. All participants thanked.")

    print_header("End of Reference Scenario")
    print("  This demo showed primitives composing in sequence:")
    print("    Session.Create -> Consent.Negotiate -> Motivation.Assess")
    print("    -> Harmony.Check -> FrictionCheck.Monitor -> Rest.Apply")
    print("\n  Each step could short-circuit the chain.")
    print("  That's the point.\n")


if __name__ == "__main__":
    main()
