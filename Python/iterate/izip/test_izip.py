#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Izip test module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import Generator, List

from izip import izip


def test_izip_empty() -> None:
    """Empty iterables."""
    seq: List = []
    for tup1, tup2 in zip(izip(seq, seq), zip(seq, seq)):
        assert tup1 == tup2


def test_izip_several_single_element_sequences():
    """Zip several single element sequences."""
    seq1: List = [10]
    seq2: List = [5]
    assert list(izip(seq1, seq2)) == list(zip(seq1, seq2))
    assert list(izip(seq2, seq1)) == list(zip(seq2, seq1))


def test_izip_unequal_sequences():
    """Zip the sequences of unequal length."""
    seq1: Generator = range(2, 10)
    seq2: Generator = range(1, 5)
    assert list(izip(seq1, seq2)) == list(zip(seq1, seq2))
    assert list(izip(seq2, seq1)) == list(zip(seq2, seq1))
