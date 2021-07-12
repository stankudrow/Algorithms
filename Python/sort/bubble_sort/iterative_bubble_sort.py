#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iterative bubble sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(1) -> this implementation requires O(n)


def iter_bubble_sort(seq: Sequence) -> List:
    """
    Iterative bubble sort on a sequence.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    seq: List = list(seq)
    length: int = len(seq)
    for i in range(length):
        swapped: bool = False
        for j in range(length - i - 1):
            cur, nxt = seq[j], seq[j + 1]
            if cur > nxt:
                seq[j], seq[j + 1] = nxt, cur
                swapped = True
        if not swapped:
            break
    return seq
