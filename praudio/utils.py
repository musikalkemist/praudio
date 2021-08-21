"""
This module contains utility functions that are used throughout the library.
"""

from pathlib import Path


def extract_extension_from_file(file: str) -> str:
    """Extract extension from file name.

    :param file: Path of file we want to extract the extension from.

    :return: Extension of file (e.g., mp3)
    """
    return Path(file).suffix.lower()[1:]


def add_extension_to_file(file: str,
                          extension: str) -> str:
    """Add extension to a file.

    :param file: File path to which to add an extension
    :param extension: Extension to append to file (e.g., mp3)

    :return: File with extension
    """
    return file + "." + extension
