#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The icycle test module."""


__author__ = "Stanislav D. Kudriavtsev"


from itertools import cycle

from pytest import fixture, raises

from icycle import icycle


# pylint: disable=redefined-outer-name


@fixture
def non_iters():
    """Non-iterables for (i)cycle."""
    return [-3, 0, 1.5, 2 - 1j, 4.2j, None]


@fixture()
def iters():
    """Iterables for (i)cycle."""
    return [[], [1, 2], {-3, 4}, (6, 9.7, -16), {"a": 1, "b": 2}]


def _test_mech(data):
    """The test function for (i)cycle functions."""
    for iter_ in data:
        icyc = icycle(iter_)
        cyc = cycle(iter_)
        for _ in range(2 * len(iter_)):
            assert next(cyc) == next(icyc)


def test_cycle_to_success(iters):
    """Test successful cycles (iterables only)."""
    _test_mech(iters)


def test_cycle_to_fail(non_iters):
    """Test unsuccessful cycles (numbers)."""
    for niter in non_iters:
        with raises(TypeError):
            next(icycle(niter))
