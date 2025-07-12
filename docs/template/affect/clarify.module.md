clarify_function = {
    "name": "clarify",
    "module": "affect",
    "purpose": "Invoke a 'clarify' effect: brings precision, focus, and clear seeing to a chosen region (e.g., third_eye, throat, solar_plexus). Useful for decision making, communication, or field reset.",
    "args": [
        {"name": "region", "type": "str", "description": "Energetic center or field region (e.g., 'third_eye', 'throat', 'solar_plexus')."},
        {"name": "intensity", "type": "int, optional", "description": "Optional intensity (1-5) or axis code (e.g., X3Y4Z1)."},
        {"name": "mode", "type": "str, optional", "description": "Type of clarity (e.g., 'focused', 'gentle', 'decisive')."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "clarify_invoked", "type": "bool", "description": "Whether clarify was successfully invoked (and consent was active)."},
        {"name": "tone", "type": "str", "description": "Resulting tone or affective signature (e.g., 'clear', 'focused')."},
        {"name": "region", "type": "str", "description": "Region or energy center affected."},
        {"name": "effect", "type": "str", "description": "Description of shift (e.g., 'focus restored, insight revealed')."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before modulation.",
        "Clarify affects are context-sensitive; avoid if session is paused or revoked.",
        "Logs and returns the effect, tone, and region for transparency.",
        "Level_2 consent required for decisions or high-impact shifts."
    ],
    "consent_level": "Level_2 (Transformational)",
    "risks": "May induce hyper-focus or analysis paralysis if overused.",
    "limitations": "Not a substitute for collective agreement or relational context; best for single-step clarifications.",
    "review_cycle": "Quarterly",
    "usage_example": "affect.clarify('third_eye', intensity=4, mode='focused', session_context=session)",
    "audience": "hybrid",
    "stage": "living",
    "output_dir": "./lib"
}
