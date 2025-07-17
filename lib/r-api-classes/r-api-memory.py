# Audience: hybrid | Stage: living
"""
🔰 R.API MEMORY - Sacred Memory Management for Dream Workshop

This module provides session memory, journaling, and insight management for Dream Workshop.
It enables users to save, replay, tag, and evolve their creative journey across sessions.

Core Functions:
- save_session(): Save session data and insights
- replay(): Replay and review past sessions
- tag_insight(): Tag and categorize insights
- export(): Export session data and insights
- search_memories(): Search through past sessions
- evolve_ideas(): Track idea evolution over time

Features:
- Session journaling with rich metadata
- Insight tagging and categorization
- Memory replay with context preservation
- Idea evolution tracking
- Export capabilities for external tools
- Search and discovery across sessions

All functions follow A2A (Agent-to-Agent) protocol for consent and safety.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from memory import save_session, replay, tag_insight, export, search_memories, evolve_ideas

def memory_save_session(session_id, session_data, insights=None, tags=None, session_context=None):
    """
    🔰 MEMORY SAVE SESSION - Sacred Memory Preservation
    
    Save session data, insights, and metadata for Dream Workshop's memory system.
    
    Args:
        session_id (str): Unique identifier for the session
        session_data (dict): Core session information to preserve
        insights (list, optional): Insights and wisdom from the session
        tags (list, optional): Tags for categorization and discovery
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred response containing memory preservation results
    
    Example:
        session_data = {
            'session_type': 'creative_journey',
            'duration': 45,
            'key_moments': ['Breakthrough in understanding creative blocks']
        }
        result = memory_save_session('creative_journey_001', session_data, 
                                   insights=['My creativity flows when I trust the process'],
                                   tags=['creative_breakthrough'], session_context=session)
        print(f"Session saved: {result['session_saved']}")
    """
    return save_session(session_id, session_data, insights, tags, session_context)

def memory_replay(session_id=None, memory_id=None, replay_mode="full", session_context=None):
    """
    🔰 MEMORY REPLAY - Sacred Memory Revisitation
    
    Replay and review past sessions with context preservation.
    
    Args:
        session_id (str, optional): Session identifier to replay
        memory_id (str, optional): Memory identifier to replay
        replay_mode (str, optional): How to replay the memory
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred response containing replayed memory data
    
    Example:
        result = memory_replay('creative_journey_001', replay_mode='insights', session_context=session)
        print(f"Replayed insights: {result['insights']}")
    """
    return replay(session_id, memory_id, replay_mode, session_context)

def memory_tag_insight(session_id, insight_text, tags, insight_type="general", significance_level=3, session_context=None):
    """
    🔰 MEMORY TAG INSIGHT - Sacred Insight Curation
    
    Tag and categorize insights for better organization and discovery.
    
    Args:
        session_id (str): Session identifier where the insight emerged
        insight_text (str): The insight or wisdom to tag
        tags (list): Tags for categorization and discovery
        insight_type (str, optional): Type of insight
        significance_level (int, optional): Importance level (1-5 scale)
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Sacred response containing insight curation results
    
    Example:
        result = memory_tag_insight('creative_journey_001', 
                                  'My creativity flows when I trust the process',
                                  ['creative_breakthrough', 'self_trust'], 
                                  'creative', 5, session_context=session)
        print(f"Insight tagged: {result['insight_tagged']}")
    """
    return tag_insight(session_id, insight_text, tags, insight_type, significance_level, session_context)

def memory_export(session_id=None, memory_id=None, export_format="json", include_metadata=True, session_context=None):
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
    
    Example:
        result = memory_export('creative_journey_001', export_format='json', session_context=session)
        print(f"Export completed: {result['export_complete']}")
    """
    return export(session_id, memory_id, export_format, include_metadata, session_context)

def memory_search_memories(query, search_type="all", limit=10, session_context=None):
    """
    🔰 MEMORY SEARCH - Sacred Memory Discovery
    
    Search through past sessions and insights for discovery and integration.
    
    Args:
        query (str): Search query or keywords
        search_type (str, optional): What to search ('all', 'insights', 'sessions', 'tags')
        limit (int, optional): Maximum number of results
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Search results with matches and metadata
    
    Example:
        result = memory_search_memories('creativity', search_type='insights', session_context=session)
        print(f"Found {result['results_count']} relevant results")
    """
    return search_memories(query, search_type, limit, session_context)

def memory_evolve_ideas(idea_id=None, idea_text=None, evolution_type="development", session_context=None):
    """
    🔰 MEMORY EVOLVE IDEAS - Sacred Idea Evolution
    
    Track idea evolution over time across sessions for continuous development.
    
    Args:
        idea_id (str, optional): Existing idea identifier
        idea_text (str, optional): New idea or evolution
        evolution_type (str, optional): Type of evolution ('development', 'refinement', 'expansion')
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Evolution tracking result with idea history
    
    Example:
        result = memory_evolve_ideas(idea_text='Refined creative project concept', 
                                   evolution_type='refinement', session_context=session)
        print(f"Evolution tracked: {result['evolution_complete']}")
    """
    return evolve_ideas(idea_id, idea_text, evolution_type, session_context)

# Example usage and integration patterns
def example_dream_workshop_memory_integration():
    """
    Example of how to integrate memory module with Dream Workshop session flow.
    """
    # Create session context
    session_context = {
        "version": "1.0.0",
        "session_id": "dream_workshop_session_001",
        "consent_status": "active",
        "intent": "creative_guidance"
    }
    
    # 1. Save a creative journey session
    print("=== Saving Session ===")
    session_data = {
        "session_type": "creative_journey",
        "duration": 45,
        "participants": ["user"],
        "key_moments": [
            "Breakthrough in understanding creative blocks",
            "Discovery of new artistic direction"
        ],
        "emotional_arc": [
            {"time": "0:00", "emotion": "frustrated", "intensity": 3},
            {"time": "45:00", "emotion": "inspired", "intensity": 5}
        ],
        "creative_outputs": [
            "New painting concept",
            "Poem about creative freedom"
        ]
    }
    
    insights = [
        "My creativity flows when I trust the process",
        "Self-doubt is often a sign of growth"
    ]
    
    tags = ["creative_breakthrough", "self_trust", "artistic_growth"]
    
    save_result = memory_save_session("creative_journey_001", session_data, insights, tags, session_context)
    print(f"Session saved: {save_result['session_saved']}")
    print(f"Insights preserved: {save_result['insights_count']}")
    
    # 2. Tag a specific insight
    print("\n=== Tagging Insight ===")
    tag_result = memory_tag_insight("creative_journey_001", 
                                  "My creativity flows when I trust the process",
                                  ["creative_breakthrough", "self_trust"], 
                                  "creative", 5, session_context)
    print(f"Insight tagged: {tag_result['insight_tagged']}")
    print(f"Tags applied: {tag_result['tags_applied']}")
    
    # 3. Replay session insights
    print("\n=== Replaying Insights ===")
    replay_result = memory_replay("creative_journey_001", replay_mode="insights", session_context=session_context)
    print(f"Replay mode: {replay_result['replay_mode']}")
    print(f"Insights replayed: {len(replay_result['insights'])}")
    
    # 4. Search for related memories
    print("\n=== Searching Memories ===")
    search_result = memory_search_memories("creativity", search_type="insights", session_context=session_context)
    print(f"Search query: {search_result['query']}")
    print(f"Results found: {search_result['results_count']}")
    
    # 5. Track idea evolution
    print("\n=== Tracking Idea Evolution ===")
    evolve_result = memory_evolve_ideas(idea_text="Refined creative project concept", 
                                      evolution_type="refinement", session_context=session_context)
    print(f"Evolution tracked: {evolve_result['evolution_complete']}")
    print(f"Evolution type: {evolve_result['evolution_type']}")
    
    # 6. Export session data
    print("\n=== Exporting Session ===")
    export_result = memory_export("creative_journey_001", export_format="json", session_context=session_context)
    print(f"Export completed: {export_result['export_complete']}")
    print(f"Export format: {export_result['format']}")
    
    return {
        "session_saved": save_result,
        "insight_tagged": tag_result,
        "session_replayed": replay_result,
        "memories_searched": search_result,
        "idea_evolved": evolve_result,
        "session_exported": export_result
    }

def example_memory_workflow():
    """
    Example of a complete memory workflow for Dream Workshop.
    """
    session_context = {
        "version": "1.0.0",
        "session_id": "memory_workflow_demo",
        "consent_status": "active",
        "intent": "memory_demonstration"
    }
    
    # Complete workflow demonstration
    workflow_steps = []
    
    # Step 1: Save session
    session_data = {"session_type": "reflection", "duration": 30}
    step1 = memory_save_session("reflection_001", session_data, 
                               insights=["Taking breaks helps my creative flow"],
                               tags=["self_care", "practical_tip"], 
                               session_context=session_context)
    workflow_steps.append(("Save Session", step1))
    
    # Step 2: Tag additional insight
    step2 = memory_tag_insight("reflection_001", 
                              "Gentle self-compassion opens creative channels",
                              ["self_compassion", "emotional_growth"], 
                              "emotional", 4, session_context=session_context)
    workflow_steps.append(("Tag Insight", step2))
    
    # Step 3: Search for related insights
    step3 = memory_search_memories("self-compassion", search_type="insights", session_context=session_context)
    workflow_steps.append(("Search Memories", step3))
    
    # Step 4: Replay session summary
    step4 = memory_replay("reflection_001", replay_mode="summary", session_context=session_context)
    workflow_steps.append(("Replay Summary", step4))
    
    return {
        "workflow_complete": True,
        "steps": workflow_steps,
        "total_steps": len(workflow_steps)
    }

if __name__ == "__main__":
    print("🔰 R.API MEMORY - Sacred Memory Management")
    print("=" * 50)
    
    # Run example integration
    result = example_dream_workshop_memory_integration()
    
    print("\n" + "=" * 50)
    print("Memory Workflow Demo:")
    workflow = example_memory_workflow()
    for step_name, step_result in workflow["steps"]:
        print(f"\n{step_name}:")
        print(f"  Status: {step_result.get('session_saved', step_result.get('insight_tagged', step_result.get('search_complete', 'Completed')))}")
        print(f"  Effect: {step_result.get('effect', 'Step completed')}") 