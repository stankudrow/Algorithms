#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Linear search test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, param

from iterative_linear_search import iter_linear_search as isearch
from recursive_linear_search import rec_linear_search as rsearch


@mark.parametrize("seq, val", [([], 0), ((), 0), ("", 0)])
def test_empty_sequences(seq, val):
    """Empty sequences."""
    assert isearch(seq, val) is rsearch(seq, val) is None


@mark.parametrize(
    "seq, val, res", [([1], 1, 0),
                      ((2,), 0, None),
                      param("3", 1, 1, marks=mark.xfail)]
)
def test_single_element_sequences(seq, val, res):
    """Search a value in a single element sequence."""
    assert isearch(seq, val) == rsearch(seq, val) == res


@mark.parametrize("seq", ["abcdef",
                          range(2, 10),
                          param("qwerty", marks=mark.xfail)])
def test_sequential_findings(seq):
    """Find all positions in a sequence."""
    for ind, elem in enumerate(seq):
        assert isearch(seq, elem) == rsearch(seq, elem) == ind
