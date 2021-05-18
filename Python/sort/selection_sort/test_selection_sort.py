#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Selection sort test module"""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark

from selection_sort import selection_sort


# pylint: disable=arguments-out-of-order


@mark.parametrize("seq, res", [([], []), ("", []), ((), [])])
def test_selection_sort_empties(seq, res):
    """Empty sequences."""
    assert selection_sort(seq) == res


@mark.parametrize("seq", [[1], "1", (1,)])
def test_selection_sort_single_element_sequence(seq):
    """Sort single element sequence."""
    assert selection_sort(seq) == list(seq)


@mark.parametrize(
    "seq", [[3, 6, 3, 1, 8], (-1, 7, -3, 6, 3), "qwerty"],
)
def test_merge_sort_sequence(seq):
    """Sort arbitrary sequences."""
    assert selection_sort(seq) == sorted(seq)
