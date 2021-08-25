import numpy as np
import pytest

from praudio.transforms.mfcc import MFCC
from praudio.transforms.transform import TransformType
from utils_transforms import sample_signal


@pytest.fixture
def mfcc():
    return MFCC(14, 100, 50, 75, "hann")


def test_mfcc_instance_is_instantiated_correctly(mfcc):
    assert isinstance(mfcc, MFCC)
    assert mfcc.num_mfcc == 14
    assert mfcc.frame_length == 100
    assert mfcc.hop_length == 50
    assert mfcc.win_length == 75
    assert mfcc.window == "hann"
    assert mfcc.name == TransformType.MFCC


def test_mfcc_is_extracted(mfcc, sample_signal):
    """
    GIVEN a Signal object
    AND an power spectrogram object
    WHEN the signal is passed to process
    THEN the power spectrogram is extracted
    AND the modified Signal object with the new power spectrogram is returned
    """
    signal = mfcc.process(sample_signal)
    assert signal.name == "mfcc_dummy"
    assert type(signal.data) == np.ndarray
    assert len(signal.data.shape) == 2
    assert type(signal.data[0][0]) == np.float_
