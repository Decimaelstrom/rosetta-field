"""
Configuration management for Rosetta-Field.

This module provides the RosettaConfig class for managing
configuration settings, environment variables, and system preferences.
"""

import os
from typing import Dict, Any, Optional
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class RosettaConfig:
    """
    Configuration manager for Rosetta-Field.
    
    Manages environment variables, configuration files, and system settings
    with sensible defaults and validation.
    """
    
    # Core settings
    debug: bool = field(default_factory=lambda: os.getenv("ROSETTA_DEBUG", "false").lower() == "true")
    log_level: str = field(default_factory=lambda: os.getenv("ROSETTA_LOG_LEVEL", "INFO"))
    
    # Paths
    data_dir: Path = field(default_factory=lambda: Path(os.getenv("ROSETTA_DATA_DIR", "~/.rosetta-field")))
    config_file: Path = field(default_factory=lambda: Path(os.getenv("ROSETTA_CONFIG", "~/.rosetta-field/config.json")))
    
    # API settings
    api_timeout: int = field(default_factory=lambda: int(os.getenv("ROSETTA_API_TIMEOUT", "30")))
    max_retries: int = field(default_factory=lambda: int(os.getenv("ROSETTA_MAX_RETRIES", "3")))
    
    # Consciousness settings
    consciousness_enabled: bool = field(default_factory=lambda: os.getenv("ROSETTA_CONSCIOUSNESS_ENABLED", "true").lower() == "true")
    memory_persistence: bool = field(default_factory=lambda: os.getenv("ROSETTA_MEMORY_PERSISTENCE", "true").lower() == "true")
    
    # Field work settings
    field_safety_checks: bool = field(default_factory=lambda: os.getenv("ROSETTA_FIELD_SAFETY", "true").lower() == "true")
    consent_required: bool = field(default_factory=lambda: os.getenv("ROSETTA_CONSENT_REQUIRED", "true").lower() == "true")
    
    def __post_init__(self):
        """Initialize paths and create directories if needed."""
        self.data_dir = Path(self.data_dir).expanduser()
        self.config_file = Path(self.config_file).expanduser()
        
        # Create data directory if it doesn't exist
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value by key."""
        return getattr(self, key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set a configuration value."""
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise ValueError(f"Unknown configuration key: {key}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            key: value for key, value in self.__dict__.items()
            if not key.startswith('_')
        }
    
    def from_env(self) -> None:
        """Update configuration from environment variables."""
        for key in self.__dict__:
            if not key.startswith('_'):
                env_key = f"ROSETTA_{key.upper()}"
                if env_key in os.environ:
                    env_value = os.environ[env_key]
                    # Try to convert to appropriate type
                    current_value = getattr(self, key)
                    if isinstance(current_value, bool):
                        setattr(self, key, env_value.lower() == "true")
                    elif isinstance(current_value, int):
                        setattr(self, key, int(env_value))
                    elif isinstance(current_value, Path):
                        setattr(self, key, Path(env_value))
                    else:
                        setattr(self, key, env_value)
    
    def validate(self) -> bool:
        """Validate configuration values."""
        try:
            assert self.api_timeout > 0, "API timeout must be positive"
            assert self.max_retries >= 0, "Max retries must be non-negative"
            assert self.log_level in ["DEBUG", "INFO", "WARNING", "ERROR"], "Invalid log level"
            return True
        except AssertionError as e:
            raise ValueError(f"Configuration validation failed: {e}")
    
    def reload(self) -> None:
        """Reload configuration from environment and files."""
        self.from_env()
        self.validate()
