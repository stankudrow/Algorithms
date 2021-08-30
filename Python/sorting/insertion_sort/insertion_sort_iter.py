#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The iterative insertion sort algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(1) -> this implementation requires O(n)


def insertion_sort_iter(seq: Sequence) -> List:
    """
    Sort a sequence with the iterative insertion sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    lst: List = list(seq)
    size: int = len(seq)
    for i in range(1, size):
        key = lst[i]
        j: int = i - 1
        while (j >= 0) and (lst[j] > key):
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
