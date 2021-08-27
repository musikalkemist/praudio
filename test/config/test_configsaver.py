import os

import pytest

from praudio.config.configsaver import ConfigSaver


@pytest.fixture
def config_saver():
    return ConfigSaver()


def test_config_saver_is_instantiated_correctly(config_saver):
    assert isinstance(config_saver, ConfigSaver)


def test_configs_are_saved(config_saver):
    dummy_config = {
        "param": 1,
        "param2": [1, 2, 3],
        "param3": {
            "p1": "a",
            "p2": 2
        }
    }
    config_saver.save("dummyconfig.yml", dummy_config)
    assert os.path.isfile("dummyconfig.yml")
    os.remove("dummyconfig.yml")
