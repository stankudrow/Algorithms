#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The recursive selection sort algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(n)


def selection_sort_rec(seq: Sequence) -> List:
    """
    Sort a sequence with the recursive selection sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """

    def rselectsort(seq: List, length: int):
        """Recursive selection sort algorithm."""
        if length in (0, 1):
            return
        last: int = length - 1
        key: int = last
        for j in range(last - 1, -1, -1):
            if seq[j] > seq[key]:
                key = j
        seq[last], seq[key] = seq[key], seq[last]
        rselectsort(seq, last)

    lst: List = list(seq)
    rselectsort(lst, len(lst))
    return lst
