#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge algorithm module."""


from typing import Sequence


# Complexity: best avg  worst
# Time:       Ω(n) Ө(n) O(n)
# Space:      Ω(1) Ө(1) O(1)


# a subrountine for mergesort function
def merge(seq1: Sequence, seq2: Sequence) -> Sequence:
    """
    Merge two sorted sequences into the new sorted one.

    Parameters
    ----------
    seq1 : Sequence
    seq2 : Sequence

    Returns
    -------
    Sequence
        sorted sequence from input ones merged.

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
    #mseq += seq1[ind1:] + seq2[ind2:]  # only for lists
    while ind1 < len1:
        mseq.append(seq1[ind1])
        ind1 += 1
    while ind2 < len2:
        mseq.append(seq2[ind2])
        ind2 += 1
    return mseq


# Complexity: best avg  worst
# Time:       Ω(1) Ө(n*log_2(n)) O(n*log_2(n))
# Space:      Ω(1) Ө(1) O(1)


def merge_sort(seq: Sequence) -> Sequence:
    """
    Sort sequence via merging.

    Parameters
    ----------
    seq : Sequence
        sequence to sort

    Returns
    -------
    """
    leng = len(seq)
    if leng <= 1:
        return seq
    else:
        half = leng // 2
        left = seq[:half]
        right = seq[half:]
    return merge(merge_sort(left), merge_sort(right))

