#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


def k_min(elements, k):
    return k_heapsort(elements, k)


def k_heapsort(elements, k):
    """
    Se hace un heapify y luego se extraen k elementos.
    El último extraido es el k-min.
    """
    heap = elements.copy()
    heapq.heapify(heap)  # O(n) (https://docs.python.org/2/library/heapq.html#heapq.heapify)

    # Sacar k elementos y devolver el último. O(klog(n)) [O(nlog(n) en el peor caso]
    # Como k puede ser 0, el elemento que busco es k + 1
    item = None
    for _ in range(k + 1):
        item = heapq.heappop(heap)
    return item
