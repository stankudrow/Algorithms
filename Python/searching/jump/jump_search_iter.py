#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iterative jump search algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from math import sqrt
from typing import Any, Optional, Sequence


# Complexity: worst case
# Time      : O(sqrt(n))
# Space     : O(1)


def jump_search_iter(seq: Sequence, value: Any) -> Optional[int]:
    """
    Iterative jump search algorithm.

    Notes
    -----
    Jump search works only on sorted sequences.

    Parameters
    ----------
    seq : Sequence
        where to search.
    value : Any
        what to search.

    Returns
    -------
    Optional[int]
        the index of value if it is in sequence, otherwise None.

    """

    def get_jump(value: int) -> int:
        """Return a jump value for jump search."""
        return int(sqrt(value))

    length = len(seq)
    jump = get_jump(length)
    left, right = 0, length
    while left < right:
        elem = seq[left]
        if elem == value:
            return left
        if elem > value:
            right = min(left, right)
            left = max(0, left - jump) + 1
            jump = get_jump(jump)
            continue
        if (left + jump) >= right:
            jump = get_jump(jump)
            left += jump
            continue
        left += jump
    return None
