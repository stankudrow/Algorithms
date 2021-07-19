#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python count function implementation module."""


__author__ = "Stanislav D. Kudriavtsev"


from numbers import Number
from typing import Generator


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# Generator[yield_type, send_type, return_type]
# https://stackoverflow.com/questions/38419654/proper-type-annotation-of-python-functions-with-yield


# in itertools module `count` is a class
def icount(start: Number = 0, step: Number = 1) -> Generator[Number, None, None]:
    """
    Python count function implementation.

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
    Generator[Number, None, None]

    """
    if not (isinstance(start, Number) and isinstance(step, Number)):
        raise TypeError("a number is required")
    val = start
    while True:
        yield val
        val += step
