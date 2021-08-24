import numpy as np
import pytest

from praudio.transforms.scaling.minmaxscaler import MinMaxScaler
from utils import sample_signal


@pytest.fixture
def min_max_scaler():
    return MinMaxScaler(-1., 1.)


def test_loader_instance_is_instantiated_correctly(min_max_scaler):
    assert isinstance(min_max_scaler, MinMaxScaler)
    assert min_max_scaler.min_val == -1.
    assert min_max_scaler.max_val == 1.


def test_signal_is_normalised(min_max_scaler, sample_signal):
    """
    GIVEN a Signal object
    AND a min_val max_val normaliser object
    WHEN the signal is passed to process
    THEN the signal is normalised
    """
    original_signal = sample_signal.data[:]
    signal = min_max_scaler.process(sample_signal)
    assert signal.name == "minmaxscaler_dummy"
    assert type(signal.data) == np.ndarray
    assert len(signal.data) == len(original_signal)
    assert signal.data.max() == 1
    assert signal.data.min() == -1


def test_1d_array_is_min_max_normalised(min_max_scaler):
    array = np.array([-2, 0, 2])
    norm_array = min_max_scaler._scale(array)
    assert np.array_equal(norm_array, np.array([-1, 0, 1]))


def test_2d_array_is_min_max_normalised(min_max_scaler):
    array = np.array([
        [-2, 0, 2],
        [-4, 0, 4]
    ])
    expected_norm_array = np.array([
        [-.5, 0, .5],
        [-1, 0, 1]
    ])
    norm_array = min_max_scaler._scale(array)
    assert np.array_equal(norm_array, expected_norm_array)