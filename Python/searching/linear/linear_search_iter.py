#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Iterative linear search algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Optional, Sequence


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


def linear_search_iter(seq: Sequence, value: Any) -> Optional[int]:
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
