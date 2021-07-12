#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recursive bubble sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(n)


def rec_bubble_sort(seq: Sequence) -> List:
    """
    Recursive bubble sort on a sequence.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """

    def rbubblesort(seq: List, length: int):
        """Recursive bubble sort algorithm."""
        if length in (0, 1):
            return
        for j in range(length - 1):
            cur, nxt = seq[j], seq[j + 1]
            if cur > nxt:
                seq[j], seq[j + 1] = nxt, cur
        rbubblesort(seq, length - 1)

    seq: List = list(seq)
    rbubblesort(seq, len(seq))
    return seq
