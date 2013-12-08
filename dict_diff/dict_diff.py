#!/usr/bin/env python


def dict_diff(before, after):
    set_a = set(before.items())
    set_b = set(after.items())

    return {
        'removed   ': {k:v for k,v in set_a - set_b if k not in after},
        'added     ': {k:v for k,v in set_b - set_a if k not in before},
        'changed   ': {k:(v, after[k]) for k,v in set_a - set_b if k in after and k in before},
        'unchanged ': dict(set_a.intersection(set_b)),
    }


if __name__ == '__main__':
    before = {
        'a': 1,
        'b': 2,
        'x': 5,
    }

    after = {
        'b': 3,
        'x': 5,
        'y': 6,
    }

    from pprint import pprint
    print 'Before:'
    pprint(before)
    print '\nAfter:'
    pprint(after)
    print '\nChanges:'
    pprint(dict_diff(before, after))
