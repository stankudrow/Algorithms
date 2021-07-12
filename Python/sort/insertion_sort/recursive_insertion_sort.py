#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recursive insertion sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(n)


def rec_insertion_sort(seq: Sequence) -> List:
    """
    Recursive insertion sort on a sequence.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """

    def rinsertsort(seq: List, length: int):
        """Recursive insertion sort algorithm."""
        if length in (0, 1):
            return
        rinsertsort(seq, length - 1)
        key = seq[length - 1]
        j = length - 2
        while (j >= 0) and (seq[j] > key):
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = key

    seq: List = list(seq)
    rinsertsort(seq, len(seq))
    return seq
