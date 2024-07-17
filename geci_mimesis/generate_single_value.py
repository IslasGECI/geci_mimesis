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
    right_field = selector_type_of_field(field)
    return right_field(field)


def get_right_key(field: dict) -> str:
    field_type: str = field["type"]
    if "constraints" in field:
        return f"{field_type}_constraints"
    return field_type


def selector_type_of_field(field: dict):
    field_type: str = get_right_key(field)
    different_field = {
        "integer_constraints": integer_field,
        "integer": integer_field_without_constraints,
    }
    return different_field[field_type]
