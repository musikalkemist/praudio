from pathlib import Path

import pytest
import numpy as np

from praudio.io.loader import Loader
from praudio.io.signal import Signal
from praudio.errors import FileExtensionError


DUMMY_AUDIO_FILE = Path(Path(__file__).parent.parent,
                        "dummydataset", "dummy").with_suffix(".wav")


@pytest.fixture
def loader():
    return Loader(44100, True, np.float32)


def test_loader_instance_is_instantiated_correctly(loader):
    assert isinstance(loader, Loader)
    assert loader.mono is True
    assert loader.sample_rate == 44100
    assert loader.data_type == np.float32


def test_load_throws_file_format_error(loader):
    """
    GIVEN a file with a not allowed format (e.g, jpeg)
    AND a Loader object
    WHEN the file is passed to the load method
    THEN a FileExtensionError is thrown
    """
    with pytest.raises(FileExtensionError):
        loader.load("dummy_file.jpg")


def test_audio_file_is_loaded_correctly(loader):
    """
    GIVEN a file with an allowed format
    AND a Loader object
    WHEN the file is passed to the load method
    THEN the file is loaded
    AND it's returned as a Signal object
    """
    signal = loader.load(DUMMY_AUDIO_FILE)
    assert isinstance(signal, Signal)
    assert signal.sample_rate == 44100
    assert type(signal.data) == np.ndarray
    assert signal.file == DUMMY_AUDIO_FILE


def test_raise_file_extension_error_if_file_extension_isnt_allowed(loader):
    with pytest.raises(FileExtensionError) as err:
        loader._raise_file_extension_error_if_file_extension_isnt_allowed("dummy_file.jpg")
    assert str(err.value) == "'jpg' extension can't be loaded."