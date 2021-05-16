#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Linear search test module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List

from binary_search import ibinary_search as ibins, rbinary_search as rbins


def test_linear_search_empty():
    """Empty sequence."""
    seq: List = []
    assert ibins(seq, 0) is rbins(seq, 0) is None
    assert ibins(seq, None) is rbins(seq, None) is None


def test_linear_search_single_element():
    """Search a value in a single element sequence."""
    elem = 10
    felem = elem - 1
    seq = [elem]
    assert ibins(seq, elem) == rbins(seq, elem) == seq.index(elem)
    # [1].index(0) will cause ValueError
    assert ibins(seq, felem) is rbins(seq, felem) != 0


def test_linear_search_successive_findings():
    """Find all positions in a sequence."""
    seq = [i for i in range(5)]  # pylint: disable = unnecessary-comprehension
    for ind, elem in enumerate(seq):
        assert ibins(seq, elem) == rbins(seq, elem) == ind
