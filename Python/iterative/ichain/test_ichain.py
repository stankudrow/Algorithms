#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The ichain test module."""


__author__ = "Stanislav D. Kudriavtsev"


from itertools import chain

from pytest import mark, param

from ichain import ichain


# pylint: disable=redefined-outer-name


@mark.parametrize(
    "iters",
    [
        ("hello"),
        ("hello", "world"),
        ((5, 6), (-2, -3), "chars"),
        param(("5", 5), marks=mark.xfail(reason="non-iterable")),
    ],
)
def test_chain(iters):
    """Chain iterables."""
    assert list(ichain(*iters)) == list(chain(*iters))
