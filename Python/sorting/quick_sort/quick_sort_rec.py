#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The recursive Hoare quick sort algorithm.

The quick sort algorithm was invented by Sir Antony Hoare in 1959.

References
----------
    * https://en.wikipedia.org/wiki/Quicksort
    * https://foxford.ru/wiki/informatika/bystraya-sortirovka-hoara-python
    * https://stackoverflow.com/questions/18262306/quicksort-with-python
    * https://www.geeksforgeeks.org/quick-sort/

"""


__author__ = "Stanislav D. Kudriavtsev"


from random import choice
from typing import List, Sequence


# Complexity: worst case
# Time      : from O(n*log(n)) to O(n**2)
# Space:    : from O(log(n)) to O(n)


def quick_sort_rec(seq: Sequence) -> List:
    """
    Sort a sequence with the Hoare quick sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    if len(seq) > 1:
        pivot = choice(seq)
        less: List = []
        equal: List = []
        greater: List = []
        for elem in seq:
            if elem < pivot:
                less.append(elem)
            elif elem > pivot:
                greater.append(elem)
            else:
                equal.append(elem)
        return quick_sort_rec(less) + equal + quick_sort_rec(greater)
    return list(seq)
