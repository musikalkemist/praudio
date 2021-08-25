"""
This module contains TransformFactory, a class that enables to
instantiate transform objects.
"""

import logging

from praudio.transforms.transform import Transform
from praudio.transforms import Log, MagnitudeSpectrogram, MelSpectrogram, \
    MinMaxScaler, MFCC, PowerSpectrogram, STFT, RowStandardiser, Standardiser


logger = logging.getLogger(__name__)


class TransformFactory:
    """Factory that instantiates Transform objects."""

    def __init__(self):
        self.transform_types = {
            "log": Log,
            "magnitudespectrogram": MagnitudeSpectrogram,
            "melspectrogram": MelSpectrogram,
            "minmaxscaler": MinMaxScaler,
            "mfcc": MFCC,
            "powerspectrogram": PowerSpectrogram,
            "stft": STFT,
            "rowstandardiser": RowStandardiser,
            "standardiser": Standardiser,
        }
        logger.info("Instantiated TrnasformFactory object")

    def create(self, transform_type: str, **kwargs) -> Transform:
        """Instantiate and return concrete transform.

        :param transform_type: Type of transform object to instantiate

        :return: Instance of concrete transform
        """
        self._raise_type_error_if_transform_isnt_avaialbe(transform_type)
        transform = self.transform_types.get(transform_type)
        return transform(**kwargs)

    def _raise_type_error_if_transform_isnt_avaialbe(self, transform_type):
        if transform_type not in self.transform_types:
            raise TypeError("It's not possible to instantiate a "
                            f"'{transform_type}' beause this transform "
                            "doesn't exist.")
