#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The merge sort algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence

from merge import merge


# Complexity: worst case
# Time      : O(n*log_2(n))
# Space     : O(n)


# The merge function here is meant to be pure.
# A less costly approach is to make assignments in place.

# This link provided some insights:
# https://www.techiedelight.com/iterative-merge-sort-algorithm-bottom-up/

def iter_merge_sort(seq: Sequence) -> List:
    """
    Sort a sequence with the iterative insertion sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    length: int = len(seq)
    size: int = 1
    mseq: List = list(seq)  # to be merged
    while size < length:
        for lbound in range(0, length, 2 * size):
            start: int = lbound
            mid: int = start + size
            end: int = min(start + 2*size, length)
            mseq[start:end] = merge(mseq[start:mid], mseq[mid:end])
        size *= 2
    return mseq
