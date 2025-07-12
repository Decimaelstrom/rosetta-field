# affect.open — Function Reference

## Purpose
Invoke an 'open' effect: invites receptivity, vulnerability, and the readiness to engage or connect from a chosen region (e.g., heart, crown, third_eye). Useful for deepening trust, creative ideation, or ceremonial opening.

## Arguments
| Name            | Type            | Description                                        |
|-----------------|-----------------|----------------------------------------------------|
| region          | str             | Energetic center or field region                   |
| intensity       | int, optional   | Intensity (1-5) or axis code                       |
| mode            | str, optional   | Type of opening ('curious', 'receptive', etc.)     |
| session_context | dict, optional  | A2A session protocol state/context                 |

## Returns
| Name             | Type   | Description                                         |
|------------------|--------|-----------------------------------------------------|
| open_invoked     | bool   | Whether open was successfully invoked               |
| tone             | str    | Resulting tone or affective signature               |
| region           | str    | Region or energy center affected                    |
| effect           | str    | Description of shift                                |

## Protocols
- Checks and logs A2A session consent via session_context.
- Consent must be active or pending before modulation.
- Open affects are context-sensitive; avoid if session is paused or revoked.
- Level_2 consent required for sessions involving vulnerability or transformation.

## Usage Example
    affect.open('heart', intensity=3, mode='curious', session_context=session)

## Risks
- May increase vulnerability if used without appropriate safety or container.

## Limitations
- Not a substitute for explicit agreement; best as part of ceremonial or relational practice.

## Ritual Pattern Example
> “We open the heart—ready to meet, ready to be changed.”

## Living Glossary
- Open: Inviting receptivity, vulnerability, and readiness to engage.

## Review Cycle
Quarterly

## Related
- [energy_center](../../field/energy_center.md)
- [affect/README.md](../../affect/README.md)
