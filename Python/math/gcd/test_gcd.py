#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Factorial test module."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, raises

from gcd_iter import gcd_iter
from gcd_rec import gcd_rec


# pylint: disable=arguments-out-of-order


@mark.parametrize("num1, num2", [(1.0, 2), (1, 2.0), (0, -1.0), (-1, 0.0)])
def test_incorrect_inputs(num1, num2):
    """Test non-integers."""
    with raises(TypeError):
        gcd_iter(num1, num2)
    with raises(TypeError):
        gcd_rec(num1, num2)


@mark.parametrize(
    "num1, num2",
    [(0, 0), (3, 0), (4, 1), (12, 3), (12, 4), (12, 6), (12, 10), (12, 12)],
)
def test_various_inputs(num1, num2):
    """Test various inputs."""
    for params in ((num1, num2), (-num1, num2), (num1, -num2), (-num1, -num2)):
        assert gcd_iter(*params) == gcd_rec(*params)
        params = params[::-1]
        assert gcd_iter(*params) == gcd_rec(*params)
