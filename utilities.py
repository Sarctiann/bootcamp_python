import inspect
import re

# For debugging purposes
if __name__ == "__main__":
    from typing import Literal


def get_annotations_and_rvalues(fn):
    source = inspect.getsource(fn)
    var_tps = {
        k: [t, v]
        for k, t, v in re.findall(r"(\w+) ?: ?([\w\"\[\], ']+[^ ]) ?= ?(.+)\n", source)
    }

    return var_tps


# For debugging purposes
if __name__ == "__main__":

    def test_func():
        a: int = 10
        b: Literal["a", "b"] = "a"
        return a, b

    x = get_annotations_and_rvalues(test_func)
    print(x)
