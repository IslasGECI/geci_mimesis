from mimesis import Field


def number_field(field: dict) -> list:
    field = Field()
    return field("numeric.float_number", start=0.0, end=1.67)


def integer_field(field: dict) -> list:
    field = Field()
    return field("numeric.integer_number", start=0, end=67)


def enum_field(field: dict) -> list:
    enum_list: list = field["constraints"]["enum"]
    field_generator = Field()
    return field_generator("choice", items=enum_list)
