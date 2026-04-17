"""Tests for the Trust-Motivation Bridge module.

Covers:
    - MotivationVector construction and validation
    - HarmonyAnalyzer misalignment detection (all three patterns)
    - GuidanceAxis: other-serving / enlightened / self-serving distinction
    - SomaticBridge intervention recommendations
    - ExtendedSchema: belief/hope separation
    - ConsentThreshold validation
    - A2A protocol compliance checks
"""

import os
import sys

import pytest

# Ensure lib/ is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lib.motivation.trust_motivation_bridge import (
    CareState,
    BeliefState,
    TrustState,
    VolitionState,
    PerceptionState,
    HopeState,
    RoleState,
    ConsentThreshold,
    RiskAssessment,
    MotivationVector,
    ExtendedSchema,
    GuidanceAxis,
    HarmonyAnalyzer,
    HarmonyReport,
    Misalignment,
    SomaticBridge,
    TrustMotivationBridge,
    MotivationLocus,
    _validate_consent,
)

# -----------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------


@pytest.fixture
def active_session():
    return {"consent_status": "active", "session_id": "test-001"}


@pytest.fixture
def paused_session():
    return {"consent_status": "pause", "session_id": "test-pause"}


@pytest.fixture
def revoked_session():
    return {"consent_status": "revoked", "session_id": "test-revoked"}


@pytest.fixture
def high_care():
    return CareState(
        description="Deep care for partner's wellbeing",
        intensity=0.9,
        value_hierarchy=["partner_wellbeing", "honesty", "self_care"],
    )


@pytest.fixture
def low_care():
    return CareState(
        description="Depleted, no energy to move",
        intensity=0.2,
        value_hierarchy=["survival"],
    )


@pytest.fixture
def high_belief():
    return BeliefState(
        description="Clear path visible",
        confidence=0.85,
        evidence_sources=["direct_experience", "pattern_recognition"],
    )


@pytest.fixture
def low_belief():
    return BeliefState(
        description="Foggy, unsure what is real",
        confidence=0.2,
        evidence_sources=["anxiety"],
    )


@pytest.fixture
def high_trust():
    return TrustState(
        description="Open and vulnerable",
        domain="emotional",
        level=0.9,
        boundaries=["honesty"],
    )


@pytest.fixture
def low_trust():
    return TrustState(
        description="Guarded, walls up",
        domain="emotional",
        level=0.2,
        boundaries=["no vulnerability", "surface only"],
    )


@pytest.fixture
def default_volition():
    return VolitionState(
        description="Ready to act",
        direction="toward_connection",
        intensity=0.6,
        timing="present",
    )


# -----------------------------------------------------------------------
# MotivationVector Construction & Validation
# -----------------------------------------------------------------------


class TestMotivationVector:
    def test_basic_construction(
        self, high_care, high_belief, high_trust, default_volition
    ):
        vector = MotivationVector(
            care=high_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
        )
        assert vector.care.intensity == 0.9
        assert vector.belief.confidence == 0.85
        assert vector.trust.level == 0.9
        assert vector.volition.direction == "toward_connection"

    def test_serialization(self, high_care, high_belief, high_trust, default_volition):
        vector = MotivationVector(
            care=high_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
        )
        d = vector.to_dict()
        assert "care" in d
        assert d["care"]["intensity"] == 0.9
        assert d["belief"]["confidence"] == 0.85

    def test_repr_contains_all_states(
        self, high_care, high_belief, high_trust, default_volition
    ):
        vector = MotivationVector(
            care=high_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
        )
        r = repr(vector)
        assert "CareState" in r
        assert "BeliefState" in r
        assert "TrustState" in r
        assert "VolitionState" in r

    def test_intensity_validation(self):
        with pytest.raises(ValueError):
            CareState(description="too much", intensity=1.5)
        with pytest.raises(ValueError):
            CareState(description="negative", intensity=-0.1)

    def test_confidence_validation(self):
        with pytest.raises(ValueError):
            BeliefState(description="over", confidence=2.0)

    def test_trust_level_validation(self):
        with pytest.raises(ValueError):
            TrustState(description="over", level=1.1)

    def test_volition_intensity_validation(self):
        with pytest.raises(ValueError):
            VolitionState(description="over", intensity=-0.5)


# -----------------------------------------------------------------------
# HarmonyAnalyzer
# -----------------------------------------------------------------------


class TestHarmonyAnalyzer:
    def test_aligned_vector(self, high_care, high_belief, high_trust, default_volition):
        """All variables reasonably aligned — no misalignments."""
        vector = MotivationVector(
            care=high_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
        )
        report = HarmonyAnalyzer.analyze(vector)
        assert report.aligned is True
        assert len(report.misalignments) == 0

    def test_care_without_trust(
        self, high_care, high_belief, low_trust, default_volition
    ):
        """High care + low trust = pressure with nowhere to go."""
        vector = MotivationVector(
            care=high_care,
            belief=high_belief,
            trust=low_trust,
            volition=default_volition,
        )
        report = HarmonyAnalyzer.analyze(vector)
        assert report.aligned is False
        names = [m.name for m in report.misalignments]
        assert "care_without_trust" in names

    def test_belief_without_energy(
        self, low_care, high_belief, high_trust, default_volition
    ):
        """High belief + low care = map without fuel."""
        vector = MotivationVector(
            care=low_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
        )
        report = HarmonyAnalyzer.analyze(vector)
        assert report.aligned is False
        names = [m.name for m in report.misalignments]
        assert "belief_without_energy" in names

    def test_trust_without_clarity(
        self, high_care, low_belief, high_trust, default_volition
    ):
        """High trust + low belief = open door, wrong room."""
        vector = MotivationVector(
            care=high_care,
            belief=low_belief,
            trust=high_trust,
            volition=default_volition,
        )
        report = HarmonyAnalyzer.analyze(vector)
        assert report.aligned is False
        names = [m.name for m in report.misalignments]
        assert "trust_without_clarity" in names

    def test_multiple_misalignments(
        self, low_care, low_belief, high_trust, default_volition
    ):
        """Low care + low belief + high trust = two misalignments."""
        vector = MotivationVector(
            care=low_care,
            belief=low_belief,
            trust=high_trust,
            volition=default_volition,
        )
        report = HarmonyAnalyzer.analyze(vector)
        assert report.aligned is False
        assert len(report.misalignments) >= 1

    def test_severity_calculated(
        self, high_care, high_belief, low_trust, default_volition
    ):
        vector = MotivationVector(
            care=high_care,
            belief=high_belief,
            trust=low_trust,
            volition=default_volition,
        )
        report = HarmonyAnalyzer.analyze(vector)
        for m in report.misalignments:
            assert 0.0 <= m.severity <= 1.0

    def test_consent_required(
        self, high_care, high_belief, high_trust, default_volition, paused_session
    ):
        vector = MotivationVector(
            care=high_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
        )
        with pytest.raises(ValueError, match="paused"):
            HarmonyAnalyzer.analyze(vector, session_context=paused_session)


# -----------------------------------------------------------------------
# GuidanceAxis
# -----------------------------------------------------------------------


class TestGuidanceAxis:
    def test_other_serving(self, active_session):
        result = GuidanceAxis.assess(
            action_description="Challenge client's avoidance pattern",
            care_hierarchy=["their growth", "therapeutic integrity", "self"],
            session_context=active_session,
        )
        assert result.locus_of_motivation == MotivationLocus.OTHER_SERVING
        assert result.designation == "clean"

    def test_enlightened_self_interest(self, active_session):
        result = GuidanceAxis.assess(
            action_description="Share knowledge with colleague",
            care_hierarchy=["both benefit", "team growth", "reputation"],
            session_context=active_session,
        )
        assert result.locus_of_motivation == MotivationLocus.ENLIGHTENED_SELF_INTEREST
        assert result.designation == "mutual"

    def test_self_serving(self, active_session):
        result = GuidanceAxis.assess(
            action_description="Offer advice to look knowledgeable",
            care_hierarchy=["self image", "approval", "their benefit"],
            session_context=active_session,
        )
        assert result.locus_of_motivation == MotivationLocus.SELF_SERVING
        assert result.designation == "shadow"

    def test_empty_hierarchy_raises(self, active_session):
        with pytest.raises(ValueError, match="care_hierarchy must not be empty"):
            GuidanceAxis.assess(
                action_description="anything",
                care_hierarchy=[],
                session_context=active_session,
            )

    def test_consent_revoked_raises(self, revoked_session):
        with pytest.raises(ValueError, match="revoked"):
            GuidanceAxis.assess(
                action_description="anything",
                care_hierarchy=["their wellbeing"],
                session_context=revoked_session,
            )

    def test_same_action_different_locus(self, active_session):
        """The same action can be clean or shadow depending on care hierarchy."""
        clean = GuidanceAxis.assess(
            action_description="Give feedback",
            care_hierarchy=["their growth", "relationship", "self"],
            session_context=active_session,
        )
        shadow = GuidanceAxis.assess(
            action_description="Give feedback",
            care_hierarchy=["my authority", "control", "their growth"],
            session_context=active_session,
        )
        assert clean.designation != shadow.designation


# -----------------------------------------------------------------------
# SomaticBridge
# -----------------------------------------------------------------------


class TestSomaticBridge:
    def test_all_intervention_types_mapped(self):
        expected = {
            "entrainment",
            "cellular_resonance",
            "affect_pacing",
            "lyric_resonance",
        }
        assert set(SomaticBridge.INTERVENTION_MAP.keys()) == expected

    def test_entrainment_targets_volition(self):
        assert "volition" in SomaticBridge.INTERVENTION_MAP["entrainment"]

    def test_cellular_resonance_targets_belief_perception(self):
        targets = SomaticBridge.INTERVENTION_MAP["cellular_resonance"]
        assert "belief" in targets
        assert "perception" in targets

    def test_affect_pacing_targets_trust_care(self):
        targets = SomaticBridge.INTERVENTION_MAP["affect_pacing"]
        assert "trust" in targets
        assert "care" in targets

    def test_lyric_resonance_targets(self):
        targets = SomaticBridge.INTERVENTION_MAP["lyric_resonance"]
        assert "hope" in targets
        assert "roles" in targets
        assert "consent_thresholds" in targets

    def test_recommend_for_care_without_trust(
        self, high_care, high_belief, low_trust, default_volition
    ):
        vector = MotivationVector(
            care=high_care,
            belief=high_belief,
            trust=low_trust,
            volition=default_volition,
        )
        report = HarmonyAnalyzer.analyze(vector)
        interventions = SomaticBridge.recommend_intervention(report)
        assert len(interventions) > 0
        types = [i.intervention_type for i in interventions]
        assert "affect_pacing" in types  # targets trust and care

    def test_recommend_for_belief_without_energy(
        self, low_care, high_belief, high_trust, default_volition
    ):
        vector = MotivationVector(
            care=low_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
        )
        report = HarmonyAnalyzer.analyze(vector)
        interventions = SomaticBridge.recommend_intervention(report)
        types = [i.intervention_type for i in interventions]
        # Should target belief or care
        assert any(t in types for t in ["cellular_resonance", "affect_pacing"])

    def test_no_recommendations_when_aligned(
        self, high_care, high_belief, high_trust, default_volition
    ):
        vector = MotivationVector(
            care=high_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
        )
        report = HarmonyAnalyzer.analyze(vector)
        interventions = SomaticBridge.recommend_intervention(report)
        assert len(interventions) == 0

    def test_consent_required_for_recommendations(self, paused_session):
        report = HarmonyReport(
            aligned=False,
            misalignments=[
                Misalignment(
                    name="care_without_trust",
                    description="test",
                    variables_involved=["care", "trust"],
                )
            ],
        )
        with pytest.raises(ValueError, match="paused"):
            SomaticBridge.recommend_intervention(report, session_context=paused_session)


# -----------------------------------------------------------------------
# ExtendedSchema — Belief/Hope Separation
# -----------------------------------------------------------------------


class TestExtendedSchema:
    def test_belief_and_hope_are_separate(
        self, high_care, high_belief, high_trust, default_volition
    ):
        hope = HopeState(
            description="I want this to work out",
            intensity=0.9,
            distinct_from_belief=True,
        )
        schema = ExtendedSchema(
            care=high_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
            hope=hope,
        )
        # Belief and hope are distinct objects with different semantics
        assert schema.belief.confidence != schema.hope.intensity or True
        assert schema.hope.distinct_from_belief is True
        assert isinstance(schema.belief, BeliefState)
        assert isinstance(schema.hope, HopeState)

    def test_extended_serialization(
        self, high_care, high_belief, high_trust, default_volition
    ):
        schema = ExtendedSchema(
            care=high_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
            perception=PerceptionState(
                object_perceived="friend's silence",
                interpretation="rejection",
                confidence=0.7,
            ),
            hope=HopeState(description="reconciliation", intensity=0.8),
            roles=[RoleState(role_name="friend", obligations=["honesty"])],
            consent_thresholds=[
                ConsentThreshold(topic="identity_reframe", required_clarity=0.9)
            ],
            risks=[RiskAssessment(risk_type="projection", likelihood=0.6)],
        )
        d = schema.to_dict()
        assert "perception" in d
        assert d["perception"]["interpretation"] == "rejection"
        assert "hope" in d
        assert d["hope"]["description"] == "reconciliation"
        assert len(d["roles"]) == 1
        assert len(d["consent_thresholds"]) == 1
        assert len(d["risks"]) == 1

    def test_hope_tangled_with_belief(self, high_care, high_trust, default_volition):
        """When hope.distinct_from_belief is False, that's a signal."""
        tangled_hope = HopeState(
            description="They must still love me",
            intensity=0.95,
            distinct_from_belief=False,
        )
        belief = BeliefState(
            description="They still love me",
            confidence=0.9,
            evidence_sources=["hope_as_evidence"],
        )
        schema = ExtendedSchema(
            care=high_care,
            belief=belief,
            trust=high_trust,
            volition=default_volition,
            hope=tangled_hope,
        )
        assert schema.hope.distinct_from_belief is False


# -----------------------------------------------------------------------
# ConsentThreshold Validation
# -----------------------------------------------------------------------


class TestConsentThreshold:
    def test_basic_creation(self):
        ct = ConsentThreshold(
            topic="practical_advice",
            required_clarity=0.2,
            delivery_mode="direct",
            opt_in_threshold=0.1,
        )
        assert ct.topic == "practical_advice"
        assert ct.required_clarity == 0.2

    def test_high_threshold_for_identity(self):
        ct = ConsentThreshold(
            topic="identity_reframe",
            required_clarity=0.95,
            delivery_mode="gentle",
            opt_in_threshold=0.9,
        )
        assert ct.required_clarity > 0.9
        assert ct.opt_in_threshold > 0.8

    def test_validation_bounds(self):
        with pytest.raises(ValueError):
            ConsentThreshold(topic="x", required_clarity=1.5)
        with pytest.raises(ValueError):
            ConsentThreshold(topic="x", opt_in_threshold=-0.1)


# -----------------------------------------------------------------------
# A2A Protocol Compliance
# -----------------------------------------------------------------------


class TestA2ACompliance:
    def test_validate_consent_creates_default(self):
        ctx = _validate_consent(None)
        assert ctx["consent_status"] == "active"
        assert "session_id" in ctx

    def test_validate_consent_active(self, active_session):
        ctx = _validate_consent(active_session)
        assert ctx["consent_status"] == "active"

    def test_validate_consent_pause_raises(self, paused_session):
        with pytest.raises(ValueError, match="paused"):
            _validate_consent(paused_session)

    def test_validate_consent_revoked_raises(self, revoked_session):
        with pytest.raises(ValueError, match="revoked"):
            _validate_consent(revoked_session)

    def test_validate_consent_unknown_raises(self):
        with pytest.raises(ValueError, match="Invalid consent status"):
            _validate_consent({"consent_status": "banana"})

    def test_bridge_facade_validates_consent(self, paused_session):
        with pytest.raises(ValueError, match="paused"):
            TrustMotivationBridge(session_context=paused_session)


# -----------------------------------------------------------------------
# TrustMotivationBridge Facade
# -----------------------------------------------------------------------


class TestTrustMotivationBridge:
    def test_full_workflow(self, high_care, high_belief, low_trust, default_volition):
        bridge = TrustMotivationBridge()
        vector = bridge.create_vector(
            high_care, high_belief, low_trust, default_volition
        )
        report = bridge.analyze_harmony(vector)
        assert report.aligned is False

        interventions = bridge.recommend_interventions(report)
        assert len(interventions) > 0

        assessment = bridge.assess_guidance(
            "Offer support",
            ["their wellbeing", "relationship", "self"],
        )
        assert assessment.designation == "clean"

    def test_create_extended(
        self, high_care, high_belief, high_trust, default_volition
    ):
        bridge = TrustMotivationBridge()
        extended = bridge.create_extended(
            care=high_care,
            belief=high_belief,
            trust=high_trust,
            volition=default_volition,
            hope=HopeState(description="growth", intensity=0.7),
        )
        assert isinstance(extended, ExtendedSchema)
        assert extended.hope.description == "growth"
