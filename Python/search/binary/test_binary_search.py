#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Binary search test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, param

from binary_search import ibinary_search as ibins, rbinary_search as rbins


@mark.parametrize("seq, val", [([], 0), ((), 0), ("", 0)])
def test_binary_search_empty(seq, val):
    """Empty sequences."""
    assert ibins(seq, val) is rbins(seq, val) is None


@mark.parametrize(
    "seq, val, res", [([1], 1, 0), ((2,), 0, None), param("3", 1, 1, marks=mark.xfail)]
)
def test_binary_search_single_element(seq, val, res):
    """Search a value in a single element sequence."""
    assert ibins(seq, val) == rbins(seq, val) == res


@mark.parametrize("seq", ["abcdef", range(2, 10), param("qwerty", marks=mark.xfail)])
def test_binary_search_sequential_findings(seq):
    """Find all positions in a sequence."""
    for ind, elem in enumerate(seq):
        assert ibins(seq, elem) == rbins(seq, elem) == ind
