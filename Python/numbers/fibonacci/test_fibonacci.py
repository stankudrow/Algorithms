#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Binary search test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, raises

from fib_gen import fib_gen
from fib_rec import fib_rec


@mark.parametrize("nonint", [2.5, "3", [4]])
def test_non_integers(nonint):
    """Test non-integers."""
    with raises(TypeError):
        fib_gen(nonint)
    with raises(TypeError):
        fib_rec(nonint)


@mark.parametrize("invint", [-2, 0])
def test_invalid_integers(invint):
    """Test invalid integers."""
    with raises(ValueError):
        fib_gen(invint)
    with raises(ValueError):
        fib_rec(invint)


@mark.parametrize("nth", [1, 2, 5, 9, 10, 100])
def test_first_terms(nth):
    """Test n first terms."""
    assert list(fib_gen(nth)) == [fib_rec(term) for term in range(1, nth + 1)]
