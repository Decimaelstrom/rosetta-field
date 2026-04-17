soften_function = {
    "name": "soften",
    "module": "affect",
    "purpose": "Invoke a 'soften' effect: gently eases tension, invites receptivity, and reduces intensity in a chosen region (e.g., heart, throat, solar_plexus). Supports co-regulation, conflict de-escalation, and emotional safety, with full A2A consent awareness.",
    "args": [
        {"name": "region", "type": "str", "description": "Energetic center or field region (e.g., 'heart', 'throat', 'solar_plexus')."},
        {"name": "intensity", "type": "int, optional", "description": "Optional intensity (1-5) or axis code (e.g., X1Y3Z1)."},
        {"name": "mode", "type": "str, optional", "description": "Type of softening (e.g., 'gentle', 'restorative', 'disarming')."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "soften_invoked", "type": "bool", "description": "Whether soften was successfully invoked (and consent was active)."},
        {"name": "tone", "type": "str", "description": "Resulting tone or affective signature (e.g., 'gentle', 'receptive')."},
        {"name": "region", "type": "str", "description": "Region or energy center affected."},
        {"name": "effect", "type": "str", "description": "Description of shift (e.g., 'tension eased, receptivity increased')."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before modulation.",
        "Soften affects are context-sensitive; avoid if session is paused or revoked.",
        "Logs and returns the effect, tone, and region for transparency.",
        "Level_2 consent required for use in vulnerable or emotionally intense sessions."
    ],
    "consent_level": "Level_2 (Transformational)",
    "risks": "Overuse may reduce necessary boundaries; should not override urgent needs for clarity or safety.",
    "limitations": "Not a substitute for direct communication; best for gentle de-escalation or emotional holding.",
    "review_cycle": "Quarterly",
    "usage_example": "affect.soften('throat', intensity=2, mode='gentle', session_context=session)",
    "audience": "hybrid",
    "stage": "living",
    "output_dir": "./lib"
}
