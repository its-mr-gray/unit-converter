import pytest

from app.converters import convert_temp
from tests.test_helpers.test_cases import TEMP_CONVERSION_CASES


@pytest.mark.parametrize(
    "input_val, from_unit, to_unit, expected", TEMP_CONVERSION_CASES
)
def test_temp_conversions(input_val, from_unit, to_unit, expected):
    assert convert_temp(input_val, from_unit, to_unit) == pytest.approx(
        expected, rel=1e-5, abs=1e-4
    )


def test_invalid_from_unit():
    with pytest.raises(ValueError, match="Unknown unit."):
        convert_temp(10, "calvin", "celsius")


def test_invalid_to_unit():
    with pytest.raises(ValueError, match="Unknown unit."):
        convert_temp(10, "kelvin", "selsius")


def test_invalid_value_type():
    with pytest.raises(TypeError, match="Invalid value."):
        convert_temp("120", "kelvin", "celsius")
