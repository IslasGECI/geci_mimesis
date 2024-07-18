from pytest import approx
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


def _average(lst):
    return sum(lst) / len(lst)


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


def test_get_right_field() -> None:
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
    obtained = dt.get_right_field(island)
    assert obtained in all_islet

    assert all([dt.get_right_field(field) < 1.67 for _ in range(10)])
    mean_field = _average([dt.get_right_field(field) for _ in range(500)])
    assert approx(mean_field, abs=1e-1) == 1.67 / 2
