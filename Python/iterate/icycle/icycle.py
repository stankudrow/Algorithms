#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python cycle function implementation module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Generator, Iterable


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# Generator[yield_type, send_type, return_type]
# https://stackoverflow.com/questions/38419654/proper-type-annotation-of-python-functions-with-yield


# in itertools module `cycle` is a class
def icycle(iterable: Iterable) -> Generator[Any, None, None]:
    """
    Python cycle function implementation.

    Parameters
    ----------
    iterable: Iterable

    Raises
    ------
    TypeError
        if a non-iterable is passed

    Returns
    -------
    Generator[Any, None, None]

    """
    while True:
        for item in iterable:
            yield item
