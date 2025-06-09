# base case: meters
LENGTH_CONVERSION_FACTORS = {
    "millimeters": 0.001,
    "centimeters": 0.01,
    "meters": 1.0,
    "kilometers": 1000.0,
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.9144,
    "miles": 1609.344,
}

# base case: grams
WEIGHT_CONVERSION_FACTORS = {
    "milligrams": 0.001,
    "grams": 1.0,
    "kilograms": 1000.0,
    "ounces": 28.34952,
    "pounds": 453.5924,
}

# handler mappings using base case: kelvin
TO_KELVIN = {
    "celsius": lambda c: c + 273.15,
    "fahrenheit": lambda f: (f - 32) * (5 / 9) + 273.15,
    "kelvin": lambda k: k,
}

FROM_KELVIN = {
    "celsius": lambda k: k - 273.15,
    "fahrenheit": lambda k: (k - 273.15) * (9 / 5) + 32,
    "kelvin": lambda k: k,
}
