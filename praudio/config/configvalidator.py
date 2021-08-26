"""This module has simple validation for config files."""

import logging
from pathlib import Path

from praudio.errors import ParameterMissingError


logger = logging.getLogger(__name__)


default_expected_parameters = (
    "save_dir",
    "dataset_dir",
    "file_preprocessor"
)


class ConfigValidator:
    """ConfigValidator checks that configurations in a file respect basic
    constrains. The higher-level keys should be present and 'dataset_dir'
    should exist."""

    def __init__(self, expected_parameters: tuple = default_expected_parameters):
        self.expected_parameters = expected_parameters
        logger.info("Instantiated ConfigValidator object")

    def validate(self, configs: dict):
        """Raise error if configurations aren't valid.

        :param configs: Dictionary with configurations
        """
        self._raise_parameter_missing_error_if_param_is_missing(configs)
        self._raise_file_exists_error_if_dataset_dir_doesnt_exist(configs["dataset_dir"])

    def _raise_parameter_missing_error_if_param_is_missing(self, configs: dict):
        for param in self.expected_parameters:
            if param not in configs:
                raise ParameterMissingError(f"Parameter '{param}' is missing from configuration")

    @staticmethod
    def _raise_file_exists_error_if_dataset_dir_doesnt_exist(dataset_dir: str):
        if not Path(dataset_dir).is_dir():
            raise FileExistsError(f"Dataset dir '{dataset_dir}' provided in "
                                  "config file doesn't exist")
