"""Abstract interface for storing feature arrays on disk."""

from abc import ABC, abstractmethod

import numpy as np


class Saver(ABC):
    """Abstract class that provides an interface to store signals / feature
    arrays.

    Attributes:
        - extension: Save extension (e.g., "npy")
    """

    def __init__(self, extension: str):
        self.extension = extension

    @abstractmethod
    def save(self,
             file: str,
             array: np.ndarray):
        """Store array to disk.

        :param file: Path where to save file without extension
        :param array: Numpy array to store
        """
