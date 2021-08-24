"""This module features a class that extracts Mel spectrograms from signals."""

import logging

import librosa

from praudio.transforms.transform import Transform, TransformType
from praudio.io.signal import Signal


logger = logging.getLogger(__name__)


class MelSpectrogram(Transform):
    """This class extracts a Mel spectrogram from a signal.
    It's a concrete Transform. librosa facilities are used to extract Mel
    spectrograms.

    Attributes:
        - num_mels: Number of mel bands
        - min_freq: Lowest frequency in Hertz. Frequencies below this
            threshold are filtered out
        - max_freq: Highest frequency in Hertz. Frequencies above this
            threshold are filtered out
        - max_freq: Number of mel bands
        - frame_length: Length of the windowed signal after padding with zeros
        - hop_length: Number of audio samples between adjacent STFT columns
        - win_length: Each frame of audio is windowed by window of length
            win_length and then padded with zeros to match frame_length
        - window: Windowing method employed for STFT. Default is 'hann'
    """

    def __init__(self,
                 num_mels: int = 64,
                 min_freq: int = 0,
                 max_freq: int = 8000,
                 frame_length: int = 2048,
                 hop_length: int = 1024,
                 win_length: int = 2048,
                 window: str = "hann"):
        super().__init__(TransformType.MELSPECTROGRAM)
        self.num_mels = num_mels
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.frame_length = frame_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.window = window

    def process(self, signal: Signal) -> Signal:
        """Extract Mel Spectrogram and modify signal.

        :param signal: Signal object.

        :return: Modified signal
        """
        signal.name = self._prepend_transform_name(signal.name)
        signal.data = librosa.feature.melspectrogram(
                            signal.data,
                            sr=signal.sample_rate,
                            n_mels=self.num_mels,
                            n_fft=self.frame_length,
                            hop_length=self.hop_length,
                            win_length=self.win_length,
                            window=self.window)
        logger.info("Applied %s to %s", self.name.value, signal.file)
        return signal
