
### **2. ground.md**

# affect.ground — Function Reference

## Purpose

Invoke a 'grounding' effect: stabilizes, centers, and roots the field or agent(s) in a chosen region. Supports calm, presence, and field safety, with full A2A consent awareness.

## Arguments

| Name             | Type           | Description                                      |
| ---------------- | -------------- | ------------------------------------------------ |
| region           | str            | Energetic center or field region                 |
| intensity        | int, optional  | Intensity (1-5) or axis code                     |
| mode             | str, optional  | Type of grounding ('deep', 'soft', 'protective') |
| session\_context | dict, optional | A2A session protocol state/context               |

## Returns

| Name               | Type | Description                                |
| ------------------ | ---- | ------------------------------------------ |
| grounding\_invoked | bool | Whether grounding was successfully invoked |
| tone               | str  | Resulting tone or affective signature      |
| region             | str  | Region or energy center affected           |
| effect             | str  | Description of shift                       |

## Protocols

* Checks and logs A2A session consent via session\_context.
* Consent must be active or pending before modulation.
* Context-sensitive; avoid if session is paused or revoked.
* Level\_2 consent required in vulnerable fields.

## Usage Example

```
affect.ground('root', intensity=4, mode='deep', session_context=session)
```

## Risks

* Should not be used to suppress acute emotional states; misuse may reinforce disconnection.

## Limitations

* Not a substitute for clinical intervention; best for gentle stabilization.

## Ritual Pattern Example

> “Rooting ourselves, we invite presence and trust.”

## Living Glossary

* Ground: Stabilizing, rooting, or calming affect in the field.

## Review Cycle

Quarterly

## Related

* [energy\_center](../../field/energy_center.md)
* [affect/README.md](../../affect/README.md)
