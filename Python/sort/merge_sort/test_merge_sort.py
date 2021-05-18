#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge sort test module"""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, param

from merge_sort import merge, merge_sort


# pylint: disable=arguments-out-of-order


@mark.parametrize("seq, res", [([], []), ("", []), ((), [])])
def test_merge_empties(seq, res):
    """Empty sequences."""
    assert merge(seq, seq) == res


@mark.parametrize(
    "seq1, seq2, res",
    [([5], [2], [2, 5]), ("b", "a", ["a", "b"]), ((4,), (1,), [1, 4])],
)
def test_merge_single_element_sequence(seq1, seq2, res):
    """Single element sequences."""
    assert merge(seq1, seq2) == res
    assert merge(seq2, seq1) == res


@mark.parametrize(
    "seq1, seq2, res",
    [
        ([3, 5], [2, 4], [2, 3, 4, 5]),
        ("br", "egg", ["b", "e", "g", "g", "r"]),
        (param((4, 1, 6), (1, 7, 2), [1, 1, 2, 4, 6, 7], marks=mark.xfail)),
    ],
)
def test_merge_sequences_of_equal_lengths(seq1, seq2, res):
    """Two sorted sequences of equal length."""
    assert merge(seq1, seq2) == res
    assert merge(seq2, seq1) == res


@mark.parametrize(
    "seq1, seq2, res",
    [
        ([3, 5, 7], [2, 4], [2, 3, 4, 5, 7]),
        ("br", "abcd", ["a", "b", "b", "c", "d", "r"]),
        (param((4, 1, 6), (7, 2), [1, 2, 4, 6, 7], marks=mark.xfail)),
    ],
)
def test_merge_sequences_of_unequal_lengths(seq1, seq2, res):
    """Two sorted sequences of unequal length."""
    assert merge(seq1, seq2) == res
    assert merge(seq2, seq1) == res


@mark.parametrize("seq, res", [([], []), ("", ""), ((), ())])
def test_merge_sort_empty_sequence(seq, res):
    """Sort empty sequence."""
    assert merge_sort(seq) == res


@mark.parametrize("seq, res", [([1], [1]), ("1", "1"), ((1,), (1,))])
def test_merge_sort_single_element_sequence(seq, res):
    """Sort single element sequence."""
    assert merge_sort(seq) == res


@mark.parametrize(
    "seq", [[3, 6, 3, 1, 8], (-1, 7, -3, 6, 3), "qwerty"],
)
def test_merge_sort_sequence(seq):
    """Sort arbitrary sequences."""
    assert merge_sort(seq) == sorted(seq)
