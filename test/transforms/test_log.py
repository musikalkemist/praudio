import numpy as np
import pytest

from praudio.transforms.log import Log
from utils import sample_signal
from utils import sample_2d_signal


@pytest.fixture
def log():
    return Log(0.1)


def test_loader_instance_is_instantiated_correctly(log):
    assert isinstance(log, Log)
    assert log.boost == .1


def test_value_error_is_thrown_if_negative_boost_is_passed_in_constructor():
    with pytest.raises(ValueError):
        Log(-2)


def test_1dim_signal_is_scaled(log, sample_signal):
    """
    GIVEN a Signal object
    AND a Log object
    WHEN the signal is passed to process
    THEN the log of the signal is calgulated
    AND returned as part of the Signal object
    """
    original_signal = sample_signal.data[:]
    signal = log.process(sample_signal)
    assert signal.name == "log_dummy"
    assert type(signal.data) == np.ndarray
    assert len(signal.data) == len(original_signal)


def test_2dim_signal_is_scaled(log, sample_2d_signal):
    """
    GIVEN a Signal object
    AND a Log object
    WHEN the signal is passed to process
    THEN the log of the signal is calgulated
    AND returned as part of the Signal object
    """
    original_signal = sample_2d_signal.data[:]
    signal = log.process(sample_2d_signal)
    assert signal.name == "log_dummy"
    assert type(signal.data) == np.ndarray
    assert signal.data.shape == original_signal.shape


def test_signal_with_0s_is_scaled(log, sample_signal):
    sample_signal.data =np.zeros(100)
    original_signal = sample_signal.data[:]
    signal = log.process(sample_signal)
    assert signal.name == "log_dummy"
    assert type(signal.data) == np.ndarray
    assert signal.data.shape == original_signal.shape




