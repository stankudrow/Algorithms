#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iterative binary search algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Optional, Sequence


# Complexity: worst case
# Time      : O(log_2(n))
# Space     : O(1)


def binary_search_iter(seq: Sequence, value: Any) -> Optional[int]:
    """
    Iterative binary search.

    Notes
    -----
    Binary search works only on sorted sequences.

    Parameters
    ----------
    seq : Sequence
        where to search.
    value : Any
        what to search.

    Returns
    -------
    Optional[int]
        the index of value if in sequence or None.

    """
    # sequence borders
    left: int = 0
    right: int = len(seq) - 1
    while left <= right:
        # middle element and its index
        midi = (left + right) // 2
        mide = seq[midi]
        if mide == value:
            return midi
        if mide < value:
            left = midi + 1
        else:
            right = midi - 1
    return None
