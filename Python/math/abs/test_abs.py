#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The abs(olute value) test module."""


__author__ = "Stanislav D. Kudriavtsev"


from math import isclose

from pytest import mark, raises

from abs_ import abs_


# pylint: disable=arguments-out-of-order


@mark.parametrize("num", ["str", (1,), {-1: 1}])
def test_incorrect_inputs(num):
    """Test incorrect input values."""
    with raises(TypeError):
        abs_(num)


@mark.parametrize("num", [-3, -2.89, -1 - 4.3j, -0, 0, 1, 2.3, 5 - 3.6j, 7.89 + 3j])
def test_various_inputs(num):
    """Test various inputs."""
    assert isclose(abs_(num), abs(num))
