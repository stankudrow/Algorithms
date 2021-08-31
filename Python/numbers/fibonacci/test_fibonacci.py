#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fibonacci numbers test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, raises

from fibonacci_gen import fibonacci_gen as fib_gen
from fibonacci_rec import fibonacci_rec as fib_rec
from even_fibonacci_gen import even_fibonacci_gen as efib_gen


@mark.parametrize("nonint", [2.5, "3", [4]])
def test_non_integers(nonint):
    """Test non-integers."""
    with raises(TypeError):
        fib_gen(nonint)
    with raises(TypeError):
        fib_rec(nonint)
    with raises(TypeError):
        efib_gen(nonint)


@mark.parametrize("invint", [-2, 0])
def test_invalid_integers(invint):
    """Test invalid integers."""
    with raises(ValueError):
        fib_gen(invint)
    with raises(ValueError):
        fib_rec(invint)
    with raises(ValueError):
        efib_gen(invint)


@mark.parametrize("nth", list(range(1, 101)))
def test_fibonacci_nth(nth):
    """Test n first terms."""
    infibgen = fib_gen()
    infslice = [next(infibgen) for _ in range(nth)]
    fibrec = [fib_rec(term) for term in range(1, nth + 1)]
    fibgen = list(fib_gen(nth))
    assert fibgen == infslice == fibrec


@mark.parametrize(
    "nth, res",
    [
        (1, [0]),
        (2, [0, 2]),
        (4, [0, 2, 8, 34]),
        (10, [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418]),
    ],
)
def test_even_fibonacci_nth(nth, res):
    """Test n first terms."""
    inefibgen = efib_gen()
    infslice = [next(inefibgen) for _ in range(nth)]
    assert list(efib_gen(nth)) == infslice == res
    