"""
This module features a class that extracts a magnitude spectrogram from a
signal.
"""

import logging

import numpy as np

from praudio.transform.transform import Transform
from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class Log(Transform):
    """This class applies logarithmic transformation on a signal.

    Attributes:
        - boost: Value added to the signal before taking the logarithm
    """

    def __init__(self,
                 boost: float = 1e-7):
        super().__init__("log")
        if boost < 0:
            raise ValueError(f"log_boost must be > 0. {boost} provided")
        self.boost = boost
        logger.info("Instantiated Log object")

    def process(self, signal: Signal) -> Signal:
        """Apply logarithm to signal.

        :param signal: Signal object.

        :return: Modified signal
        """
        signal.data = np.log(signal.data + self.boost)
        signal.name = self.name + "_" + signal.name
        logger.info("Applied logarithm to %s", signal.file)
        return signal
