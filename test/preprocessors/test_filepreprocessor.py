import os
from pathlib import Path

from praudio.preprocessors.filepreprocessor import FilePreprocessor
from praudio.io.numpysaver import NumpySaver
from praudio.transformschain import TransformsChain
from praudio.io.loader import Loader
from utils_preprocess import file_preprocessor


DUMMY_AUDIO_FILE = Path(Path(__file__).parent.parent,
                        "dummydataset", "dummy").with_suffix(".wav")


def test_file_preprocessor_is_instantiated_correctly(file_preprocessor):
    assert isinstance(file_preprocessor, FilePreprocessor)
    assert isinstance(file_preprocessor.loader, Loader)
    assert isinstance(file_preprocessor.transforms_chain, TransformsChain)
    assert isinstance(file_preprocessor.saver, NumpySaver)


def test_file_is_preprocessed(file_preprocessor):
    """
    GIVEN an audio file
    AND a save path
    AND a file preprocess object
    WHEN the audio file and the save path are passed to 'preprocess'
    THEN the audio file is loaded
    AND it is transformed
    AND the transformed signal is stored at the save path
    """
    file_preprocessor.preprocess(DUMMY_AUDIO_FILE, "dummy_save")
    assert os.path.isfile("dummy_save.npy")
    os.remove("dummy_save.npy")



