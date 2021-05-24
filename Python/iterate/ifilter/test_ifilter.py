#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ifilter test module."""


__author__ = "Stanislav D. Kudriavtsev"


from itertools import filterfalse
from typing import Callable, List

from pytest import mark

from ifilter import ifilter


def test_ifilter_empty_iterable():
    """Empty iterable."""
    func: Callable = lambda arg: arg == 0
    assert list(ifilter(func, [])) == list(filter(func, []))
    assert list(ifilter(func, [], True)) == list(filterfalse(func, []))


def test_ifilter_empty_function():
    """Empty function."""
    func = None
    seq: List = [-1, 0, 1]
    assert list(ifilter(func, seq)) == list(filter(func, seq))
    assert list(ifilter(func, seq, True)) == list(filterfalse(func, seq))


@mark.parametrize(
    "function, iterable",
    [(lambda arg: arg < 0, range(-5, 6)), (lambda arg: arg.isupper(), "AbcDef")],
)
def test_ifilter_iterables(function, iterable):
    """Filter several test cases."""
    assert list(ifilter(function, iterable)) == list(filter(function, iterable))
    assert list(ifilter(function, iterable, True)) == list(
        filterfalse(function, iterable)
    )
