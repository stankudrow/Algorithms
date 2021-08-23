#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iterative jump search algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from math import sqrt
from typing import Any, Optional, Sequence


# Complexity: worst case
# Time      : O(sqrt(n))
# Space     : O(1)


def iter_jump_search(seq: Sequence, value: Any) -> Optional[int]:
    """
    Iterative jump search.

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
            index = max(-1, index - jump) + 1
            jump = get_jump(jump)
            continue
        if jump > 1:
            index = min(index + jump, end - 1)
        else:
            index += jump
    return None
