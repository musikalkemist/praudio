"""This module provides a class to perform per-row z-score scaling."""

import numpy as np

from praudio.transforms.scaling.scaler import Scaler
from praudio.transforms.transform import TransformType
from praudio.errors import NotA2DSignalError


class RowStandardiser(Scaler):
    """RowStandardiser scales a signal, so that its values are centred around
    the mean with a unit standard deviation. The mean of the signal
    is zero and the resultant distribution has a unit standard deviation.

    The mean / std deviation are calculated for each row. For example,
    if used to scale a spectrogram, RowStandardiser would scale the
    spectrogram for each band.

    Note: RowStandardiser can be used only with 2-dimensional signals (e.g.,
        MFCC). With a time-series, this scaler will throw an error.
    """

    def __init__(self):
        super().__init__(TransformType.ROWSTANDARDISER)
        self._min_std = 1e-7

    def _scale(self, array: np.ndarray):
        try:
            array_mean = np.mean(array, axis=1)
        except np.AxisError as err:
            raise NotA2DSignalError(f"Signal can't be scaled with {self.name}") from err

        array_mean = np.expand_dims(array_mean, axis=1)
        array_std = np.std(array, axis=1)
        array_std = np.expand_dims(array_std, axis=1)
        scaled_array = (array - array_mean) / np.maximum(array_std, self._min_std)
        return scaled_array
