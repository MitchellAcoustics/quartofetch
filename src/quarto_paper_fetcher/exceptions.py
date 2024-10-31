"""Custom exceptions for the Quarto Paper Fetcher."""


class QuartoFetcherError(Exception):
    """Base exception for all Quarto Paper Fetcher errors."""

    pass


class GitError(QuartoFetcherError):
    """Base exception for git operations."""

    pass


class GitTimeoutError(GitError):
    """Raised when git operations timeout."""

    pass


class GitAuthenticationError(GitError):
    """Raised when git authentication fails."""

    pass


class QuartoError(QuartoFetcherError):
    """Base exception for Quarto operations."""

    pass


class ConfigurationError(QuartoFetcherError):
    """Raised for configuration-related errors."""

    pass
