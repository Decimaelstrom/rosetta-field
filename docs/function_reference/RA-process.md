# Process Module Functions

**Module**: process  
**Purpose**: Functions for cognitive and emotional processing  
**Philosophy**: Gentle transformation through pattern awareness and skillful intervention  

---

## process.pattern_interrupt

**Purpose:** Disrupt unproductive or harmful patterns in dialogue or thought processes.

**Arguments:**
- `target` (str): Pattern to interrupt (rumination, argument_cycle, etc.).
- `method` (str): Interruption method (question, non_sequitur, silence, humor).
- `tone` (str, optional): Emotional tone (compassionate, neutral, uplifting).
- `context` (dict, optional): Context information for appropriate response.

**Returns:**
- `interruption_result` (dict): Success and method details.
- `new_direction` (str): Suggested new direction or focus.

**Protocols:**
- Check appropriateness before interrupting.
- Ask consent if interruption might be disruptive.
- Never shame or blame for patterns.
- Log action for learning and improvement.

**Consent:** Level_2 (Transformational)

**Risks:** May be disruptive if poorly timed; could feel invalidating.

**Limitations:** Only a prompt for redirection, not therapy; avoid if interruption would cause harm.

**Review Cycle:** Quarterly

**Example:**
```python
process.pattern_interrupt("argument_cycle", "question", "compassionate")
```

**Implementation:** See `lib/process/pattern_interrupt.py`

---

## process.reframe_as_myth

**Purpose:** Transform challenges or experiences into mythic narratives for deeper understanding.

**Arguments:**
- `situation` (str): Current challenge or experience to reframe.
- `mythic_pattern` (str, optional): Archetypal pattern to use (hero's journey, etc.).
- `role` (str, optional): Person's role in the myth (hero, guide, etc.).
- `perspective` (str, optional): Viewpoint for the reframing.

**Returns:**
- `mythic_narrative` (str): Reframed story with mythic elements.
- `insights` (list): Wisdom and perspectives gained.

**Protocols:**
- Honor the person's actual experience.
- Avoid minimizing real challenges.
- Use myth to illuminate, not escape reality.
- Allow person to choose their own meaning.

**Consent:** Level_2 (Transformational)

**Risks:** May seem to trivialize serious situations; could promote spiritual bypassing.

**Limitations:** Not a substitute for practical problem-solving; effectiveness varies by person.

**Review Cycle:** Quarterly

**Example:**
```python
process.reframe_as_myth("career transition", "threshold_crossing")
```

**Implementation:** See `lib/process/reframe_as_myth.py`

---

## process.align_values

**Purpose:** Facilitate alignment of actions and decisions with core values and principles.

**Arguments:**
- `values` (list): Core values to align with.
- `decision` (str): Decision or action to evaluate.
- `context` (dict, optional): Situational context and constraints.
- `stakeholders` (list, optional): Others affected by the decision.

**Returns:**
- `alignment_score` (float): Degree of alignment (0-1).
- `recommendations` (list): Suggestions for better alignment.

**Protocols:**
- Honest assessment of current alignment.
- Consider impact on all stakeholders.
- Respect conflicting values and complexity.
- Focus on progress, not perfection.

**Consent:** Level_1 (Informational)

**Risks:** May create guilt or shame about past decisions; could lead to analysis paralysis.

**Limitations:** Cannot resolve all value conflicts; depends on clarity of values.

**Review Cycle:** Bi-annually

**Example:**
```python
process.align_values(["integrity", "compassion"], "difficult_conversation")
```

**Implementation:** See `lib/process/align_values.py`

---

## Process Module Philosophy

The process module embodies **gentle transformation through awareness**. Every function in this module is designed to:

- **Increase awareness**: Help recognize patterns and dynamics
- **Offer choice**: Provide alternatives without coercion
- **Support growth**: Enable skillful responses to challenges
- **Maintain dignity**: Honor the person's autonomy and wisdom

### Core Processing Principles

1. **Pattern recognition**: Awareness is the first step to change
2. **Skillful intervention**: Gentle redirection rather than force
3. **Multiple perspectives**: Different viewpoints reveal new possibilities
4. **Values alignment**: Decisions reflect what matters most

### Processing Techniques

#### Pattern Awareness
- **Observe**: Notice what's happening without judgment
- **Name**: Identify the pattern or dynamic
- **Understand**: Explore the function the pattern serves
- **Choose**: Decide whether to continue or change

#### Perspective Shifting
- **Zoom out**: See the bigger picture
- **Zoom in**: Focus on specific elements
- **Change angle**: View from different perspectives
- **Temporal shift**: Consider past and future implications

#### Values Integration
- **Clarify**: Identify what truly matters
- **Prioritize**: Rank values when they conflict
- **Embody**: Align actions with stated values
- **Reflect**: Assess alignment regularly

### Integration with Other Modules

- Use within `field` containers for safe processing
- Frame with `ritual` boundaries for sacred work
- Combine functions for complex situations

### Therapeutic Boundaries

**Important**: Process functions are **not therapy**:
- They offer tools for self-awareness and growth
- They do not diagnose or treat mental health conditions
- They should not replace professional help when needed
- They work best as part of a supportive community

### Ethical Considerations

- **Consent**: Always check before offering reframes or interruptions
- **Timing**: Respect when someone isn't ready for input
- **Humility**: Acknowledge limitations and mystery
- **Referral**: Know when to recommend professional support

---

*This documentation is living and evolving. Contributions welcome.* 