import pytest
import numpy as np

from praudio.io.numpysaver import NumpySaver


@pytest.fixture
def loader():
    return Loader(44100, True, np.float32)


def test_loader_instance_is_instantiated_correctly(loader):
    assert isinstance(loader, Loader)
    assert loader.mono == True
    assert loader.sample_rate == 44100
    assert loader.data_type == np.float32
