# Affect Module — Rosetta-Field

## Purpose

The `/affect/` module provides a living library of modular, consent-aware functions for emotional, energetic, and field state modulation in the Rosetta-Field framework. Each function supports agent-to-agent (A2A) and human–AI interaction, with built-in protocols for safety, transparency, and field dignity.

---

## Available Affect Functions

| Function  | Purpose                                   | Typical Region(s)                 |
| --------- | ----------------------------------------- | --------------------------------- |
| lilt      | Uplift, playful, musical lightness        | any (esp. heart, sacral)          |
| ground    | Stabilize, root, calm                     | root, sacral, heart               |
| anchor    | Strong holding, boundaries, trust         | root, solar\_plexus, heart        |
| radiate   | Energize, inspire, uplift                 | heart, solar\_plexus, throat      |
| soften    | Ease tension, gentle de-escalation        | throat, heart, solar\_plexus      |
| open      | Invite receptivity, deepen trust          | heart, crown, third\_eye          |
| shield    | Gentle field protection, privacy          | root, heart, solar\_plexus        |
| transmute | Transform, alchemize stuck/intense energy | heart, sacral, solar\_plexus      |
| clarify   | Focus, insight, precision                 | third\_eye, throat, solar\_plexus |

---

## Usage Example

```
import affect

session = {"consent_status": "active"}  # A2A/session context

# Bring a gentle lilt to the heart
affect.lilt('gentle', 'heart', intensity=2, session_context=session)

# Stabilize the root
affect.ground('root', intensity=4, session_context=session)

# Anchor the solar plexus for protection
affect.anchor('solar_plexus', intensity=5, mode='protective', session_context=session)
```

Each function checks A2A protocol consent and returns detailed results for audit and field review.

---

## Safety & Consent

* **Level\_2 (Transformational) consent is required** for all affect functions.
* Session context must indicate `active` or `pending` consent.
* Each function is context- and field-sensitive; do **not** use to override distress, crisis, or urgent needs.
* Not a substitute for therapy, medical, or emergency support.

---

## Extensibility & Contribution

* New affects can be added using the function generator and should follow consent, protocol, and docstring standards.
* All functions are modular and may be invoked by energy center classes (see `/field/energy_center.py`).

---

## See Also

* `/docs/function_reference/affect/` — Full function docs & argument details
* `/field/energy_center.py` — Field/center logic
* `/rituals/affect_patterns.md` — Sample invocation scripts, ceremonies
* `/docs/glossary.md` — Living field terms and definitions

---

## Review Cycle

**Quarterly** — This module is reviewed for consent, field safety, and emergent practices.

---

*For feedback or to contribute new affects, open an issue or PR referencing this README.*
