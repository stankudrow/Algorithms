#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The merge sort algorithm module."""


__author__ = "Stanislav D. Kudriavtsev"


from typing import List, Sequence


# Complexity: worst case
# Time      : O(n)
# Space     : O(1)


# a subrountine for mergesort function
def merge(seq1: Sequence, seq2: Sequence) -> List:
    """
    Merge two sorted sequences into the new sorted one.

    Parameters
    ----------
    seq1 : Sequence
    seq2 : Sequence

    Returns
    -------
    List

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
    # either seq1 or seq2 is exhausted, so it is just []
    mseq += list(seq1)[ind1:] + list(seq2)[ind2:]  # for mypy
    return mseq


# Complexity: worst case
# Time      : O(n*log_2(n))
# Space     : O(n)


def rec_merge_sort(seq: Sequence) -> List:
    """
    Sort a sequence with the recursive merge sort algorithm.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    length: int = len(seq)
    if length <= 1:
        return list(seq)
    half: int = length // 2
    left: Sequence = seq[:half]
    right: Sequence = seq[half:]
    return merge(rec_merge_sort(left), rec_merge_sort(right))
