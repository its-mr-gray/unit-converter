from app.variables import (
    FROM_KELVIN,
    LENGTH_CONVERSION_FACTORS,
    TO_KELVIN,
    WEIGHT_CONVERSION_FACTORS,
)


def convert_length(val: float | int, from_unit: str, to_unit: str) -> float:
    """
    Converts length between units.

    Args:
        val (float, int): The given value of a unit to convert.
        from_unit (str): The unit to be converted.
        to_unit (str): The desired unit to be converted to.

    Returns
        float: The floating point result of conversion.
    """
    validate_errors(
        val=val,
        from_unit=from_unit,
        to_unit=to_unit,
        conversion_factors=LENGTH_CONVERSION_FACTORS,
    )

    val_in_meters = val * LENGTH_CONVERSION_FACTORS[from_unit.lower()]

    result = val_in_meters / LENGTH_CONVERSION_FACTORS[to_unit.lower()]

    return result


def convert_weight(val: float | int, from_unit: str, to_unit: str) -> float:
    """
    Converts weight between units.

    Args:
        val (float, int): The given value of a unit to convert.
        from_unit (str): The unit to be converted.
        to_unit (str): The desired unit to be converted to.

    Returns
        float: The floating point result of conversion.
    """
    validate_errors(
        val=val,
        from_unit=from_unit,
        to_unit=to_unit,
        conversion_factors=WEIGHT_CONVERSION_FACTORS,
    )

    val_in_grams = val * WEIGHT_CONVERSION_FACTORS[from_unit.lower()]

    result = val_in_grams / WEIGHT_CONVERSION_FACTORS[to_unit.lower()]

    return result


def convert_temp(val: float | int, from_unit: str, to_unit: str) -> float | int:
    """
    Converts temperatures between units.

    Args:
        val (float, int): The given value of a unit to convert.
        from_unit (str): The unit to be converted.
        to_unit (str): The desired unit to be converted to.

    Returns
        float, int: The numeric result of conversion.
    """
    validate_temp_errors(val=val, from_unit=from_unit, to_unit=to_unit)

    val_in_kelvin = TO_KELVIN[from_unit.lower()](val)
    result = FROM_KELVIN[to_unit.lower()](val_in_kelvin)

    return result


def validate_errors(
    val: float | int, from_unit: str, to_unit: str, conversion_factors: dict[str, float]
) -> None:
    """
    Validates potential errors in unit conversion.

    Args:
        val (float, int): The given value of a unit to convert.
        from_unit (str): The unit to be converted.
        to_unit (str): The desired unit to be converted to.
        conversion_factors (dict[str, float]): The dictionary of base conversion cases.

    Returns
        None
    """
    if not isinstance(val, (int, float)):
        raise TypeError("Invalid value.")

    if val < 0:
        raise ValueError("Negative values disallowed.")

    if (
        from_unit.lower() not in conversion_factors
        or to_unit.lower() not in conversion_factors
    ):
        raise ValueError("Unknown unit.")


def validate_temp_errors(val: float | int, from_unit: str, to_unit: str) -> None:
    """
    Validates potential errors in temperature conversion.

    Args:
        val (float, int): The given value of a unit to convert.
        from_unit (str): The unit to be converted.
        to_unit (str): The desired unit to be converted to.

    Returns:
        None
    """

    if not isinstance(val, (float, int)):
        raise TypeError("Invalid value.")

    if from_unit.lower() == "kelvin" and val < 0:
        raise ValueError("Negative Kelvin values disallowed")

    if from_unit.lower() not in TO_KELVIN or to_unit.lower() not in FROM_KELVIN:
        raise ValueError("Unknown unit.")
