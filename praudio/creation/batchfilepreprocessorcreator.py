"""
This module contains a class that instantiates a BatchFilePreprocessorCreator
object from configurations.
"""

import logging

from praudio.preprocessors.batchfilepreprocessor import BatchFilePreprocessor
from praudio.creation.filepreprocessorcreator import FilePreprocessorCreator


logger = logging.getLogger(__name__)


class BatchFilePreprocessorCreator:
    """BatchFilePreprocessorCreator instantiates a BatchFilePreprocessor
    object from config.

    It offloads the creation of the FilePreprocessor object to
    FilePreprocessorChainCreator.

    Attributes:
        - file_preprocessor_creator: Instantiate a FilePreprocessor
    """

    def __init__(self, file_preprocessor_creator: FilePreprocessorCreator):
        self.file_preprocessor_creator = file_preprocessor_creator
        logger.info("Instantiated BatchFilePreprocessorCreator object")

    def create(self, configs: dict) -> BatchFilePreprocessor:
        """Create a batch file preprocessor from configurations.

        :param configs: Nested dictionary which contains config
            params of the type::
                {
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

        :return: Instantiated batch file preprocessor
        """
        file_preprocessor = self.file_preprocessor_creator.create(configs["file_preprocessor"])
        batch_file_preprocessor = BatchFilePreprocessor(file_preprocessor,
                                                        configs["dataset_dir"],
                                                        configs["save_dir"])

        return batch_file_preprocessor
