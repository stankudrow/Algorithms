#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Python itertools chain class implementation."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Iterator, Tuple


# Complexity: worst case
# Time      : O(n) - total number of items
# Space     : O(1)


# Generator[yield_type, send_type, return_type]
# https://stackoverflow.com/questions/38419654/proper-type-annotation-of-python-functions-with-yield
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html


def ichain(*iterables: Tuple[Iterator, ...]) -> Iterator[Any]:
    """
    Yield elements of sequential iterators.

    Parameters
    ----------
    *iterables : TYPE

    References
    ----------
    https://docs.python.org/3/library/itertools.html#itertools.chain

    Yields
    ------
    Iterator[Any]

    """
    # chain.from_iterable may be redundant
    for iterable in iterables:
        for item in iterable:
            yield item
