"""
This module features a class that extracts a magnitude spectrogram from a
signal.
"""

import logging

import numpy as np

from praudio.transforms.transform import Transform, TransformType
from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class Log(Transform):
    """This class applies logarithmic transformation on a signal.

    Attributes:
        - boost: Value added to the signal before taking the logarithm
    """

    def __init__(self,
                 boost: float = 1e-7):
        super().__init__(TransformType.LOG)
        if boost <= 0:
            raise ValueError(f"'boost' argument must be > 0. {boost} provided")
        self.boost = boost

    def process(self, signal: Signal) -> Signal:
        """Apply logarithm to signal.

        :param signal: Signal object.

        :return: Modified signal
        """
        signal.name = self._prepend_transform_name(signal.name)
        signal.data = np.log(signal.data + self.boost)
        logger.info("Applied %s to %s", self.name.value, signal.file)
        return signal
