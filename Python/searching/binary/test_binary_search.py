#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Binary search test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, param

from binary_search_iter import binary_search_iter as isearch
from binary_search_rec import binary_search_rec as rsearch


@mark.parametrize("seq, val", [([], 0), ((), 0), ("", 0)])
def test_empty_sequences(seq, val):
    """Empty sequences."""
    assert isearch(seq, val) is None
    assert rsearch(seq, val) is None


@mark.parametrize(
    "seq, val, res",
    [
        ([1], 1, 0),
        ((2,), 0, None),
        ("3", "3", 0),
        param("3", 3, None, marks=mark.xfail(reason="TypeError")),
    ],
)
def test_single_element_sequences(seq, val, res):
    """Search a value in a single element sequence."""
    assert isearch(seq, val) == res
    assert rsearch(seq, val) == res


@mark.parametrize(
    "seq, val, res",
    [
        ([1, 2], 1, 0),
        ([2, 3], 3, 1),
        ([3, 4], 2, None),
        ([0, 1], -1, None),
        ([-1, 0], 2, None),
    ],
)
def test_two_element_sequences(seq, val, res):
    """Search a value in a sequence with two elements."""
    assert isearch(seq, val) == res


@mark.parametrize("upto", [2, 4, 6, 10, 15, 21, 41])
def test_sequential_findings(upto):
    """Find all elemets of a sequence."""
    seq = list(range(upto))
    for ind, elem in enumerate(seq):
        assert isearch(seq, elem) == ind
        assert rsearch(seq, elem) == ind


@mark.parametrize(
    "seq, results",
    [
        ([-2, 0, 2],
         {-10: None, -2: 0, -1: None, 0: 1, 1: None, 2: 2, 10: None}),
        ([1, 5, 6, 9],
         {-1: None, 1: 0, 3: None, 5: 1, 6: 2, 8: None, 9: 3, 12: None})
    ]
)
def test_values(seq, results):
    """Find all elemets of a sequence."""
    for value, expected in results.items():
        ianswer = isearch(seq, value)
        ranswer = rsearch(seq, value)
        if ianswer is None:
            assert ianswer is ranswer is expected
        else:
            assert ianswer == ranswer == expected
