#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fibonacci recursive implementation with memoisation."""


__author__ = "Stanislav D. Kudriavtsev"


from numbers import Integral
from typing import Dict


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# a canonical way is to use functools.lru_cache
def fibonacci_rec(nth: int) -> int:
    """
    Return the nth Fibonacci number.

    The first Fibonacci number is zero, the second is one and so forth.

    Notes
    -----
    	the algorithm is recursive with memoisation.

    Parameters
    ----------
    nth : int
        nth Fibonacci number.

    Raises
    ------
    TypeError
        if nth is not None and not integer.
    ValueError
        if nth is integer and is not natural.

    Returns
    -------
    int

    """

    def _fibrec(term: int) -> int:
        """Return the nth Fibonacci number."""
        if term not in cache:
            cache[term] = _fibrec(term - 2) + _fibrec(term - 1)
        return cache[term]

    if not isinstance(nth, Integral):
        raise TypeError(f"{repr(nth)} is not integer")
    if nth < 1:
        raise ValueError(f"{repr(nth)} is not natural")
    cache: Dict[int, int] = {1: 0, 2: 1}
    return _fibrec(nth)
