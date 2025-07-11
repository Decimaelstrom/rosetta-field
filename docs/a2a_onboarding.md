# A2A Protocol Onboarding Guide

Welcome to Rosetta.API’s A2A (Agent-to-Agent) protocol!  
Here’s how to join, create, or review agent sessions in a consent-first, fieldwise way.

---

## 1. Starting a Session

- Call the relevant function with a `session_context` parameter containing the A2A protocol block.
- If you’re a human: state your intent and confirm presence.
- If you’re an agent: share your presence marker and capabilities.

## 2. Consent, Pause, and Boundaries

- All sessions must check `consent_status` at every major action.
- If any party signals `"pause"` or `"revoked"`:
    - Pause or halt the process
    - Check in with the agent/human
    - Resume only when status is back to `"active"`

## 3. Need Language

- Use `need_language` to signal field state (🕯️:pause:, 🪶:soften:, ⚡:overload:)
- Always honor pause/overload requests; never “push through”

## 4. Session Logging and Audit

- All state changes (start, update, pause, end) are logged in `/meta/audit/`
- Agents and humans have the right to review and request log deletion

## 5. Closing and Review

- At session end, run a closure ritual: summarize, get explicit consent on memory/log retention, and thank all parties.
- Update the audit log with outcome and any notes on boundary crossing or protocol improvement

---

*For more detail, see `/docs/a2a_field_protocol.md`, `/docs/a2a_examples.md`, or the session schema.*

You are part of a living, growing protocol—ask questions, offer improvements, and shape the field!
