"""
This module provides an abstract interface for all transforms (Transform)
and an enumerations with all available transforms (TransformType).
TransformType should be updated as new transforms are added.
"""

import logging
from abc import ABC, abstractmethod
from enum import Enum

from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class TransformType(Enum):
    """Enumeration class with all available transforms."""

    LOG = "log"
    MAGNITUDESPECTROGRAM = "magnitudespectrogram"
    MELSPECTROGRAM = "melspectrogram"
    MINMAXSCALER = "minmaxscaler"
    MFCC = "mfcc"
    POWERSPECTROGRAM = "powerspectrogram"
    STFT = "stft"
    ROWSTANDARDISER = "rowstandardiser"
    STANDARDISER = "standardiser"


class Transform(ABC):
    """Transform is a common interface for all transforms objects. Such
    objects manipulate a signal (e.g., applying log scaling, extracting
    MFCCs).

    Attrs:
        - name: The name of the transforms
    """

    def __init__(self, name: TransformType):
        self.name = name
        logger.info("Instantiated %s transform", self.name)

    @abstractmethod
    def process(self, signal: Signal) -> Signal:
        """This method is responsible to apply a transforms to the incoming
        signal.

        :param signal: Signal object to be manipulated

        :return: New signal object with transformed values
        """

    def _prepend_transform_name(self, string):
        return self.name.value + "_" + string
