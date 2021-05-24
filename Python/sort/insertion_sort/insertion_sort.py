#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insertion sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n^2)
# Space:    : O(1)   -> this implementation requires O(n)


def insertion_sort(seq: Sequence) -> List:
    """
    Insertion sort on a sequence.

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
    seq = list(seq)  # ensure purity, adds O(n) of space complexity
    leng: int = len(seq)
    for index in range(1, leng):
        ielem: int = seq[index]
        jndex: int = index - 1
        while (jndex >= 0) and (seq[jndex] > ielem):
            seq[jndex + 1] = seq[jndex]
            jndex -= 1
        seq[jndex + 1] = ielem
    return seq
