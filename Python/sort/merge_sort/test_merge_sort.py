#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge test module"""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List

from merge_sort import merge, merge_sort

# pylint: disable=arguments-out-of-order

def test_merge_empties():
    """Empty sequences."""
    seq1: List = []
    seq2: List = []
    assert merge(seq1, seq2) == []


def test_merge_single_element_sequence():
    """Single element sequences."""
    seq1: List = [5]
    seq2: List = [10]
    res: List = [5, 10]
    assert merge(seq1, seq2) == res
    assert merge(seq2, seq1) == res


def test_merge_two_sequences_of_equal_lengths():
    """Two sorted sequences of equal length."""
    seq1: List = [1, 3, 5]
    seq2: List = [2, 3, 4]
    res: List = [1, 2, 3, 3, 4, 5]
    assert merge(seq1, seq2) == res
    assert merge(seq2, seq1) == res


def test_merge_two_sequences_of_unequal_lengths():
    """Two sorted sequences of unequal length."""
    seq1: List = [1, 4, 7]
    seq2: List = [-1, 2, 3, 4, 6, 10]
    res: List = [-1, 1, 2, 3, 4, 4, 6, 7, 10]
    assert merge(seq1, seq2) == res
    assert merge(seq2, seq1) == res


def test_merge_sort_empty_sequence():
    """Sort empty sequence."""
    assert merge_sort([]) == []

def test_merge_sort_single_element_sequence():
    """Sort single element sequence."""
    seq: List = [5]
    assert merge_sort(seq) == seq

def test_merge_sort_two_elements_sequence():
    """Sort two elements sequence."""
    seq: List = [5, 2]
    assert merge_sort(seq) == seq[::-1]

def test_merge_sort_sequence():
    """Sort single element sequence."""
    seq: List = list(range(10))
    assert merge_sort(seq) == seq
