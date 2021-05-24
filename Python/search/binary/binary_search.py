#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Binary search algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Optional, Sequence


# Complexity: worst case
# Time      : O( log_2(n) )
# Space     : O(1) for iterative and O( log_2(n) ) for recursive version.


def ibinary_search(seq: Sequence, value: Any) -> Optional[int]:
    """
    Iterative binary search.

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


def rbinary_search(seq: Sequence, value: Any) -> Optional[int]:
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
        the index of value if in sequence or None.

    """

    def rbins(seq: Sequence, val: Any, low: int, high: int) -> Optional[int]:
        """
        Recursive implementation itself

        Parameters
        ----------
        seq : Sequence
            where to search
        val : Any
            what to search.
        low : int
            left border index.
        high : int
            right border index.

        Returns
        -------
        Optional[int]
            the index of value if in sequence or None.

        """
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
