#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python zip function implementation module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Generator, Iterable, Tuple


# Complexity: worst case
# Time      : O(n)
# Space     : O(m)


# Generator[yield_type, send_type, return_type]
def izip(*iterables: Iterable) -> Generator[Tuple[Any, ...], None, None]:
    """
    Python zip function implementation.

    Parameters
    ----------
    *iterable : Tuple[Iterable, ...]

    Yields
    ------
    Tuple[Any, ...]

    """
    sentinel = object()  # allows None as a value in iterables
    iters = [iter(iter_) for iter_ in iterables]
    while iters:  # until exhausted if all are of equal length
        res = []
        for iter_ in iters:
            elem = next(iter_, sentinel)  # sentinel instead None allows None values
            if elem is sentinel:
                return  # until the smallest iterator is exhausted
            res.append(elem)
        yield tuple(res)


# It turned out to be as same as here:
# https://docs.python.org/3/library/functions.html#zip
