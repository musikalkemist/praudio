import shutil
from pathlib import Path

from praudio.preprocess import _init_batch_file_preprocessor
from praudio.preprocessors.batchfilepreprocessor import BatchFilePreprocessor
from praudio.utils import create_dir_hierarchy


SAMPLE_CONFIG_FILE = Path(Path(__file__).parent,
                          "config", "sampleconfig").with_suffix(".yml")


def test_batch_file_preprocessor_is_initialised_from_config_file():
    create_dir_hierarchy("path/to/dataset/")
    bfp = _init_batch_file_preprocessor(SAMPLE_CONFIG_FILE)
    shutil.rmtree("path")
    assert isinstance(bfp, BatchFilePreprocessor)