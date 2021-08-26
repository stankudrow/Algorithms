#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Greatest Common Divisor iterative implementation."""


__author__ = "Stanislav D. Kudriavtsev"


# Complexity: worst case
# Time      : O(log(max(num1, num2)))
# Space     : O(1)


def gcd_iter(num1: int, num2: int) -> int:
    """
    Return the greatest common divisor of two numbers.

    Parameters
    ----------
    num1 : int
    num2 : int

    Raises
    ------
    TypeError
        if num1 or num2 is not integer.

    Returns
    -------
    int

    """
    for num in (num1, num2):
        if not isinstance(num, int):
            raise TypeError(f"{num} is not integer")
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
