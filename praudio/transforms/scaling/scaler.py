"""This module provides a base class for concrete feature scalers."""

import logging
from abc import abstractmethod

import numpy as np

from praudio.transforms.transform import Transform
from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class Scaler(Transform):
    """Scaler is a base class for different types of concrete Scalers."""

    def process(self, signal: Signal) -> Signal:
        """Apply scaling to signal.

        :param signal: Signal object to normalise

        :return: Modified signal
        """
        signal.name = self._prepend_transform_name(signal.name)
        signal.data = self._scale(signal.data)
        logger.info("Applied %s on %s", self.name, signal.file)
        return signal

    @abstractmethod
    def _scale(self, array: np.ndarray):
        """Concrete Scalers must implement this method. In this method,
        the specific scaling strategy must be implemented.

        :param array: Array to scale

        :return: Scaled array
        """
