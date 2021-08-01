#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iterative shell sort algorithm module.

The Shell sort algorithm was invented by Donald Shell.

This algorithm is known as:
    * diminishing increment sort
    * n-gap insertion sort

Shell sort is a generalisation of insertion sort (1-gap) algorithm.
"""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n**2) (simple case of gap choice)
# Space:    : O(1) -> this implementation requires O(n)


def iter_shell_sort(seq: Sequence) -> List:
    """
    Iterative shell sort on a sequence.

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
    while gap > 0:
        for i in range(0, size):
            for j in range(i + gap, size, gap):
                if seq[i] > seq[j]:
                    seq[i], seq[j] = seq[j], seq[i]
        gap //= 2
    return seq
