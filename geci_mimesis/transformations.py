from mimesis import Field


def add_offset(augend: int, addend: int) -> int:
    return augend + addend


def number_field(field: dict) -> list:
    field = Field()
    return field("numeric.float_number", start=0.0, end=1.67)
