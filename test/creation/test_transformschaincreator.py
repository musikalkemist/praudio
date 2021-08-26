import pytest

from praudio.transformschain import TransformsChain
from praudio.creation.transformfactory import TransformFactory
from praudio.creation.transformschaincreator import TransformsChainCreator
from praudio.transforms import Log, MagnitudeSpectrogram, MinMaxScaler
from utils_creation import transforms_chain_creator


@pytest.fixture
def configs():
    configs = {
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
    return configs


def test_transforms_chain_creator_is_instantiated(transforms_chain_creator):
    assert isinstance(transforms_chain_creator, TransformsChainCreator)
    assert isinstance(transforms_chain_creator.transform_factory, TransformFactory)


def test_transforms_chain_is_created_correctly(transforms_chain_creator,
                                               configs):
    """
    GIVEN a TransformsChainCreator object
    AND correct transforms configs as dicts of dicts
    WHEN 'create' is called
    AND the configs passed
    THEN a TransformsChain object with the correct transforms is created
    AND the TransformsChain object is returned
    """
    transforms_chain = transforms_chain_creator.create(configs)
    assert isinstance(transforms_chain, TransformsChain)
    assert len(transforms_chain.transforms) == 3


def test_transforms_are_generated_from_configs(transforms_chain_creator,
                                               configs):
    """
    GIVEN a TransformsChainCreator object
    AND correct transforms configs as dicts of dicts
    WHEN '_create_transforms' is called
    AND the configs passed
    THEN a list of transforms is instantiated
    AND the list is returned
    """
    transforms = transforms_chain_creator._create_transforms(configs)
    assert len(transforms) == 3
    assert isinstance(transforms[0], MagnitudeSpectrogram)
    assert isinstance(transforms[1], Log)
    assert isinstance(transforms[2], MinMaxScaler)

