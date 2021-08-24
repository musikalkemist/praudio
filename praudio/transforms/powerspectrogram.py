"""
This module features a class that extracts a power spectrogram from a
signal.
"""

import logging

import numpy as np

from praudio.transforms.transform import TransformType, Transform
from praudio.transforms.stft import STFT
from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class PowerSpectrogram(Transform):
    """This class extracts a power spectrogram from a signal. It's a
    concrete Transform.

    Attributes:
        - power: Power to which we raise the spectrum. Default is 2
        - stft: STFT object used to extract Short-Time Fourier Transform
    """

    def __init__(self,
                 frame_length: int = 2048,
                 hop_length: int = 1024,
                 win_length: int = 2048,
                 window: str = "hann",
                 power: int = 2):
        super().__init__(TransformType.POWERSPECTROGRAM)
        self.power = power
        self.stft = STFT(frame_length,
                         hop_length,
                         win_length,
                         window)


    def process(self, signal: Signal) -> Signal:
        """Extract power spectrogram from waveform and modify signal.
        First we extract the STFT. Then, we apply the absolute value and
        raise it to the target power.

        :param signal: Signal object. Note: this transforms works only with
            waveform data

        :return: Modified signal
        """
        signal = self.stft.process(signal)
        signal.name = self._prepend_transform_name(signal.name)
        signal.data = self._raise_to_power(np.abs(signal.data))
        logger.info("Applied %s to %s", self.name.value, signal.file)
        return signal

    def _raise_to_power(self, array: np.ndarray):
        return array ** self.power
