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


#
