#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python zip function implementation module."""


from typing import Any, Generator, Iterable, Tuple


# Complexity
# Time      : O(n)
# Space     : O(m)


# Generator[yield_type, send_type, return_type]
def izip(*iterables: Iterable) -> Generator[Tuple[Any, ...], None, None]:
    """
    Implementation of the Python zip function.

    Parameters
    ----------
    *iterable : Tuple[Iterable, ...]
        iterable objects to zip.

    Returns
    -------
    None
        if the smallest iterable is exhausted

    Yields
    ------
    Tuple[Any, ...]
        i-th element from each iterable.

    """
    # make from iterables iterators
    iters = [iter(iter_) for iter_ in iterables]
    while iters:  # until exhausted
        res = []
        for iter_ in iters:
            elem = next(iter_, None)
            if elem is None:
                return  # until the smallest iterator is exhausted
            res.append(elem)
        yield tuple(res)
