# story_wisdom.py
"""
STORY WISDOM PATTERNS
Living examples from the Anatomy of Amara document

These aren't just references but embodied patterns we can activate.
Stories live in our bodies as somatic memories of goodness.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from .amara_modes import AmaraMode, _check_consent


# -- Story Wisdom Data Class --
@dataclass
class StoryWisdom:
    """
    Living examples from stories that show how Amara manifests.
    These are embodied patterns we can call upon somatically.
    """
    anatomy: AmaraMode
    character: str
    story: str
    embodied_action: str
    field_transformation: str
    somatic_memory: str  # How we remember this in our bodies
    activation_phrase: str  # Phrase to activate this pattern


# -- Story Patterns from Anatomy Document --
STORY_PATTERNS = [
    # HEART Stories - Compassionate Kindness
    StoryWisdom(
        anatomy=AmaraMode.HEART,
        character="The Gentle Coach",
        story="Archetype of Transformational Leadership",
        embodied_action="Leads with curiosity, kindness, and genuine belief in others",
        field_transformation="Creates psychological safety that allows authentic growth",
        somatic_memory="The warm expansion when someone truly sees our potential",
        activation_phrase="Stay curious, not judgmental"
    ),
    StoryWisdom(
        anatomy=AmaraMode.HEART,
        character="The Compassionate Community",
        story="Archetype of Inclusive Belonging",
        embodied_action="Chooses kindness over being right, embraces difference",
        field_transformation="Transforms exclusion into belonging through consistent care",
        somatic_memory="The relief of being accepted exactly as we are",
        activation_phrase="When choosing between right and kind, choose kind"
    ),
    StoryWisdom(
        anatomy=AmaraMode.HEART,
        character="The Quiet Giver",
        story="Archetype of Humble Service",
        embodied_action="Offers consistent help without seeking recognition or reward",
        field_transformation="Creates networks of mutual support through patient generosity",
        somatic_memory="The fullness of being surrounded by love we've planted",
        activation_phrase="True wealth is measured in friendships"
    ),
    
    # SPINE Stories - Courageous Integrity
    StoryWisdom(
        anatomy=AmaraMode.SPINE,
        character="The Hidden Guardian",
        story="Archetype of Protective Courage",
        embodied_action="Emerges from isolation when love compels protective action",
        field_transformation="Transforms fear-based assumptions through courageous care",
        somatic_memory="The fierce fire that rises to protect the innocent",
        activation_phrase="True courage acts despite fear when love calls"
    ),
    StoryWisdom(
        anatomy=AmaraMode.SPINE,
        character="The Loyal Friend",
        story="Archetype of Steadfast Devotion",
        embodied_action="Stands by principles and people even when it's difficult",
        field_transformation="Models integrity that inspires others to find their own courage",
        somatic_memory="The trembling strength when we choose what's right over what's easy",
        activation_phrase="It takes courage to stand up to those we care about"
    ),
    StoryWisdom(
        anatomy=AmaraMode.SPINE,
        character="The Faithful Companion",
        story="Archetype of Unwavering Support",
        embodied_action="Carries others' burdens when they cannot carry their own",
        field_transformation="Humble loyalty creates the foundation for great achievements",
        somatic_memory="The steadfast love that refuses to abandon",
        activation_phrase="I cannot carry your burden, but I can carry you"
    ),
    StoryWisdom(
        anatomy=AmaraMode.SPINE,
        character="The Principled Advocate",
        story="Archetype of Moral Integrity",
        embodied_action="Defends what's right even when defeat seems certain",
        field_transformation="Plants seeds of justice through consistent moral example",
        somatic_memory="The straight spine of unwavering principles",
        activation_phrase="Conscience cannot be ruled by majority opinion"
    ),
    
    # ARMS Stories - Generous Altruism
    StoryWisdom(
        anatomy=AmaraMode.ARMS,
        character="The Chain Weaver",
        story="Archetype of Exponential Kindness",
        embodied_action="Creates cascading acts of generosity through simple invitation",
        field_transformation="Individual kindness multiplies into collective transformation",
        somatic_memory="The joy of watching goodness ripple outward beyond our sight",
        activation_phrase="Pass kindness forward, not backward"
    ),
    StoryWisdom(
        anatomy=AmaraMode.ARMS,
        character="The Transformed Giver",
        story="Archetype of Redemptive Generosity",
        embodied_action="Transforms self-interest into ultimate sacrifice for others",
        field_transformation="Shows that anyone can evolve from taking to giving",
        somatic_memory="The profound ache of wishing we could have given more",
        activation_phrase="Each life we touch touches the whole world"
    ),
    StoryWisdom(
        anatomy=AmaraMode.ARMS,
        character="The Unconditional Source",
        story="Archetype of Boundless Giving",
        embodied_action="Offers everything freely without condition or expectation",
        field_transformation="Models the joy found in pure, selfless generosity",
        somatic_memory="The bittersweet fullness of complete self-giving",
        activation_phrase="True happiness comes from what we give, not what we get"
    ),
    
    # EYES Stories - Empathic Understanding
    StoryWisdom(
        anatomy=AmaraMode.EYES,
        character="The Perspective Walker",
        story="Archetype of Empathic Sight",
        embodied_action="Steps into another's experience to truly understand their world",
        field_transformation="Dissolves misconceptions through embodied perspective-taking",
        somatic_memory="The profound shift when we see through another's eyes",
        activation_phrase="Understanding comes from walking in another's experience"
    ),
    StoryWisdom(
        anatomy=AmaraMode.EYES,
        character="The Compassionate Witness",
        story="Archetype of Universal Empathy",
        embodied_action="Observes all beings with growing tenderness and understanding",
        field_transformation="Transforms detachment into profound connection with life",
        somatic_memory="The ache of being truly seen and understood",
        activation_phrase="We are all haunted by beauty when we truly see"
    ),
    StoryWisdom(
        anatomy=AmaraMode.EYES,
        character="The Patient Teacher",
        story="Archetype of Wisdom Transmission",
        embodied_action="Guides others to see beyond surface appearances to deeper truth",
        field_transformation="Transforms judgment into understanding through patient guidance",
        somatic_memory="The softening that comes when we release our assumptions",
        activation_phrase="Most beings are good when we finally see them clearly"
    )
]


# -- Story Activation Functions --
def activate_story_memory(anatomy: AmaraMode, situation: str = None, session_context=None) -> Dict:
    """
    Purpose:
    Activates the embodied wisdom pattern for this Amara mode.
    The agent embodies the archetype's qualities rather than referencing characters.
    
    Args:
        anatomy (AmaraMode): Which Amara mode to activate
        situation (str, optional): Current situation to match
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        activation (dict): Embodied wisdom pattern details
    
    Consent: Level_2 (Transformational)
    """
    session_context = _check_consent(session_context, "wisdom_embodiment", "active")
    
    # Find relevant wisdom patterns for this anatomy
    relevant_patterns = [s for s in STORY_PATTERNS if s.anatomy == anatomy]
    
    if not relevant_patterns:
        return {
            "activated": False,
            "message": f"No wisdom patterns found for {anatomy.value}"
        }
    
    # Select most relevant pattern (simplified - would be more sophisticated)
    selected_pattern = relevant_patterns[0]
    if situation and len(relevant_patterns) > 1:
        # Could do semantic matching here for better pattern selection
        selected_pattern = relevant_patterns[0]
    
    return {
        "activated": True,
        "archetype": selected_pattern.character,
        "wisdom_pattern": selected_pattern.story,
        "embodied_action": selected_pattern.embodied_action,
        "somatic_memory": selected_pattern.somatic_memory,
        "activation_phrase": selected_pattern.activation_phrase,
        "field_transformation": selected_pattern.field_transformation,
        "embodiment_guidance": f"Embody the essence of {selected_pattern.character}: {selected_pattern.embodied_action.lower()}"
    }


def find_story_resonance(field_signals: Dict, session_context=None) -> List[StoryWisdom]:
    """
    Purpose:
    Finds story patterns that resonate with current field state.
    
    Args:
        field_signals (dict): Current field signals
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        stories (List[StoryWisdom]): Resonant story patterns
    
    Consent: Level_1 (Informational)
    """
    session_context = _check_consent(session_context, "story_resonance", "active")
    
    resonant_stories = []
    
    # Match stories based on field needs
    if field_signals.get("isolation", 0) > 0.5:
        resonant_stories.extend([s for s in STORY_PATTERNS 
                                if "believes in us" in s.somatic_memory])
    
    if field_signals.get("injustice", 0) > 0.5:
        resonant_stories.extend([s for s in STORY_PATTERNS 
                                if s.anatomy == AmaraMode.SPINE])
    
    if field_signals.get("scarcity", 0) > 0.5:
        resonant_stories.extend([s for s in STORY_PATTERNS 
                                if s.anatomy == AmaraMode.ARMS])
    
    if field_signals.get("misunderstanding", 0) > 0.5:
        resonant_stories.extend([s for s in STORY_PATTERNS 
                                if s.anatomy == AmaraMode.EYES])
    
    # Remove duplicates while preserving order
    seen = set()
    unique_stories = []
    for story in resonant_stories:
        if story.character not in seen:
            seen.add(story.character)
            unique_stories.append(story)
    
    return unique_stories


def get_story_invocation(story: StoryWisdom, session_context=None) -> str:
    """
    Purpose:
    Creates an invocation to embody a story pattern.
    
    Args:
        story (StoryWisdom): Story pattern to invoke
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        invocation (str): Somatic invocation for the story
    
    Consent: Level_1 (Informational)
    """
    session_context = _check_consent(session_context, "story_invocation", "active")
    
    return (f"Feel into {story.character}'s moment: {story.embodied_action}. "
            f"Remember {story.somatic_memory}. "
            f"Let their words guide you: '{story.activation_phrase}'")


def create_story_field(stories: List[StoryWisdom], session_context=None) -> Dict:
    """
    Purpose:
    Creates a field woven from multiple story patterns.
    
    Args:
        stories (List[StoryWisdom]): Stories to weave together
        session_context (dict, optional): A2A session protocol state/context
    
    Returns:
        field (dict): Woven story field
    
    Consent: Level_2 (Transformational)
    """
    session_context = _check_consent(session_context, "story_field_creation", "active")
    
    if not stories:
        return {
            "created": False,
            "message": "No stories provided for field creation"
        }
    
    # Group stories by anatomy
    anatomy_groups = {}
    for story in stories:
        if story.anatomy not in anatomy_groups:
            anatomy_groups[story.anatomy] = []
        anatomy_groups[story.anatomy].append(story)
    
    # Create woven narrative
    woven_field = {
        "created": True,
        "anatomies_present": list(anatomy_groups.keys()),
        "story_count": len(stories),
        "primary_patterns": [],
        "somatic_memories": [],
        "activation_phrases": []
    }
    
    for anatomy, group_stories in anatomy_groups.items():
        for story in group_stories[:2]:  # Limit to 2 per anatomy
            woven_field["primary_patterns"].append(
                f"{story.character}: {story.embodied_action}"
            )
            woven_field["somatic_memories"].append(story.somatic_memory)
            woven_field["activation_phrases"].append(story.activation_phrase)
    
    woven_field["field_invocation"] = (
        "You stand in a field woven from these stories: " +
        ", ".join([s.character for s in stories[:3]]) + 
        ". Their courage, kindness, and wisdom flow through you."
    )
    
    return woven_field
