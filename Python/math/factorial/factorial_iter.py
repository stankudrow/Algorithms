#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Factorial iterative implementation."""


__author__ = "Stanislav D. Kudriavtsev"


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


def factorial_iter(num: int) -> int:
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
    if not isinstance(num, int):
        raise TypeError("an integer number is required")
    if num < 0:
        raise ValueError("a non-negative integer number is required")
    product = 1
    for factor in range(2, num + 1):
        product *= factor
    return product
