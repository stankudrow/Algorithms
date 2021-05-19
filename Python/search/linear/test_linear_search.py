#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Linear search test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, param

from linear_search import ilinear_search as ilins, rlinear_search as rlins


@mark.parametrize("seq, val", [([], 0), ((), 0), ("", 0)])
def test_linear_search_empty(seq, val):
    """Empty sequences."""
    assert ilins(seq, val) is rlins(seq, val) is None


@mark.parametrize(
    "seq, val, res", [([1], 1, 0), ((2,), 0, None), param("3", 1, 1, marks=mark.xfail)]
)
def test_linear_search_single_element(seq, val, res):
    """Search a value in a single element sequence."""
    assert ilins(seq, val) == rlins(seq, val) == res


@mark.parametrize("seq", ["abcdef", range(2, 10), param("qwerty", marks=mark.xfail)])
def test_linear_search_sequential_findings(seq):
    """Find all positions in a sequence."""
    for ind, elem in enumerate(seq):
        assert ilins(seq, elem) == rlins(seq, elem) == ind
