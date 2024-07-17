from mimesis import Field


def number_field(field: dict) -> list:
    field_generator = Field()
    return field_generator("numeric.float_number", start=0.0, end=1.67)


def integer_field(field: dict) -> list:
    constraints: dict = field["constraints"]
    field_generator = Field()
    return field_generator(
        "numeric.integer_number", start=constraints["minimum"], end=constraints["maximum"]
    )


def enum_field(field: dict) -> list:
    enum_list: list = field["constraints"]["enum"]
    field_generator = Field()
    return field_generator("choice", items=enum_list)


def integer_field_without_constraints(field: dict) -> list:
    field_generator = Field()
    return field_generator("numeric.integer_number")


def get_right_field(field: dict) -> list:
    if "constraints" in field:
        return integer_field(field)
    return integer_field_without_constraints(field)


def get_right_key(field: dict) -> str:
    return "integer_constraints"
