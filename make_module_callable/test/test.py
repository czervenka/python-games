#!/usr/bin/env python
import sys
sys.path.insert(0, '..')

import callable_module


assert callable_module('a', kwarg='b') == callable_module.test('a', kwarg='b'), "Calling module runs it's test method."
callable_module.x = 1
assert callable_module.x == 1, "Callable module has __setattr__."
