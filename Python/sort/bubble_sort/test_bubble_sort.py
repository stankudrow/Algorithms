#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bubble sort test module"""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark

from bubble_sort import bubble_sort


# pylint: disable=arguments-out-of-order


@mark.parametrize("seq, res", [([], []), ("", []), ((), [])])
def test_bubble_sort_empties(seq, res):
    """Empty sequences."""
    assert bubble_sort(seq) == res


@mark.parametrize("seq", [[1], "1", (1,)])
def test_bubble_sort_single_element_sequence(seq):
    """Sort single element sequence."""
    assert bubble_sort(seq) == list(seq)


@mark.parametrize(
    "seq", [[3, 6, 3, 1, 8], (-1, 7, -3, 6, 3), "qwerty"],
)
def test_bubble_sort_sequence(seq):
    """Sort arbitrary sequences."""
    assert bubble_sort(seq) == sorted(seq)
