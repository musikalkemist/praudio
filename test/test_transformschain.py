import pytest

from praudio.transformschain import TransformsChain
from praudio.transforms import MagnitudeSpectrogram, Log, MinMaxScaler
from transforms.utils_transforms import sample_signal

magnitude_spectrogram = MagnitudeSpectrogram()
log = Log()
min_max_scaler = MinMaxScaler(-2, 2)
transforms = [magnitude_spectrogram, log, min_max_scaler]


@pytest.fixture(scope="module")
def transforms_chain():
    return TransformsChain(transforms)


def test_transforms_chain_is_instantiated_correctly(transforms_chain):
    assert isinstance(transforms_chain, TransformsChain)
    assert transforms_chain.transforms == transforms


def test_transforms_names_are_returned_correctly(transforms_chain):
    assert transforms_chain.transforms_names == [
        "magnitudespectrogram",
        "log",
        "minmaxscaler"
    ]


def test_signal_is_sequentially_processed(transforms_chain, sample_signal):
    """
    GIVEN a Signal object
    AND a TransofrmsChain object
    WHEN the signal is passed to process
    THEN transforms are sequentially applied to the Signal
    AND the modified Signal is returned
    """
    transformed_signal =  transforms_chain.process(sample_signal)
    assert transformed_signal.name == \
           "minmaxscaler_log_magnitudespectrogram_stft_dummy"
    assert len(transformed_signal.data.shape) == 2
    assert transformed_signal.data.min() == -2
    assert transformed_signal.data.max() == 2


