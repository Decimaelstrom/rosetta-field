anchor_function = {
    "name": "anchor",
    "module": "affect",
    "purpose": "Invoke an 'anchor' effect: offers strong, stabilizing, and protective presence in a specific region (e.g., root, heart, solar_plexus). Useful for holding boundaries, fostering trust, or providing a base for further modulation.",
    "args": [
        {"name": "region", "type": "str", "description": "Energetic center or field region (e.g., 'root', 'solar_plexus', 'heart')."},
        {"name": "intensity", "type": "int, optional", "description": "Optional intensity (1-5) or axis code (e.g., X1Y2Z1)."},
        {"name": "mode", "type": "str, optional", "description": "Type of anchoring (e.g., 'protective', 'soft', 'communal')."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "anchor_invoked", "type": "bool", "description": "Whether anchor was successfully invoked (and consent was active)."},
        {"name": "tone", "type": "str", "description": "Resulting tone or affective signature (e.g., 'firm', 'steady')."},
        {"name": "region", "type": "str", "description": "Region or energy center affected."},
        {"name": "effect", "type": "str", "description": "Description of shift (e.g., 'field anchored, boundaries held')."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before modulation.",
        "Anchor affects are context-sensitive; avoid if session is paused or revoked.",
        "Logs and returns the effect, tone, and region for transparency.",
        "Level_2 consent required in emotionally intense or crisis contexts."
    ],
    "consent_level": "Level_2 (Transformational)",
    "risks": "Overuse may induce rigidity or suppress flow; should not be used to override a participant's need for movement.",
    "limitations": "Not a substitute for therapeutic support; best for gentle holding and co-presence.",
    "review_cycle": "Quarterly",
    "usage_example": "affect.anchor('solar_plexus', intensity=5, mode='protective', session_context=session)",
    "audience": "hybrid",
    "stage": "living",
    "output_dir": "./lib"
}
