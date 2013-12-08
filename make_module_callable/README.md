Callable module
===============
It is nice to play with Python magic. This is en example how to pretend a
callable module.

Use this idea with extreme caution as this kind of magic makes mostly more
difficulties than profit.

Example
-------

    my_mdule.py
        import make_module_callable
        def call_function(arg):
            print arg
        make_module_callable(call_function)

    test.py
        import my_module
        my_module('Hello!')
        >>> Hello!
