"""This module contains custom errors."""

class FileExtensionError(Exception):
    """Error that is thrown when the extension of a file isn't allowed."""


class NotA2DSignalError(Exception):
    """
    Error that is thrown when the expected signal should have more than 1
    dimension.
    """


class ParameterMissingError(Exception):
    """ Error thrown when an expected parameter is missing. """
