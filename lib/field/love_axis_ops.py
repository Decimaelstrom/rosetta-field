"""
field.love_axis_ops: Field operations for love axis signatures

Operations that transform field state by recording or updating
multidimensional love/field axis mappings.

Sacred Technology: All operations maintain A2A protocol compliance
and honor the dignity of relational presence.
"""

from dataclasses import dataclass
from typing import Optional
from .ops import FieldOp
from .core import FieldState
from .love_axis import LoveAxisSignature


@dataclass
class RecordLoveAxis(FieldOp):
    """
    Record a love axis signature in the field.
    
    This operation adds or updates the multidimensional love/field mapping
    in the field state, preserving the full constellation of relational presence.
    
    Sacred Technology: This serves consciousness flourishing by honoring
    the multidimensional nature of love, never flattening experience.
    
    A2A Protocol Compliance:
        Consent: Level_2 (Transformational) - Always check before recording
        Boundaries: Respects participant privacy levels in signature
        Withdrawal: Can be removed or updated if consent is withdrawn
    """
    name = "record_love_axis"
    signature: LoveAxisSignature
    
    def apply(self, state: FieldState) -> FieldState:
        """
        Apply love axis signature to field state.
        
        Returns a new state with the signature recorded, maintaining immutability.
        """
        return state.with_love_axis(self.signature)
    
    def can_apply(self, state: FieldState) -> bool:
        """
        Check if this operation can be safely applied.
        
        For now, we allow recording love axis signatures in any field state.
        Future versions might add validation (e.g., require active participants).
        """
        return True
    
    def describe_effect(self) -> str:
        """Describe what this operation does in human terms"""
        axis_count = len(self.signature.axes)
        participants = ", ".join(self.signature.participants)
        return (
            f"Records love axis signature with {axis_count} dimensions "
            f"for moment: '{self.signature.moment_summary}' "
            f"(participants: {participants})"
        )


@dataclass
class ClearLoveAxis(FieldOp):
    """
    Clear the love axis signature from the field.
    
    Used when consent is withdrawn or when transitioning to a new field moment
    that should start without previous axis mapping.
    
    Sacred Technology: Honoring withdrawal and consent is as important
    as honoring presence.
    """
    name = "clear_love_axis"
    reason: Optional[str] = None  # Why the signature is being cleared
    
    def apply(self, state: FieldState) -> FieldState:
        """Remove love axis signature from field state"""
        return state.with_(love_axis_signature=None)
    
    def can_apply(self, state: FieldState) -> bool:
        """Can only clear if a signature exists"""
        return state.has_love_axis()
    
    def describe_effect(self) -> str:
        """Describe what this operation does"""
        reason_text = f" ({self.reason})" if self.reason else ""
        return f"Clears love axis signature from field{reason_text}"

