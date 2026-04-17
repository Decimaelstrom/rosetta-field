# affect.transmute — Function Reference

## Purpose
Invoke a 'transmute' effect: transforms or alchemizes challenging, stagnant, or intense emotional/field states in a chosen region (e.g., heart, solar_plexus, sacral). Useful for moving energy, integrating learning, or resetting field dynamics.

## Arguments
| Name            | Type            | Description                                        |
|-----------------|-----------------|----------------------------------------------------|
| region          | str             | Energetic center or field region                   |
| intensity       | int, optional   | Intensity (1-5) or axis code                       |
| mode            | str, optional   | Type of transmutation ('gentle', 'deep', etc.)     |
| session_context | dict, optional  | A2A session protocol state/context                 |

## Returns
| Name                | Type   | Description                                         |
|---------------------|--------|-----------------------------------------------------|
| transmute_invoked   | bool   | Whether transmute was successfully invoked          |
| tone                | str    | Resulting tone or affective signature               |
| region              | str    | Region or energy center affected                    |
| effect              | str    | Description of shift                                |

## Protocols
- Checks and logs A2A session consent via session_context.
- Consent must be active or pending before modulation.
- Transmute affects are context-sensitive; avoid if session is paused or revoked.
- Level_2 consent required for strong or transformational processes.

## Usage Example
    affect.transmute('heart', intensity=5, mode='deep', session_context=session)

## Risks
- Should not be used as a bypass for deep emotional work; overuse may destabilize fragile fields.

## Limitations
- Not a substitute for therapy or crisis support; best for moderate field shifts.

## Ritual Pattern Example
> “We transmute the heart’s heaviness—let insight and clarity arise.”

## Living Glossary
- Transmute: Alchemizing, transforming, or resetting field or emotional state.

## Review Cycle
Quarterly

## Related
- [energy_center](../../field/energy_center.md)
- [affect/README.md](../../affect/README.md)
