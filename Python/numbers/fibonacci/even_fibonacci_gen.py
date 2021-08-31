#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fibonacci even numbers generator."""


__author__ = "Stanislav D. Kudriavtsev"


from numbers import Integral
from typing import Iterator, Optional


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


def even_fibonacci_gen(nth: Optional[int] = None) -> Iterator[int]:
    """
    Return the Fibonacci even numbers generator.

    Examples
    --------
    even_fibonacci_gen(-1) -> ValueError: -1 is not a positive integer number
    even_fibonacci_gen(0) -> ValueError: 0 is not a positive integer number
    even_fibonacci_gen(1.2) -> TypeError: 1.2 is not an integer number
    list(even_fibonacci_gen(1)) -> [0]
    list(even_fibonacci_gen(4)) -> [0, 2, 8, 34]
    even_fibonacci_gen() -> upperly unbound generator

    Parameters
    ----------
    nth : Optional[int], optional
        up to nth Fibonacci number if provided. The default is None.

    Raises
    ------
    TypeError
        if nth is not None and not integer.
    ValueError
        if nth is integer and is less than 1.

    Yields
    ------
    Iterator[int]

    """

    def _evenfibgen(_nth: Optional[int] = None) -> Iterator[int]:
        """Yield the Fibonacci even numbers generator."""
        yield 0
        fnum1, fnum2 = 1, 2
        cnt = 1
        if _nth is None:
            _nth = -1
        while cnt != _nth:
            yield fnum2
            fnum1, fnum2 = fnum1 + 2 * fnum2, 2 * fnum1 + 3 * fnum2
            cnt += 1

    if nth is not None:
        if not isinstance(nth, Integral):
            raise TypeError(f"{repr(nth)} is not an integer number")
        if nth < 1:
            raise ValueError(f"{repr(nth)} is not a positive integer number")
    return _evenfibgen(nth)
