#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Python itertools repeat class implementation."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Optional


# Complexity: worst case
# Time      : O(n) -> depends on the number of times to repeat
# Space     : O(1)


def irepeat(obj: object, cnt: Optional[int] = None) -> object:
    """
    Yield the object cnt times if specified or infinitely.

    Notes
    -----
    The Python itertools repeat class implementation.

    Parameters
    ----------
    obj : object
        to be repeated.
    cnt : Optional[int], optional
        the number of times counter. The default is None.

    Raises
    ------
    TypeError
        if object is not provided or cnt is not integer.

    References
    ----------
    https://docs.python.org/3/library/itertools.html#itertools.repeat

    Yields
    ------
    object

    """
    def _repeat(obj: object, cnt: Optional[int] = None) -> object:
        """Yield repeat generator."""
        if cnt is None:
            while True:
                yield obj
        else:
            for _ in range(cnt):
                yield obj

    if not (cnt is None or isinstance(cnt, int)):
        raise TypeError(f'cnt = {cnt} is not integer')
    return _repeat(obj, cnt)
