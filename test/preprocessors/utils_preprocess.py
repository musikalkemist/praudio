import pytest

from praudio.preprocessors.filepreprocessor import FilePreprocessor
from praudio.io.numpysaver import NumpySaver
from praudio.transformschain import TransformsChain
from praudio.transforms import MagnitudeSpectrogram, Log
from praudio.io.loader import Loader


@pytest.fixture
def file_preprocessor():
    log = Log()
    ms = MagnitudeSpectrogram()
    transforms_chain = TransformsChain([ms, log])
    return FilePreprocessor(Loader(), transforms_chain, NumpySaver())