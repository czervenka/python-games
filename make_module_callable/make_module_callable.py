def make_callable(callback):
    # imports are here because we destroy the original module
    import sys
    import types
    from functools import update_wrapper
    # get the module
    module_name = callback.__module__
    if module_name == __name__:  # special case when making callable self
        properties = globals()
    else:
        module = sys.modules[module_name]
        properties = module.__dict__

    # keep functions static
    properties = {k:(staticmethod(v) if callable(v) else v) for k,v in properties.items()}
    # imitate __call__property
    properties['__call__'] = staticmethod(callback)
    # create new module-like object ...
    new_module = type('module', (types.ModuleType,), properties)
    # ... and replace the original modul
    sys.modules[module_name] = new_module(module_name)

# whould be shame if this module would not be callable too ;)
make_callable(make_callable)
