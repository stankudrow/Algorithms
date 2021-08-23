#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fibonacci generator."""


__author__ = "Stanislav D. Kudriavtsev"


from numbers import Integral
from typing import Iterator, Optional


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


def fib_gen(nth: Optional[int] = None) -> Iterator[int]:
    """
    Return the Fibonacci generator.

    The first Fibonacci number is zero, the second is one and so forth.

    Parameters
    ----------
    nth : Optional[int], optional
        nth Fibonacci number. The default is None.

    Raises
    ------
    TypeError
        if nth is not None and not integer.
    ValueError
        if nth is integer and is not natural.

    Yields
    ------
    Iterator[int]

    """

    def _fibgen(num: Optional[int] = None) -> Iterator[int]:
        """Yield the Fibonacci generator."""
        current: int = 0
        next_: int = 1
        counter: int = 1
        if num is None:
            num = -1
        while counter <= num:
            yield current
            current, next_ = next_, current + next_
            counter += 1

    if nth is not None:
        if not isinstance(nth, Integral):
            raise TypeError(f"{repr(nth)} is not integer")
        if nth < 1:
            raise ValueError(f"{repr(nth)} is not natural")
    return _fibgen(nth)
