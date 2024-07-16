from mimesis import Field


def number_field(field: dict) -> list:
    field = Field()
    return field("numeric.float_number", start=0.0, end=1.67)


def enum_field(field: dict) -> list:
    field = Field()
    return field("choice", items=["Todos Santos Norte"])
