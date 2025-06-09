ROUTES = [
    "temperature",
    "weight",
    "length",
]

MISSING_PARAMS = [
    ("val=100&from_unit=x", "to_unit"),
    ("from_unit=x&to_unit=y", "val"),
    ("val=100&to_unit=y", "from_unit"),
]


INVALID_UNIT_CASES = [
    ("val=100&from_unit=flkasjdf&to_unit=kilograms", "Unknown unit."),
    ("val=100&from_unit=grams&to_unit=askdjf;la", "Unknown unit."),
]
