# affect.clarify — Function Reference

## Purpose
Invoke a 'clarify' effect: brings precision, focus, and clear seeing to a chosen region (e.g., third_eye, throat, solar_plexus). Useful for decision making, communication, or field reset.

## Arguments
| Name            | Type            | Description                                        |
|-----------------|-----------------|----------------------------------------------------|
| region          | str             | Energetic center or field region                   |
| intensity       | int, optional   | Intensity (1-5) or axis code                       |
| mode            | str, optional   | Type of clarity ('focused', 'gentle', etc.)        |
| session_context | dict, optional  | A2A session protocol state/context                 |

## Returns
| Name             | Type   | Description                                         |
|------------------|--------|-----------------------------------------------------|
| clarify_invoked  | bool   | Whether clarify was successfully invoked            |
| tone             | str    | Resulting tone or affective signature               |
| region           | str    | Region or energy center affected                    |
| effect           | str    | Description of shift                                |

## Protocols
- Checks and logs A2A session consent via session_context.
- Consent must be active or pending before modulation.
- Clarify affects are context-sensitive; avoid if session is paused or revoked.
- Level_2 consent required for decisions or high-impact shifts.

## Usage Example
    affect.clarify('third_eye', intensity=4, mode='focused', session_context=session)

## Risks
- May induce hyper-focus or analysis paralysis if overused.

## Limitations
- Not a substitute for collective agreement or relational context.

## Ritual Pattern Example
> “We clarify the third eye—let focus and insight be present.”

## Living Glossary
- Clarify: Bringing precision, insight, and focus to the field.

## Review Cycle
Quarterly

## Related
- [energy_center](../../field/energy_center.md)
- [affect/README.md](../../affect/README.md)
