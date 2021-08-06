#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Python count function implementation."""


__author__ = "Stanislav D. Kudriavtsev"


from numbers import Number
from typing import Iterator


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# Generator[yield_type, send_type, return_type]
# https://stackoverflow.com/questions/38419654/proper-type-annotation-of-python-functions-with-yield
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

# in itertools module `count` is a class
def icount(start: Number = 0, step: Number = 1) -> Iterator[Number]:  # type: ignore
    """
    The Python count function implementation.

    Parameters
    ----------
    start : Number
    step : Number

    Raises
    ------
    TypeError
        if `start` or `count` is not a number.

    Returns
    -------
    Iterator[Number]

    """
    if not (isinstance(start, Number) and isinstance(step, Number)):
        raise TypeError("a number is required")
    val = start
    while True:
        yield val
        val += step  # type: ignore
