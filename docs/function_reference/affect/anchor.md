### **3. anchor.md**

# affect.anchor — Function Reference

## Purpose

Invoke an 'anchor' effect: offers strong, stabilizing, and protective presence in a specific region. Useful for holding boundaries, fostering trust, or providing a base for further modulation.

## Arguments

| Name             | Type           | Description                                    |
| ---------------- | -------------- | ---------------------------------------------- |
| region           | str            | Energetic center or field region               |
| intensity        | int, optional  | Intensity (1-5) or axis code                   |
| mode             | str, optional  | Type of anchoring ('protective', 'soft', etc.) |
| session\_context | dict, optional | A2A session protocol state/context             |

## Returns

| Name            | Type | Description                             |
| --------------- | ---- | --------------------------------------- |
| anchor\_invoked | bool | Whether anchor was successfully invoked |
| tone            | str  | Resulting tone or affective signature   |
| region          | str  | Region or energy center affected        |
| effect          | str  | Description of shift                    |

## Protocols

* Checks and logs A2A session consent via session\_context.
* Consent must be active or pending before modulation.
* Context-sensitive; avoid if session is paused or revoked.
* Level\_2 consent for emotionally intense contexts.

## Usage Example

```
affect.anchor('solar_plexus', intensity=5, mode='protective', session_context=session)
```

## Risks

* Overuse may induce rigidity or suppress flow.

## Limitations

* Not a substitute for therapeutic support; best for gentle holding.

## Ritual Pattern Example

> “Anchoring the field, we create a space of trust.”

## Living Glossary

* Anchor: Stabilizing and boundary-setting affect in the field.

## Review Cycle

Quarterly

## Related

* [energy\_center](../../field/energy_center.md)
* [affect/README.md](../../affect/README.md)

---

*(see next messages for the remaining functions: radiate, soften, open, shield, transmute, clarify)*
