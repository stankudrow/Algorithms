#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python filter function implementation module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Callable, Generator, Iterable


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# Generator[yield_type, send_type, return_type]
def ifilter(
    function: Callable, iterable: Iterable, false: bool = False
) -> Generator[Any, None, None]:
    """
    Implementation of the Python filter function.

    Notes
    -----
    false key does not make ifilter to work like itertools.filterfalse.

    Parameters
    ----------
    function : Callable
        function to apply on an item of iterable.
    iterable : Iterable
    false : bool, optional
        filter on the false condition. The default is False.

    Raises
    ------
    TypeError
        if function is not callable or iterable is not iterable.

    Returns
    -------
    Generator[Any, None, None]
        filtered items from iterable.

    """
    # import pdb; pdb.set_trace()
    if function is None:
        function = bool
    if false:
        func = lambda arg: not function(arg)
    else:
        func = function
    return (item for item in iterable if func(item))
