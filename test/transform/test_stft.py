import numpy as np
import pytest

from praudio.transform.stft import STFT
from utils import sample_signal


@pytest.fixture
def stft():
    return STFT(100, 50, 75, "hann")


def test_loader_instance_is_instantiated_correctly(stft):
    assert isinstance(stft, STFT)
    assert stft.frame_length == 100
    assert stft.hop_length == 50
    assert stft.win_length == 75
    assert stft.window == "hann"
    assert stft.name == "stft"


def test_stft_is_extracted(stft, sample_signal):
    """
    GIVEN a Signal object
    AND an STFT object
    WHEN the signal is passed to process
    THEN the complex Short-Time Fourier Transform is extracted
    AND the modified Signal object with the new STFT is returned
    """
    signal = stft.process(sample_signal)
    assert signal.name == "stft"
    assert type(signal.data) == np.ndarray
    assert len(signal.data.shape) == 2
    assert type(signal.data[0][0]) == np.complex_
