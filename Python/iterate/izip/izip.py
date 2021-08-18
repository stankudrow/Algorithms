#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Python builtin zip class implementation."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Iterable, Tuple


# Complexity: worst case
# Time      : O(n)
# Space     : O(m)


# Generator[yield_type, send_type, return_type]
# https://stackoverflow.com/questions/38419654/proper-type-annotation-of-python-functions-with-yield
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html


def izip(*iterables: Iterable) -> Iterable[Tuple[Any, ...]]:
    """
    Yield the tuple with sequentially chosen elements from iterables.

    Notes
    -----
    The Python builtin zip class implementation.

    Parameters
    ----------
    *iterable : Tuple[Iterable, ...]

    References
    ----------
    https://docs.python.org/3/library/functions.html#zip

    Yields
    ------
    Iterable[Tuple[Any, ...]]

    """
    sentinel = object()  # allows None as a value in iterables
    iters = [iter(iter_) for iter_ in iterables]
    while iters:  # until exhausted if all are of equal length
        res = []
        for iter_ in iters:
            elem = next(iter_, sentinel)  # object enable None's processing
            if elem is sentinel:
                return  # until the smallest iterator is exhausted
            res.append(elem)
        yield tuple(res)
