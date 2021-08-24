import numpy as np
import pytest

from praudio.transform.scaling.rowstandardiser import RowStandardiser
from praudio.errors import NotA2DSignalError
from utils import sample_2d_signal


@pytest.fixture
def row_standardiser():
    return RowStandardiser()


def test_loader_instance_is_instantiated_correctly(row_standardiser):
    assert isinstance(row_standardiser, RowStandardiser)


def test_signal_is_scaled(row_standardiser, sample_2d_signal):
    """
    GIVEN a Signal object with 2 dimensions
    AND a RowStandardiser object
    WHEN the signal is passed to process
    THEN the signal is standardised
    """
    original_signal = sample_2d_signal.data[:]
    signal = row_standardiser.process(sample_2d_signal)
    assert signal.name == "rowstandardiser_dummy"
    assert type(signal.data) == np.ndarray
    assert len(signal.data) == len(original_signal)


def test_scaling_1d_array_throws_not_2_dim_array_error(row_standardiser):
    array = np.array([-2, 0, 2])
    with pytest.raises(NotA2DSignalError):
        norm_array = row_standardiser._scale(array)


def test_2d_array_is_min_max_normalised(row_standardiser):
    array = np.array([
        [-2, 0, 2],
        [-4, 0, 4]
    ])
    expected_norm_array = np.array([
        [-1.22474, 0, 1.22474],
        [-1.22474, 0, 1.22474]
    ])
    norm_array = row_standardiser._scale(array)
    assert np.allclose(norm_array, expected_norm_array)


def test_array_with_0_std_dev_is_standardised(row_standardiser):
    array = np.array([
        [1, 1, 1],
        [-4, 0, 4]
    ])
    expected_norm_array = np.array([
        [0, 0, 0],
        [-1.22474, 0, 1.22474]
    ])
    norm_array = row_standardiser._scale(array)
    assert np.allclose(norm_array, expected_norm_array)