#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The merge sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence

from merge import merge


# Complexity: worst case
# Time      : O(n*log_2(n))
# Space     : O(n)


def rec_merge_sort(seq: Sequence) -> List:
    """
    Sort a sequence with the recursive merge sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    length: int = len(seq)
    if length <= 1:
        return list(seq)
    half: int = length // 2
    left: Sequence = seq[:half]
    right: Sequence = seq[half:]
    return merge(rec_merge_sort(left), rec_merge_sort(right))
