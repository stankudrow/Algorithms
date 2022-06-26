#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The iterative shaker/cocktail sort algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(1) -> this implementation requires O(n)


def shaker_sort_iter(seq: Sequence) -> List:
    """
    Sort a sequence with the iterative shaker/cocktail sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List
    """
    lst: List = list(seq)
    left = 0
    right = len(lst) - 1
    while True:
        swapped = False
        for i in range(left, right - left):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        if not swapped:
            break
        left += 1
        swapped = False
        for i in range(right - left, left - 1, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                swapped = True
        if not swapped:
            break
    return lst
