#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The iterative bubble sort algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(1) -> this implementation requires O(n)


def iter_bubble_sort(seq: Sequence) -> List:
    """
    Sort a sequence with the iterative bubble sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    lst: List = list(seq)
    length: int = len(lst)
    for i in range(length):
        swapped: bool = False
        for j in range(length - i - 1):
            cur, nxt = lst[j], lst[j + 1]
            if cur > nxt:
                lst[j], lst[j + 1] = nxt, cur
                swapped = True
        if not swapped:
            break
    return lst
