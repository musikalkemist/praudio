""" This module contains facilities to store configuration files. """

import logging

import yaml


logger = logging.getLogger(__name__)


class ConfigSaver:
    """ConfigSaver saves a Python object as a yaml file."""

    def __init__(self):
        logger.info("Initialised ConfigSaver object")
        self._indent = 4

    def save(self,
             file: str,
             configs: dict):
        """Store configurations as a yaml file.

        :param file: Path where to save file
        :param configs: Configurations
        """
        with open(file, "w", encoding="latin-1") as yaml_file:
            yaml.dump(configs,
                      yaml_file,
                      indent=self._indent)
        logger.info("Configs saved at %s", file)
