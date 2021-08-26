"""
This module contains a class that instantiates a transforms chain object
from configuration for each transform in the chain.
"""

import logging

from typing import Dict, List

from praudio.creation.transformfactory import TransformFactory
from praudio.transformschain import TransformsChain
from praudio.transforms.transform import Transform


logger = logging.getLogger(__name__)


class TransformsChainCreator:
    """TransformsChainCreator instantiates a TransformsChain object from
    config, offloading the creation of concrete transforms to a transform
    factory.

    Attributes:
        - transform_factory (TransformFactory): Factory that instantiates
            transforms
    """

    def __init__(self, transform_factory: TransformFactory):
        self.transform_factory = transform_factory
        logger.info("Instantiated TransformsChainCreator object")

    def create(self, configs: Dict[str, dict]) -> TransformsChain:
        """Create a transforms chain from transform configurations.

        :param configs: Dictionary of dictionary. Each nested dict provides
            configurations for a transform. Configs example:
                {
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

            Check out concrete transforms' documentation to check all the
            available arguments to pass in the configs.

        :return: Instantiated transforms chain
        """
        transforms = self._create_transforms(configs)
        transforms_chain = TransformsChain(transforms)
        return transforms_chain

    def _create_transforms(self, configs: Dict[str, dict]) -> List[Transform]:
        transforms = []
        for transform_type, transform_config in configs.items():
            transform = self.transform_factory.create(transform_type,
                                                      **transform_config)
            transforms.append(transform)
        return transforms
