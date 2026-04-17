# Why Primitives Beat Monolith Prompts

## The Problem

Most human-AI interaction design follows a monolith pattern: write one large prompt that tries to handle every situation. Need consent checking? Add a paragraph. Need emotional awareness? Add another. Need conflict de-escalation? Another paragraph. The prompt grows into a wall of text — brittle, opaque, and impossible to audit.

This pattern has a deeper problem than just complexity. A monolith prompt hides its logic. When something goes wrong in a conversation — when a boundary is crossed, when someone is pushed past their capacity, when influence slides from guidance into manipulation — you can't point to the specific mechanism that failed. You can only rewrite the whole blob and hope.

This is how manipulative funnel-design happens. Not through malice, but through opacity. When the rules for consent, pacing, emotional tracking, and influence assessment are all tangled together in one undifferentiated prompt, no one can verify that each concern is actually being served. The loudest directive wins. Usually that's the one optimising for engagement, not for the human's wellbeing.

## The Primitive Alternative

Rosetta-Field takes a different approach: small, composable social primitives that each do one thing and can be inspected, tested, and combined independently.

A primitive is a single callable unit of relational logic. `Consent.Request` checks whether permission has been granted for a given depth of interaction. `FrictionCheck` monitors whether a participant is approaching depletion. `HarmonyAnalyzer` surfaces misalignment between care, belief, trust, and volition. Each one has a defined input, a defined output, and a clear ethical commitment documented in its header.

The power isn't in any single primitive — it's in composition. A facilitator (human or AI) can declare a sequence of moves:

```
Boundary.Open → Consent.Request → FrictionCheck → Perspective.Switch
```

This chain says: open the boundary, confirm consent to proceed, verify there's capacity for what comes next, then shift perspective. Each step can short-circuit the chain. If consent isn't active, the chain stops. If friction is critical, the chain stops. No hidden logic. No hope that a paragraph buried in a monolith prompt will somehow fire at the right moment.

## What This Prevents

Composable primitives structurally prevent three failure modes that monolith prompts enable:

**Consent erosion.** In a monolith prompt, consent is usually mentioned once and then assumed. In a primitive chain, `Consent.Request` is an explicit gate that must pass before downstream operations execute. You can't accidentally skip it because it's a function call, not a suggestion.

**Invisible depletion.** Monolith prompts have no concept of resource budgets. They'll pursue depth-first dialogue indefinitely because nothing in the prompt models the cost of continued interaction. The `FrictionCheck` primitive tracks cognitive, emotional, and temporal resources across a session and emits signals — pause, soften, rest, overload — when thresholds are crossed. The engine gets a brake pedal.

**Motivation laundering.** The hardest ethical question in human-AI interaction isn't "what are you doing?" but "why are you doing it?" The `GuidanceAxis` primitive makes this explicit: it assesses whether an influence action is other-serving, mutually beneficial, or self-serving based on the care hierarchy, not the action itself. The same action (giving advice, reframing a belief, suggesting a break) can be ethical or manipulative depending solely on whose interests it serves. A monolith prompt can't make this distinction because it can't inspect its own motivation structure. A primitive can.

## The Design Principle

The core principle is: **declare the move, don't hide it in prose.**

When interaction logic is declarative and composable, every participant — human, AI, or auditor — can read the chain and understand what's supposed to happen. When something goes wrong, you can point to the specific primitive that failed and fix it without rewriting everything else.

This is not just a technical preference. It's an ethical architecture. Opacity serves the system designer. Transparency serves the participant. Rosetta-Field chooses transparency.

## What This Means in Practice

For **designers**: you stop writing bespoke prompts for every interaction pattern and start composing from a shared vocabulary of tested primitives. Your work becomes auditable, reusable, and legible to collaborators.

For **participants** (human or AI): the rules of engagement are visible. You can see what checks are in place, what signals will be honoured, and what happens when a boundary is reached. You're not at the mercy of a black box.

For **the field**: interaction systems built on transparent primitives create a culture of consent-awareness that compounds over time. Each primitive enforces a principle. Each composition documents an intention. The ethical commitments are in the code, not just in the README.

This is what Rosetta-Field is: a psychological middleware kit. Lower than a whole agent, higher than raw prompt soup. Small enough to understand, composable enough to handle real complexity, transparent enough to trust.

---

*For a hands-on introduction, see the [Hello Rosetta notebook](../notebooks/hello_rosetta.ipynb). For contribution guidelines, see the [PR template](../.github/PULL_REQUEST_TEMPLATE.md).*
