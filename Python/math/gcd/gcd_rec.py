#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Greatest Common Divisor recursive implementation."""


__author__ = "Stanislav D. Kudriavtsev"


# Complexity: worst case
# Time      : O(log(max(num1, num2)))
# Space     : O(log(max(num1, num2)))


def gcd_rec(num1: int, num2: int) -> int:
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

    def _gcd(dividend: int, divisor: int) -> int:
        """Return the gcd of two numbers."""
        if divisor:
            return _gcd(divisor, dividend % divisor)
        return dividend

    for num in (num1, num2):
        if not isinstance(num, int):
            raise TypeError(f"{num} is not integer")
    return _gcd(num1, num2)
