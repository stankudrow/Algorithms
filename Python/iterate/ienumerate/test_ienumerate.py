#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ienumerate test module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List

from pytest import raises

from ienumerate import ienumerate


def test_ienumerate_empty() -> None:
    """Empty iterables."""
    seq: List = []
    for tup1, tup2 in zip(ienumerate(seq), enumerate(seq)):
        assert tup1 == tup2


def test_ienumerate_successive():
    """A successive enumeration of a sequence."""
    seq = range(10)
    start = -3
    for tup1, tup2 in zip(ienumerate(seq, start), enumerate(seq, start)):
        assert tup1 == tup2


def test_ienumerate_not_int_start():
    """Raise TypeError on non-integer start."""
    with raises(TypeError):
        next(ienumerate([2, 4], 0.8))
