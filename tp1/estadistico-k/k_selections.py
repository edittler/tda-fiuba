#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def k_min(elements, k):
    return k_selections(elements.copy(), k)


def k_selections(l, k):
    """
    Estadistico de orden k por k-selecciones. l es el conjunto de elementos, k
    es el orden del elemento mas chico que se quiere encontrar.
    """

    # selection sort parcial (solo los primeros K)
    for index in range(0, k + 1):
        min_value_index = index
        min_value = l[index]
        for inner_index in range(index + 1, len(l)):
            if l[inner_index] < min_value:
                min_value_index = inner_index
                min_value = l[inner_index]
        l[min_value_index], l[index] = l[index], l[min_value_index]
    return l[k]
