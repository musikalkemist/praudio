"""
This module features the 'preprocess' entry point. This script allows the
user to batch preprocess a dataset of audio files, specifying the types of
transforms to apply to the data, and their parameters, in a config file.

To use the entry point run:

$ preprocess /path/to/config.yml
"""

import argparse
from pathlib import Path

from praudio.config.configloader import create_config_loader
from praudio.config.configsaver import ConfigSaver
from praudio.creation.batchfilepreprocessorcreator import create_batch_file_preprocessor_creator


def _parse_config_file() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file",
                        help="path to config file",
                        type=str)
    args = parser.parse_args()
    return args.config_file


def _init_batch_file_preprocessor(config_file: str):
    config_loader = create_config_loader()
    batch_file_preprocessor_creator = create_batch_file_preprocessor_creator()
    configs = config_loader.load(config_file)
    batch_file_preprocessor = batch_file_preprocessor_creator.create(configs)
    return batch_file_preprocessor, configs


def _save_configs(configs: dict):
    config_saver = ConfigSaver()
    save_path = str(Path(configs["save_dir"], "configs").with_suffix(".yml"))
    config_saver.save(save_path, configs)


def preprocess():
    config_file = _parse_config_file()
    batch_file_preprocessor, configs = _init_batch_file_preprocessor(config_file)
    batch_file_preprocessor.preprocess()
    _save_configs(configs)



if __name__ == "__main__":
    preprocess()
