#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The iterative shell sort algorithm.

The Shell sort algorithm was invented by Donald Shell in 1959.

Notes
-----
    The shell sort is a generalisation of the insertion sort (1-gap) algorithm.

References
----------
    * https://en.wikipedia.org/wiki/Shellsort
    * https://www.geeksforgeeks.org/shellsort/
    * https://www.tutorialspoint.com/Shell-Sort

"""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : depends on the gap -> O(n**2) for this implementation
# Space:    : O(1) -> this implementation requires O(n)


def iter_shell_sort(seq: Sequence) -> List:
    """
    Sort a sequence with the Shell sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    seq = list(seq)  # copy -> purity sake
    size = len(seq)
    gap = size // 2
    while gap:
        for i in range(size):
            for j in range(i + gap, size, gap):
                if seq[i] > seq[j]:
                    seq[i], seq[j] = seq[j], seq[i]
        gap //= 2
    return seq
