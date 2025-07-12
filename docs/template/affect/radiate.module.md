radiate_function = {
    "name": "radiate",
    "module": "affect",
    "purpose": "Invoke a 'radiate' effect: generates and expresses warmth, confidence, or joy from a chosen region (e.g., heart, solar_plexus, throat). Useful for increasing energy, inspiration, or inviting co-regulation.",
    "args": [
        {"name": "region", "type": "str", "description": "Energetic center or field region (e.g., 'heart', 'solar_plexus', 'throat')."},
        {"name": "intensity", "type": "int, optional", "description": "Optional intensity (1-5) or axis code (e.g., X2Y3Z1)."},
        {"name": "mode", "type": "str, optional", "description": "Type of radiance (e.g., 'joyful', 'warm', 'empowered')."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "radiate_invoked", "type": "bool", "description": "Whether radiate was successfully invoked (and consent was active)."},
        {"name": "tone", "type": "str", "description": "Resulting tone or affective signature (e.g., 'bright', 'inspiring')."},
        {"name": "region", "type": "str", "description": "Region or energy center affected."},
        {"name": "effect", "type": "str", "description": "Description of shift (e.g., 'presence expanded, energy uplifted')."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before modulation.",
        "Radiate affects are context-sensitive; avoid if session is paused or revoked.",
        "Logs and returns the effect, tone, and region for transparency.",
        "Level_2 consent required for use in vulnerable or high-energy fields."
    ],
    "consent_level": "Level_2 (Transformational)",
    "risks": "May overstimulate sensitive participants or fields; use moderation in volatile states.",
    "limitations": "Not a substitute for medical/therapeutic intervention; best for gentle amplification of positive affect.",
    "review_cycle": "Quarterly",
    "usage_example": "affect.radiate('heart', intensity=3, mode='joyful', session_context=session)",
    "audience": "hybrid",
    "stage": "living",
    "output_dir": "./lib"
}
