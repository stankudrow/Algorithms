#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The izip test module."""


__author__ = "Stanislav D. Kudriavtsev"


from itertools import zip_longest

from pytest import fixture

from izip import izip


# pylint: disable=redefined-outer-name


@fixture()
def iterables():
    """Iterables for izip."""
    return [[], [0], [1, 0], [-1, 0, 1], "hello", (None, [None], {None})]


def test_zip(iterables):
    """Zip several test cases."""
    for it1 in iterables:
        for it2 in iterables:
            assert list(izip(it1, it2)) == list(zip(it1, it2))


def test_zip_longest(iterables):
    """Zip longest several test cases."""
    for it1 in iterables:
        for it2 in iterables:
            izi = list(izip(it1, it2, longest=True))
            zli = list(zip_longest(it1, it2))
            assert izi == zli  # instances
