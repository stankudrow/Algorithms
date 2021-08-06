#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The ifilter test module."""


__author__ = "Stanislav D. Kudriavtsev"


from itertools import filterfalse

from pytest import fixture

from ifilter import ifilter


# pylint: disable=redefined-outer-name


@fixture()
def funciters():
    """Functions and iterables for ifilter."""
    return [
        (lambda x: x ** 2, range(10, 11)),
        (lambda c: c.isalpha(), "The answer is 42 anyway."),
    ]


def test_no_function_empty_iterable():
    """Empty function and iterable."""
    entry = (None, [])
    assert list(ifilter(*entry)) == list(filter(*entry))


def test_no_function_nonempty_iterable():
    """Empty function, nonempty iterable."""
    entry = (None, [-1, 0, 1])
    assert list(ifilter(*entry)) == list(filter(*entry))


def test_filter_iterables(funciters):
    """Filter on true (default) condition."""
    for func, iter_ in funciters:
        assert list(ifilter(func, iter_)) == list(filter(func, iter_))


def test_filterfalse_iterables(funciters):
    """Filter on false condition."""
    for func, iter_ in funciters:
        myfilter = ifilter(func, iter_, True)
        stdfilter = filterfalse(func, iter_)
        assert list(myfilter) == list(stdfilter)
