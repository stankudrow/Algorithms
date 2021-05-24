#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Linear search algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Optional, Sequence


# Complexity: worst case
# Time      : O(n)
# Space     : O(1) for iterative and O(n) for recursive version.


def ilinear_search(seq: Sequence, value: Any) -> Optional[int]:
    """
    Iterative linear search.

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
    for index, element in enumerate(seq):
        if element == value:
            return index
    return None


def rlinear_search(seq: Sequence, value: Any) -> Optional[int]:
    """
    Recursive linear search.

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
    if seq:
        if seq[0] == value:
            return 0
        index = rlinear_search(seq[1:], value)
        if index is not None:
            return index + 1
    return None
