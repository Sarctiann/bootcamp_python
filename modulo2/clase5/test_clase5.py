try:
    from .clase5 import get_first_element  # type: ignore # noqa
except ImportError:
    assert False, "No se pudo importar la función `get_first_element`"

try:
    from .clase5 import make_dict  # type: ignore # noqa
except ImportError:
    assert False, "No se pudo importar la función `make_dict`"

try:
    from .clase5 import reset_price  # type: ignore # noqa
except ImportError:
    assert False, "No se pudo importar la función `modify_prices`"

try:
    from .clase5 import backup_prices  # type: ignore # noqa
except ImportError:
    assert False, "No se pudo importar la función `backup_prices`"


# -----------------------------------------------------------------------------

from .clase5 import restrictive_map


def test_restrictive_map():
    assert restrictive_map("key1") == "value1"
    assert restrictive_map("key2") == "value2"
    assert restrictive_map("key3") == "value3"
    try:
        restrictive_map("key4")
    except KeyError as e:
        assert isinstance(e, KeyError)
    else:
        assert False, "No se lanzó la excepción KeyError"


# -----------------------------------------------------------------------------


def test_get_first_element():
    assert get_first_element([1, 2, 3]) == 1
    assert get_first_element([4, 5, 6]) == 4
    assert get_first_element([7, 8, 9]) == 7


def test_make_dict():
    keys = ["key1", "key2", "key3"]
    values = ["value1", "value2", "value3"]

    result = make_dict(keys, values)
    assert result.get("key1") == "value1", "El valor de la clave 'key1' es incorrecto"
    assert result.get("key2") == "value2", "El valor de la clave 'key2' es incorrecto"
    assert result.get("key3") == "value3", "El valor de la clave 'key3' es incorrecto"


prices = [100, 200, 300]
db = {"prices": prices}


def test_modify_prices():
    reset_price(db, 1)
    new_prices = db.get("prices", [])
    assert 100 in new_prices, "La función alteró un indice incorrecto"
    assert 200 not in new_prices, "La función no alteró el indice esperado"
    assert 0 not in new_prices, "La función no alteró ningún índice"
    assert 300 in new_prices, "La función alteró un indice incorrecto"


def test_backup_prices():
    bkp = backup_prices(db)
    ori_prices_origin = db.get("prices", [])
    bkp_prices_origin = bkp.get("prices_origin", [])
    bkp_prices = bkp.get("prices", [])

    assert (
        ori_prices_origin is bkp_prices_origin
    ), "La clave 'prices_origin' no apunta a la lista original"

    assert (
        bkp_prices_origin == bkp_prices
    ), "La lista 'prices' no es igual a 'prices_origin'"

    assert (
        ori_prices_origin is not bkp_prices
    ), "'prices_origin' y 'prices' son el mismo objeto"
