import geci_mimesis as dt


field: dict = {
    "name": "Horas_traslado",
    "type": "number",
    "format": "default",
    "long_name": "Commuting time",
    "nombre_largo": "Tiempo de traslado",
    "units": "hr",
    "constraints": {"minimum": 0, "maximum": 1.67},
}


def test_number_field():
    obtained = dt.number_field(field)
    assert obtained < 1.67


all_islet: list = [
    "Asuncion",
    "Coronado Medio",
    "Coronado Norte",
    "Coronado Sur",
    "Coronado Terron de Azucar",
    "Natividad",
    "San Benito Este",
    "San Benito Medio",
    "San Benito Oeste",
    "San Jeronimo",
    "San Martin",
    "San Roque",
    "Todos Santos",
    "Todos Santos Norte",
    "Todos Santos Sur",
]

island: dict = {
    "type": "string",
    "name": "Isla",
    "format": "default",
    "constraints": {"enum": all_islet},
}


def test_enum_field():
    obtained = dt.enum_field(island)
    assert obtained in all_islet


captures: dict = {
    "name": "Capturas",
    "type": "integer",
    "format": "default",
    "long_name": "Number of removed goats by flight",
    "nombre_largo": "Número de cabras removidas por vuelo",
    "constraints": {"minimum": 1, "maximum": 52},
}


def test_integer_field():
    obtained = dt.integer_field(captures)
    assert obtained < 52
    assert obtained > 1


def test_get_right_field():
    captures: dict = {
        "name": "Capturas",
        "type": "integer",
        "format": "default",
        "long_name": "Number of removed goats by flight",
        "nombre_largo": "Número de cabras removidas por vuelo",
        "constraints": {"minimum": 1, "maximum": 2},
    }
    obtained = dt.get_right_field(captures)
    superior_limit = 2
    assert obtained <= superior_limit
    assert obtained >= 1
    captures_without_constraints: dict = {
        "name": "Capturas",
        "type": "integer",
        "format": "default",
        "long_name": "Number of removed goats by flight",
        "nombre_largo": "Número de cabras removidas por vuelo",
    }
    obtained = dt.get_right_field(captures_without_constraints)


def test_get_right_key() -> None:
    obtained = get_right_key(captures)
    expected = "integer_constraints"
    assert obtained == expected


expedition: dict = {
    "name": "Expedicion",
    "type": "integer",
    "format": "default",
    "long_name": "Expedition ID",
    "nombre_largo": "ID de expedición",
}


def test_integer_field_without_constraints():
    obtained = dt.integer_field_without_constraints(expedition)
    assert isinstance(obtained, int)
