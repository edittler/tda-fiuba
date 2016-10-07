#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


def k_min(elements, k):
    return heap_select(elements.copy(), k)

def heap_select(elements, k):
    """
    Se almancenan los k elementos más chicos en un heap de máximo y
    se devuelve el k-esimo valor
    """
    minimos = [(-i, i) for i in elements[:k+1]]
    heapq.heapify(minimos)

    for elem in elements[k+1:]:
        # Se inserta el elemento si y solo si es menor al máximo del heap.
        # En el caso de insertarlo, se saca el máximo.
        if elem < minimos[0][1]:
            heapq.heappush(minimos, (-elem,elem))
            heapq.heappop(minimos)

    return minimos[0][1]
