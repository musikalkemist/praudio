import numpy as np
import pytest

from praudio.transform.magnitudespectrogram import MagnitudeSpectrogram
from utils import sample_signal


@pytest.fixture
def magnitude_spectrogram():
    return MagnitudeSpectrogram(100, 50, 75, "hann")


def test_magnitude_spectrogram_instance_is_instantiated_correctly(
        magnitude_spectrogram):
    assert isinstance(magnitude_spectrogram, MagnitudeSpectrogram)
    assert magnitude_spectrogram.frame_length == 100
    assert magnitude_spectrogram.hop_length == 50
    assert magnitude_spectrogram.win_length == 75
    assert magnitude_spectrogram.window == "hann"
    assert magnitude_spectrogram.name == "magnitude_spectrogram"


def test_magnitude_spectrogram_is_extracted(magnitude_spectrogram, sample_signal):
    """
    GIVEN a Signal object
    AND an magnitude spectrogram object
    WHEN the signal is passed to process
    THEN the magnitude spectrogram is extracted
    AND the modified Signal object with the new magnitude spectrogram is returned
    """
    signal = magnitude_spectrogram.process(sample_signal)
    assert signal.name == "magnitude_spectrogram"
    assert type(signal.data) == np.ndarray
    assert len(signal.data.shape) == 2
    assert type(signal.data[0][0]) == np.float_
