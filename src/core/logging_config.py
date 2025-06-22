import logging
import sys
from pathlib import Path
from typing import Optional
import structlog
from structlog.processors import CallsiteParameter

def setup_logging(log_level: str = "INFO", log_file: Optional[Path] = None):
    """Configure structured logging for the application."""
    
    # Create logs directory if needed
    if log_file and log_file.parent:
        log_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Configure Python's logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper()),
    )
    
    # Processors for structlog
    processors = [
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.dev.ConsoleRenderer() if log_level == "DEBUG" else structlog.processors.JSONRenderer(),
    ]
    
    # Configure structlog
    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

def get_logger(name: str) -> structlog.BoundLogger:
    """Get a logger instance for a module."""
    return structlog.get_logger(name)

# Context manager for adding temporary context to logs
class LogContext:
    """Add temporary context to all logs within a block."""
    
    def __init__(self, **kwargs):
        self.context = kwargs
        self.tokens = []
    
    def __enter__(self):
        for key, value in self.context.items():
            token = structlog.contextvars.bind_contextvars(**{key: value})
            self.tokens.append(token)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        for token in self.tokens:
            structlog.contextvars.unbind_contextvars(token)