#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The iterative comb sort algorithm.

The comb sort algorithm was:
    * designed by Włodzimierz Dobosiewicz and Artur Borowy in 1980;
    * rediscovered and named by Stephen Lacey and Richard Box in 1991.

Notes
-----
    The comb sort is a generalisation of the bubble sort (1-gap) algorithm.

References
----------
    * https://en.wikipedia.org/wiki/Comb_sort
    * https://www.geeksforgeeks.org/comb-sort/
    * https://www.tutorialspoint.com/Comb-Sort
"""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2) (simple case of gap choice)
# Space:    : O(1) -> this implementation requires O(n)


def comb_sort_iter(seq: Sequence) -> List:
    """
    Sort a sequence with the iterative comb sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    lst = list(seq)  # copy -> purity sake
    size = len(lst)
    gap = size
    shrink = 1.3
    tosort = True
    while (gap != 1) or tosort:
        gap = max(int(gap / shrink), 1)
        tosort = False
        for i in range(size - gap):
            j = i + gap
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                tosort = True
    return lst
