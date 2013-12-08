import sys
import make_module_callable

def test(arg, kwarg='abc'):
    return arg, kwarg

make_module_callable(test)

