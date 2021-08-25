import os

import pytest
import numpy as np

from praudio.io.numpysaver import NumpySaver


@pytest.fixture
def saver():
    return NumpySaver()


def test_saver_is_instantiated_correctly(saver):
    assert isinstance(saver, NumpySaver)
    assert saver.extension == "npy"


def test_saver_stores_numpy_array(saver):
    """
    GIVEN a numpy array
    AND a NumpySaver
    WHEN the array is passed to the 'save' method
    AND a save path is also passed
    THEN the numpy array is saved as a npy file on disk
    """
    array = np.array([1, 2])
    saver.save("array", array)
    assert os.path.isfile("array.npy")
    os.remove("array.npy")


