import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class BrowserConfig:
    """Browser automation configuration."""
    headless: bool = True
    timeout: int = 40000  # milliseconds
    viewport_width: int = 1920
    viewport_height: int = 1080

@dataclass
class PerformanceConfig:
    """Performance and concurrency settings."""
    max_concurrent_sessions: int = 3
    max_retries: int = 3
    retry_delay: float = 1.0

class Config:
    """Main configuration class."""
    
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path("../config/settings.yaml")
        self._raw_config: Dict[str, Any] = {}
        self._load_config()
        
        # Initialize sub-configurations
        self.browser = self._load_browser_config()
        self.performance = self._load_performance_config()
    
    def _load_config(self) -> None:
        """Load configuration from YAML file."""
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                self._raw_config = yaml.safe_load(f) or {}
        
        # Apply environment variable overrides
        # Example: TB_BROWSER_HEADLESS=false
        for key, value in os.environ.items():
            if key.startswith("TB_"):
                self._apply_env_override(key, value)
    
    def _apply_env_override(self, key: str, value: str) -> None:
        """Apply a single environment variable override."""
        pass
    
    def _load_browser_config(self) -> BrowserConfig:
        """Load browser configuration section."""
        browser_dict = self._raw_config.get('browser', {})
        return BrowserConfig(**browser_dict)
    
    def _load_performance_config(self) -> PerformanceConfig:
        """Load performance configuration section."""
        perf_dict = self._raw_config.get('performance', {})
        return PerformanceConfig(**perf_dict)

# Global config instance
_config: Optional[Config] = None

def get_config() -> Config:
    """Get the global configuration instance."""
    global _config
    if _config is None:
        _config = Config()
    return _config