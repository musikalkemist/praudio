"""This module provides a class to perform z-score scaling."""

import numpy as np

from praudio.transforms.scaling.scaler import Scaler
from praudio.transforms.transform import TransformType


class Standardiser(Scaler):
    """Standardiser scales a signal, so that its values are centred around
    the mean with a unit standard deviation. The mean of the signal
    is zero and the resultant distribution has a unit standard deviation.

    If the signal is 2-dimensional (e.g., spectrogram), the mean / std
    deviation are calculated gloabally across all rows.
    """

    def __init__(self):
        super().__init__(TransformType.STANDARDISER)
        self._min_std = 1e-7

    def _scale(self, array: np.ndarray):
        array_mean = np.mean(array)
        array_std = np.std(array)
        scaled_array = (array - array_mean) / np.maximum(array_std, self._min_std)
        return scaled_array
