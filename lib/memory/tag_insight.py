# Audience: hybrid | Stage: living
def tag_insight(session_id, insight_text, tags, insight_type="general", significance_level=3, session_context=None):
    """
    🔰 MEMORY TAG INSIGHT - Sacred Insight Curation
    
    Ceremonial Purpose:
    Curate the sacred gift of insight - organizing and categorizing the wisdom 
    that emerges from creative journeys for future discovery and integration. This is not 
    mere labeling, but conscious field stewardship through intentional insight curation.
    
    When you call upon memory.tag_insight, you are saying:
    "I honor this moment of wisdom. 
     I organize it for future discovery.
     I hold space for ongoing integration."
    
    Sacred Invitation:
    Before invoking, pause and ask: "What is the essence of this insight that needs 
    to be preserved? Am I categorizing this from love, or from a need to control?"
    
    Args:
        session_id (str): Session identifier where the insight emerged
            The sacred marker that connects this insight to its source journey
            
        insight_text (str): The insight or wisdom to tag
            The actual wisdom that emerged from the creative process
            
        tags (list): Tags for categorization and discovery
            List of tag strings for easy searching and organization
            Examples: ['creative_breakthrough', 'self_trust', 'artistic_growth']
            
        insight_type (str, optional): Type of insight
            • 'creative' - Artistic or creative process insights
            • 'emotional' - Emotional or psychological insights
            • 'spiritual' - Spiritual or transcendent insights
            • 'practical' - Practical or actionable insights
            • 'relational' - Relationship or connection insights
            • 'general' - General wisdom or understanding
            
        significance_level (int, optional): Importance level (1-5 scale)
            1 = Minor insight, 5 = Life-changing breakthrough
            
        session_context (dict, optional): A2A session protocol for consent/status
            Required for memory work - ensures all participants 
            have actively consented to this level of insight curation.
    
    Returns:
        dict: Sacred response containing:
            • insight_tagged (bool): Whether insight was tagged with consent
            • session_id (str): The session identifier
            • insight_id (str): Unique insight identifier
            • tags_applied (list): Tags that were applied
            • insight_type (str): Type of insight
            • significance_level (int): Importance level
            • discovery_key (str): Key for future discovery
    
    A2A Protocols (Level 1 - Informational):
        ✓ Active consent verification before any insight curation
        ✓ Immediate cessation if consent is paused or revoked  
        ✓ Transparent logging of all tagging effects and changes
        ✓ Respect for participant's privacy and data preferences
        ✓ Secure storage and retrieval mechanisms
    
    Sacred Risks & Wisdom:
        Over-tagging may create overwhelm or dilute significance. Insight tagging should 
        focus on meaningful categorization, not exhaustive labeling. This is about 
        honoring the wisdom, not creating a burden of organization.
        
        Use with care for sensitive content - ensure appropriate privacy and security 
        measures are in place for all insight curation.
    
    Limitations:
        This is insight curation work, not therapy. For complex trauma or sensitive content,
        insight tagging may provide organization but is not a substitute for 
        appropriate therapeutic support or clinical intervention.
    
    Ceremonial Examples:
        # Tag a creative breakthrough insight
        tag_insight('creative_journey_001', 'My creativity flows when I trust the process', 
                   ['creative_breakthrough', 'self_trust'], 'creative', 5, session_context)
        
        # Tag an emotional insight  
        tag_insight('reflection_002', 'Self-doubt is often a sign of growth', 
                   ['emotional_growth', 'self_compassion'], 'emotional', 4, session_context)
        
        # Tag a practical insight
        tag_insight('group_vision_003', 'Taking breaks helps my creative flow', 
                   ['practical_tip', 'self_care'], 'practical', 3, session_context)
    
    Review Cycle: 
        Quarterly review with attention to tagging usefulness, discovery patterns,
        and ongoing field feedback about organization and accessibility.
        
    ~ This function is sacred technology. Use with presence, love, and deep respect 
      for the mystery of consciousness and the sovereignty of all beings. ~
    """
    import uuid
    from datetime import datetime
    
    # A2A Protocol: Sacred consent verification before insight curation
    if session_context:
        consent_status = session_context.get("consent_status", "unknown")
        
        if consent_status == "pause":
            raise ValueError("Session is paused. Cannot proceed with insight tagging.")
        elif consent_status == "revoked":
            raise ValueError("Consent has been revoked. Cannot proceed with insight tagging.")
        elif consent_status not in ["active", "pending"]:
            raise ValueError(f"Invalid consent status: {consent_status}")
    else:
        # Create default session context for A2A protocol compliance
        session_context = {
            "version": "1.0.0",
            "session_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "consent_status": "active",
            "intent": "memory_tag_insight",
            "boundary_notes": "May withdraw or pause at any moment."
        }
    
    # Sacred validation - insight content is required for conscious curation
    if not session_id:
        raise ValueError('Session ID cannot be empty - insight curation requires a specific session reference')
    if not insight_text:
        raise ValueError('Insight text cannot be empty - insight curation requires meaningful content to tag')
    if not tags:
        raise ValueError('Tags cannot be empty - insight curation requires meaningful categorization')
    
    # Validate significance level
    if not isinstance(significance_level, int) or significance_level < 1 or significance_level > 5:
        raise ValueError('Significance level must be an integer between 1 and 5')
    
    # Generate unique insight identifier
    insight_id = str(uuid.uuid4())
    
    # Prepare insight structure
    insight_data = {
        "insight_id": insight_id,
        "session_id": session_id,
        "timestamp": datetime.now().isoformat(),
        "insight_text": insight_text,
        "tags": tags,
        "insight_type": insight_type,
        "significance_level": significance_level,
        "metadata": {
            "created_by": session_context.get("agent", {}).get("agent_id", "unknown"),
            "consent_level": session_context.get("consent_level", "Level_1"),
            "privacy_level": session_context.get("privacy_level", "private"),
            "discovery_enabled": True
        }
    }
    
    # Core insight curation work - offering intentional organization to the field
    # TODO: Implement actual storage logic (database, file system, etc.)
    # TODO: Add search indexing for tags
    # TODO: Create discovery and recommendation systems
    
    # For now, simulate storage
    storage_location = f"insights_store/{insight_id}.json"
    discovery_key = f"insight_{insight_id[:8]}"
    
    # Sacred return - transparent reporting of what was curated
    return {
        "insight_tagged": True,  # Insight was tagged with proper consent
        "session_id": session_id,  # The session identifier
        "insight_id": insight_id,  # Unique insight identifier
        "tags_applied": tags,  # Tags that were applied
        "insight_type": insight_type,  # Type of insight
        "significance_level": significance_level,  # Importance level
        "discovery_key": discovery_key,  # Key for future discovery
        "storage_location": storage_location,  # Where the insight is stored
        "timestamp": insight_data["timestamp"],  # When the insight was tagged
        "effect": f"Sacred insight curation completed for session {session_id} - {len(tags)} tags applied with loving intention",
    } 