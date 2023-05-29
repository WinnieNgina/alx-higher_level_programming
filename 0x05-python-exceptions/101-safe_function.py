#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        results = fct(*args)
    except Exception as e:
        sys.stderr.write(("Exception: {}\n").format(e))
        results = None
    return results

