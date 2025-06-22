"""Custom exceptions for the ticket bot."""

class TicketBotException(Exception):
    """Base exception for all ticket bot errors."""
    pass

class BrowserException(TicketBotException):
    """Browser-related errors."""
    pass

class NavigationException(BrowserException):
    """Navigation-specific errors."""
    pass

class ConfigurationException(TicketBotException):
    """Configuration-related errors."""
    pass