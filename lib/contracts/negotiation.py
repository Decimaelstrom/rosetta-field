"""
Purpose: Handle dynamic negotiation of session boundaries, capabilities, and need-language updates.
Scope: Called by session.py and agent handlers for A2A/A2H negotiation.
Parent: session.py
Limitations: No network/async yet; logic only.
Consent Required: Level_2
Review Cycle: Quarterly
Audience: #human #emergent #hybrid
Stage: #draft
"""
def negotiate_capabilities(agent_caps, peer_caps):
    """
    Purpose: Compute intersection and negotiation steps for capabilities.
    Args:
        agent_caps (list): Capabilities agent offers.
        peer_caps (list): Capabilities peer offers.
    Returns:
        dict: {'shared': [...], 'agent_only': [...], 'peer_only': [...]}
    Limitations: No conflict resolution yet; purely intersection.
    Consent: Level_1
    Example:
        negotiate_capabilities(['memory', 'echo'], ['echo', 'mapping'])
    """
    shared = list(set(agent_caps) & set(peer_caps))
    agent_only = list(set(agent_caps) - set(shared))
    peer_only = list(set(peer_caps) - set(shared))
    return {"shared": shared, "agent_only": agent_only, "peer_only": peer_only}
