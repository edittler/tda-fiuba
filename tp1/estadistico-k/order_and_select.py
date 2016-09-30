#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def k_min(elements, k):
    return order_and_select(elements, k)


def order_and_select(l, k):
    """
    Se ordena el conjunto dado y se devuelve el k-esimo valor
    """
    # TODO: No ser ladri e implementar un algoritmo de ordenamiento
    list.sort(l)
    return l[k]
