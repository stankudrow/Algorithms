#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Factorial test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, raises

from factorial_iter import factorial_iter
from factorial_rec import factorial_rec


@mark.parametrize("nonint", [2.5, "3", [4]])
def test_non_integers(nonint):
    """Test non-integers."""
    with raises(TypeError):
        factorial_iter(nonint)
    with raises(TypeError):
        factorial_rec(nonint)


@mark.parametrize("invint", [-2])
def test_invalid_integers(invint):
    """Test invalid integers."""
    with raises(ValueError):
        factorial_iter(invint)
    with raises(ValueError):
        factorial_rec(invint)


@mark.parametrize("nth", [*range(1, 11)])
def test_first_nums(nth):
    """Test n first numbers."""
    assert factorial_iter(nth) == factorial_rec(nth)
