#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The ienumerate test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, raises

from ienumerate import ienumerate


@mark.parametrize("seq", [[], (), "", {}])
def test_empty_iterable(seq) -> None:
    """Empty iterables."""
    for tup1, tup2 in zip(ienumerate(seq), enumerate(seq)):
        assert tup1 == tup2


def test_successive_iterable():
    """Successive iterable."""
    seq = range(-10, 10)
    for tup1, tup2 in zip(ienumerate(seq), enumerate(seq)):
        assert tup1 == tup2


@mark.parametrize("seq, starts", [(range(10), [-2, 2, 10])])
def test_start(seq, starts):
    """Several starts for enumeration."""
    seq = list(seq)
    for start in starts:
        for tup1, tup2 in zip(ienumerate(seq, start), enumerate(seq, start)):
            assert tup1 == tup2


@mark.parametrize("noniter", [None, 21, 4.2])
def test_noniterable(noniter):
    """TypeError on non-iterable."""
    with raises(TypeError):
        next(ienumerate(noniter))


@mark.parametrize("start", [None, 4.2, []])
def test_incorrect_start(start):
    """TypeError on an incorrect start value."""
    with raises(TypeError):
        next(ienumerate([21], start))
