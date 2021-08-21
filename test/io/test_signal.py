import numpy as np

from praudio.io.signal import Signal


def test_signal_is_instantiated_correctly():
    dummy_data = np.array([1, 2])
    signal = Signal("dummy", 22050, dummy_data, "dummy_path")
    assert signal.name == "dummy"
    assert signal.sample_rate == 22050
    assert np.array_equal(signal.data, dummy_data)
    assert signal.file == "dummy_path"