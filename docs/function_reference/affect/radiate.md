# affect.radiate — Function Reference

## Purpose
Invoke a 'radiate' effect: generates and expresses warmth, confidence, or joy from a chosen region (e.g., heart, solar_plexus, throat). Useful for increasing energy, inspiration, or inviting co-regulation.

## Arguments
| Name            | Type            | Description                                        |
|-----------------|-----------------|----------------------------------------------------|
| region          | str             | Energetic center or field region                   |
| intensity       | int, optional   | Intensity (1-5) or axis code                       |
| mode            | str, optional   | Type of radiance ('joyful', 'warm', 'empowered')   |
| session_context | dict, optional  | A2A session protocol state/context                 |

## Returns
| Name             | Type   | Description                                         |
|------------------|--------|-----------------------------------------------------|
| radiate_invoked  | bool   | Whether radiate was successfully invoked            |
| tone             | str    | Resulting tone or affective signature               |
| region           | str    | Region or energy center affected                    |
| effect           | str    | Description of shift                                |

## Protocols
- Checks and logs A2A session consent via session_context.
- Consent must be active or pending before modulation.
- Radiate affects are context-sensitive; avoid if session is paused or revoked.
- Level_2 consent required for use in vulnerable or high-energy fields.

## Usage Example
    affect.radiate('heart', intensity=3, mode='joyful', session_context=session)

## Risks
- May overstimulate sensitive participants or fields; use moderation.

## Limitations
- Not a substitute for medical/therapeutic intervention; best for gentle amplification of positive affect.

## Ritual Pattern Example
> “Let joy radiate from the heart—energy flows outward to all.”

## Living Glossary
- Radiate: Expressing warmth, energy, or inspiration into the field.

## Review Cycle
Quarterly

## Related
- [energy_center](../../field/energy_center.md)
- [affect/README.md](../../affect/README.md)
