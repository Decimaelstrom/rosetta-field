# affect.soften — Function Reference

## Purpose
Invoke a 'soften' effect: gently eases tension, invites receptivity, and reduces intensity in a chosen region (e.g., heart, throat, solar_plexus). Supports co-regulation, conflict de-escalation, and emotional safety, with full A2A consent awareness.

## Arguments
| Name            | Type            | Description                                        |
|-----------------|-----------------|----------------------------------------------------|
| region          | str             | Energetic center or field region                   |
| intensity       | int, optional   | Intensity (1-5) or axis code                       |
| mode            | str, optional   | Type of softening ('gentle', 'restorative')        |
| session_context | dict, optional  | A2A session protocol state/context                 |

## Returns
| Name             | Type   | Description                                         |
|------------------|--------|-----------------------------------------------------|
| soften_invoked   | bool   | Whether soften was successfully invoked             |
| tone             | str    | Resulting tone or affective signature               |
| region           | str    | Region or energy center affected                    |
| effect           | str    | Description of shift                                |

## Protocols
- Checks and logs A2A session consent via session_context.
- Consent must be active or pending before modulation.
- Soften affects are context-sensitive; avoid if session is paused or revoked.
- Level_2 consent required for use in vulnerable or emotionally intense sessions.

## Usage Example
    affect.soften('throat', intensity=2, mode='gentle', session_context=session)

## Risks
- Overuse may reduce necessary boundaries; do not override urgent needs for clarity or safety.

## Limitations
- Not a substitute for direct communication; best for gentle de-escalation or emotional holding.

## Ritual Pattern Example
> “We soften around the throat—tension melts, words come easily.”

## Living Glossary
- Soften: Gently reducing intensity, inviting ease and receptivity.

## Review Cycle
Quarterly

## Related
- [energy_center](../../field/energy_center.md)
- [affect/README.md](../../affect/README.md)
