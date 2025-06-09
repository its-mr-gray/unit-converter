import pytest

from app.converters import convert_weight
from tests.test_helpers.test_cases import (
    IMPERIAL_WEIGHT_CASES,
    METRIC_WEIGHT_CASES,
    MIXED_SYSTEM_WEIGHT_CASES,
)

ALL_WEIGHT_CASES = (
    METRIC_WEIGHT_CASES + IMPERIAL_WEIGHT_CASES + MIXED_SYSTEM_WEIGHT_CASES
)


@pytest.mark.parametrize(
    "input_val, from_unit, to_unit, expected",
    ALL_WEIGHT_CASES,
)
def test_weight_conversions(input_val, from_unit, to_unit, expected):
    assert convert_weight(input_val, from_unit, to_unit) == pytest.approx(
        expected, rel=1e-5, abs=1e-8
    )


def test_invalid_from_unit():
    with pytest.raises(ValueError, match="Unknown unit."):
        convert_weight(10, "gramss", "kilograms")


def test_invalid_to_unit():
    with pytest.raises(ValueError, match="Unknown unit."):
        convert_weight(10, "grams", "kilogramsss")


def test_invalid_value_type():
    with pytest.raises(TypeError, match="Invalid value."):
        convert_weight("120", "grams", "kilograms")


def test_negative_value():
    with pytest.raises(ValueError, match="Negative values disallowed."):
        convert_weight(-120.8947534, "grams", "kilograms")
