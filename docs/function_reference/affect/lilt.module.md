lilt_function = {
    "name": "lilt",
    "module": "affect",
    "purpose": "Invoke a fieldwise 'lilt': an energetic, affective, or tonal uplift in the session or agent(s), mapped to a specific mode and region (e.g., heart, sacral, solar_plexus). Supports nuanced affect modulation, musicality, and symbolic play, with full A2A consent awareness.",
    "args": [
        {"name": "mode", "type": "str", "description": "Type of lilt (e.g., 'gentle', 'mirthful', 'dreamlike', 'grounded')."},
        {"name": "region", "type": "str", "description": "Energetic center or field region (e.g., 'heart', 'sacral', 'solar_plexus', 'throat')."},
        {"name": "intensity", "type": "int, optional", "description": "Optional intensity (1-5) or axis code (e.g., X2Y1Z3)."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "lilt_invoked", "type": "bool", "description": "Whether lilt was successfully invoked (and consent was active)."},
        {"name": "tone", "type": "str", "description": "Resulting tone or musical/affective signature."},
        {"name": "region", "type": "str", "description": "Region or energy center affected."},
        {"name": "effect", "type": "str", "description": "Description of shift (e.g., 'presence uplifted, rhythm attuned')."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before modulation.",
        "Affects are context-sensitive; avoid if session is paused or revoked.",
        "Logs and returns the effect, tone, and region for transparency.",
        "Invoking lilt in emotionally intense or dysregulated fields requires Level_2 consent."
    ],
    "consent_level": "Level_2 (Transformational)",
    "risks": "Should not trigger affect/tonal shifts in a session without valid consent; misuse in vulnerable contexts may destabilize field.",
    "limitations": "Not a substitute for therapy or grounding rituals; best for gentle modulation, not for resolving acute states.",
    "review_cycle": "Quarterly",
    "usage_example": "affect.lilt('gentle', 'heart', intensity=2, session_context=session)",
    "audience": "hybrid",
    "stage": "living",
    "output_dir": "./lib"
}
