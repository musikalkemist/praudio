import numpy as np
import pytest

from praudio.transforms.scaling.standardiser import Standardiser
from praudio.transforms.transform import TransformType
from utils import sample_signal


@pytest.fixture
def standardiser():
    return Standardiser()


def test_loader_instance_is_instantiated_correctly(standardiser):
    assert isinstance(standardiser, Standardiser)
    assert standardiser.name == TransformType.STANDARDISER


def test_signal_is_scaled(standardiser, sample_signal):
    """
    GIVEN a Signal object
    AND a Standardiser object
    WHEN the signal is passed to process
    THEN the signal is standardised
    """
    original_signal = sample_signal.data[:]
    signal = standardiser.process(sample_signal)
    assert signal.name == "standardiser_dummy"
    assert type(signal.data) == np.ndarray
    assert len(signal.data) == len(original_signal)


def test_1d_array_is_standardised(standardiser):
    array = np.array([-2, 0, 2])
    norm_array = standardiser._scale(array)
    expected_array = np.array([-1.22474, 0, 1.22474])
    assert np.allclose(norm_array, expected_array)


def test_2d_array_is_min_max_normalised(standardiser):
    array = np.array([
        [-2, 0, 2],
        [-4, 0, 4]
    ])
    expected_norm_array = np.array([
        [-0.77459, 0, 0.77459],
        [-1.549193, 0, 1.549193]
    ])
    norm_array = standardiser._scale(array)
    assert np.allclose(norm_array, expected_norm_array)


def test_array_with_0_std_dev_is_standardised(standardiser):
    array = np.array([1, 1, 1])
    norm_array = standardiser._scale(array)
    expected_array = np.array([0, 0, 0])
    assert np.allclose(norm_array, expected_array)