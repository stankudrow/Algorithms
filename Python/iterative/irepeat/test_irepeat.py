#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The irepeat test module."""


__author__ = "Stanislav D. Kudriavtsev"


from itertools import repeat

from pytest import mark, raises

from irepeat import irepeat


# pylint: disable=redefined-outer-name


def test_init():
    """Test initialisation."""
    with raises(TypeError):
        irepeat()
    assert irepeat(None)
    assert irepeat(object, None)
    assert irepeat(object, 5)
    with raises(TypeError):
        irepeat(object, 5.5)


@mark.parametrize(
    "obj, cnt",
    [(1, -1), (1, 0), (1, 1), (1, 4)]
)
def test_finite_repetitions(obj, cnt):
    """Test finte repetitions."""
    assert list(irepeat(obj, cnt)) == list(repeat(obj, cnt))


@mark.parametrize(
    "obj, times",
    [([1], 2), (None, 10)]
)
def test_infinite_repetitions(obj, times):
    """Test infinte repetitions."""
    repeater = repeat(obj)
    irepeater = irepeat(obj)
    for _ in range(times):
        assert next(irepeater) == next(repeater)
