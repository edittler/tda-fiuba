#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


def k_min(elements, k):
    return heap_select(elements, k)


def heap_select(elements, k):
    """
    Se almancenan los k elementos más chicos en un heal y
    se devuelve el k-esimo valor
    """
    heap = heapq.nsmallest(k+1, elements)
    # Hay que averiguar cual es el orden de nsmallest
    return heap[-1]
