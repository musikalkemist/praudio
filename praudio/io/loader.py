"""This module provides a class to load audio files."""

import logging

import librosa
import numpy as np
import numpy.typing as npt

from praudio.io.signal import Signal
from praudio.utils import extract_extension_from_file
from praudio.errors import FileExtensionError


logger = logging.getLogger(__name__)


class Loader:
    """Loader is responsible for loading audio files. It's a tiny wrapper
    around librosa.load.

    Attributes:
        sample_rate: Sampling rate at which we want to load the audio file
        mono: Boolean value. If True, load file with 1 channel. If False,
            load file as is
        dtype: Data type of the loaded signal
    """

    def __init__(self,
                 sample_rate: int = 22050,
                 mono: bool = True,
                 data_type: npt.DTypeLike = np.float32):
        self.sample_rate = sample_rate
        self.mono = mono
        self.data_type = data_type

        self._signal_type = "waveform"
        self._audio_file_extensions = [
            "wav", "wave", "mp3",
            "ogg", "flac"
        ]
        logger.info("Loader initialised.")

    def load(self, file: str) -> Signal:
        """Load audio file and returns Signal object.

        :param file: Path to audio file to load
        :return: Loaded Signal object
        """
        self._raise_file_extension_error_if_file_extension_isnt_allowed(file)
        waveform, _ = librosa.load(file,
                                   mono=self.mono,
                                   sr=self.sample_rate,
                                   dtype=self.data_type)
        signal = Signal(self._signal_type,
                        self.sample_rate,
                        waveform,
                        file)
        logger.info("Loaded audio file at %s", file)
        return signal

    def _raise_file_extension_error_if_file_extension_isnt_allowed(self, file):
        extension = extract_extension_from_file(file)
        if extension not in self._audio_file_extensions:
            raise FileExtensionError(f"'{extension}' extension can't be loaded.")
