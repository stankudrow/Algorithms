#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The merge (sequences) algorithm."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n)
# Space     : O(m)


# Typically this function is a subrountine for merge_sort algorithm.
def merge(seq1: Sequence, seq2: Sequence) -> List:
    """
    Merge two sorted sequences into a new sorted one.

    Parameters
    ----------
    seq1 : Sequence
    seq2 : Sequence

    Returns
    -------
    Sequence

    """
    ind1: int = 0
    len1: int = len(seq1)
    ind2: int = 0
    len2: int = len(seq2)
    mseq = []  # merged sequence
    while (ind1 < len1) and (ind2 < len2):
        elem1, elem2 = seq1[ind1], seq2[ind2]
        if elem1 < elem2:
            mseq.append(elem1)
            ind1 += 1
        else:
            mseq.append(elem2)
            ind2 += 1
    mseq += list(seq1)[ind1:] + list(seq2)[ind2:]  # for mypy
    return mseq
