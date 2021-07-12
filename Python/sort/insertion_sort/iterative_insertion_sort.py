#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iterative insertion sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(1) -> this implementation requires O(n)


def iter_insertion_sort(seq: Sequence) -> List:
    """
    Iterative insertion sort on a sequence.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    seq: List = list(seq)
    length: int = len(seq)
    for i in range(1, length):
        key = seq[i]
        j: int = i - 1
        while (j >= 0) and (seq[j] > key):
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = key
    return seq
