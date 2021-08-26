#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Factorial recursive implementation."""


__author__ = "Stanislav D. Kudriavtsev"


from functools import lru_cache


# Complexity: worst case
# Time      : O(n)
# Space     : O(n)


def factorial_rec(num: int) -> int:
    """
    Return the factorial of an integer non-negative number.

    Parameters
    ----------
    num : int

    Raises
    ------
    TypeError
        if num is not integer.
    ValueError
        if num is less than zero.

    Returns
    -------
    int

    """

    @lru_cache
    def _factorial(number: int) -> int:
        """Return the factorial of an integer non-negative number."""
        if number in (0, 1):
            return 1
        return number * _factorial(number - 1)

    if not isinstance(num, int):
        raise TypeError("an integer number is required")
    if num < 0:
        raise ValueError("a non-negative integer number is required")
    return _factorial(num)
