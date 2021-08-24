import numpy as np
import pytest

from praudio.transform.melspectrogram import MelSpectrogram
from utils import sample_signal


@pytest.fixture
def mel_spectrogram():
    return MelSpectrogram(32, 10, 10000, 100, 50, 75, "hann")


def test_mel_spectrogram_instance_is_instantiated_correctly(mel_spectrogram):
    assert isinstance(mel_spectrogram, MelSpectrogram)
    assert mel_spectrogram.num_mels == 32
    assert mel_spectrogram.min_freq == 10
    assert mel_spectrogram.max_freq == 10000
    assert mel_spectrogram.frame_length == 100
    assert mel_spectrogram.hop_length == 50
    assert mel_spectrogram.win_length == 75
    assert mel_spectrogram.window == "hann"
    assert mel_spectrogram.name == "mel_spectrogram"


def test_mel_spectrogram_is_extracted(mel_spectrogram, sample_signal):
    """
    GIVEN a Signal object
    AND a mel spectrogram object
    WHEN the signal is passed to process
    THEN the mel spectrogram is extracted
    AND the modified Signal object with the new mel spectrogram is returned
    """
    signal = mel_spectrogram.process(sample_signal)
    assert signal.name == "mel_spectrogram"
    assert type(signal.data) == np.ndarray
    assert len(signal.data.shape) == 2
    assert signal.data.shape[0] == 32
    assert type(signal.data[0][0]) == np.float_
