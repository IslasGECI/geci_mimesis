import numpy as np
import geci_mimesis as dt


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained


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


island: dict = {
    "type": "string",
    "name": "Isla",
    "format": "default",
    "constraints": {
        "enum": [
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
    },
}


def test_enum_field():
    obtained = dt.enum_field(field)
    assert obtained == "Todos Santos Norte"
