#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Python cycle function implementation."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Iterable


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# Generator[yield_type, send_type, return_type]
# https://stackoverflow.com/questions/38419654/proper-type-annotation-of-python-functions-with-yield
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html


# in itertools module `cycle` is a class
def icycle(iterable: Iterable[Any]) -> Iterable[Any]:
    """
    Yield elements from the iterable with indefinite repetition.

    Notes
    -----
    The Python cycle function implementation.

    Parameters
    ----------
    iterable: Iterable[Any]

    Raises
    ------
    TypeError
        if a non-iterable is passed.

    References
    ----------
    https://docs.python.org/3/library/itertools.html#itertools.cycle

    Yields
    ------
    Iterable[Any]

    """
    while True:
        for item in iterable:
            yield item
