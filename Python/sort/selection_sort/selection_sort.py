#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Selection sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n^2)
# Space:    : O(1)   -> this implementation requires O(n)


def selection_sort(seq: Sequence) -> List:
    """
    Selection sort on a sequence.

    The function casts the incoming sequence to the list for purity sake.

    Parameters
    ----------
    seq : Sequence
        sequence to sort.

    Returns
    -------
    List
        the sorted sequence.

    """
    seq = list(seq)  # ensure purity, adds O(n) at most
    leng = len(seq)
    for index in range(leng):
        icurr = index
        for jndex in range(index + 1, leng):
            if seq[jndex] < seq[icurr]:
                icurr = jndex
        seq[index], seq[icurr] = seq[icurr], seq[index]
    return seq
