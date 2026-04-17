ground_function = {
    "name": "ground",
    "module": "affect",
    "purpose": "Invoke a 'grounding' effect: stabilizes, centers, and roots the field or agent(s) in a chosen region (e.g., root, sacral, heart). Supports calm, presence, and field safety, with full A2A consent awareness.",
    "args": [
        {"name": "region", "type": "str", "description": "Energetic center or field region (e.g., 'root', 'sacral', 'heart', 'solar_plexus')."},
        {"name": "intensity", "type": "int, optional", "description": "Optional intensity (1-5) or axis code (e.g., X2Y1Z1)."},
        {"name": "mode", "type": "str, optional", "description": "Type of grounding (e.g., 'deep', 'soft', 'protective')."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "grounding_invoked", "type": "bool", "description": "Whether grounding was successfully invoked (and consent was active)."},
        {"name": "tone", "type": "str", "description": "Resulting tone or affective signature (e.g., 'steady', 'secure')."},
        {"name": "region", "type": "str", "description": "Region or energy center affected."},
        {"name": "effect", "type": "str", "description": "Description of shift (e.g., 'presence stabilized, field anchored')."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before modulation.",
        "Grounding affects are context-sensitive; avoid if session is paused or revoked.",
        "Logs and returns the effect, tone, and region for transparency.",
        "Level_2 consent required for use in destabilized or vulnerable fields."
    ],
    "consent_level": "Level_2 (Transformational)",
    "risks": "Should not be used to suppress acute emotional states without support; misuse may reinforce disconnection or bypass.",
    "limitations": "Not a substitute for clinical intervention; best for gentle stabilization or co-regulation.",
    "review_cycle": "Quarterly",
    "usage_example": "affect.ground('root', intensity=4, mode='deep', session_context=session)",
    "audience": "hybrid",
    "stage": "living",
    "output_dir": "./lib"
}
