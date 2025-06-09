METRIC_LENGTH_CASES = [
    (10.0, "millimeters", "centimeters", 1.0),
    (1.0, "centimeters", "millimeters", 10.0),
    (1000.0, "millimeters", "meters", 1.0),
    (1.0, "meters", "millimeters", 1000.0),
    (1000000.0, "millimeters", "kilometers", 1.0),
    (1.0, "kilometers", "millimeters", 1000000.0),
    (100.0, "centimeters", "meters", 1.0),
    (1.0, "meters", "centimeters", 100.0),
    (100000.0, "centimeters", "kilometers", 1.0),
    (1.0, "kilometers", "centimeters", 100000.0),
    (1000.0, "meters", "kilometers", 1.0),
    (1.0, "kilometers", "meters", 1000.0),
]

IMPERIAL_LENGTH_CASES = [
    (12.0, "inches", "feet", 1.0),
    (1.0, "feet", "inches", 12.0),
    (36.0, "inches", "yards", 1.0),
    (1.0, "yards", "inches", 36.0),
    (63360.0, "inches", "miles", 1.0),
    (1.0, "miles", "inches", 63360.0),
    (3.0, "feet", "yards", 1.0),
    (1.0, "yards", "feet", 3.0),
    (5280.0, "feet", "miles", 1.0),
    (1.0, "miles", "feet", 5280.0),
    (1760.0, "yards", "miles", 1.0),
    (1.0, "miles", "yards", 1760.0),
]

MIXED_SYSTEM_LENGTH_CASES = [
    (25.4, "millimeters", "inches", 1.0),
    (1.0, "inches", "millimeters", 25.4),
    (304.8, "millimeters", "feet", 1.0),
    (1.0, "feet", "millimeters", 304.8),
    (914.4, "millimeters", "yards", 1.0),
    (1.0, "yards", "millimeters", 914.4),
    (1609344, "millimeters", "miles", 1.0),
    (1.0, "miles", "millimeters", 1609344),
    (2.54, "centimeters", "inches", 1.0),
    (1.0, "inches", "centimeters", 2.54),
    (30.48, "centimeters", "feet", 1.0),
    (1.0, "feet", "centimeters", 30.48),
    (91.44, "centimeters", "yards", 1.0),
    (1.0, "yards", "centimeters", 91.44),
    (160934.4, "centimeters", "miles", 1.0),
    (1.0, "miles", "centimeters", 160934.4),
    (39.37008, "inches", "meters", 1.0),
    (1.0, "meters", "inches", 39.37008),
    (3.28084, "feet", "meters", 1.0),
    (1.0, "meters", "feet", 3.28084),
    (1.093613, "yards", "meters", 1.0),
    (1.0, "meters", "yards", 1.093613),
    (1609.344, "meters", "miles", 1.0),
    (1.0, "miles", "meters", 1609.344),
    (0.6213712, "miles", "kilometers", 1.0),
    (1.0, "kilometers", "miles", 0.6213712),
]

METRIC_WEIGHT_CASES = [
    (1000, "milligrams", "grams", 1.0),
    (1.0, "grams", "milligrams", 1000),
    (1000000, "milligrams", "kilograms", 1.0),
    (1.0, "kilograms", "milligrams", 1000000),
    (1000, "grams", "kilograms", 1.0),
    (1.0, "kilograms", "grams", 1000),
]

IMPERIAL_WEIGHT_CASES = [
    (16, "ounces", "pounds", 1.0),
    (1.0, "pounds", "ounces", 16),
]

MIXED_SYSTEM_WEIGHT_CASES = [
    (28349.52, "milligrams", "ounces", 1.0),
    (1.0, "ounces", "milligrams", 28349.52),
    (453592.4, "milligrams", "pounds", 1.0),
    (1.0, "pounds", "milligrams", 453592.4),
    (28.34952, "grams", "ounces", 1.0),
    (1.0, "ounces", "grams", 28.34952),
    (453.5924, "grams", "pounds", 1.0),
    (1.0, "pounds", "grams", 453.5924),
    (0.02834952, "kilograms", "ounces", 1.0),
    (1.0, "ounces", "kilograms", 0.02834952),
    (0.4535924, "kilograms", "pounds", 1.0),
    (1.0, "pounds", "kilograms", 0.4535924),
]


TEMP_CONVERSION_CASES = [
    (0, "celsius", "fahrenheit", 32),
    (32, "fahrenheit", "celsius", 0),
    (0, "fahrenheit", "kelvin", 255.3722),
    (255.3722, "kelvin", "fahrenheit", 0),
    (0, "celsius", "kelvin", 273.15),
    (273.15, "kelvin", "celsius", 0),
]
