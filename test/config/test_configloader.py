import shutil
from pathlib import Path

import pytest

from praudio.config.configloader import ConfigLoader, create_config_loader
from praudio.config.configvalidator import ConfigValidator
from praudio.utils import create_dir_hierarchy
from utils_config import configs


DUMMY_CONFIG_FILE = Path(Path(__file__).parent, "sampleconfig").with_suffix(".yml")


@pytest.fixture
def config_loader(mocker):
    return ConfigLoader(ConfigValidator())


def test_config_loader_is_instantiated(config_loader):
    assert isinstance(config_loader, ConfigLoader)
    assert isinstance(config_loader.validator, ConfigValidator)


def test_config_is_loaded(config_loader, configs):
    """
    GIVEN a ConfigLoader
    AND a valid config file
    WHEN 'load' is called
    AND the config file is passed
    THEN the config file is loaded
    AND the configurations are returned as a dictionary
    """
    # we must temporarily create the hierarchy of dirs below for 'dataset_dir',
    # otherwise the validator would thrown an error
    create_dir_hierarchy("path/to/dataset/")
    loaded_configs = config_loader.load(DUMMY_CONFIG_FILE)
    shutil.rmtree("path")
    assert loaded_configs == configs


def test_config_loader_throws_file_exists_error_if_dataset_dir_doesnt_eixst(
        config_loader, configs):
    """
    GIVEN a ConfigLoader
    AND a config file with a dataset_dir that doesn't exist
    WHEN 'load' is called
    AND the config file is passed
    THEN FileExistsError is thrown
    """
    with pytest.raises(FileExistsError):
        loaded_configs = config_loader.load(DUMMY_CONFIG_FILE)


def test_config_loader_is_created():
    conf_loader = create_config_loader()
    assert isinstance(conf_loader, ConfigLoader)