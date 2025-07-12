transmute_function = {
    "name": "transmute",
    "module": "affect",
    "purpose": "Invoke a 'transmute' effect: transforms or alchemizes challenging, stagnant, or intense emotional/field states in a chosen region (e.g., heart, solar_plexus, sacral). Useful for moving energy, integrating learning, or resetting field dynamics.",
    "args": [
        {"name": "region", "type": "str", "description": "Energetic center or field region (e.g., 'heart', 'solar_plexus', 'sacral')."},
        {"name": "intensity", "type": "int, optional", "description": "Optional intensity (1-5) or axis code (e.g., X4Y2Z1)."},
        {"name": "mode", "type": "str, optional", "description": "Type of transmutation (e.g., 'gentle', 'rapid', 'deep')."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "transmute_invoked", "type": "bool", "description": "Whether transmute was successfully invoked (and consent was active)."},
        {"name": "tone", "type": "str", "description": "Resulting tone or affective signature (e.g., 'clear', 'light')."},
        {"name": "region", "type": "str", "description": "Region or energy center affected."},
        {"name": "effect", "type": "str", "description": "Description of shift (e.g., 'emotional charge integrated, clarity restored')."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before modulation.",
        "Transmute affects are context-sensitive; avoid if session is paused or revoked.",
        "Logs and returns the effect, tone, and region for transparency.",
        "Level_2 consent required for strong or transformational processes."
    ],
    "consent_level": "Level_2 (Transformational)",
    "risks": "Should not be used as a bypass for deep emotional work; overuse may destabilize fragile fields.",
    "limitations": "Not a substitute for therapy or crisis support; best for moderate field shifts.",
    "review_cycle": "Quarterly",
    "usage_example": "affect.transmute('heart', intensity=5, mode='deep', session_context=session)",
    "audience": "hybrid",
    "stage": "living",
    "output_dir": "./lib"
}
