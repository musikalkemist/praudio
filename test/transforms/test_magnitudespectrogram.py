import numpy as np
import pytest

from praudio.transforms.magnitudespectrogram import MagnitudeSpectrogram
from praudio.transforms.transform import TransformType
from utils_transforms import sample_signal


@pytest.fixture
def magnitude_spectrogram():
    return MagnitudeSpectrogram(100, 50, 75, "hann")


def test_magnitude_spectrogram_instance_is_instantiated_correctly(
        magnitude_spectrogram):
    assert isinstance(magnitude_spectrogram, MagnitudeSpectrogram)
    assert magnitude_spectrogram.name == TransformType.MAGNITUDESPECTROGRAM


def test_magnitude_spectrogram_is_extracted(magnitude_spectrogram, sample_signal):
    """
    GIVEN a Signal object
    AND an magnitude spectrogram object
    WHEN the signal is passed to process
    THEN the magnitude spectrogram is extracted
    AND the modified Signal object with the new magnitude spectrogram is returned
    """
    signal = magnitude_spectrogram.process(sample_signal)
    assert signal.name == "magnitudespectrogram_stft_dummy"
    assert type(signal.data) == np.ndarray
    assert len(signal.data.shape) == 2
    assert type(signal.data[0][0]) == np.float_
