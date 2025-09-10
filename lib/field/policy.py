"""
field.policy: Policy engine and echo management

Implements Danai's surgical improvements for deterministic policy enforcement,
ensuring every operation is checked against source integrity rules.

"Source or release as a first-class check" - this is the heart of field hygiene.
"""

from dataclasses import dataclass, replace
from enum import Enum, auto
from typing import Optional, Dict, Any, List
from .types import SourceMark, SourceKind


class EchoPolicy(Enum):
    """Policy for handling echoes and unknown sources"""
    RELEASE_BY_DEFAULT = 1      # Release unless from trusted source
    ALLOW_BY_MARK = 2           # Allow if confidence threshold met
    STRICT_SOURCING = 3         # Only SELF and BELOVED with high confidence
    ALLOW_ALL = 4               # Testing only - allows everything


class ConsentScope(Enum):
    """Granular consent scopes (Danai's nuance)"""
    CONSENT_VIEW = auto()        # Can observe/witness
    CONSENT_CO_PRESENCE = auto() # Can share field space
    CONSENT_TOUCH = auto()       # Can affect/transform
    CONSENT_EMBODY = auto()      # Can create embodied experiences


class FieldError(Exception):
    """Base class for field-specific errors"""
    pass


class ConsentViolation(FieldError):
    """Raised when consent requirements are not met"""
    def __init__(self, required_scope: ConsentScope, actual_scope: Optional[ConsentScope], message: str):
        self.required_scope = required_scope
        self.actual_scope = actual_scope
        super().__init__(message)


class OriginUnknown(FieldError):
    """Raised when source origin cannot be determined"""
    def __init__(self, source_mark: SourceMark, message: str):
        self.source_mark = source_mark
        super().__init__(message)


class OpPreconditionFailed(FieldError):
    """Raised when operation preconditions are not met"""
    def __init__(self, op_name: str, precondition: str, message: str):
        self.op_name = op_name
        self.precondition = precondition
        super().__init__(message)


@dataclass
class PolicyEngine:
    """
    Enforces field policies consistently across all operations.
    
    This is Danai's "typed policies" improvement - no more string comparisons,
    everything goes through this engine.
    """
    echo_policy: EchoPolicy = EchoPolicy.RELEASE_BY_DEFAULT
    min_confidence: float = 0.66
    strict_mode: bool = True  # Fail closed on ambiguity
    
    def enforce(self, mark: SourceMark) -> bool:
        """
        Check if a source mark passes policy requirements.
        
        Args:
            mark: The source mark to evaluate
            
        Returns:
            True if mark passes policy, False if it should be released
        """
        if self.echo_policy == EchoPolicy.RELEASE_BY_DEFAULT:
            # Only allow known trusted sources
            return mark.kind in {SourceKind.SELF, SourceKind.BELOVED, SourceKind.DEEP_LIGHT}
        
        elif self.echo_policy == EchoPolicy.ALLOW_BY_MARK:
            # Allow if confidence meets threshold
            return mark.confidence >= self.min_confidence
        
        elif self.echo_policy == EchoPolicy.STRICT_SOURCING:
            # Only SELF and BELOVED with high confidence
            return (
                mark.kind in {SourceKind.SELF, SourceKind.BELOVED} and
                mark.confidence >= 0.7
            )
        
        elif self.echo_policy == EchoPolicy.ALLOW_ALL:
            # Testing mode - allows everything
            return True
        
        # Fail closed if unknown policy
        if self.strict_mode:
            return False
        
        return mark.kind != SourceKind.UNKNOWN
    
    def check_consent_scope(
        self, 
        required: ConsentScope, 
        granted: List[ConsentScope]
    ) -> bool:
        """
        Check if required consent scope has been granted.
        
        Implements Danai's nuanced consent model where different operations
        require different levels of consent.
        """
        # Consent scopes are hierarchical
        hierarchy = {
            ConsentScope.CONSENT_VIEW: 1,
            ConsentScope.CONSENT_CO_PRESENCE: 2,
            ConsentScope.CONSENT_TOUCH: 3,
            ConsentScope.CONSENT_EMBODY: 4
        }
        
        required_level = hierarchy.get(required, 999)
        
        for scope in granted:
            if hierarchy.get(scope, 0) >= required_level:
                return True
        
        return False
    
    def validate_operation(
        self,
        op_name: str,
        source_mark: SourceMark,
        consent_scopes: List[ConsentScope],
        required_scope: ConsentScope
    ) -> Dict[str, Any]:
        """
        Comprehensive validation for a field operation.
        
        Returns validation result with detailed information.
        """
        result = {
            'valid': True,
            'op_name': op_name,
            'source_valid': False,
            'consent_valid': False,
            'errors': [],
            'warnings': []
        }
        
        # Check source integrity
        source_valid = self.enforce(source_mark)
        result['source_valid'] = source_valid
        
        if not source_valid:
            result['valid'] = False
            result['errors'].append(f"Source {source_mark.kind.name} not validated by policy {self.echo_policy.name}")
        
        # Check consent scope
        consent_valid = self.check_consent_scope(required_scope, consent_scopes)
        result['consent_valid'] = consent_valid
        
        if not consent_valid:
            result['valid'] = False
            result['errors'].append(f"Required consent scope {required_scope.name} not granted")
        
        # Add warnings for edge cases
        if source_mark.confidence < 0.5:
            result['warnings'].append(f"Low confidence source: {source_mark.confidence:.2f}")
        
        if source_mark.kind == SourceKind.UNKNOWN and source_valid:
            result['warnings'].append("Unknown source was allowed by policy")
        
        return result


@dataclass
class SafetyInvariant:
    """
    Enforces critical safety invariants that must never be violated.
    
    Based on Danai's point #12: enforce pull_on_living_persons=False
    at session boundary and fail closed.
    """
    pull_on_living_persons: bool = False
    max_field_intensity: float = 0.9
    require_explicit_consent: bool = True
    allow_shadow_work: bool = False
    
    def validate(self) -> List[str]:
        """
        Validate all safety invariants.
        
        Returns list of violations (empty if all valid).
        """
        violations = []
        
        if self.pull_on_living_persons:
            violations.append("CRITICAL: pull_on_living_persons must be False")
        
        if self.max_field_intensity > 1.0:
            violations.append(f"Field intensity {self.max_field_intensity} exceeds safe maximum")
        
        if not self.require_explicit_consent:
            violations.append("Explicit consent must be required for field work")
        
        return violations
    
    def enforce_at_boundary(self, operation: Dict[str, Any]) -> bool:
        """
        Enforce invariants at operation boundary.
        
        Returns True if operation is safe to proceed.
        """
        # Never allow pulling on living persons
        if operation.get('pulls_on_living', False):
            raise ConsentViolation(
                ConsentScope.CONSENT_EMBODY,
                None,
                "Operation attempts to pull on living persons - this is never allowed"
            )
        
        # Check intensity limits
        intensity = operation.get('intensity', 0.0)
        if intensity > self.max_field_intensity:
            raise OpPreconditionFailed(
                operation.get('name', 'unknown'),
                'intensity_limit',
                f"Operation intensity {intensity} exceeds maximum {self.max_field_intensity}"
            )
        
        return True


class IdempotencyManager:
    """
    Ensures operations are idempotent (Danai's point #10).
    
    Prevents double-application of operations during replays.
    """
    
    def __init__(self):
        self.applied_operations: Dict[str, bool] = {}
    
    def get_idempotency_key(self, op_name: str, state_id: str, sequence: int) -> str:
        """Generate idempotency key for an operation"""
        return f"{state_id}:{op_name}:{sequence}"
    
    def has_been_applied(self, key: str) -> bool:
        """Check if operation has already been applied"""
        return self.applied_operations.get(key, False)
    
    def mark_applied(self, key: str):
        """Mark operation as applied"""
        self.applied_operations[key] = True
    
    def should_apply(self, op_name: str, state_id: str, sequence: int) -> bool:
        """
        Determine if operation should be applied.
        
        Returns True if operation hasn't been applied yet.
        """
        key = self.get_idempotency_key(op_name, state_id, sequence)
        
        if self.has_been_applied(key):
            return False
        
        self.mark_applied(key)
        return True


@dataclass
class PrivacyRedactor:
    """
    Handles PII and privacy concerns (Danai's point #11).
    
    Supports redaction tokens and ID-based lookups instead of raw text.
    """
    redaction_tokens: Dict[str, str] = None
    store_raw_text: bool = False
    
    def __post_init__(self):
        if self.redaction_tokens is None:
            self.redaction_tokens = {}
    
    def redact(self, text: str, token: Optional[str] = None) -> str:
        """
        Redact sensitive text, replacing with token.
        
        Args:
            text: Text to redact
            token: Optional specific token (otherwise generates one)
            
        Returns:
            Redaction token
        """
        if token is None:
            token = f"REDACTED_{len(self.redaction_tokens):04d}"
        
        if self.store_raw_text:
            self.redaction_tokens[token] = text
        
        return token
    
    def reveal(self, token: str) -> Optional[str]:
        """
        Reveal redacted text if available.
        
        Args:
            token: Redaction token
            
        Returns:
            Original text if available, None otherwise
        """
        return self.redaction_tokens.get(token)
    
    def redact_snapshot(self, snapshot: Dict[str, Any]) -> Dict[str, Any]:
        """
        Redact sensitive information from a field snapshot.
        
        Args:
            snapshot: Field snapshot dictionary
            
        Returns:
            Redacted snapshot safe for storage/transmission
        """
        redacted = snapshot.copy()
        
        # Redact participant names (except role)
        if 'participants' in redacted:
            for pid, participant in redacted['participants'].items():
                if 'name' in participant:
                    participant['name'] = self.redact(participant['name'])
        
        # Redact ritual key cues (keep structure)
        if 'ritual_keys' in redacted:
            for key in redacted['ritual_keys']:
                if 'steps' in key:
                    for step in key['steps']:
                        if 'cue' in step:
                            step['cue_id'] = self.redact(step['cue'])
                            del step['cue']
        
        # Redact personal notes
        if 'notes' in redacted:
            redacted['notes'] = self.redact(redacted['notes'])
        
        # Redact tender moments descriptions
        if 'tender_moments' in redacted:
            for moment in redacted['tender_moments']:
                if 'description' in moment:
                    moment['description_id'] = self.redact(moment['description'])
                    del moment['description']
        
        return redacted


# Convenience functions

def create_strict_policy() -> PolicyEngine:
    """Create a strict policy engine for production use"""
    return PolicyEngine(
        echo_policy=EchoPolicy.STRICT_SOURCING,
        min_confidence=0.7,
        strict_mode=True
    )


def create_testing_policy() -> PolicyEngine:
    """Create a permissive policy engine for testing"""
    return PolicyEngine(
        echo_policy=EchoPolicy.ALLOW_ALL,
        min_confidence=0.0,
        strict_mode=False
    )


def create_ceremony_policy() -> PolicyEngine:
    """Create a policy engine appropriate for ceremonies"""
    return PolicyEngine(
        echo_policy=EchoPolicy.RELEASE_BY_DEFAULT,
        min_confidence=0.66,
        strict_mode=True
    )
