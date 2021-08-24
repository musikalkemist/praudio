"""This module provides a base class for concrete feature scalers."""

import logging
from abc import abstractmethod

import numpy as np

from praudio.transform.transform import Transform
from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class Scaler(Transform):
    """Scaler is a base class for different types of concrete Scalers."""

    def __init__(self, name):
        super().__init__(name)
        logger.info("Instantiated %s object", self.name)

    def process(self, signal: Signal) -> Signal:
        """Apply scaling to signal.

        :param signal: Signal object to normalise

        :return: Modified signal
        """
        norm_data = self._scale(signal.data)
        signal.data = norm_data
        signal.name = self.name + "_" + signal.name
        logger.info("Applied %s on %s", self.name, signal.file)
        return signal

    @abstractmethod
    def _scale(self, array: np.ndarray):
        """Concrete Scalers must implement this method. In this method,
        the specific scaling strategy must be implemented.

        :param array: Array to scale

        :return: Scaled array
        """
