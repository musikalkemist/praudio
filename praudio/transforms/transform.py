"""This module provides an abstract interface for all transforms."""

from abc import ABC, abstractmethod

from praudio.io.signal import Signal


class Transform(ABC):
    """Transform is a common interface for all transforms objects. Such
    objects manipulate a signal (e.g., applying log scaling, extracting
    MFCCs).

    Attrs:
        - name: The name of the transforms
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def process(self, signal: Signal) -> Signal:
        """This method is responsible to apply a transforms to the incoming
        signal.

        :param signal: Signal object to be manipulated

        :return: New signal object with transformed values
        """
