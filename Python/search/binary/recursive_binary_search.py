#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recursive binary search algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Optional, Sequence


# Complexity: worst case
# Time      : O(log_2(n))
# Space     : O(log_2(n))


def recursive_binary_search(seq: Sequence, value: Any) -> Optional[int]:
    """
    Recursive binary search.

    Notes
    -----
    Binary search works only on sorted sequences

    Parameters
    ----------
    seq : Sequence
        where to search.
    value : Any
        what to search.

    Returns
    -------
    Optional[int]
        the index of value if it is in sequence or None.

    """

    def rbins(seq: Sequence, val: Any, low: int, high: int) -> Optional[int]:
        """Core function of recursive binary search."""
        while low <= high:
            # middle element and its index
            midi = (low + high) // 2
            mide = seq[midi]
            if mide == val:
                return midi
            if mide < val:
                return rbins(seq, val, midi + 1, high)
            return rbins(seq, val, low, midi - 1)
        return None

    return rbins(seq, value, 0, len(seq) - 1)
