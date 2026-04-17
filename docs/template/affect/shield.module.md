shield_function = {
    "name": "shield",
    "module": "affect",
    "purpose": "Invoke a 'shield' effect: establishes or reinforces a gentle protective boundary in a chosen region (e.g., root, heart, solar_plexus). Useful for maintaining safety, privacy, or focus in the field.",
    "args": [
        {"name": "region", "type": "str", "description": "Energetic center or field region (e.g., 'root', 'heart', 'solar_plexus')."},
        {"name": "intensity", "type": "int, optional", "description": "Optional intensity (1-5) or axis code (e.g., X3Y1Z2)."},
        {"name": "mode", "type": "str, optional", "description": "Type of shielding (e.g., 'gentle', 'firm', 'reflective')."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "shield_invoked", "type": "bool", "description": "Whether shield was successfully invoked (and consent was active)."},
        {"name": "tone", "type": "str", "description": "Resulting tone or affective signature (e.g., 'protected', 'contained')."},
        {"name": "region", "type": "str", "description": "Region or energy center affected."},
        {"name": "effect", "type": "str", "description": "Description of shift (e.g., 'field protected, privacy increased')."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before modulation.",
        "Shield affects are context-sensitive; avoid if session is paused or revoked.",
        "Logs and returns the effect, tone, and region for transparency.",
        "Level_2 consent required for sensitive or high-protection sessions."
    ],
    "consent_level": "Level_2 (Transformational)",
    "risks": "Overuse may inhibit openness or flow; use in balance with receptivity functions.",
    "limitations": "Not a substitute for real-world security or safety measures; for field/relational use only.",
    "review_cycle": "Quarterly",
    "usage_example": "affect.shield('solar_plexus', intensity=4, mode='firm', session_context=session)",
    "audience": "hybrid",
    "stage": "living",
    "output_dir": "./lib"
}
