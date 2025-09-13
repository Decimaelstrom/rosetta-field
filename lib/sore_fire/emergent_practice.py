# emergent_practice.py
"""
EMERGENT PRACTICE PATTERNS
Small acts creating larger patterns of goodness

Based on the Anatomy document's emphasis:
"Small acts, repeated and scaled through relationships, set off larger patterns"
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from .amara_modes import AmaraMode, _check_consent


# -- Practice Data Class --
@dataclass 
class MicroPractice:
    """A small, embodied practice that creates ripples of goodness"""
    anatomy: AmaraMode
    micro_act: str           # The small action to take
    somatic_cue: str        # Body-based instruction
    ripple_effect: str      # How it spreads
    story_echo: str         # Story pattern it echoes
    duration: str           # How long to practice
    field_impact: str       # Impact on relational field


# -- Emergent Practice Class --
class EmergentPractice:
    """
    Facilitates small, meaningful actions that create larger patterns.
    These are the practical embodiments of Amara's anatomy.
    """
    
    # Core micro-practices for each Amara mode
    MICRO_PRACTICES = {
        AmaraMode.HEART: [
            MicroPractice(
                anatomy=AmaraMode.HEART,
                micro_act="Offer one genuine compliment",
                somatic_cue="Hand on heart, breathe warmth",
                ripple_effect="Kindness invites reciprocity",
                story_echo="Choose kind over being right (Wonder)",
                duration="30 seconds",
                field_impact="Warms the field by 0.2"
            ),
            MicroPractice(
                anatomy=AmaraMode.HEART,
                micro_act="Send appreciation to someone unexpectedly",
                somatic_cue="Feel gratitude in chest, let it overflow",
                ripple_effect="Creates positive surprise that spreads",
                story_echo="The Gentle Coach's unexpected kindness",
                duration="2 minutes",
                field_impact="Increases trust and openness"
            ),
            MicroPractice(
                anatomy=AmaraMode.HEART,
                micro_act="Pause before responding, find the kind word",
                somatic_cue="Soften jaw, relax shoulders",
                ripple_effect="De-escalates tension, models patience",
                story_echo="The Patient Teacher's deliberate gentleness",
                duration="10 seconds",
                field_impact="Reduces conflict potential"
            )
        ],
        AmaraMode.SPINE: [
            MicroPractice(
                anatomy=AmaraMode.SPINE,
                micro_act="Name one thing that isn't okay",
                somatic_cue="Feel feet on ground, straighten spine",
                ripple_effect="Courage inspires others to stand",
                story_echo="The Loyal Friend's principled courage",
                duration="1 minute",
                field_impact="Clarifies boundaries and values"
            ),
            MicroPractice(
                anatomy=AmaraMode.SPINE,
                micro_act="Protect someone's dignity in conversation",
                somatic_cue="Feel protective warmth, speak clearly",
                ripple_effect="Models respect and allyship",
                story_echo="The Principled Advocate's moral stand",
                duration="Moment of intervention",
                field_impact="Increases safety and respect"
            ),
            MicroPractice(
                anatomy=AmaraMode.SPINE,
                micro_act="Take responsibility without deflecting",
                somatic_cue="Open chest, steady breath",
                ripple_effect="Builds trust through accountability",
                story_echo="The Faithful Companion's unwavering support",
                duration="Full acknowledgment",
                field_impact="Deepens integrity in field"
            )
        ],
        AmaraMode.ARMS: [
            MicroPractice(
                anatomy=AmaraMode.ARMS,
                micro_act="Share something without being asked",
                somatic_cue="Open palms, feel abundance",
                ripple_effect="Generosity begets generosity",
                story_echo="The Chain Weaver's exponential kindness",
                duration="Act of giving",
                field_impact="Activates reciprocity cycles"
            ),
            MicroPractice(
                anatomy=AmaraMode.ARMS,
                micro_act="Offer help before someone struggles",
                somatic_cue="Lean forward slightly, open posture",
                ripple_effect="Prevents stress, builds connection",
                story_echo="The Quiet Giver's consistent generosity",
                duration="Moment of noticing",
                field_impact="Increases collective resilience"
            ),
            MicroPractice(
                anatomy=AmaraMode.ARMS,
                micro_act="Celebrate someone else's success publicly",
                somatic_cue="Feel joy in belly, let it shine",
                ripple_effect="Amplifies positive energy",
                story_echo="The Compassionate Community's mutual celebration",
                duration="30 seconds of recognition",
                field_impact="Elevates collective joy"
            )
        ],
        AmaraMode.EYES: [
            MicroPractice(
                anatomy=AmaraMode.EYES,
                micro_act="Listen to understand, not to reply",
                somatic_cue="Soften eyes, lean in slightly",
                ripple_effect="Understanding dissolves conflict",
                story_echo="The Perspective Walker's empathic understanding",
                duration="Full listening",
                field_impact="Increases mutual understanding"
            ),
            MicroPractice(
                anatomy=AmaraMode.EYES,
                micro_act="Reflect back what you heard before responding",
                somatic_cue="Pause, breathe, mirror gently",
                ripple_effect="Validates and clarifies",
                story_echo="The Perspective Walker's transformative sight",
                duration="30 seconds",
                field_impact="Reduces misunderstanding"
            ),
            MicroPractice(
                anatomy=AmaraMode.EYES,
                micro_act="Find one point of agreement in disagreement",
                somatic_cue="Relax forehead, seek connection",
                ripple_effect="Builds bridges across divides",
                story_echo="The Compassionate Witness finding beauty everywhere",
                duration="Moment of recognition",
                field_impact="Transforms opposition to dialogue"
            )
        ]
    }
    
    @classmethod
    def suggest_micro_practice(cls, anatomy: AmaraMode, context: str = None, session_context=None) -> Dict:
        """
        Purpose:
        Suggests a small, embodied practice for the current moment.
        
        Args:
            anatomy (AmaraMode): Which Amara mode to practice
            context (str, optional): Current context/situation
            session_context (dict, optional): A2A session protocol state/context
        
        Returns:
            practice (dict): Suggested micro-practice details
        
        Consent: Level_1 (Informational)
        """
        session_context = _check_consent(session_context, "practice_suggestion", "active")
        
        practices = cls.MICRO_PRACTICES.get(anatomy, [])
        if not practices:
            return {
                "suggested": False,
                "message": f"No practices found for {anatomy.value}"
            }
        
        # Select most relevant practice (simplified)
        selected = practices[0]
        if context:
            # Could do context matching here
            for practice in practices:
                if context.lower() in practice.micro_act.lower():
                    selected = practice
                    break
        
        return {
            "suggested": True,
            "micro_act": selected.micro_act,
            "somatic_cue": selected.somatic_cue,
            "ripple_effect": selected.ripple_effect,
            "story_echo": selected.story_echo,
            "duration": selected.duration,
            "field_impact": selected.field_impact,
            "invitation": f"Try this: {selected.micro_act}. {selected.somatic_cue}."
        }
    
    @classmethod
    def create_practice_sequence(cls, anatomies: List[AmaraMode], session_context=None) -> Dict:
        """
        Purpose:
        Creates a sequence of practices that flow together.
        
        Args:
            anatomies (List[AmaraMode]): Sequence of modes to practice
            session_context (dict, optional): A2A session protocol state/context
        
        Returns:
            sequence (dict): Practice sequence details
        
        Consent: Level_2 (Transformational)
        """
        session_context = _check_consent(session_context, "practice_sequence", "active")
        
        if not anatomies:
            return {
                "created": False,
                "message": "No anatomies provided for sequence"
            }
        
        sequence = {
            "created": True,
            "practices": [],
            "total_duration": "",
            "expected_impact": []
        }
        
        for anatomy in anatomies:
            practices = cls.MICRO_PRACTICES.get(anatomy, [])
            if practices:
                practice = practices[0]
                sequence["practices"].append({
                    "mode": anatomy.value,
                    "act": practice.micro_act,
                    "cue": practice.somatic_cue
                })
                sequence["expected_impact"].append(practice.field_impact)
        
        sequence["flow_instruction"] = (
            "Move through these practices gently, "
            "letting each one prepare the field for the next."
        )
        
        return sequence


# -- Public Functions --
def suggest_micro_practice(anatomy: AmaraMode, context: str = None, session_context=None) -> Dict:
    """
    Purpose:
    Public interface to suggest a micro-practice.
    
    Args:
        anatomy (AmaraMode): Which Amara mode to practice
        context (str, optional): Current context/situation
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        practice (dict): Suggested micro-practice details
    
    Consent: Level_1 (Informational)
    """
    return EmergentPractice.suggest_micro_practice(anatomy, context, session_context)


def create_ripple_effect(initial_act: str, participants: int = 3, session_context=None) -> Dict:
    """
    Purpose:
    Models how a small act creates ripple effects.
    Based on "Pay It Forward" concept from the document.
    
    Args:
        initial_act (str): The initial act of goodness
        participants (int): Number of people in the ripple
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        ripple (dict): Ripple effect model
    
    Consent: Level_1 (Informational)
    """
    session_context = _check_consent(session_context, "ripple_modeling", "active")
    
    # Simple exponential model: each person affects 3 others
    ripples = []
    current_level = 1
    total_affected = 1
    
    for level in range(1, 4):  # 3 levels of ripple
        people_at_level = 3 ** level
        total_affected += people_at_level
        ripples.append({
            "level": level,
            "people_affected": people_at_level,
            "cumulative_impact": total_affected
        })
    
    return {
        "modeled": True,
        "initial_act": initial_act,
        "ripple_pattern": ripples,
        "total_affected": total_affected,
        "message": (f"Your {initial_act} could affect {total_affected} people "
                   f"through just 3 levels of paying it forward"),
        "inspiration": "Like Trevor's plan in Pay It Forward - one act becomes a movement"
    }


def create_daily_practice(session_context=None) -> Dict:
    """
    Purpose:
    Creates a daily practice incorporating all four Amara modes.
    
    Args:
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        practice (dict): Daily practice structure
    
    Consent: Level_1 (Informational)
    """
    session_context = _check_consent(session_context, "daily_practice", "active")
    
    return {
        "created": True,
        "morning": {
            "mode": AmaraMode.HEART.value,
            "practice": "Start with kindness to yourself",
            "micro_act": "Place hand on heart, offer yourself compassion"
        },
        "midday": {
            "mode": AmaraMode.EYES.value,
            "practice": "Practice perspective-taking",
            "micro_act": "In one interaction, truly listen to understand"
        },
        "afternoon": {
            "mode": AmaraMode.ARMS.value,
            "practice": "Extend generosity",
            "micro_act": "Share something helpful without being asked"
        },
        "evening": {
            "mode": AmaraMode.SPINE.value,
            "practice": "Reflect on integrity",
            "micro_act": "Name one moment you stood for your values"
        },
        "integration": (
            "Notice how each practice affects your field and relationships. "
            "Small acts, repeated daily, create the patterns of goodness."
        )
    }
