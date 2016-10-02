#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


def k_min(elements, k):
    return heap_select(elements, k)


def heap_select(elements, k):
    """
    Se almancenan los k elementos más chicos en un heap de máximo y
    se devuelve el k-esimo valor
    """
    heap = elements[:k+1]
    heapq._heapify_max(heap)
    for elem in elements[k+1:]:
        # Se inserta el elemento si y solo si es menor al máximo del heap.
        # En el caso de insertarlo, se saca el máximo.
        heapq._heappushpop_max(heap, elem)

    return heap[0]
