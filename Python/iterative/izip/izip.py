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


def izip(
    *iterables: Tuple[Iterable, ...], longest: bool = False
) -> Iterable[Tuple[Any, ...]]:
    """
    Yield the tuple with sequentially chosen elements from iterables.

    Parameters
    ----------
    *iterables : Tuple[Iterable, ...]
        to zip.
    longest : bool, optional
        zip according to the longest iterable. The default is False.

    References
    ----------
    https://docs.python.org/3/library/functions.html#zip

    Yields
    ------
    Tuple[Any, ...]

    """
    sentinel = object()  # allows None as a value in iterables
    iters = [iter(iter_) for iter_ in iterables]
    iters_len = len(iterables)
    while True:
        res = []
        longest_count = 0
        for iter_ in iters:
            elem = next(iter_, sentinel)
            if elem is sentinel:
                if longest:
                    elem = None
                    longest_count += 1
                else:
                    return  # the smallest iterator is exhausted
            res.append(elem)
            if longest and longest_count == iters_len:
                return
        yield tuple(res)
