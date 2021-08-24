"""This module contains a class to extract MFCCs from a signal."""

import logging

import librosa

from praudio.transforms.transform import Transform, TransformType
from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class MFCC(Transform):
    """This class extracts MFCCs from a signal. It's a concrete Transform.
    librosa facilities are used to extract MFCCs.

    Attributes:
        - num_mfcc: Number of coefficients to return
        - frame_length: Length of the windowed signal after padding with zeros
        - hop_length: Number of audio samples between adjacent STFT columns
        - win_length: Each frame of audio is windowed by window of length
            win_length and then padded with zeros to match frame_length
        - window: Windowing method employed for STFT. Default is 'hann'
    """

    def __init__(self,
                 num_mfcc: int = 13,
                 frame_length: int = 2048,
                 hop_length: int = 1024,
                 win_length: int = 2048,
                 window: str = "hann"):
        super().__init__(TransformType.MFCC)
        self.num_mfcc = num_mfcc
        self.frame_length = frame_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.window = window

    def process(self, signal: Signal) -> Signal:
        """Extract MFCCs and modify signal.

        :param signal: Signal object. Note: this transforms works only with
            waveform data

        :return: Modified signal
        """
        signal.name = self._prepend_transform_name(signal.name)
        signal.data = librosa.feature.mfcc(signal.data,
                                           sr=signal.sample_rate,
                                           n_fft=self.frame_length,
                                           hop_length=self.hop_length,
                                           win_length=self.win_length,
                                           window=self.window)
        logger.info("Applied %s to %s", self.name.value, signal.file)
        return signal
