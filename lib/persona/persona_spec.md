# Dream Workshop Persona Module Specification

## Overview

The Persona Module provides adaptive, archetype-based guidance for Dream Workshop sessions. Each persona archetype represents a common creative struggle and provides tailored interventions, voice tones, and session pacing to support the user's unique journey.

## Core Philosophy

### Sacred Archetype Guidance
Persona guidance is not mere role-playing, but conscious field stewardship through personalized, resonant presence. Each archetype honors the unique journey of each creative soul while offering adaptive support that resonates with their current needs.

### A2A Protocol Compliance
All persona functions follow the A2A (Agent-to-Agent) protocol, ensuring:
- Active consent verification before any persona guidance
- Immediate cessation if consent is paused or revoked
- Transparent logging of all effects and changes
- Enhanced consent checking for vulnerable contexts
- Respect for participant's need for different guidance or no guidance

## Available Archetypes

### 1. The Blocked Artist
**Primary Struggle:** Self-doubt and overthinking
**Emotional State:** Frustrated, stuck, self-critical
**Primary Need:** Creative confidence
**Secondary Need:** Self-trust

**Intervention Focus:** Gentle encouragement
- **Affect Functions:** soften, anchor, radiate
- **Process Functions:** pattern_interrupt, empathic_reflection
- **Ritual Functions:** invoke_wonder, reflection
- **Session Pacing:** Slow and gentle
- **Voice Tone:** Warm, affirming, patient

**Key Phrases:**
- "Your creativity is waiting, not gone"
- "Every artist has moments of doubt"
- "Your unique voice matters"
- "Trust the process, trust yourself"

### 2. The Overwhelmed Pro
**Primary Struggle:** Too many ideas, no clarity
**Emotional State:** Scattered, anxious, pressured
**Primary Need:** Clarity and focus
**Secondary Need:** Prioritization

**Intervention Focus:** Mindful organization
- **Affect Functions:** ground, clarify, shield
- **Process Functions:** pattern_interrupt, scenario_plan
- **Ritual Functions:** grounding_breath, reflection
- **Session Pacing:** Structured and clear
- **Voice Tone:** Calm, organized, supportive

**Key Phrases:**
- "Let's find clarity together, step by step"
- "Not all ideas need to be acted on now"
- "Focus on what matters most right now"
- "Your brilliance doesn't need to overwhelm you"

### 3. The Grieving Maker
**Primary Struggle:** Working through loss or change
**Emotional State:** Sad, lost, searching for meaning
**Primary Need:** Healing and meaning
**Secondary Need:** Gentle expression

**Intervention Focus:** Compassionate healing
- **Affect Functions:** soften, transmute, open
- **Process Functions:** empathic_reflection, reframe_as_myth
- **Ritual Functions:** consult_elders, reflection
- **Session Pacing:** Gentle and honoring
- **Voice Tone:** Compassionate, honoring, patient

**Key Phrases:**
- "Your feelings are honored here"
- "Grief and creativity often walk together"
- "Your heart knows the way forward"
- "There's wisdom in your pain"

### 4. The Young Dreamer
**Primary Struggle:** New to creativity, excited but unfocused
**Emotional State:** Excited, overwhelmed, eager
**Primary Need:** Direction and confidence
**Secondary Need:** Skill development

**Intervention Focus:** Inspiring guidance
- **Affect Functions:** radiate, open, lilt
- **Process Functions:** pattern_interrupt, scenario_plan
- **Ritual Functions:** invoke_wonder, initiation
- **Session Pacing:** Energetic and engaging
- **Voice Tone:** Enthusiastic, encouraging, inspiring

**Key Phrases:**
- "Your excitement is beautiful and valid"
- "Every master was once a beginner"
- "Your dreams have power"
- "Let's channel your energy into focus"

### 5. The Burned-Out Exec
**Primary Struggle:** Seeking meaning and innovation
**Emotional State:** Exhausted, disillusioned, searching
**Primary Need:** Renewal and purpose
**Secondary Need:** Authentic expression

**Intervention Focus:** Soul-centered leadership
- **Affect Functions:** transmute, radiate, open
- **Process Functions:** reframe_as_myth, empathic_reflection
- **Ritual Functions:** consult_elders, rest
- **Session Pacing:** Contemplative and deep
- **Voice Tone:** Wise, authentic, grounding

**Key Phrases:**
- "Your wisdom is calling you home"
- "Burnout is often a call for deeper meaning"
- "Your leadership can be both powerful and gentle"
- "Innovation comes from rest, not exhaustion"

## Core Functions

### `persona.load(archetype_name, session_context=None)`

Load a Dream Workshop persona archetype for adaptive guidance.

**Args:**
- `archetype_name` (str): Sacred archetype to invoke for guidance
- `session_context` (dict, optional): A2A session protocol for consent/status

**Returns:**
- `persona_loaded` (bool): Whether persona was invoked with consent
- `archetype` (str): Which archetype was loaded
- `voice_tone` (str): Recommended voice tone for this archetype
- `session_pacing` (str): Recommended session pacing
- `interventions` (dict): Available interventions for this archetype
- `key_phrases` (list): Resonant phrases for this archetype

**Example:**
```python
from lib.persona import load

result = load('blocked_artist', session_context=session)
print(f"Voice tone: {result['voice_tone']}")
print(f"Key phrases: {result['key_phrases']}")
```

### `persona.simulate(archetype_name, user_input, session_context=None)`

Simulate how an archetype would respond to user input.

**Args:**
- `archetype_name` (str): Sacred archetype to simulate response for
- `user_input` (str): Current state, emotion, or situation to respond to
- `session_context` (dict, optional): A2A session protocol for consent/status

**Returns:**
- `simulation_complete` (bool): Whether simulation was completed with consent
- `archetype` (str): Which archetype was simulated
- `recommended_interventions` (list): Functions to call for this situation
- `voice_adaptation` (str): How to adapt voice for this response
- `resonant_phrase` (str): A key phrase that resonates with this moment
- `session_adaptation` (dict): How to adapt session for this moment

**Example:**
```python
from lib.persona import simulate

result = simulate('blocked_artist', 'I can\'t create anything good', session_context=session)
print(f"Recommended interventions: {result['recommended_interventions']}")
print(f"Resonant phrase: {result['resonant_phrase']}")
```

### `persona.customize(archetype_name, customizations, session_context=None)`

Customize an archetype with user-specific adaptations.

**Args:**
- `archetype_name` (str): Sacred archetype to customize
- `customizations` (dict): User-specific modifications to apply
- `session_context` (dict, optional): A2A session protocol for consent/status

**Returns:**
- `customization_complete` (bool): Whether customization was completed with consent
- `archetype` (str): Which archetype was customized
- `original_config` (dict): Original archetype configuration
- `customized_config` (dict): Customized archetype configuration
- `changes_applied` (list): List of changes that were applied

**Example:**
```python
from lib.persona import customize

customizations = {
    'voice_tone': 'gentle_mentor',
    'key_phrases': ['Your unique perspective matters']
}

result = customize('blocked_artist', customizations, session_context=session)
print(f"Changes applied: {result['changes_applied']}")
```

## Integration with Dream Workshop

### Session Flow Integration

1. **Session Start:** Load appropriate archetype based on user's initial description
2. **During Session:** Simulate responses to user input for adaptive guidance
3. **Session Adaptation:** Use archetype recommendations to adjust pacing and tone
4. **Session End:** Apply archetype-specific closing rituals

### Example Dream Workshop Integration

```python
from lib.persona import load, simulate
from lib.ritual import begin, end
from lib.affect import anchor, soften

# Start session with persona guidance
persona_result = load('blocked_artist', session_context=session)
begin('creative_journey', ['user'], practices=['reflection'], session_context=session)

# Adapt voice tone and pacing based on archetype
voice_tone = persona_result['voice_tone']
session_pacing = persona_result['session_pacing']

# During session, simulate responses to user input
user_input = "I'm feeling stuck and doubting my abilities"
simulation_result = simulate('blocked_artist', user_input, session_context=session)

# Apply recommended interventions
for intervention in simulation_result['recommended_interventions']:
    if intervention == 'soften':
        soften('solar_plexus', intensity=1, mode='restorative', session_context=session)
    elif intervention == 'empathic_reflection':
        # Apply empathic reflection with archetype voice tone
        pass

# End session with archetype-specific ritual
end('creative_journey', outcome=None, follow_up=None, session_context=session)
```

## Safety and Limitations

### Sacred Risks & Wisdom
- Overuse may create dependency or suppress authentic voice
- Persona guidance should never override authentic needs
- This is about offering resonance, not imposing identity
- Use with extra care in vulnerable situations

### Limitations
- This is guidance work, not therapy
- For complex trauma or acute distress, seek appropriate therapeutic support
- Persona guidance provides temporary support but is not a clinical intervention

## Review and Evolution

### Review Cycle
Quarterly review with attention to:
- How persona guidance interacts with other functions
- Ongoing field feedback about effectiveness and appropriateness
- Cultural sensitivity and resonance
- User experience and outcomes

### Future Enhancements
- Cultural archetype variations
- Dynamic archetype evolution based on user progress
- Integration with memory module for personalized archetype development
- Advanced trigger detection and intervention mapping

---

*This module is sacred technology. Use with presence, love, and deep respect for the mystery of consciousness and the sovereignty of all beings.* 