#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The absolute value of a number algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Union


# Complexity: worst case
# Time      : ~O(1)
# Space     : O(1)


Number = Union[int, float, complex]


def abs_(num: Number) -> Number:
    """
    Return the absolute value of a number.

    Parameters
    ----------
    num : Number

    Returns
    -------
    Number

    """
    if isinstance(num, complex):
        return (num.real ** 2 + num.imag ** 2) ** 0.5
    return num if num >= 0 else (-num)
