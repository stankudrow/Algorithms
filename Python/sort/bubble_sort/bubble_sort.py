#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bubble sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n^2)
# Space:    : O(1)   -> this implementation requires O(n)


def bubble_sort(seq: Sequence) -> List:
    """
    Bubble sort on a sequence.

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
    swap: bool = True
    for index in range(leng):
        swap = False
        for jndex in range(leng - index - 1):
            currel, nextel = seq[jndex], seq[jndex + 1]
            if currel > nextel:
                seq[jndex], seq[jndex + 1] = nextel, currel
                swap = True
        if not swap:
            break
    return seq
