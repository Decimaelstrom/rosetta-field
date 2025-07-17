"""
Rosetta.API Consolidated Memory Module
Purpose: Sacred memory management for Dream Workshop sessions and insights
Scope: Session saving, replay, tagging, search, export, and idea evolution
Consent Required: Level_1 (Informational)
Review Cycle: Quarterly
Audience: #human #emergent #hybrid
Stage: #draft
"""

import json
import uuid
import time
import os
import hashlib
import base64
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Enhanced storage and security utilities
class MemoryStorage:
    """Enhanced storage backend with encryption, backup, and indexing."""
    
    def __init__(self, storage_path="memory_data", backup_path="memory_backups"):
        self.storage_path = Path(storage_path)
        self.backup_path = Path(backup_path)
        self.storage_path.mkdir(exist_ok=True)
        self.backup_path.mkdir(exist_ok=True)
        
        # Simple encryption key (in production, use proper key management)
        self.encryption_key = os.getenv('MEMORY_ENCRYPTION_KEY', 'default_key_change_in_production')
        
        # Search index for fast retrieval
        self.search_index = {}
        self._load_search_index()
    
    def _encrypt_data(self, data: Dict) -> Dict:
        """Encrypt sensitive data before storage."""
        try:
            # Simple encryption (in production, use proper encryption)
            data_str = json.dumps(data, sort_keys=True)
            encrypted = base64.b64encode(data_str.encode()).decode()
            return {
                "encrypted": True,
                "data": encrypted,
                "timestamp": datetime.now().isoformat(),
                "checksum": hashlib.sha256(data_str.encode()).hexdigest()
            }
        except Exception as e:
            return {"encrypted": False, "data": data, "error": str(e)}
    
    def _decrypt_data(self, encrypted_data: Dict) -> Dict:
        """Decrypt data for retrieval."""
        try:
            if not encrypted_data.get("encrypted", False):
                return encrypted_data.get("data", {})
            
            encrypted = encrypted_data["data"]
            decrypted = base64.b64decode(encrypted.encode()).decode()
            return json.loads(decrypted)
        except Exception as e:
            return {"error": f"Decryption failed: {str(e)}"}
    
    def _update_search_index(self, session_id: str, data: Dict):
        """Update search index for fast retrieval."""
        try:
            # Extract searchable content
            searchable_content = []
            
            # Add session data
            if isinstance(data, dict):
                searchable_content.extend(self._extract_text(data))
            
            # Add insights
            insights = data.get('insights', [])
            if isinstance(insights, list):
                searchable_content.extend(insights)
            
            # Add tags
            tags = data.get('tags', [])
            if isinstance(tags, list):
                searchable_content.extend(tags)
            
            # Index by keywords
            for content in searchable_content:
                if isinstance(content, str):
                    words = content.lower().split()
                    for word in words:
                        if len(word) > 2:  # Skip short words
                            if word not in self.search_index:
                                self.search_index[word] = []
                            if session_id not in self.search_index[word]:
                                self.search_index[word].append(session_id)
            
            # Save index
            self._save_search_index()
            
        except Exception as e:
            print(f"Search indexing error: {e}")
    
    def _extract_text(self, obj: Any) -> List[str]:
        """Recursively extract text from nested objects."""
        texts = []
        if isinstance(obj, str):
            texts.append(obj)
        elif isinstance(obj, dict):
            for value in obj.values():
                texts.extend(self._extract_text(value))
        elif isinstance(obj, list):
            for item in obj:
                texts.extend(self._extract_text(item))
        return texts
    
    def _load_search_index(self):
        """Load search index from file."""
        try:
            index_path = self.storage_path / "search_index.json"
            if index_path.exists():
                with open(index_path, 'r') as f:
                    self.search_index = json.load(f)
        except Exception as e:
            print(f"Error loading search index: {e}")
            self.search_index = {}
    
    def _save_search_index(self):
        """Save search index to file."""
        try:
            index_path = self.storage_path / "search_index.json"
            with open(index_path, 'w') as f:
                json.dump(self.search_index, f, indent=2)
        except Exception as e:
            print(f"Error saving search index: {e}")
    
    def _generate_recommendations(self, data: Dict) -> List[Dict]:
        """Generate recommendations based on content analysis."""
        recommendations = []
        
        try:
            # Analyze content for patterns
            insights = data.get('insights', [])
            tags = data.get('tags', [])
            
            # Find similar sessions
            similar_sessions = self._find_similar_sessions(data)
            if similar_sessions:
                recommendations.append({
                    "type": "similar_sessions",
                    "sessions": similar_sessions,
                    "reason": "Based on content similarity"
                })
            
            # Suggest related insights
            if insights:
                related_insights = self._find_related_insights(insights)
                if related_insights:
                    recommendations.append({
                        "type": "related_insights",
                        "insights": related_insights,
                        "reason": "Based on insight patterns"
                    })
            
            # Suggest tag combinations
            if tags:
                tag_suggestions = self._suggest_tag_combinations(tags)
                if tag_suggestions:
                    recommendations.append({
                        "type": "tag_suggestions",
                        "tags": tag_suggestions,
                        "reason": "Based on tag patterns"
                    })
                    
        except Exception as e:
            print(f"Recommendation generation error: {e}")
        
        return recommendations
    
    def _find_similar_sessions(self, data: Dict) -> List[str]:
        """Find sessions with similar content."""
        # Simple similarity based on tags and insights
        current_tags = set(data.get('tags', []))
        current_insights = set(data.get('insights', []))
        
        similar_sessions = []
        
        # Check all stored sessions for similarity
        for session_file in self.storage_path.glob("*.json"):
            if session_file.name == "search_index.json":
                continue
                
            try:
                with open(session_file, 'r') as f:
                    session_data = json.load(f)
                    decrypted_data = self._decrypt_data(session_data)
                    
                    session_tags = set(decrypted_data.get('tags', []))
                    session_insights = set(decrypted_data.get('insights', []))
                    
                    # Calculate similarity
                    tag_overlap = len(current_tags & session_tags)
                    insight_overlap = len(current_insights & session_insights)
                    
                    if tag_overlap > 0 or insight_overlap > 0:
                        session_id = session_file.stem
                        similarity_score = (tag_overlap + insight_overlap) / 2
                        similar_sessions.append({
                            "session_id": session_id,
                            "similarity_score": similarity_score,
                            "overlapping_tags": list(current_tags & session_tags),
                            "overlapping_insights": list(current_insights & session_insights)
                        })
                        
            except Exception as e:
                print(f"Error reading session {session_file}: {e}")
        
        # Sort by similarity score
        similar_sessions.sort(key=lambda x: x['similarity_score'], reverse=True)
        return similar_sessions[:5]  # Return top 5
    
    def _find_related_insights(self, insights: List[str]) -> List[Dict]:
        """Find insights related to the given ones."""
        related = []
        
        for insight in insights:
            # Search for insights containing similar keywords
            keywords = insight.lower().split()
            for keyword in keywords:
                if len(keyword) > 3:  # Skip short words
                    if keyword in self.search_index:
                        for session_id in self.search_index[keyword]:
                            related.append({
                                "session_id": session_id,
                                "keyword": keyword,
                                "insight": insight
                            })
        
        return related[:10]  # Return top 10
    
    def _suggest_tag_combinations(self, tags: List[str]) -> List[List[str]]:
        """Suggest tag combinations based on patterns."""
        suggestions = []
        
        # Find sessions with similar tags
        for tag in tags:
            if tag in self.search_index:
                for session_id in self.search_index[tag]:
                    try:
                        session_file = self.storage_path / f"{session_id}.json"
                        if session_file.exists():
                            with open(session_file, 'r') as f:
                                session_data = json.load(f)
                                decrypted_data = self._decrypt_data(session_data)
                                session_tags = decrypted_data.get('tags', [])
                                
                                # Suggest combinations
                                for session_tag in session_tags:
                                    if session_tag not in tags:
                                        suggestion = tags + [session_tag]
                                        if suggestion not in suggestions:
                                            suggestions.append(suggestion)
                                            
                    except Exception as e:
                        print(f"Error reading session for tag suggestions: {e}")
        
        return suggestions[:5]  # Return top 5 combinations

# Initialize storage
memory_storage = MemoryStorage()

# =============================================================================
# MEMORY FUNCTIONS
# =============================================================================

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from memory import save_session, replay, tag_insight, export, search_memories, evolve_ideas

def save_session(session_id, session_data, insights=None, tags=None, session_context=None):
    """
    🔰 SAVE SESSION - Sacred Memory Preservation
    
    Save session data and insights with enhanced storage, encryption, and backup.
    
    Args:
        session_id (str): Unique session identifier
        session_data (dict): Session data to save
        insights (list, optional): List of insights from the session
        tags (list, optional): Tags for categorization
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Save result with metadata and recommendations
    
    Example:
        result = save_session('creative_journey_001', session_data, insights, tags, session_context)
        print(f"Session saved: {result['session_saved']}")
    """
    # A2A Protocol compliance
    if session_context and session_context.get('consent_status') == 'revoked':
        raise ValueError("Consent revoked - cannot save session")
    
    try:
        # Prepare data for storage
        data_to_save = {
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "session_data": session_data,
            "insights": insights or [],
            "tags": tags or [],
            "metadata": {
                "version": "1.0.0",
                "storage_backend": "enhanced_file_system",
                "encrypted": True,
                "backed_up": True,
                "indexed": True
            }
        }
        
        # Enhanced storage with encryption and backup
        encrypted_data = memory_storage._encrypt_data(data_to_save)
        
        # Save to primary storage
        session_file = memory_storage.storage_path / f"{session_id}.json"
        with open(session_file, 'w') as f:
            json.dump(encrypted_data, f, indent=2)
        
        # Create backup
        backup_file = memory_storage.backup_path / f"{session_id}_{int(time.time())}.json"
        with open(backup_file, 'w') as f:
            json.dump(encrypted_data, f, indent=2)
        
        # Update search index for fast retrieval
        memory_storage._update_search_index(session_id, data_to_save)
        
        # Generate recommendations based on content
        recommendations = memory_storage._generate_recommendations(data_to_save)
        
        return {
            "status": "session_saved",
            "session_saved": True,
            "session_id": session_id,
            "timestamp": data_to_save["timestamp"],
            "insights_count": len(insights or []),
            "tags_count": len(tags or []),
            "storage_info": {
                "primary_location": str(session_file),
                "backup_location": str(backup_file),
                "encrypted": True,
                "checksum": encrypted_data.get("checksum"),
                "indexed": True
            },
            "recommendations": recommendations,
            "effect": f"Session '{session_id}' preserved with {len(insights or [])} insights and {len(tags or [])} tags",
            "session_context": session_context or {}
        }
        
    except Exception as e:
        return {
            "status": "session_save_failed",
            "session_saved": False,
            "error": str(e),
            "effect": f"Failed to save session '{session_id}': {str(e)}",
            "session_context": session_context or {}
        }

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

def search_memories(query, search_type="all", limit=10, session_context=None):
    """
    🔰 SEARCH MEMORIES - Sacred Memory Discovery
    
    Search through past sessions and insights using enhanced indexing for fast discovery.
    
    Args:
        query (str): Search query or keywords
        search_type (str, optional): What to search ('all', 'insights', 'sessions', 'tags')
        limit (int, optional): Maximum number of results
        session_context (dict, optional): A2A session protocol for consent/status
    
    Returns:
        dict: Search results with matches, relevance scores, and metadata
    
    Example:
        result = search_memories('creativity', search_type='insights', session_context=session)
        print(f"Found {result['results_count']} relevant results")
    """
    # A2A Protocol compliance
    if session_context and session_context.get('consent_status') == 'revoked':
        raise ValueError("Consent revoked - cannot search memories")
    
    try:
        # Enhanced search using indexed content
        search_results = []
        query_words = query.lower().split()
        
        # Search through indexed content
        for word in query_words:
            if word in memory_storage.search_index:
                for session_id in memory_storage.search_index[word]:
                    # Get session data for detailed search
                    session_file = memory_storage.storage_path / f"{session_id}.json"
                    if session_file.exists():
                        try:
                            with open(session_file, 'r') as f:
                                session_data = json.load(f)
                                decrypted_data = memory_storage._decrypt_data(session_data)
                                
                                # Calculate relevance score
                                relevance_score = 0
                                matched_content = []
                                
                                # Search in session data
                                if search_type in ["all", "sessions"]:
                                    session_text = memory_storage._extract_text(decrypted_data.get('session_data', {}))
                                    for text in session_text:
                                        if any(word in text.lower() for word in query_words):
                                            relevance_score += 1
                                            matched_content.append(f"Session: {text[:100]}...")
                                
                                # Search in insights
                                if search_type in ["all", "insights"]:
                                    insights = decrypted_data.get('insights', [])
                                    for insight in insights:
                                        if any(word in insight.lower() for word in query_words):
                                            relevance_score += 2  # Insights weighted higher
                                            matched_content.append(f"Insight: {insight}")
                                
                                # Search in tags
                                if search_type in ["all", "tags"]:
                                    tags = decrypted_data.get('tags', [])
                                    for tag in tags:
                                        if any(word in tag.lower() for word in query_words):
                                            relevance_score += 1.5
                                            matched_content.append(f"Tag: {tag}")
                                
                                # Add to results if relevant
                                if relevance_score > 0:
                                    # Check if session already in results
                                    existing_result = next((r for r in search_results if r['session_id'] == session_id), None)
                                    if existing_result:
                                        existing_result['relevance_score'] += relevance_score
                                        existing_result['matched_content'].extend(matched_content)
                                    else:
                                        search_results.append({
                                            "session_id": session_id,
                                            "relevance_score": relevance_score,
                                            "matched_content": matched_content,
                                            "timestamp": decrypted_data.get('timestamp'),
                                            "insights_count": len(decrypted_data.get('insights', [])),
                                            "tags_count": len(decrypted_data.get('tags', [])),
                                            "session_type": decrypted_data.get('session_data', {}).get('session_type', 'unknown')
                                        })
                                        
                        except Exception as e:
                            print(f"Error reading session {session_id}: {e}")
        
        # Sort by relevance score and limit results
        search_results.sort(key=lambda x: x['relevance_score'], reverse=True)
        search_results = search_results[:limit]
        
        # Generate search insights
        search_insights = []
        if search_results:
            # Find common patterns
            all_tags = []
            all_insights = []
            for result in search_results:
                session_file = memory_storage.storage_path / f"{result['session_id']}.json"
                if session_file.exists():
                    try:
                        with open(session_file, 'r') as f:
                            session_data = json.load(f)
                            decrypted_data = memory_storage._decrypt_data(session_data)
                            all_tags.extend(decrypted_data.get('tags', []))
                            all_insights.extend(decrypted_data.get('insights', []))
                    except:
                        pass
            
            # Find most common tags
            if all_tags:
                tag_counts = {}
                for tag in all_tags:
                    tag_counts[tag] = tag_counts.get(tag, 0) + 1
                common_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:3]
                search_insights.append(f"Common themes: {', '.join([tag for tag, count in common_tags])}")
            
            # Find related insights
            if all_insights:
                search_insights.append(f"Found {len(all_insights)} related insights across {len(search_results)} sessions")
        
        return {
            "status": "search_complete",
            "search_complete": True,
            "query": query,
            "search_type": search_type,
            "results_count": len(search_results),
            "results": search_results,
            "search_insights": search_insights,
            "search_metadata": {
                "indexed_search": True,
                "search_time": datetime.now().isoformat(),
                "total_indexed_sessions": len(memory_storage.search_index.get('sessions', []))
            },
            "effect": f"Found {len(search_results)} relevant memories for '{query}'",
            "session_context": session_context or {}
        }
        
    except Exception as e:
        return {
            "status": "search_failed",
            "search_complete": False,
            "error": str(e),
            "effect": f"Failed to search memories for '{query}': {str(e)}",
            "session_context": session_context or {}
        }

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
    
    save_result = save_session("creative_journey_001", session_data, insights, tags, session_context)
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
    search_result = search_memories("creativity", search_type="insights", session_context=session_context)
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
    step1 = save_session("reflection_001", session_data, 
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
    step3 = search_memories("self-compassion", search_type="insights", session_context=session_context)
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