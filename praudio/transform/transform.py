"""This module provides an abstract interface for all transforms."""

import logging
from abc import ABC, abstractmethod

from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class Transform(ABC):
    """Transform is a common interface for all transform objects. Such
    objects manipulate a signal (e.g., applying log scaling, extracting
    MFCCs).

    Attrs:
        - name: The name of the transform
    """

    def __init__(self, name: str):
        self.name = name
        logging.info("Instantiated %s transform object", self.name)

    @abstractmethod
    def process(self, signal: Signal) -> Signal:
        """This method is responsible to apply a transform to the incoming
        signal.

        :param signal: Signal object to be manipulated

        :return: New signal object with transformed values
        """
