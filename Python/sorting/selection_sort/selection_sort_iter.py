#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The iterative selection sort algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(1) -> this implementation requires O(n)


def selection_sort_iter(seq: Sequence) -> List:
    """
    Sort a sequence with the iterative selection sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    lst: List = list(seq)
    size: int = len(seq)
    for i in range(size):
        key: int = i
        for j in range(i + 1, size):
            if lst[j] < lst[key]:
                key = j
        lst[i], lst[key] = lst[key], lst[i]
    return lst
