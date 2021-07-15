#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python enumerate function implementation module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Generator, Iterable, Tuple


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# Generator[yield_type, send_type, return_type]
# https://stackoverflow.com/questions/38419654/proper-type-annotation-of-python-functions-with-yield


def ienumerate(
    iterable: Iterable, start: int = 0
) -> Generator[Tuple[int, Any], None, None]:
    """
    Implementation of the Python enumerate function.

    Parameters
    ----------
    iterable : Iterable
        sequence to enumerate.
    start : int, optional
        the start index of enumeration. The default is 0.

    Raises
    ------
    TypeError
        if `iterable` is not an iterable object or `start` is not an integer.

    References
    ----------
    https://docs.python.org/3/library/functions.html#enumerate

    Yields
    ------
    Generator[Tuple[int, Any], None, None]

    """
    iterable = iter(iterable)
    if not isinstance(start, int):
        tname = type(start).__name__
        raise TypeError(f"{tname} object cannot be interpreted as an integer")
    count = start
    for item in iterable:
        yield (count, item)
        count += 1
