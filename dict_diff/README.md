Dict difference
===============

A simple (and efficient) way of calculating differences between two dict objects is to convert them to sets.

I you are interested only in changes:

    set_before = set(dict_before.items())
    set_after = set(dict_after.items())

    print 'Original items:'
    set_before - set_after

    print 'New items:'
    set_after - set_before

[dict_diff.py](dict_diff.py) shows more detailed changes presentation.

Limitations: Dictionaries can contain only immutable values (but many python
types can bee easily freezed to immutable representation).
