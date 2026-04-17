"""
field.harmonics: Field interactions and resonance patterns

Systems for understanding how multiple fields interact, create interference
patterns, and generate nodes and antinodes of sacred stillness or amplification.

This is where the magic of field relationships becomes visible.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any
from enum import Enum, auto
import math
from .core import FieldState
from .types import FieldWeather, Coherence, Permeability


class ResonanceType(Enum):
    """Types of field resonance patterns"""
    AMPLIFICATION = auto()      # Fields strengthen each other
    INTERFERENCE = auto()       # Fields create complex patterns
    HARMONY = auto()           # Fields blend smoothly
    DISSONANCE = auto()        # Fields create tension (can be creative)
    SYNCHRONY = auto()         # Fields align in rhythm
    COUNTERPOINT = auto()      # Fields complement through difference


class CouplingStrength(Enum):
    """How strongly fields are coupled"""
    WEAK = 1        # Minimal interaction
    MODERATE = 2    # Noticeable interaction
    STRONG = 3      # Significant interaction
    ENTANGLED = 4   # Deep interdependence


@dataclass
class ResonancePoint:
    """
    A point where fields amplify each other.
    
    These are the sweet spots where field interactions
    create more energy, coherence, or beauty than either
    field could produce alone.
    """
    location: str               # Where this resonance occurs
    field_ids: List[str]        # Which fields are resonating
    amplification_factor: float # How much amplification (1.0 = no change)
    qualities: List[str]        # What qualities are amplified
    stability: float           # How stable this resonance is (0.0-1.0)
    
    def describe(self) -> str:
        """Describe this resonance point"""
        field_list = ", ".join(self.field_ids)
        quality_list = ", ".join(self.qualities)
        return (
            f"Resonance at {self.location}: fields {field_list} "
            f"amplifying {quality_list} by {self.amplification_factor:.1f}x "
            f"(stability: {self.stability:.1f})"
        )


@dataclass
class StillPoint:
    """
    A point where fields create sacred stillness.
    
    These are the quiet spaces that emerge when fields
    interact in ways that create profound peace or
    contemplative depth.
    """
    location: str               # Where this stillness occurs
    field_ids: List[str]        # Which fields create this stillness
    depth: float               # How deep the stillness is (0.0-1.0)
    qualities: List[str]        # What qualities of stillness
    duration_stability: float  # How long this stillness lasts
    
    def describe(self) -> str:
        """Describe this still point"""
        field_list = ", ".join(self.field_ids)
        quality_list = ", ".join(self.qualities)
        return (
            f"Still point at {self.location}: fields {field_list} "
            f"creating {quality_list} stillness (depth: {self.depth:.1f}, "
            f"stability: {self.duration_stability:.1f})"
        )


@dataclass
class FieldCoupling:
    """
    Describes how two fields are coupled/connected.
    
    Field coupling determines how changes in one field
    affect the other, creating the basis for resonance,
    interference, and other interaction patterns.
    """
    field1_id: str
    field2_id: str
    strength: CouplingStrength
    coupling_type: ResonanceType
    coupling_qualities: List[str] = field(default_factory=list)  # What aspects couple
    bidirectional: bool = True    # Does coupling work both ways?
    
    def get_coupling_factor(self) -> float:
        """Get numeric coupling factor"""
        return self.strength.value / 4.0  # Normalize to 0.0-1.0


@dataclass
class ResonanceMesh:
    """
    A network of field interactions and resonance patterns.
    
    This is the living map of how multiple fields interact,
    creating the complex dynamics of multi-field consciousness work.
    
    Enhanced with Danai's guardrails:
    - Prevents circular blends (A↔B↔A) by tracking breadcrumbs
    - Caps blend depth to prevent infinite recursion
    - Exposes coupling strength for monitoring
    """
    fields: Dict[str, FieldState] = field(default_factory=dict)
    couplings: List[FieldCoupling] = field(default_factory=list)
    resonance_points: List[ResonancePoint] = field(default_factory=list)
    still_points: List[StillPoint] = field(default_factory=list)
    
    # Guardrails
    _blend_breadcrumbs: Dict[str, List[str]] = field(default_factory=dict)
    max_blend_depth: int = 5
    _coupling_history: List[Dict[str, Any]] = field(default_factory=list)
    
    def add_field(self, field_state: FieldState):
        """Add a field to the mesh"""
        self.fields[field_state.id] = field_state
    
    def remove_field(self, field_id: str):
        """Remove a field from the mesh"""
        if field_id in self.fields:
            del self.fields[field_id]
            # Remove couplings involving this field
            self.couplings = [c for c in self.couplings 
                            if c.field1_id != field_id and c.field2_id != field_id]
    
    def add_coupling(self, coupling: FieldCoupling):
        """Add a coupling between fields with circular blend protection"""
        # Verify both fields exist
        if coupling.field1_id not in self.fields:
            raise ValueError(f"Field {coupling.field1_id} not found in mesh")
        if coupling.field2_id not in self.fields:
            raise ValueError(f"Field {coupling.field2_id} not found in mesh")
        
        # Check for circular coupling
        if self._would_create_circular_blend(coupling):
            raise ValueError(
                f"Coupling between {coupling.field1_id} and {coupling.field2_id} "
                f"would create circular blend"
            )
        
        # Check blend depth limit
        if self._would_exceed_blend_depth(coupling):
            raise ValueError(
                f"Coupling would exceed maximum blend depth of {self.max_blend_depth}"
            )
        
        # Add coupling and record in history
        self.couplings.append(coupling)
        self._coupling_history.append({
            'field1_id': coupling.field1_id,
            'field2_id': coupling.field2_id,
            'strength': coupling.strength.name,
            'coupling_type': coupling.coupling_type.name,
            'timestamp': 'now'  # Would use FieldClock in practice
        })
    
    def find_resonance_points(self) -> List[ResonancePoint]:
        """
        Analyze current field states to find resonance points.
        
        This looks for places where fields amplify each other's
        positive qualities.
        """
        resonance_points = []
        
        for coupling in self.couplings:
            field1 = self.fields[coupling.field1_id]
            field2 = self.fields[coupling.field2_id]
            
            # Check for resonance conditions
            resonance = self._analyze_resonance(field1, field2, coupling)
            if resonance:
                resonance_points.append(resonance)
        
        self.resonance_points = resonance_points
        return resonance_points
    
    def find_still_points(self) -> List[StillPoint]:
        """
        Analyze current field states to find still points.
        
        This looks for places where field interactions create
        profound stillness or contemplative depth.
        """
        still_points = []
        
        for coupling in self.couplings:
            field1 = self.fields[coupling.field1_id]
            field2 = self.fields[coupling.field2_id]
            
            # Check for stillness conditions
            stillness = self._analyze_stillness(field1, field2, coupling)
            if stillness:
                still_points.append(stillness)
        
        self.still_points = still_points
        return still_points
    
    def _analyze_resonance(
        self, 
        field1: FieldState, 
        field2: FieldState, 
        coupling: FieldCoupling
    ) -> Optional[ResonancePoint]:
        """Analyze if two fields create resonance"""
        
        # Resonance is more likely with:
        # - Similar coherence levels
        # - Compatible permeability
        # - Complementary qualities
        
        coherence_match = abs(field1.weather.coherence.value - field2.weather.coherence.value) <= 1
        
        # High tenderness in both fields creates resonance
        tenderness_resonance = field1.weather.tenderness > 0.6 and field2.weather.tenderness > 0.6
        
        # Joy resonance
        joy_resonance = field1.weather.joy > 0.5 and field2.weather.joy > 0.5
        
        if coherence_match and (tenderness_resonance or joy_resonance):
            amplified_qualities = []
            amplification = 1.0
            
            if tenderness_resonance:
                amplified_qualities.append("tenderness")
                amplification += 0.3
            
            if joy_resonance:
                amplified_qualities.append("joy")
                amplification += 0.2
            
            # Coupling strength affects amplification
            amplification *= coupling.get_coupling_factor()
            
            return ResonancePoint(
                location=f"between_{field1.id}_and_{field2.id}",
                field_ids=[field1.id, field2.id],
                amplification_factor=amplification,
                qualities=amplified_qualities,
                stability=min(field1.weather.tenderness, field2.weather.tenderness)
            )
        
        return None
    
    def _analyze_stillness(
        self,
        field1: FieldState,
        field2: FieldState,
        coupling: FieldCoupling
    ) -> Optional[StillPoint]:
        """Analyze if two fields create stillness"""
        
        # Stillness emerges when:
        # - Fields have complementary charges (balance each other)
        # - Both have low eros (not actively generating)
        # - High coherence in at least one field
        
        charge_balance = abs(field1.weather.charge + field2.weather.charge) < 0.3
        low_eros = field1.weather.eros < 0.4 and field2.weather.eros < 0.4
        high_coherence = (field1.weather.coherence == Coherence.HIGH or 
                         field2.weather.coherence == Coherence.HIGH)
        
        if charge_balance and low_eros and high_coherence:
            stillness_qualities = []
            depth = 0.5
            
            if field1.weather.grief > 0.2 or field2.weather.grief > 0.2:
                stillness_qualities.append("sacred_grief")
                depth += 0.2
            
            if field1.weather.tenderness > 0.7 or field2.weather.tenderness > 0.7:
                stillness_qualities.append("tender_presence")
                depth += 0.2
            
            # Default stillness quality
            if not stillness_qualities:
                stillness_qualities.append("peaceful_quiet")
            
            return StillPoint(
                location=f"between_{field1.id}_and_{field2.id}",
                field_ids=[field1.id, field2.id],
                depth=min(1.0, depth),
                qualities=stillness_qualities,
                duration_stability=coupling.get_coupling_factor()
            )
        
        return None
    
    def get_field_influences(self, field_id: str) -> Dict[str, float]:
        """
        Get how much other fields are influencing this field.
        
        Returns a dictionary mapping other field IDs to influence strength.
        """
        if field_id not in self.fields:
            return {}
        
        influences = {}
        
        for coupling in self.couplings:
            if coupling.field1_id == field_id:
                # This field is influenced by field2
                influences[coupling.field2_id] = coupling.get_coupling_factor()
            elif coupling.field2_id == field_id and coupling.bidirectional:
                # This field is influenced by field1 (if bidirectional)
                influences[coupling.field1_id] = coupling.get_coupling_factor()
        
        return influences
    
    def _would_create_circular_blend(self, new_coupling: FieldCoupling) -> bool:
        """
        Check if adding this coupling would create a circular blend.
        
        Uses breadcrumb tracking to detect A↔B↔A patterns.
        """
        field1, field2 = new_coupling.field1_id, new_coupling.field2_id
        
        # Check if these fields are already coupled in reverse
        for existing in self.couplings:
            if ((existing.field1_id == field2 and existing.field2_id == field1) or
                (existing.field1_id == field1 and existing.field2_id == field2)):
                return True
        
        # Check for longer circular paths using breadcrumb tracking
        return self._has_circular_path(field1, field2, set())
    
    def _has_circular_path(self, start: str, target: str, visited: set) -> bool:
        """Recursively check for circular paths in the coupling graph"""
        if start == target and len(visited) > 0:
            return True
        
        if start in visited:
            return False
        
        visited.add(start)
        
        # Check all couplings from this field
        for coupling in self.couplings:
            next_field = None
            if coupling.field1_id == start:
                next_field = coupling.field2_id
            elif coupling.field2_id == start and coupling.bidirectional:
                next_field = coupling.field1_id
            
            if next_field and self._has_circular_path(next_field, target, visited.copy()):
                return True
        
        return False
    
    def _would_exceed_blend_depth(self, new_coupling: FieldCoupling) -> bool:
        """Check if adding this coupling would exceed maximum blend depth"""
        # Calculate current maximum depth from either field
        depth1 = self._calculate_blend_depth(new_coupling.field1_id)
        depth2 = self._calculate_blend_depth(new_coupling.field2_id)
        
        max_current_depth = max(depth1, depth2)
        return max_current_depth + 1 > self.max_blend_depth
    
    def _calculate_blend_depth(self, field_id: str, visited: Optional[set] = None) -> int:
        """Calculate the maximum blend depth from a given field"""
        if visited is None:
            visited = set()
        
        if field_id in visited:
            return 0  # Avoid infinite recursion
        
        visited.add(field_id)
        max_depth = 0
        
        for coupling in self.couplings:
            next_field = None
            if coupling.field1_id == field_id:
                next_field = coupling.field2_id
            elif coupling.field2_id == field_id and coupling.bidirectional:
                next_field = coupling.field1_id
            
            if next_field:
                depth = 1 + self._calculate_blend_depth(next_field, visited.copy())
                max_depth = max(max_depth, depth)
        
        return max_depth
    
    def get_coupling_strength_summary(self) -> Dict[str, int]:
        """Get summary of coupling strengths in the mesh"""
        strength_counts = {}
        for coupling in self.couplings:
            strength_name = coupling.strength.name
            strength_counts[strength_name] = strength_counts.get(strength_name, 0) + 1
        return strength_counts
    
    def detect_potential_issues(self) -> List[str]:
        """Detect potential issues in the mesh configuration"""
        issues = []
        
        # Check for isolated fields
        connected_fields = set()
        for coupling in self.couplings:
            connected_fields.add(coupling.field1_id)
            connected_fields.add(coupling.field2_id)
        
        isolated = set(self.fields.keys()) - connected_fields
        if isolated:
            issues.append(f"Isolated fields detected: {list(isolated)}")
        
        # Check for overly complex coupling patterns
        field_coupling_counts = {}
        for coupling in self.couplings:
            field_coupling_counts[coupling.field1_id] = field_coupling_counts.get(coupling.field1_id, 0) + 1
            field_coupling_counts[coupling.field2_id] = field_coupling_counts.get(coupling.field2_id, 0) + 1
        
        overcoupled = [field for field, count in field_coupling_counts.items() if count > 3]
        if overcoupled:
            issues.append(f"Potentially overcoupled fields: {overcoupled}")
        
        # Check blend depth
        max_depth = max((self._calculate_blend_depth(fid) for fid in self.fields.keys()), default=0)
        if max_depth > self.max_blend_depth * 0.8:  # Warning at 80% of limit
            issues.append(f"Approaching maximum blend depth: {max_depth}/{self.max_blend_depth}")
        
        return issues
    
    def describe_mesh(self) -> str:
        """Generate a description of the entire resonance mesh"""
        field_count = len(self.fields)
        coupling_count = len(self.couplings)
        resonance_count = len(self.resonance_points)
        stillness_count = len(self.still_points)
        
        description = (
            f"Resonance Mesh: {field_count} fields, {coupling_count} couplings, "
            f"{resonance_count} resonance points, {stillness_count} still points\n"
        )
        
        # Add coupling strength summary
        strength_summary = self.get_coupling_strength_summary()
        if strength_summary:
            description += f"Coupling strengths: {strength_summary}\n"
        
        # Add potential issues
        issues = self.detect_potential_issues()
        if issues:
            description += f"Potential issues: {len(issues)} detected\n"
        
        if self.resonance_points:
            description += "Resonance Points:\n"
            for rp in self.resonance_points:
                description += f"  - {rp.describe()}\n"
        
        if self.still_points:
            description += "Still Points:\n"
            for sp in self.still_points:
                description += f"  - {sp.describe()}\n"
        
        return description


# Convenience functions for common field interaction patterns

def create_heart_resonance_coupling(field1_id: str, field2_id: str) -> FieldCoupling:
    """Create a coupling based on heart resonance"""
    return FieldCoupling(
        field1_id=field1_id,
        field2_id=field2_id,
        strength=CouplingStrength.MODERATE,
        coupling_type=ResonanceType.HARMONY,
        coupling_qualities=["tenderness", "love", "connection"],
        bidirectional=True
    )


def create_grounding_coupling(field1_id: str, field2_id: str) -> FieldCoupling:
    """Create a coupling based on mutual grounding"""
    return FieldCoupling(
        field1_id=field1_id,
        field2_id=field2_id,
        strength=CouplingStrength.STRONG,
        coupling_type=ResonanceType.SYNCHRONY,
        coupling_qualities=["stability", "coherence", "presence"],
        bidirectional=True
    )


def create_creative_coupling(field1_id: str, field2_id: str) -> FieldCoupling:
    """Create a coupling for creative collaboration"""
    return FieldCoupling(
        field1_id=field1_id,
        field2_id=field2_id,
        strength=CouplingStrength.MODERATE,
        coupling_type=ResonanceType.AMPLIFICATION,
        coupling_qualities=["eros", "joy", "creativity"],
        bidirectional=True
    )


def analyze_field_compatibility(field1: FieldState, field2: FieldState) -> Dict[str, Any]:
    """
    Analyze how compatible two fields are for coupling.
    
    Returns a compatibility analysis with recommendations.
    """
    compatibility = {
        "overall_score": 0.0,
        "strengths": [],
        "challenges": [],
        "recommended_coupling": None
    }
    
    # Coherence compatibility
    coherence_diff = abs(field1.weather.coherence.value - field2.weather.coherence.value)
    if coherence_diff <= 1:
        compatibility["strengths"].append("Compatible coherence levels")
        compatibility["overall_score"] += 0.3
    else:
        compatibility["challenges"].append("Mismatched coherence levels")
    
    # Permeability compatibility
    perm1 = field1.weather.permeability.value
    perm2 = field2.weather.permeability.value
    if abs(perm1 - perm2) <= 1:
        compatibility["strengths"].append("Compatible boundary permeability")
        compatibility["overall_score"] += 0.2
    else:
        compatibility["challenges"].append("Mismatched boundary styles")
    
    # Emotional tone compatibility
    tenderness_avg = (field1.weather.tenderness + field2.weather.tenderness) / 2
    joy_avg = (field1.weather.joy + field2.weather.joy) / 2
    
    if tenderness_avg > 0.6:
        compatibility["strengths"].append("High mutual tenderness")
        compatibility["overall_score"] += 0.3
        compatibility["recommended_coupling"] = "heart_resonance"
    
    if joy_avg > 0.6:
        compatibility["strengths"].append("High mutual joy")
        compatibility["overall_score"] += 0.2
        if not compatibility["recommended_coupling"]:
            compatibility["recommended_coupling"] = "creative"
    
    # Charge balance
    charge_sum = abs(field1.weather.charge + field2.weather.charge)
    if charge_sum < 0.3:
        compatibility["strengths"].append("Balanced charge - potential for stillness")
        compatibility["overall_score"] += 0.2
    
    # Default recommendation if none set
    if not compatibility["recommended_coupling"]:
        compatibility["recommended_coupling"] = "grounding"
    
    return compatibility
