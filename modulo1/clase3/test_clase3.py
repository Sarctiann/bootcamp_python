from ...utilities import get_annotations_and_rvalues
from .clase3 import ejercicios_de_la_clase_3


ordered_answers = ejercicios_de_la_clase_3()


def _get_next_answer():
    try:
        if ordered_answers is not None:
            return next(ordered_answers)
    except StopIteration:
        print("No more answers")


function_ejercicio_1 = _get_next_answer()
source_ejercicio_1 = get_annotations_and_rvalues(function_ejercicio_1)


def test_funcionanmiento_del_ejercicio_1():
    if function_ejercicio_1 is not None:
        assert function_ejercicio_1(9) == "menor a 10", "9 es menor a 10"
        assert function_ejercicio_1(10) == "mayor o igual a 10", "10 es igual a 10"
        assert function_ejercicio_1(11) == "mayor o igual a 10", "11 es mayor a 10"
    else:
        assert False, "No se encuentra la función a (el primer ejercicio)"


def test_consignas_del_ejercicio_1():
    if (source := source_ejercicio_1["_source"]) is not None:
        assert "if" in source, "Debe haber un if en la función"
        assert "else" not in source, "Debe encontrar una solución sin usar `else`"
    else:
        assert False, "No se encuentra la función a (el primer ejercicio)"


function_ejercicio_2 = _get_next_answer()
source_ejercicio_2 = get_annotations_and_rvalues(function_ejercicio_2)


def test_funcionanmiento_del_ejercicio_2():
    if function_ejercicio_2 is not None:
        assert function_ejercicio_2(1, 10) == 10, "10 es mayor a 1"
        assert function_ejercicio_2(10, 1) == 10, "10 es mayor a 1"
        assert (
            function_ejercicio_2(1, 1) == 0
        ), "1 es igual a 1 el resultado debería ser 0"
    else:
        assert False, "No se encuentra la función b (el segundo ejercicio)"


def test_consignas_del_ejercicio_2():
    if (source := source_ejercicio_2["_source"]) is not None:
        assert "if" in source, "Debe haber al menos un if en la función"
        assert "else" in source, "Debe haber al menos un else en la función"
    else:
        assert False, "No se encuentra la función b (el segundo ejercicio)"


function_ejercicio_3 = _get_next_answer()
source_ejercicio_3 = get_annotations_and_rvalues(function_ejercicio_3)


def test_funcionanmiento_del_ejercicio_3():
    if function_ejercicio_3 is not None:
        assert function_ejercicio_3(9) == 0, "9 es menor a 10 se espera 0"
        assert function_ejercicio_3(10) == 1, "10 es igual a 10 se espera 1"
        assert function_ejercicio_3(11) == 2, "11 es mayor a 10 se espera 2"
    else:
        assert False, "No se encuentra la función c (el tercer ejercicio)"


def test_consignas_del_ejercicio_3():
    if (source := source_ejercicio_3["_source"]) is not None:
        assert "if" in source, "Debe haber un if en la función"
        assert "elif" in source, "Debe haber un elif en la función"
        assert "else" in source, "Debe haber un else en la función"
    else:
        assert False, "No se encuentra la función c (el tercer ejercicio)"


function_ejercicio_4 = _get_next_answer()
source_ejercicio_4 = get_annotations_and_rvalues(function_ejercicio_4)


def test_funcionanmiento_del_ejercicio_4():
    if function_ejercicio_4 is not None:
        assert function_ejercicio_4(5) == 10, "La sumatoria de 5 es 10"
        assert function_ejercicio_4(10) == 45, "La sumatoria de 10 es 45"
    else:
        assert False, "No se encuentra la función d (el cuarto ejercicio)"


def test_consignas_del_ejercicio_4():
    if (source := source_ejercicio_4["_source"]) is not None:
        assert "for" in source, "Debe haber un for en la función"
        assert "range" in source, "Debe haber un range en la función"
    else:
        assert False, "No se encuentra la función d (el cuarto ejercicio)"


function_ejercicio_5 = _get_next_answer()
source_ejercicio_5 = get_annotations_and_rvalues(function_ejercicio_5)


def test_funcionanmiento_del_ejercicio_5():
    if function_ejercicio_5 is not None:
        assert function_ejercicio_5(5, False) == 15, "La sumatoria de 5 es 15"
        assert function_ejercicio_5(5, True) == 9, "La sumatoria de 5 es 9"
    else:
        assert False, "No se encuentra la función e (el quinto ejercicio)"


def test_consignas_del_ejercicio_5():
    if (source := source_ejercicio_5["_source"]) is not None:
        assert "while" in source, "Debe haber un while en la función"
        assert "if" in source, "Debe haber un if en la función"
        assert "continue" in source, "Debe haber un continue en la función"
    else:
        assert False, "No se encuentra la función e (el quinto ejercicio)"


function_ejercicio_6 = _get_next_answer()
source_ejercicio_6 = get_annotations_and_rvalues(function_ejercicio_6)


def test_funcionanmiento_del_ejercicio_6():
    if function_ejercicio_6 is not None:
        assert function_ejercicio_6(1) == "uno", "1 es uno"
        assert function_ejercicio_6(2) == "dos", "2 es dos"
        assert function_ejercicio_6(3) == "tres", "3 es tres"
        assert function_ejercicio_6(4) == "cuatro", "4 es cuatro"
        assert function_ejercicio_6(5) == "cinco", "5 es cinco"
        assert function_ejercicio_6(6) == "no encontrado", "6 no está en el rango"
        assert function_ejercicio_6(0) == "no encontrado", "0 no está en el rango"
    else:
        assert False, "No se encuentra la función f (el sexto ejercicio)"


function_ejercicio_7 = _get_next_answer()
source_ejercicio_7 = get_annotations_and_rvalues(function_ejercicio_7)


def test_funcionanmiento_del_ejercicio_7():
    if function_ejercicio_7 is not None:
        assert function_ejercicio_7(1) == "uno", "1 es uno"
        assert function_ejercicio_7(2) == "dos", "2 es dos"
        assert function_ejercicio_7(3) == "tres", "3 es tres"
        assert function_ejercicio_7(4) == "cuatro", "4 es cuatro"
        assert function_ejercicio_7(5) == "cinco", "5 es cinco"
        assert function_ejercicio_7(6) == "valor no soportado", "6 no está en el rango"
        assert function_ejercicio_7(0) == "valor no soportado", "0 no está en el rango"
    else:
        assert False, "No se encuentra la función g (el séptimo ejercicio)"


def test_consignas_del_ejercicio_7():
    if (source := source_ejercicio_7["_source"]) is not None:
        assert "match" in source, "Debe haber un match en la función"
        assert "case" in source, "Debe haber un case en la función"
        assert (
            "(" in source and ")" in source
        ), "Debe utilizar la función del ejercicio anterior en este ejercicio"
    else:
        assert False, "No se encuentra la función g (el séptimo ejercicio)"
