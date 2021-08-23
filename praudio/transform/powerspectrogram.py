"""
This module features a class that extracts a power spectrogram from a
signal.
"""

import logging

import numpy as np

from praudio.transform.stft import STFT
from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class PowerSpectrogram(STFT):
    """This class extracts a power spectrogram from a signal. It's a
    subclass of the STFT class.

    Attributes:
        - frame_length: Length of the windowed signal after padding with zeros
        - hop_length: Number of audio samples between adjacent STFT columns
        - win_length: Each frame of audio is windowed by window of length
            win_length and then padded with zeros to match frame_length
        - window: Windowing method employed for STFT. Default is 'hann'
        - power: Exponent to which power spectrogram is raised. Default
            is 2
    """

    def __init__(self,
                 frame_length: int = 2048,
                 hop_length: int = 1024,
                 win_length: int = 2048,
                 window: str = "hann",
                 power: int = 2):
        super().__init__(frame_length, hop_length, win_length, window)
        self.power = power
        self.name = "power_spectrogram"
        logger.info("Instantiated MagnitudeSpectroram object")

    def process(self, signal: Signal) -> Signal:
        """Extract power spectrogram from waveform and modify signal.

        :param signal: Signal object. Note: this transform works only with
            waveform data

        :return: Modified signal
        """
        signal = super().process(signal)
        signal.data = self._raise_to_power(np.abs(signal.data))
        signal.name = self.name
        logger.info("Extracted power spectrogram for %s", signal.file)
        return signal

    def _raise_to_power(self, array: np.ndarray):
        return array ** self.power
