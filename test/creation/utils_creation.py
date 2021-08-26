import pytest

from praudio.creation.transformfactory import TransformFactory
from praudio.creation.transformschaincreator import TransformsChainCreator
from praudio.creation.filepreprocessorcreator import FilePreprocessorCreator


@pytest.fixture
def transforms_chain_creator():
    tf = TransformFactory()
    return TransformsChainCreator(tf)


@pytest.fixture
def file_preprocessor_creator(transforms_chain_creator):
    return FilePreprocessorCreator(transforms_chain_creator)
