#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Izip test module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List

from pytest import mark

from izip import izip


def test_izip_empty_iterables():
    """Empty iterables."""
    seq: List = []
    for tup1, tup2 in zip(izip(seq, seq), zip(seq, seq)):
        assert tup1 == tup2


def test_izip_single_element_iterables():
    """Zip several single element iterables."""
    seq1: List = [10]
    seq2: List = [20]
    assert list(izip(seq1, seq2)) == list(zip(seq1, seq2))
    assert list(izip(seq2, seq1)) == list(zip(seq2, seq1))


@mark.parametrize(
    'seq1, seq2',
    [([], [1, 2]),
     ([4], []),
     (range(5), range(10))]
)
def test_izip_iterables(seq1, seq2):
    """Zip several test cases."""
    assert list(izip(seq1, seq2)) == list(zip(seq1, seq2))
    assert list(izip(seq2, seq1)) == list(zip(seq2, seq1))
