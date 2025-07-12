open_function = {
    "name": "open",
    "module": "affect",
    "purpose": "Invoke an 'open' effect: invites receptivity, vulnerability, and the readiness to engage or connect from a chosen region (e.g., heart, crown, third_eye). Useful for deepening trust, creative ideation, or ceremonial opening.",
    "args": [
        {"name": "region", "type": "str", "description": "Energetic center or field region (e.g., 'heart', 'crown', 'third_eye')."},
        {"name": "intensity", "type": "int, optional", "description": "Optional intensity (1-5) or axis code (e.g., X2Y1Z4)."},
        {"name": "mode", "type": "str, optional", "description": "Type of opening (e.g., 'curious', 'receptive', 'transcendent')."},
        {"name": "session_context", "type": "dict, optional", "description": "A2A session protocol state/context block (for consent/status)."}
    ],
    "returns": [
        {"name": "open_invoked", "type": "bool", "description": "Whether open was successfully invoked (and consent was active)."},
        {"name": "tone", "type": "str", "description": "Resulting tone or affective signature (e.g., 'expansive', 'vulnerable')."},
        {"name": "region", "type": "str", "description": "Region or energy center affected."},
        {"name": "effect", "type": "str", "description": "Description of shift (e.g., 'field widened, receptivity increased')."}
    ],
    "protocols": [
        "Checks and logs A2A session consent via session_context.",
        "Consent must be active or pending before modulation.",
        "Open affects are context-sensitive; avoid if session is paused or revoked.",
        "Logs and returns the effect, tone, and region for transparency.",
        "Level_2 consent required for sessions involving vulnerability or transformation."
    ],
    "consent_level": "Level_2 (Transformational)",
    "risks": "May increase vulnerability if used without appropriate safety or container.",
    "limitations": "Not a substitute for explicit agreement; best as part of ceremonial or relational practice.",
    "review_cycle": "Quarterly",
    "usage_example": "affect.open('heart', intensity=3, mode='curious', session_context=session)",
    "audience": "hybrid",
    "stage": "living",
    "output_dir": "./lib"
}
