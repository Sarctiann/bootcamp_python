from ...utilities import get_annotations_and_rvalues
from .clase3 import ejercicios_de_la_clase_3


ordered_answers = ejercicios_de_la_clase_3()
collected_types = get_annotations_and_rvalues(ejercicios_de_la_clase_3)


def _get_next_answer():
    try:
        if ordered_answers is not None:
            return next(ordered_answers)
    except StopIteration:
        print("No more answers")
