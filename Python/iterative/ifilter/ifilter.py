#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Python builtin filter class implementation."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Any, Callable, Iterable


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# Generator[yield_type, send_type, return_type]
# https://stackoverflow.com/questions/38419654/proper-type-annotation-of-python-functions-with-yield
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html


def ifilter(
    function: Callable, iterable: Iterable, false: bool = False
) -> Iterable[Any]:
    """
    Filter out the elements from iterable in accordance to function.

    Notes
    -----
    The Python builtin filter class implementation.
    The `false` key makes ifilter to work like itertools.filterfalse class.

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
        if `function` is not callable or `iterable` is not iterable.

    References
    ----------
    https://docs.python.org/3/library/functions.html#filter
    https://docs.python.org/3/library/itertools.html#itertools.filterfalse

    Yields
    ------
    Iterable[Any]

    """

    def _falsify(func: Callable):
        """Negate the result of foo function."""
        def _not(arg: Any):
            """Return the negated result of foo function."""
            return not func(arg)
        return _not

    if function is None:
        function = bool
    if false:
        func = _falsify(function)  # pylint is satisfied
    else:
        func = function
    return (item for item in iterable if func(item))
