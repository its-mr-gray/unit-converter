import pytest

from app.converters import convert_length
from tests.test_helpers.test_cases import (
    IMPERIAL_LENGTH_CASES,
    METRIC_LENGTH_CASES,
    MIXED_SYSTEM_LENGTH_CASES,
)

ALL_LENGTH_CASES = (
    METRIC_LENGTH_CASES + IMPERIAL_LENGTH_CASES + MIXED_SYSTEM_LENGTH_CASES
)


@pytest.mark.parametrize(
    "input_val, from_unit, to_unit, expected",
    ALL_LENGTH_CASES,
)
def test_length_conversions(input_val, from_unit, to_unit, expected):
    assert convert_length(input_val, from_unit, to_unit) == pytest.approx(
        expected, rel=1e-5, abs=1e-8
    )


def test_invalid_from_unit():
    with pytest.raises(ValueError, match="Unknown unit."):
        convert_length(10, "meterssss", "yards")


def test_invalid_to_unit():
    with pytest.raises(ValueError, match="Unknown unit."):
        convert_length(10, "meters", "yardsss")


def test_invalid_value_type():
    with pytest.raises(TypeError, match="Invalid value."):
        convert_length("120", "meters", "yards")


def test_negative_value():
    with pytest.raises(ValueError, match="Negative values disallowed."):
        convert_length(-120.8947534, "meters", "yards")
