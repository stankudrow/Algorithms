#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recursive jump search algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from math import sqrt
from typing import Any, Optional, Sequence


# Complexity: worst case
# Time      : O(sqrt(n))
# Space     : O(log(n))


def rec_jump_search(seq: Sequence, value: Any) -> Optional[int]:
    """
    Recursive jump search.

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
        the index of value if in sequence or None.

    """
    def get_jump(value: int) -> int:
        """Return a jump value for jump search."""
        return int(sqrt(value))

    size = len(seq)
    jump = get_jump(size)
    end = size
    index = 0
    while index < end:
        elem = seq[index]
        if elem >= value:
            if elem == value:
                return index
            end = index
            index = max(0, index - jump)
            jump = get_jump(jump)
            continue
        index += min(jump, end)
    return None

    def _rjs(seq: Sequence, left: int, right: int) -> Optional[int]:
        """Recursive jump search core function."""
        while index < end:
            elem = seq[index]
            if elem >= value:
                if elem == value:
                    return index
                left = max(0, index - jump)
                right = min(right, right)
                return (seq, )
    _rjs(seq, 0, len(seq))