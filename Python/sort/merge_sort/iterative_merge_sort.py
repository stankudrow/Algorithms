#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge sort algorithm module."""


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
    # mseq += seq1[ind1:] + seq2[ind2:]
    while ind1 < len1:
        mseq.append(seq1[ind1])
        ind1 += 1
    while ind2 < len2:
        mseq.append(seq2[ind2])
        ind2 += 1
    return mseq


# Complexity: worst case
# Time      : O(n*log_2(n))
# Space     : O(n)


# merge function is meant to be pure
# it would have been easier to make assignments in place
# so this implementation is more expensive than classic one

# this link provided some insights:
# https://www.techiedelight.com/iterative-merge-sort-algorithm-bottom-up/

def iter_merge_sort(seq: Sequence) -> List:
    """
    Iterative merge sort on a sequence.

    Parameters
    ----------
    seq : Sequence

    Returns
    -------
    List

    """
    length: int = len(seq)
    size: int = 1
    mseq: List = list(seq)  # to be merged
    while size < length:
        for lbound in range(0, length, 2 * size):
            start: int = lbound
            mid: int = start + size
            end: int = min(start + 2*size, length)
            mseq[start:end] = merge(mseq[start:mid], mseq[mid:end])
        size *= 2
    return mseq
