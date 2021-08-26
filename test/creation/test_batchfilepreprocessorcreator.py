import pytest


from praudio.creation.batchfilepreprocessorcreator import BatchFilePreprocessorCreator
from praudio.creation.filepreprocessorcreator import FilePreprocessorCreator
from praudio.preprocessors.batchfilepreprocessor import BatchFilePreprocessor
from praudio.preprocessors.filepreprocessor import FilePreprocessor
from utils_creation import file_preprocessor_creator, transforms_chain_creator


@pytest.fixture
def batch_file_preprocessor_creator(file_preprocessor_creator):
    return BatchFilePreprocessorCreator(file_preprocessor_creator)


@pytest.fixture
def configs():
    configs = {
        "dataset_dir": "/path/to/dataset/",
        "save_dir": "/dir/where/to/store/preprocessed/dataset/",
        "file_preprocessor": {
            "loader": {
                "sample_rate": 44100,
                "mono": True
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
    }
    return configs


def test_batch_file_preprocessor_creator_is_instantiated(batch_file_preprocessor_creator):
    assert isinstance(batch_file_preprocessor_creator, BatchFilePreprocessorCreator)
    assert isinstance(batch_file_preprocessor_creator.file_preprocessor_creator,
                      FilePreprocessorCreator)


def test_transforms_chain_is_created_correctly(batch_file_preprocessor_creator,
                                               configs):
    """
    GIVEN a BatchFilePreprocessorCreator object
    AND correct configs
    WHEN 'create' is called
    AND the configs passed
    THEN a BatchFilePreprocessor object is created
    AND the BatchFilePreprocessor is returned
    """
    bfp = batch_file_preprocessor_creator.create(configs)
    assert isinstance(bfp, BatchFilePreprocessor)
    assert isinstance(bfp.preprocessor, FilePreprocessor)
    assert bfp.dataset_dir == "/path/to/dataset/"
    assert bfp.save_dir == "/dir/where/to/store/preprocessed/dataset/"


