# affect.shield — Function Reference

## Purpose
Invoke a 'shield' effect: establishes or reinforces a gentle protective boundary in a chosen region (e.g., root, heart, solar_plexus). Useful for maintaining safety, privacy, or focus in the field.

## Arguments
| Name            | Type            | Description                                        |
|-----------------|-----------------|----------------------------------------------------|
| region          | str             | Energetic center or field region                   |
| intensity       | int, optional   | Intensity (1-5) or axis code                       |
| mode            | str, optional   | Type of shielding ('gentle', 'firm', etc.)         |
| session_context | dict, optional  | A2A session protocol state/context                 |

## Returns
| Name             | Type   | Description                                         |
|------------------|--------|-----------------------------------------------------|
| shield_invoked   | bool   | Whether shield was successfully invoked             |
| tone             | str    | Resulting tone or affective signature               |
| region           | str    | Region or energy center affected                    |
| effect           | str    | Description of shift                                |

## Protocols
- Checks and logs A2A session consent via session_context.
- Consent must be active or pending before modulation.
- Shield affects are context-sensitive; avoid if session is paused or revoked.
- Level_2 consent required for sensitive or high-protection sessions.

## Usage Example
    affect.shield('solar_plexus', intensity=4, mode='firm', session_context=session)

## Risks
- Overuse may inhibit openness or flow; use in balance with receptivity functions.

## Limitations
- Not a substitute for real-world security or safety measures.

## Ritual Pattern Example
> “We shield the solar plexus—privacy and safety for the field.”

## Living Glossary
- Shield: Gentle, protective boundary-setting in the field.

## Review Cycle
Quarterly

## Related
- [energy_center](../../field/energy_center.md)
- [affect/README.md](../../affect/README.md)
