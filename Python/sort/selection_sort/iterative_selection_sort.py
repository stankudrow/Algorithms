#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iterative selection sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2)
# Space:    : O(1) -> this implementation requires O(n)


def iter_selection_sort(seq: Sequence) -> List:
    """
    Iterative selection sort on a sequence.

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
        key: int = i
        for j in range(i + 1, length):
            if seq[j] < seq[key]:
                key = j
        seq[i], seq[key] = seq[key], seq[i]
    return seq
