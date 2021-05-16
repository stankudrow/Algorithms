#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Linear search test module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List

from linear_search import ilinear_search as ilins, rlinear_search as rlins


def test_linear_search_empty():
    """Empty sequence."""
    seq: List = []
    assert ilins(seq, 0) is rlins(seq, 0) is None
    assert ilins(seq, None) is rlins(seq, None) is None


def test_linear_search_single_element():
    """Search a value in a single element sequence."""
    elem = 10
    felem = elem - 1
    seq = [elem]
    assert ilins(seq, elem) == rlins(seq, elem) == seq.index(elem)
    # [1].index(0) will cause ValueError
    assert ilins(seq, felem) is rlins(seq, felem) != 0


def test_linear_search_successive_findings():
    """Find all positions in a sequence."""
    seq = [i for i in range(5)]  # pylint: disable = unnecessary-comprehension
    for ind, elem in enumerate(seq):
        assert ilins(seq, elem) == rlins(seq, elem) == ind
