import asyncio
from core.logging_config import setup_logging, get_logger, LogContext
from core.exceptions import BrowserException

# Setup logging
setup_logging(log_level="INFO")

# Get logger for this module
logger = get_logger(__name__)

def demo_basic_logging():
    """Demonstrate basic logging."""
    logger.info("Starting demo", version="1.0.0")
    
    # Log with additional context
    logger.info("Processing item", item_id=123, status="pending")
    
    # Warning with context
    logger.warning("Slow operation", duration_ms=1500, threshold_ms=1000)
    
    # Error logging
    try:
        raise ValueError("Demo error")
    except Exception as e:
        logger.error("Operation failed", error=str(e), exc_info=True)

def demo_context_logging():
    """Demonstrate context logging."""
    with LogContext(session_id="abc123", user="demo_user"):
        logger.info("Starting session")
        
        # All logs within this context will have session_id and user
        logger.info("Performing action")
        
        with LogContext(operation="ticket_search"):
            logger.info("Searching for tickets")
            # Nested context - will have session_id, user, AND operation

async def demo_async_logging():
    """Demonstrate logging in async context."""
    logger.info("Starting async operation")
    
    await asyncio.sleep(0.1)
    
    logger.info("Async operation completed", duration_ms=100)

if __name__ == "__main__":
    print("=== Basic Logging ===")
    demo_basic_logging()
    
    print("\n=== Context Logging ===")
    demo_context_logging()
    
    print("\n=== Async Logging ===")
    asyncio.run(demo_async_logging())