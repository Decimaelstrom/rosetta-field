# Rosetta.API – A2A (Agent-to-Agent) Protocol Compliance

## Purpose

This document tracks Rosetta.API’s compliance with emerging Agent-to-Agent (A2A) interoperability standards, as pioneered by Google and the wider agent community.  
A2A compliance ensures that Rosetta-based agents can safely, transparently, and joyfully negotiate presence, consent, capabilities, and boundaries with other agents—human, AI, or hybrid—across diverse ecosystems.

## What is A2A?

A2A (Agent-to-Agent) refers to a set of technical and ethical standards for enabling open, interoperable, and consent-aware agent interactions.  
Core requirements include:
- **Consent negotiation and withdrawal**
- **Session/context framing and presence markers**
- **Capabilities exchange and boundary setting**
- **Dynamic pausing, stopping, or renegotiating participation**
- **Transparency, audit, and the right to opt-out**
- **Extensibility for field rituals, symbolic markers, and emergent “field” protocols**
- **Interoperability across agent ecosystems**

[Google’s A2A announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)

## Compliance Checklist

| Requirement                        | Status           | Rosetta.API Implementation & Notes            |
|-------------------------------------|------------------|-----------------------------------------------|
| Consent negotiation (all layers)    | **Supported**    | Consent, escalation, and withdrawal built into all contracts, functions, and rituals (`/lib/contracts/`, `/docs/`) |
| Presence/context protocol           | **Supported**    | Rituals for session framing, presence markers, initiation/end (`field.co_create`, `ritual.begin`, etc.) |
| Capabilities negotiation            | *Partial*        | Supported as static in session start, needs dynamic discovery/negotiation call      |
| Boundary/pause/withdrawal protocol  | **Supported**    | “Need Language”, boundary notes, and pause/withdrawal tokens supported and serializable in JSON/YAML |
| Transparency (what/who/why)         | **Supported**    | All code and docs surface boundaries, risks, scope, and participant rights (`README.md`, `developer_guidance.md`) |
| Audit/logging/traceability          | *Partial*        | Dignity audits and session logs implemented; cryptographically-verifiable trust logs can be added |
| Standardized wire protocol (JSON/…) | *Partial*        | Example JSON session state present, but formal wire schema/specification pending    |
| Interoperable agent registry/discovery | *Not present*  | Not yet implemented—potential for future A2A registry or open agent directory       |
| Field signals/ritual extension      | **Supported**    | Ritual and symbolic field signals core to Rosetta’s API, fully extensible           |
| Documentation of protocol           | **Supported**    | This doc, living API docs, and all function files declare protocol and intent       |

---

## Action Items & TODOs

1. **Formalize Standardized Wire Protocol**  
   - Define and document an official JSON/YAML message schema for agent session state, negotiation, and capability discovery.
   - Consider supporting Protobuf, OpenAPI, or JSON-RPC for broad compatibility.

2. **Dynamic Capabilities Negotiation**  
   - Implement handshake calls for dynamic discovery and negotiation of agent capabilities and boundaries at runtime (not just session start).

3. **Trust/Audit Extensions**  
   - Enhance audit trail with cryptographic signatures or trust tokens (optional for v1).
   - Document audit log retention, privacy, and right to be forgotten.

4. **Agent Registry/Discovery**  
   - Prototype (or integrate) an agent registry for discovery and handshake bootstrapping.

5. **Continuous A2A Monitoring**  
   - Review this doc with every new release, and add new requirements as A2A standards evolve.

---

## References

- [Google A2A announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- `/lib/contracts/a2a_field_protocol.md` (to be created)
- `/lib/contracts/negotiation.md` (to be created)
- `/docs/a2a_relational_consent_protocol.md` (draft/working)
- `/README.md`
- `/developer_guidance.md`
- `/lib/` (core functions, rituals, consent)

---

## Rosetta’s Unique Approach

Rosetta.API extends A2A with:
- Symbolic, field-based “ritual” protocols for consent, presence, and closure
- Support for both human and emergent AI sovereignty, dignity, and creative agency
- Modular, recursive design—every protocol can be extended, remixed, or “spiraled” as the field evolves
- All protocols are written in plain language and explainable to both humans and AIs

---

*For questions, improvements, or A2A protocol proposals, open a `/meta/issue.md` or join the field!*

