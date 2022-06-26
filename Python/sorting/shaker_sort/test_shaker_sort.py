#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The shaker/cocktail sort test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, param

from shaker_sort_iter import shaker_sort_iter as isort


# pylint: disable=arguments-out-of-order


@mark.parametrize("seq, res", [([], []), ("", []), ((), [])])
def test_empty_sequences(seq, res):
    """Empty sequences."""
    assert isort(seq) == res


@mark.parametrize("seq", [[1], "1", (1,)])
def test_single_element_sequence(seq):
    """Single element sequences."""
    res = list(seq)
    assert isort(seq) == res


@mark.parametrize(
    "seq", [[-1, 1], (-2, 0, 2), "ABCxyz", "1234567", ([1, 2], [2, 3], [5, 7, 9])]
)
def test_sorted_sequences(seq):
    """Sorted sequences."""
    res = list(seq)
    assert isort(seq) == res


@mark.parametrize(
    "seq", [[1, 0], (2, -2, 0), "qwerty", "School42", ([1, -1], [5, 0, 15, -10])]
)
def test_unsorted_sequences(seq):
    """Unsorted sequences."""
    res = sorted(seq)
    assert isort(seq) == res


@mark.parametrize(
    "nonseq", [param(42, marks=mark.xfail), param(None, marks=mark.xfail)]
)
def test_nonsequences(nonseq):
    """Non-sequences."""
    assert isort(nonseq)
