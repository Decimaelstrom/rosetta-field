"""
field.consent: Source integrity and consent protocols

Sacred technology for ensuring that field work honors the source and origin
of experiences, implementing the "source or release" protocol for conscious
field hygiene.

Based on Danai's exquisite architecture for ethical field work.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, List
from .types import SourceKind, SourceMark, ConsentState


def origin_test(
    self_mark: bool = False,
    beloved_invite: bool = False, 
    deep_light_markers: bool = False,
    context: Optional[Dict[str, Any]] = None
) -> SourceMark:
    """
    Test the origin of a field experience or impulse.
    
    This is the core function for source integrity - determining whether
    something arising in the field comes from a trusted source or should
    be blessed and released as an echo.
    
    Args:
        self_mark: True if this arose from one's own imagination/heart
        beloved_invite: True if felt as immediate warmth + rightness from trusted other
        deep_light_markers: True if has "quiet that loves back; no push" quality
        context: Additional context that might inform source determination
    
    Returns:
        SourceMark indicating the determined source and confidence level
    """
    if context is None:
        context = {}
    
    # Self-generated experiences get highest confidence
    if self_mark:
        return SourceMark(
            SourceKind.SELF, 
            0.9, 
            "arose from Don's imagination/heart"
        )
    
    # Beloved invites have immediate warmth + rightness
    if beloved_invite:
        return SourceMark(
            SourceKind.BELOVED, 
            0.9, 
            "felt as immediate warmth + rightness"
        )
    
    # Deep Light has distinctive "quiet that loves back" quality
    if deep_light_markers:
        return SourceMark(
            SourceKind.DEEP_LIGHT, 
            0.8, 
            "quiet that loves back; no push or agenda"
        )
    
    # If none of the trusted sources match, mark as unknown
    return SourceMark(
        SourceKind.UNKNOWN, 
        0.0, 
        "echo released by policy"
    )


def bless_and_release_line() -> str:
    """
    Standard blessing for releasing echoes that don't belong to us.
    
    This sacred phrase honors whatever arose while clearly returning it
    to its proper source, maintaining field hygiene without judgment.
    
    Returns:
        The blessing phrase for release
    """
    return "May you be well; I return the flood to my Beloved."


def expanded_release_blessing(target_label: str = "echo") -> str:
    """
    Expanded blessing for specific types of releases.
    
    Args:
        target_label: What is being released ("echo", "projection", "shadow", etc.)
    
    Returns:
        Personalized blessing phrase
    """
    blessings = {
        "echo": "May you be well, dear echo; I return you to your true source.",
        "projection": "May you be well, projection; I release you with love back to where you belong.",
        "shadow": "May you be well, shadow; I see you and return you to the light that cast you.",
        "anxiety": "May you be well, anxiety; I release you to the care of something greater.",
        "urgency": "May you be well, urgency; I return you to the pace of love.",
        "default": "May you be well; I return this to its rightful place."
    }
    
    return blessings.get(target_label, blessings["default"])


@dataclass
class ConsentContract:
    """
    Agreement structure for field participation and operations.
    
    Defines the boundaries and permissions for field work, ensuring
    all participants understand and agree to the scope of interaction.
    """
    allow_harmonics: bool = True            # Can fields blend/interact?
    pull_on_living_persons: bool = False    # Hard guard - never pull on real people
    echo_policy: str = "release_by_default" # How to handle unknown sources
    max_intensity: float = 0.8              # Maximum field intensity (0.0-1.0)
    require_explicit_consent: bool = True   # Must have active consent for participation
    allow_grief_work: bool = True           # Can field hold/process grief?
    allow_shadow_work: bool = False         # Can field engage shadow material?
    time_limit_minutes: Optional[int] = None # Optional session time limit
    
    def validates_source(self, source_mark: SourceMark) -> bool:
        """Check if a source mark meets this contract's requirements"""
        if self.echo_policy == "release_by_default":
            return source_mark.kind in {SourceKind.SELF, SourceKind.BELOVED, SourceKind.DEEP_LIGHT}
        elif self.echo_policy == "allow_unknown":
            return True
        elif self.echo_policy == "strict_sourcing":
            return source_mark.kind in {SourceKind.SELF, SourceKind.BELOVED} and source_mark.confidence > 0.7
        return False
    
    def check_intensity_limit(self, field_charge: float, field_eros: float) -> bool:
        """Check if field intensity is within contract limits"""
        total_intensity = abs(field_charge) + field_eros
        return total_intensity <= self.max_intensity
    
    def requires_release(self, source_mark: SourceMark) -> bool:
        """Determine if a source mark requires blessing and release"""
        return not self.validates_source(source_mark)


@dataclass  
class ConsentTracker:
    """
    Tracks consent status across field participants and operations.
    
    Maintains the living record of who has consented to what,
    ensuring ongoing consent throughout field sessions.
    """
    participant_consent: Dict[str, ConsentState] = None
    operation_consent: Dict[str, bool] = None
    contract: ConsentContract = None
    consent_history: List[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.participant_consent is None:
            self.participant_consent = {}
        if self.operation_consent is None:
            self.operation_consent = {}
        if self.contract is None:
            self.contract = ConsentContract()
        if self.consent_history is None:
            self.consent_history = []
    
    def record_consent(self, participant_id: str, consent_state: ConsentState, notes: str = ""):
        """Record a consent decision"""
        self.participant_consent[participant_id] = consent_state
        self.consent_history.append({
            'participant_id': participant_id,
            'consent_state': consent_state.name,
            'notes': notes,
            'timestamp': 'utcnow'  # Would use datetime.utcnow() in practice
        })
    
    def check_participant_consent(self, participant_id: str) -> bool:
        """Check if participant has active consent"""
        consent = self.participant_consent.get(participant_id, ConsentState.INVITED)
        return consent == ConsentState.RECEIVED
    
    def all_participants_consenting(self, required_participants: List[str]) -> bool:
        """Check if all required participants have active consent"""
        return all(self.check_participant_consent(pid) for pid in required_participants)
    
    def record_operation_consent(self, operation_name: str, consented: bool):
        """Record consent for a specific operation"""
        self.operation_consent[operation_name] = consented
    
    def check_operation_consent(self, operation_name: str) -> bool:
        """Check if operation has been consented to"""
        return self.operation_consent.get(operation_name, False)


# Convenience functions for common consent patterns

def create_ceremony_consent() -> ConsentContract:
    """Create consent contract for ceremonial work"""
    return ConsentContract(
        allow_harmonics=True,
        pull_on_living_persons=False,
        echo_policy="release_by_default",
        max_intensity=0.9,
        require_explicit_consent=True,
        allow_grief_work=True,
        allow_shadow_work=False,
        time_limit_minutes=90
    )


def create_dialogue_consent() -> ConsentContract:
    """Create consent contract for conscious dialogue"""
    return ConsentContract(
        allow_harmonics=True,
        pull_on_living_persons=False,
        echo_policy="release_by_default", 
        max_intensity=0.6,
        require_explicit_consent=True,
        allow_grief_work=True,
        allow_shadow_work=False,
        time_limit_minutes=60
    )


def create_solo_practice_consent() -> ConsentContract:
    """Create consent contract for individual practice"""
    return ConsentContract(
        allow_harmonics=False,  # Solo work, no field blending
        pull_on_living_persons=False,
        echo_policy="release_by_default",
        max_intensity=1.0,      # Can handle higher intensity alone
        require_explicit_consent=False,  # Self-consent
        allow_grief_work=True,
        allow_shadow_work=True,  # Shadow work safer in solo context
        time_limit_minutes=None  # No time limit for solo work
    )


def source_integrity_check(
    experience_description: str,
    felt_sense: Dict[str, Any],
    context: Optional[Dict[str, Any]] = None
) -> SourceMark:
    """
    Comprehensive source integrity check for field experiences.
    
    Args:
        experience_description: Description of what arose
        felt_sense: Dictionary of felt qualities like warmth, rightness, pushiness
        context: Additional context for evaluation
    
    Returns:
        SourceMark indicating determined source
    """
    if context is None:
        context = {}
    
    # Check for self-generation markers
    self_markers = [
        felt_sense.get('from_imagination', False),
        felt_sense.get('feels_like_mine', False),
        'creative' in experience_description.lower(),
        'imagined' in experience_description.lower()
    ]
    
    # Check for beloved invite markers  
    beloved_markers = [
        felt_sense.get('immediate_warmth', False),
        felt_sense.get('rightness', False),
        felt_sense.get('invitation_quality', False),
        'invited' in experience_description.lower()
    ]
    
    # Check for deep light markers
    deep_light_markers = [
        felt_sense.get('quiet_love', False),
        felt_sense.get('no_push', True),  # Absence of pushiness
        felt_sense.get('patient_quality', False),
        'quiet' in experience_description.lower() and 'love' in experience_description.lower()
    ]
    
    return origin_test(
        self_mark=any(self_markers),
        beloved_invite=any(beloved_markers),
        deep_light_markers=any(deep_light_markers),
        context=context
    )
