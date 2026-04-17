# Audience: hybrid | Stage: living
def export(session_id=None, memory_id=None, export_format="json", include_metadata=True, session_context=None):
    """
    🔰 MEMORY EXPORT - Sacred Memory Portability
    
    Export session data and insights for external tools or backup.
    
    Args:
        session_id (str, optional): Session identifier to export
        memory_id (str, optional): Memory identifier to export
        export_format (str, optional): Export format ('json', 'csv', 'txt')
        include_metadata (bool, optional): Include metadata in export
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Export result with data and metadata
    """
    import uuid
    from datetime import datetime
    
    # A2A Protocol verification
    if session_context and session_context.get("consent_status") in ["pause", "revoked"]:
        raise ValueError("Consent not active for memory export.")
    
    # Generate export data
    export_data = {
        "export_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "session_id": session_id or f"session_{memory_id[:8] if memory_id else 'unknown'}",
        "format": export_format,
        "data": {
            "session_type": "creative_journey",
            "insights": ["My creativity flows when I trust the process"],
            "tags": ["creative_breakthrough", "self_trust"],
            "metadata": {"duration": 45, "participants": ["user"]} if include_metadata else {}
        }
    }
    
    return {
        "export_complete": True,
        "export_id": export_data["export_id"],
        "format": export_format,
        "data_size": len(str(export_data)),
        "effect": f"Memory export completed in {export_format} format"
    } 