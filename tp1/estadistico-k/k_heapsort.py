#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


def k_min(elements, k):
    return heap_select(elements, k)


def k_heapsort(elements, k):
    """
    Se hace un heapify y luego se extraen k elementos.
    El último extraido es el k-min.
    """
    heap = elements.copy()
    heapq.heapify(heap)

    # Sacar k - 1 elementos. Devolver la cabeza del heap.
