#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recursive linear search algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Optional, Sequence


# Complexity: worst case
# Time      : O(n)
# Space     : O(n)


def linear_search_rec(seq: Sequence, value: Any) -> Optional[int]:
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
        index = linear_search_rec(seq[1:], value)
        if index is not None:
            return index + 1
    return None
