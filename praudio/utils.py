"""
This module contains utility functions that are used throughout the library.
"""

from pathlib import Path


def extract_extension(file: str) -> str:
    """Extract extension from file name.

    file: Path of file we want to extract the extension from.
    return: Extension of file (e.g., mp3)
    """
    return Path(file).suffix.lower()[1:]
