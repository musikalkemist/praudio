import pytest


from praudio.creation.filepreprocessorcreator import FilePreprocessorCreator
from praudio.creation.transformschaincreator import TransformsChainCreator
from praudio.preprocessors.filepreprocessor import FilePreprocessor
from praudio.io.numpysaver import NumpySaver
from praudio.transforms import Log, MagnitudeSpectrogram, MinMaxScaler
from utils_creation import file_preprocessor_creator, transforms_chain_creator


@pytest.fixture
def configs():
    configs = {
        "loader": {
            "sample_rate": 44100,
        },
        "transforms_chain": {
            "magnitudespectrogram": {
                "frame_length": 1024,
                "hop_length": 512,
                "win_length": 1024,
                "window": "hann"
            },
            "log": {},
            "minmaxscaler": {
                "min": -2,
                "max": 2,
            }
        }
    }
    return configs


def test_file_preprocessor_creator_is_instantiated(file_preprocessor_creator):
    assert isinstance(file_preprocessor_creator, FilePreprocessorCreator)
    assert isinstance(file_preprocessor_creator.transforms_chain_creator, TransformsChainCreator)


def test_transforms_chain_is_created_correctly(file_preprocessor_creator,
                                               configs):
    """
    GIVEN a FilePreprocessorCreator object
    AND correct configs as dicts of dicts
    WHEN 'create' is called
    AND the configs passed
    THEN a FilePreprocessor object is created
    AND the FilePreprocessor is returned
    """
    file_preprocessor = file_preprocessor_creator.create(configs)
    assert isinstance(file_preprocessor, FilePreprocessor)
    assert file_preprocessor.loader.sample_rate == 44100
    assert file_preprocessor.transforms_chain.transforms_names == [
        "magnitudespectrogram", "log", "minmaxscaler"]
    assert isinstance(file_preprocessor.saver, NumpySaver)


