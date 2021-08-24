"""
This module features a class that extracts a magnitude spectrogram from a
signal.
"""

import logging

import numpy as np

from praudio.transforms.transform import Transform, TransformType
from praudio.transforms.stft import STFT
from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class MagnitudeSpectrogram(Transform):
    """This class extracts a magnitude spectrogram from a signal. It's a
    subclass of the Transform class.

    Attributes:
        - stft: STFT object used to extract Short-Time Fourier Transform
    """

    def __init__(self,
                 frame_length: int = 2048,
                 hop_length: int = 1024,
                 win_length: int = 2048,
                 window: str = "hann"):
        """
        :param frame_length: Length of the windowed signal after padding with zeros
        :param hop_length:  Number of audio samples between adjacent STFT columns
        :param win_length: Each frame of audio is windowed by window of length
            win_length and then padded with zeros to match frame_length
        :param window: Windowing method employed for STFT. Default is 'hann'
        """
        super().__init__(TransformType.MAGNITUDESPECTROGRAM)
        self.stft = STFT(frame_length,
                         hop_length,
                         win_length,
                         window)

    def process(self, signal: Signal) -> Signal:
        """Extract magnitude spectrogram from waveform and modify signal.
        First we extract the STFT. Then, we apply the absolute value.

        :param signal: Signal object. Note: this transforms works only with
            waveform data

        :return: Modified signal
        """
        signal = self.stft.process(signal)
        signal.name = self._prepend_transform_name(signal.name)
        signal.data = np.abs(signal.data)
        logger.info("Applied %s to %s", self.name.value, signal.file)
        return signal
