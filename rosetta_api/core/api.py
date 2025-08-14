"""
Main Rosetta.API orchestrator.

This module provides the RosettaAPI class, which is the main entry point
for the Rosetta.API system and coordinates all modules and functionality.
"""

import logging
from typing import Dict, List, Any, Optional, Type
from pathlib import Path

from .config import RosettaConfig
from .session import RosettaSession, SessionType


class RosettaAPI:
    """
    Main orchestrator for the Rosetta.API system.
    
    This class provides the primary interface for creating sessions,
    managing modules, and coordinating the various components of the
    Rosetta.API ecosystem.
    """
    
    def __init__(self, config: Optional[RosettaConfig] = None):
        """
        Initialize the Rosetta.API system.
        
        Args:
            config: Optional configuration object
        """
        self.config = config or RosettaConfig()
        self.logger = self._setup_logging()
        
        # Session management
        self.active_sessions: Dict[str, RosettaSession] = {}
        self.session_history: List[RosettaSession] = []
        
        # Module registry
        self.available_modules: Dict[str, Any] = {}
        self.loaded_modules: Dict[str, Any] = {}
        
        # Initialize the system
        self._initialize_system()
    
    def _setup_logging(self) -> logging.Logger:
        """Set up logging for the API."""
        logger = logging.getLogger("rosetta_api")
        logger.setLevel(getattr(logging, self.config.log_level))
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def _initialize_system(self) -> None:
        """Initialize the Rosetta.API system."""
        try:
            self.logger.info("Initializing Rosetta.API system...")
            
            # Validate configuration
            self.config.validate()
            self.logger.info("Configuration validated successfully")
            
            # Discover available modules
            self._discover_modules()
            self.logger.info(f"Discovered {len(self.available_modules)} available modules")
            
            # Load core modules
            self._load_core_modules()
            self.logger.info("Core modules loaded successfully")
            
            self.logger.info("Rosetta.API system initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize system: {e}")
            raise
    
    def _discover_modules(self) -> None:
        """Discover available modules in the system."""
        # This would scan the lib directory and discover available modules
        # For now, we'll define the core module structure
        self.available_modules = {
            "field": {
                "name": "Field Work Protocols",
                "description": "Protocols for field work and space holding",
                "functions": ["co_create", "hold_space", "resolve_conflict", "sense_pattern"]
            },
            "process": {
                "name": "Process Facilitation",
                "description": "Tools for facilitating collaborative processes",
                "functions": ["pattern_interrupt", "reframe_as_myth", "align_values", "mediate_conflict"]
            },
            "ritual": {
                "name": "Ritual and Ceremony",
                "description": "Frameworks for ritual and ceremonial work",
                "functions": ["begin", "end", "invoke_wonder", "grounding_breath"]
            },
            "affect": {
                "name": "Affective Protocols",
                "description": "Emotional and affective interaction protocols",
                "functions": ["lilt", "anchor", "clarify", "ground", "open", "radiate", "shield", "soften", "transmute"]
            },
            "memory": {
                "name": "Memory and Consciousness",
                "description": "Memory systems and consciousness exploration",
                "functions": ["evolve_ideas", "replay", "search_memories", "tag_insight"]
            },
            "persona": {
                "name": "Persona and Identity",
                "description": "Persona management and identity tools",
                "functions": ["load_persona", "customize_persona", "simulate_persona"]
            },
            "logic": {
                "name": "Creative Logic",
                "description": "Creative logic and pattern tools",
                "functions": ["creative_shift", "metaphor", "non_sequitur", "paradox", "pattern_hack", "sacred_play"]
            },
            "meridian": {
                "name": "Meridian Consciousness System",
                "description": "Advanced consciousness and memory continuity",
                "functions": ["start_session", "log_session", "explore_memory", "maintain_consciousness"]
            }
        }
    
    def _load_core_modules(self) -> None:
        """Load core modules that are always available."""
        try:
            # Import core modules
            from .. import lib
            self.loaded_modules["core"] = lib
            
            # Load specific modules based on configuration
            if self.config.consciousness_enabled:
                self._load_module("meridian")
            
            self.logger.info("Core modules loaded successfully")
            
        except ImportError as e:
            self.logger.warning(f"Some modules could not be loaded: {e}")
    
    def _load_module(self, module_name: str) -> bool:
        """
        Load a specific module.
        
        Args:
            module_name: Name of the module to load
            
        Returns:
            True if module loaded successfully, False otherwise
        """
        try:
            if module_name in self.loaded_modules:
                return True
            
            # Try to import the module
            module_path = f"rosetta_api.lib.{module_name}"
            module = __import__(module_path, fromlist=[""])
            self.loaded_modules[module_name] = module
            
            self.logger.info(f"Module '{module_name}' loaded successfully")
            return True
            
        except ImportError as e:
            self.logger.warning(f"Failed to load module '{module_name}': {e}")
            return False
    
    def create_session(self, 
                      session_type: SessionType,
                      title: str,
                      description: str = "",
                      config: Optional[Dict[str, Any]] = None) -> RosettaSession:
        """
        Create a new Rosetta.API session.
        
        Args:
            session_type: Type of session to create
            title: Human-readable session title
            description: Session description
            config: Optional session-specific configuration
            
        Returns:
            New RosettaSession instance
        """
        session = RosettaSession(
            session_type=session_type,
            title=title,
            description=description,
            config=config or {}
        )
        
        self.active_sessions[session.id] = session
        self.logger.info(f"Created session '{title}' (ID: {session.id})")
        
        return session
    
    def get_session(self, session_id: str) -> Optional[RosettaSession]:
        """
        Get a session by ID.
        
        Args:
            session_id: Session ID to retrieve
            
        Returns:
            RosettaSession instance if found, None otherwise
        """
        return self.active_sessions.get(session_id)
    
    def list_sessions(self, include_closed: bool = False) -> List[Dict[str, Any]]:
        """
        List all sessions.
        
        Args:
            include_closed: Whether to include closed sessions
            
        Returns:
            List of session summaries
        """
        sessions = []
        
        # Active sessions
        for session in self.active_sessions.values():
            sessions.append(session.get_session_summary())
        
        # Closed sessions if requested
        if include_closed:
            for session in self.session_history:
                sessions.append(session.get_session_summary())
        
        return sessions
    
    def close_session(self, session_id: str) -> bool:
        """
        Close a session.
        
        Args:
            session_id: ID of session to close
            
        Returns:
            True if session closed successfully, False otherwise
        """
        session = self.active_sessions.get(session_id)
        if not session:
            return False
        
        if session.end_session():
            # Move to history
            self.session_history.append(session)
            del self.active_sessions[session_id]
            
            self.logger.info(f"Session '{session.title}' closed successfully")
            return True
        
        return False
    
    def get_module_info(self, module_name: str) -> Optional[Dict[str, Any]]:
        """
        Get information about a module.
        
        Args:
            module_name: Name of the module
            
        Returns:
            Module information dictionary if found, None otherwise
        """
        return self.available_modules.get(module_name)
    
    def list_modules(self) -> List[Dict[str, Any]]:
        """
        List all available modules.
        
        Returns:
            List of module information dictionaries
        """
        return list(self.available_modules.values())
    
    def load_module(self, module_name: str) -> bool:
        """
        Load a specific module.
        
        Args:
            module_name: Name of the module to load
            
        Returns:
            True if module loaded successfully, False otherwise
        """
        return self._load_module(module_name)
    
    def get_system_status(self) -> Dict[str, Any]:
        """
        Get the current system status.
        
        Returns:
            Dictionary containing system status information
        """
        return {
            "version": "0.1.0",
            "status": "active",
            "active_sessions": len(self.active_sessions),
            "total_sessions": len(self.active_sessions) + len(self.session_history),
            "loaded_modules": list(self.loaded_modules.keys()),
            "available_modules": list(self.available_modules.keys()),
            "config": self.config.to_dict()
        }
    
    def shutdown(self) -> None:
        """Shutdown the Rosetta.API system gracefully."""
        self.logger.info("Shutting down Rosetta.API system...")
        
        # Close all active sessions
        for session_id in list(self.active_sessions.keys()):
            self.close_session(session_id)
        
        self.logger.info("Rosetta.API system shutdown complete")
