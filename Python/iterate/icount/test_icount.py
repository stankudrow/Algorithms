#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Icount test module."""


__author__ = "Stanislav D. Kudriavtsev"


from itertools import count

from pytest import fixture, raises

from icount import icount


# pylint: disable=redefined-outer-name


NITERS = 10


@fixture
def numbers():
    """Numbers for (i)count."""
    return [-3, 0, 1.5, 2 - 1j, 4.2j]


@fixture()
def not_numbers():
    """Non-numbers for (i)count."""
    return [None, [1, 2], {-3, 4}, (6, 9.7)]


def _test_mech(data):
    """Core test function for count."""
    for start in data:
        for step in data:
            icnt = icount(start, step)
            cnt = count(start, step)
            for _ in range(NITERS):
                assert next(cnt) == next(icnt)


def test_count_to_success(numbers):
    """Test successful counts (numbers only)."""
    _test_mech(numbers)


def test_count_to_fail(not_numbers):
    """Test unsuccessful counts (not numbers)."""
    for entry in not_numbers:
        with raises(TypeError):
            next(icount(entry, entry))
