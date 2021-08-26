import pytest

from praudio.config.configvalidator import ConfigValidator
from praudio.errors import ParameterMissingError
from utils_config import configs


expected_parameters = (
    "save_dir",
    "dataset_dir",
    "file_preprocessor"
)


@pytest.fixture
def config_validator():
    cv = ConfigValidator(expected_parameters)
    return cv


def test_config_validator_is_instantiated(config_validator):
    assert isinstance(config_validator, ConfigValidator)
    assert config_validator.expected_parameters == expected_parameters


def test_config_validation_throws_file_exists_error(config_validator, configs):
    """
    GIVEN a ConfigLoader
    AND a config file with non existing dataset dir
    WHEN validate is called
    AND the config file is passed
    THEN FileExistsError is thrown
    """
    with pytest.raises(FileExistsError):
        config_validator.validate(configs)


def test_config_validation_throws_param_missing_error(config_validator, configs):
    """
    GIVEN a ConfigLoader
    AND a config file with a missing expected param
    WHEN validate is called
    AND the config file is passed
    THEN FileExistsError is thrown
    """
    config = {
        "dataset_dir": ".",
        "file_preprocessor": {
            "loader": {},
            "transforms_chain": {}
        }
    }
    with pytest.raises(ParameterMissingError):
        config_validator.validate(config)


def test_file_exists_error_is_thrown_when_dataset_dir_doesnt_exist(
        config_validator):
    with pytest.raises(FileExistsError):
        config_validator._raise_file_exists_error_if_dataset_dir_doesnt_exist(
            "non/existing/dir")


def test_parameter_missing_error_if_param_is_missing_in_config(
        config_validator):
    config = {
        "dataset_dir": {},
        "file_preprocessor": {
            "loader": {},
            "transforms_chain": {}
        }
    }
    with pytest.raises(ParameterMissingError):
        config_validator._raise_parameter_missing_error_if_param_is_missing(
            config)