#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recursive selection sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(n)


def rec_selection_sort(seq: Sequence) -> List:
    """
    Recursive selection sort on a sequence.

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

    seq: List = list(seq)
    rselectsort(seq, len(seq))
    return seq
