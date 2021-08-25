"""
This module contains utility functions that are used throughout the library.
"""

import os
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


def remove_extension_from_file(file: str) -> str:
    """
    :param file: File path to which to remove extension

    :return: File without extension
    """
    return str(Path(file).with_suffix(""))


def create_dir_hierarchy(dir: str):
    """Creates a hierarchy of directories, if it doesn't exists. Else,
    it doesn't do anything.

    :param dir: Path with directory hierarchy which should be created, if it
        doesn't exist
    """
    Path(dir).mkdir(parents=True, exist_ok=True)


def create_dir_hierarchy_from_file(file: str):
    """Creates a hierarchy of directories for a file, if it doesn't exists.
    Else, it doesn't do anything.

    :param file: File for which to create the relative dir hierarchy
    """
    dir = os.path.dirname(file)
    create_dir_hierarchy(dir)
