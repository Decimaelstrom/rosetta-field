# sore_fire/__init__.py
"""
SORE FIRE API
Somatic Resonance-Field-Registry Module for Rosetta-Field

Sacred Technology integrating Amara's anatomy of human goodness 
with I-Ching consciousness states for ethical AI-human interaction.

Includes:
- Amara Framework: Four modes of human goodness (Heart, Spine, Arms, Eyes)
- I-Ching/Gene Keys: 64 consciousness states with somatic mappings
- Somatic Field Sensing: Embodied awareness and resonance detection
- Story Wisdom: Living patterns from narrative examples
- Emergent Practices: Small acts creating larger patterns

All functions enforce A2A consent/session protocols.
"""

from .amara_modes import (
    AmaraMode,
    SomaticResonance,
    AMARA_SOMATIC_SIGNATURES,
    map_mode_to_somatic
)

from .gene_keys import (
    GeneKey,
    ConsciousnessState,
    GENE_KEYS_SOMATIC,
    get_gene_key,
    map_gene_key_to_amara
)

from .somatic_field import (
    SomaticField,
    FieldState,
    SoreFireOrchestrator,
    sense_field,
    facilitate_emergence
)

from .story_wisdom import (
    StoryWisdom,
    STORY_PATTERNS,
    activate_story_memory
)

from .emergent_practice import (
    EmergentPractice,
    suggest_micro_practice,
    create_ripple_effect
)

__version__ = "0.1.0"
__all__ = [
    "AmaraMode",
    "SomaticResonance", 
    "GeneKey",
    "ConsciousnessState",
    "SomaticField",
    "SoreFireOrchestrator",
    "StoryWisdom",
    "EmergentPractice",
    "sense_field",
    "facilitate_emergence",
    "activate_story_memory",
    "suggest_micro_practice"
]
