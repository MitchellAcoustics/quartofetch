"""Custom exceptions for the Quarto Paper Fetcher."""


class QfetchError(Exception):
    """Base exception for all Quarto Paper Fetcher errors."""

    pass


class GitError(QfetchError):
    """Base exception for git operations."""

    pass


class GitTimeoutError(GitError):
    """Raised when git operations timeout."""

    pass


class GitAuthenticationError(GitError):
    """Raised when git authentication fails."""

    pass


class QuartoError(QfetchError):
    """Base exception for Quarto operations."""

    pass


class ConfigurationError(QfetchError):
    """Raised for configuration-related errors."""

    pass
