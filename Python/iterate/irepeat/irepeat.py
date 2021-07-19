#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python repeat function implementation module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Generator, Optional


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# Generator[yield_type, send_type, return_type]
# https://stackoverflow.com/questions/38419654/proper-type-annotation-of-python-functions-with-yield


# in itertools module `repeat` is a class
def irepeat(obj: object, times: Optional = None) -> Generator[object, None, None]:
    """
    Python repeat function implementation.

    Parameters
    ----------
    iterable: Iterable

    Raises
    ------
    TypeError
        if `times` is not None and not an integer.

    Returns
    -------
    Generator[Number, None, None]

    """
    if times is None:
        while True:
            yield obj
    else:
        for i in range(times):
            yield obj
