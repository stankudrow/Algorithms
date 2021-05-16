#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python enumerate implementation module."""


from typing import Any, Generator, Iterable, Tuple


# Complexity: best avg  worst
# Time:       Ω(n) Ө(n) O(n)
# Space:      Ω(1) Ө(1) O(1)


# Generator[yield_type, send_type, return_type]
def ienumerate(
    iterable: Iterable, start: int = 0
) -> Generator[Tuple[int, Any], None, None]:
    """Implementation of Python enumerate function

    Parameters
    ----------
    iterable : Iterable
    start : int, default 0

    Raises
    ------
    TypeError
        if start is not integer

    References
    ----------
    https://docs.python.org/3/library/functions.html#enumerate

    Yields
    ------
    Tuple[int, Any]
        index, element
    """
    if not isinstance(start, int):
        raise TypeError(f"{type(start).__name__} is not interpretable as integer")
    count = start
    for item in iterable:
        yield (count, item)
        count += 1
