"""This module provides a class to perform minmax scaling."""

import numpy as np

from praudio.transforms.scaling.scaler import Scaler
from praudio.transforms.transform import TransformType


class MinMaxScaler(Scaler):
    """MinMaxScaler performs min max scaling on a signal. It's a
    concrete Scaler. If the signal is 2-dimensional (e.g., spectrogram), the
    mean / std deviation are calculated across all rows.

    Attributes:
        - min_val: Lowest scaling range
        - max_val: Highest scaling range

    If the signal is 2-dimensional (e.g., spectrogram), the mean / std
    deviation are calculated gloabally across all rows.
    """

    def __init__(self, min: float = 0., max: float = 1.):
        super().__init__(TransformType.MINMAXSCALER)
        self.min_val = min
        self.max_val = max

    def _scale(self, array: np.ndarray):
        scaled_array = (array - array.min()) / (array.max() - array.min())
        scaled_array = scaled_array * (self.max_val - self.min_val) + self.min_val
        return scaled_array
