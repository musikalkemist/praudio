"""
This module contains a class that instantiates a FilePreprocessor object
from configurations.
"""

import logging

from typing import Dict

from praudio.io.loader import Loader
from praudio.io.numpysaver import NumpySaver
from praudio.creation.transformschaincreator import TransformsChainCreator
from praudio.preprocessors.filepreprocessor import FilePreprocessor


logger = logging.getLogger(__name__)


class FilePreprocessorCreator:
    """FileProcessorCreator instantiates a FilePreprocessor object from
    config.

    It offloads the creation of the transforms chain object to
    TransformsChainCreator.

    Attributes:
        - transforms_chain_creator: Instantiate a TransformsChain
    """

    def __init__(self, transforms_chain_creator: TransformsChainCreator):
        self.transforms_chain_creator = transforms_chain_creator
        logger.info("Instantiated FileProcessorCreator object")

    def create(self, configs: Dict[str, dict]) -> FilePreprocessor:
        """Create a file preprocessor from transform configurations.

        The Loader and the NumpySaver are instantiated in the
        in a hardcoded way. In the future, if there'll be more
        concrete savers / loaders, it's suggested to pass the loader, savers
        factories as arguments to the constructor. The factories can then be
        used in this method to produce specific savers / loaders

        :param configs: Dictionary of dictionary. Each nested dict provides
            configurations for loader and transforms chain. Configs example:
                {
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

        :return: Instantiated file preprocessor
        """
        loader = Loader(**configs["loader"])
        transforms_chain = self.transforms_chain_creator.create(configs["transforms_chain"])
        saver = NumpySaver()
        file_preprocessor = FilePreprocessor(loader, transforms_chain, saver)
        return file_preprocessor
