#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


def heap_select(array, k):
    """
    Se almancenan los k elementos más chicos en un heal y
    se devuelve el k-esimo valor
    """
    heap = heapq.nsmallest(k+1, array)
    # Hay que averiguar cual es el orden de nsmallest
    return heap[-1]


def test_heap_select():
    l = [5, 2, 9, 7, 1, 90, 123, 8, 3]
    assert heap_select(l, 3) == 5
    l = [5, 2, 9, 7, 1, 90, 123, 8, 3]
    assert heap_select(l, 0) == 1
    l = [5, 2, 9, 7, 1, 90, 123, 8, 3]
    assert heap_select(l, len(l) - 1) == 123

test_heap_select()
