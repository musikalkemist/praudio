import pytest

from praudio.creation.transformfactory import TransformFactory
from praudio.transforms import MinMaxScaler

@pytest.fixture
def transform_factory():
    return TransformFactory()


def test_transform_factory_is_instantiated(transform_factory):
    assert isinstance(transform_factory, TransformFactory)


def test_concrete_transform_is_instantiated(transform_factory):
    """
    GIVEN a TransformFactory
    WHEN 'create' is called
    AND an available transform type string is passed
    AND additional keyword arguments are passed
    THEN the respective concrete transform is instantiated
    AND returned
    """
    kwargs = {
        "min": -2.,
        "max": 2.
    }
    min_max_scaler = transform_factory.create("minmaxscaler", **kwargs)
    assert isinstance(min_max_scaler, MinMaxScaler)
    assert min_max_scaler.min_val == -2
    assert min_max_scaler.max_val == 2


def test_type_error_is_raised_when_instantiating_non_existing_transform(
        transform_factory):
    """
    GIVEN a TransformFactory
    WHEN 'create' is called
    AND an unavailable transform type string is passed
    THEN TypeError is thrown
    """
    with pytest.raises(TypeError) as err:
        min_max_scaler = transform_factory.create("non_existing_transform")


