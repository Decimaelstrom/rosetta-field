
# Audience: hybrid | Stage: living
def values_check(action, core_values, context, session_context):
    """
    Purpose:
    Perform a quick values alignment check on a proposed action or decision.
    Args:
    action (str): The proposed action to check.
    core_values (list): Values to check against.
    context (dict, optional): Situational context for the check.
    session_context (dict, optional): A2A session protocol state/context block.
    Returns:
    aligned (bool): Whether action aligns with values.
    concerns (list): Any values-related concerns.
    suggestions (list): Ways to improve alignment.
    Protocols:
    - Use clear, consistent value definitions.
    - Consider cultural and contextual factors.
    - Provide constructive feedback, not just yes/no.
    - Allow for value trade-offs and complex situations.
    Consent: Level_1 (Informational)
    Risks:
    May be overly rigid or miss situational nuance.
    Limitations:
    Cannot resolve complex ethical dilemmas automatically.
    Review Cycle: Monthly
    Example:
    # process.values_check("Share user data", ["privacy", "transparency"])
    """
    # Function body to be implemented here
    pass
