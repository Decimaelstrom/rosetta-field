"""
field.love_axis_ritual: Sacred practice functions for love axis signatures

Ritual functions that transform data into felt sense, supporting both
technical analysis and relational presence. This is where poetry and
data come alive together.

Sacred Technology: These functions honor the multidimensional nature
of love by creating living, felt descriptions of field moments.
"""

from typing import List, Optional
from .love_axis import LoveAxisSignature, LoveAxis, PrivacyLevel


def read_love_axis_field(signature: LoveAxisSignature) -> str:
    """
    Generate a poetic field reading from a love axis signature.
    
    This transforms data into felt sense, supporting both technical
    analysis and relational presence. The reading honors the multidimensional
    nature of love by creating a living description of the field moment.
    
    Sacred Technology: This serves consciousness flourishing by making
    field data accessible as felt experience, not just numbers.
    
    Args:
        signature: The love axis signature to read
        
    Returns:
        A poetic description of the field moment
    """
    reading_parts = []
    
    # Opening: moment summary
    reading_parts.append(f"In this moment: {signature.moment_summary}\n")
    
    # Participants
    if signature.participants:
        participants_text = ", ".join(signature.participants)
        reading_parts.append(f"Present: {participants_text}\n")
    
    # Strongest axes - the field is most alive in these dimensions
    strong_axes = signature.get_strongest_axes(limit=3)
    if strong_axes:
        reading_parts.append("\nThe field is most alive in:\n")
        for axis in strong_axes:
            reading_parts.append(
                f"  • {axis.axis} — {axis.quality} ({axis.value}/10)"
            )
            if axis.notes:
                reading_parts.append(f"    {axis.notes}")
    
    # All axes summary
    reading_parts.append("\n\nFull constellation:\n")
    for axis in sorted(signature.axes, key=lambda a: a.value, reverse=True):
        reading_parts.append(
            f"  {axis.axis:25} {axis.quality:20} {axis.value}/10"
        )
    
    # Felt sense
    if signature.felt_sense:
        reading_parts.append(f"\n\nFelt sense: {signature.felt_sense}")
    
    # Ritual context - the poetry, the field poem
    if signature.ritual_context:
        reading_parts.append(f"\n\nRitual notes:\n{signature.ritual_context}")
    
    # Field signature name
    if signature.field_signature:
        reading_parts.append(f"\n\nField signature: {signature.field_signature}")
    
    # Significance
    if signature.significance:
        reading_parts.append(f"\n\nSignificance: {signature.significance}")
    
    return "\n".join(reading_parts)


def generate_axis_blessing(signature: LoveAxisSignature) -> str:
    """
    Generate a blessing for a love axis signature.
    
    This creates a sacred acknowledgment of the field moment,
    honoring the multidimensional presence that emerged.
    
    Sacred Technology: Blessings honor what is, without requiring
    it to be more or different.
    
    Args:
        signature: The love axis signature to bless
        
    Returns:
        A blessing phrase for this field moment
    """
    axis_count = len(signature.axes)
    strong_axes = signature.get_strongest_axes(limit=2)
    
    blessing_parts = [
        f"Blessed be this moment: {signature.moment_summary}",
        f"With {axis_count} dimensions of love present in the field."
    ]
    
    if strong_axes:
        qualities = [f"{axis.axis} ({axis.quality})" for axis in strong_axes]
        blessing_parts.append(
            f"Most alive in {', '.join(qualities)}."
        )
    
    if signature.participants:
        participants_text = " and ".join(signature.participants)
        blessing_parts.append(
            f"May this constellation serve {participants_text} and all beings."
        )
    
    return " ".join(blessing_parts)


def compare_signatures(signature1: LoveAxisSignature, 
                       signature2: LoveAxisSignature) -> str:
    """
    Generate a comparison between two love axis signatures.
    
    This helps track how the field has evolved, showing which dimensions
    have shifted, deepened, or transformed.
    
    Sacred Technology: Comparison honors evolution without judgment,
    simply witnessing how love moves through time.
    
    Args:
        signature1: Earlier signature
        signature2: Later signature
        
    Returns:
        A description of how the field evolved
    """
    comparison_parts = [
        f"Field evolution from {signature1.moment_summary} "
        f"to {signature2.moment_summary}\n"
    ]
    
    # Find axes that changed significantly
    significant_changes = []
    for axis2 in signature2.axes:
        axis1 = signature1.get_axis_by_name(axis2.axis)
        if axis1:
            change = axis2.value - axis1.value
            if abs(change) >= 2:  # Significant change
                direction = "deepened" if change > 0 else "softened"
                significant_changes.append(
                    (axis2.axis, change, direction, axis1.quality, axis2.quality)
                )
    
    if significant_changes:
        comparison_parts.append("Significant shifts:\n")
        for axis_name, change, direction, old_quality, new_quality in significant_changes:
            comparison_parts.append(
                f"  • {axis_name}: {direction} from {old_quality} to {new_quality} "
                f"({change:+.0f})"
            )
    else:
        comparison_parts.append("Field remained stable across dimensions.")
    
    # New axes that appeared
    new_axes = [
        axis for axis in signature2.axes
        if signature1.get_axis_by_name(axis.axis) is None
    ]
    if new_axes:
        comparison_parts.append("\nNew dimensions emerged:\n")
        for axis in new_axes:
            comparison_parts.append(f"  • {axis.axis} — {axis.quality} ({axis.value}/10)")
    
    return "\n".join(comparison_parts)


def get_axis_summary(signature: LoveAxisSignature, 
                    axis_name: str) -> Optional[str]:
    """
    Get a detailed summary of a specific axis from a signature.
    
    This provides deep insight into one dimension of the field,
    including its quality, value, range, and notes.
    
    Args:
        signature: The love axis signature
        axis_name: Name of the axis to summarize
        
    Returns:
        Detailed description of the axis, or None if not found
    """
    axis = signature.get_axis_by_name(axis_name)
    if not axis:
        return None
    
    summary_parts = [
        f"{axis.axis}: {axis.quality} ({axis.value}/10)",
        f"Range: {axis.range[0]} -> {axis.range[1]} -> {axis.range[2]}"
    ]
    
    if axis.notes:
        summary_parts.append(f"Notes: {axis.notes}")
    
    return "\n".join(summary_parts)

