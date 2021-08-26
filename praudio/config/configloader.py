"""This module has a class to load preprocessing configurations."""

import logging

import yaml

from praudio.config.configvalidator import ConfigValidator


logger = logging.getLogger(__name__)


class ConfigLoader:
    """ConfigLoader is responsible to load preprocessing configurations.

    Attributes:
        - validator: Raise error if raw configs have error
    """
    def __init__(self, config_validator: ConfigValidator):
        self.validator = config_validator
        logger.info("Instantiated ConfigLoader object")

    def load(self, config_file: str):
        with open(config_file, "r", encoding="latin-1") as file:
            configurations = yaml.full_load(file)
        self._validate(configurations)
        logger.info("Loaded configurations from %s", config_file)
        return configurations

    def _validate(self, configurations: dict):
        self.validator.validate(configurations)


def create_config_loader() -> ConfigLoader:
    """Instantiate a config validator object

    :return: New config loader
    """
    config_validator = ConfigValidator()
    return ConfigLoader(config_validator)
