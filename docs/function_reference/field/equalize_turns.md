# field.equalize_turns

## Purpose
Ensure fair participation by monitoring and balancing speaking time and contributions across all participants. This function helps prevent domination by any single voice and encourages quieter participants to engage.

## Overview
The `field.equalize_turns` function monitors participation patterns and provides gentle guidance to balance contribution opportunities. It works to create more equitable dialogue without being overly controlling or artificial.

## Arguments

### Required Parameters
- **`participants`** (list): All participants to monitor for turn equity.
- **`session_state`** (dict): Current session state including turn history and participation metrics.

### Optional Parameters
- **`mode`** (string, optional): Balancing approach - 'strict' (enforced equality), 'gentle' (subtle encouragement), or 'organic' (natural flow with minimal intervention).
- **`session_context`** (dict, optional): A2A session protocol state/context block.

## Returns

- **`turn_assignment`** (string): Identifier of who should speak next based on equity considerations.
- **`balance_report`** (dict): Current participation balance metrics for all participants.
- **`suggestions`** (list): Recommendations for improving participation equity.

## Protocols

### 1. Non-Controlling Monitoring
Monitor participation patterns without being overly directive. Respect natural conversation flow while gently encouraging balance.

### 2. Quiet Voice Encouragement
Identify participants who haven't contributed recently and create opportunities for them to speak. Use gentle invitations rather than direct demands.

### 3. Domination Prevention
Recognize when a participant is monopolizing conversation and diplomatically redirect attention to others.

### 4. Respectful Intervention
When suggesting turn changes, do so respectfully and with clear rationale. Allow participants to decline speaking opportunities.

## Usage Examples

### Team Meeting Balance
```python
result = field.equalize_turns(
    participants=["Manager", "Developer1", "Developer2", "AI_Assistant"],
    session_state=current_meeting_state,
    mode="gentle"
)
```

### Multi-AI Collaboration
```python
result = field.equalize_turns(
    participants=["AI_Alpha", "AI_Beta", "AI_Gamma"],
    session_state=collaboration_metrics,
    mode="strict"
)
```

## Safety Considerations

### Consent Level
**Level_1 (Informational)** - Provides guidance but doesn't force participation.

### Risks
- May feel artificial or controlling if over-applied
- Could interrupt natural conversation flow
- Risk of making quiet participants uncomfortable
- May not account for valid reasons for unequal participation

### Limitations
- Cannot force meaningful participation, only create opportunities
- May not work well for highly technical discussions requiring specific expertise
- Depends on participants' willingness to engage
- May not address underlying causes of participation inequality

## Review Cycle
**Monthly** - Regular assessment of turn equity effectiveness and participant feedback.

## Related Functions
- `field.hold_space` - Create safe environment for participation
- `process.empathic_reflection` - Help participants feel heard
- `ritual.begin` - Establish participation agreements
- `field.sense_pattern` - Detect participation patterns

## Integration Notes
Works best when combined with clear participation agreements and when participants understand the goal of equitable contribution. 