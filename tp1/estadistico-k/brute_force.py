#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def k_min(elements, k):
    return brute_force(elements, k)


def brute_force(l, k):
    """
    Estadístico de orden k por fuerza bruta.
    l es el conjunto de elementos,
    k es el orden del elemento más chico.
    """

    # función interna que verifica si un elemento es el k más chico
    def _is_k_lowest(elem):
        lower_elements_count = 0

        for item in l:
            if item < elem:
                lower_elements_count += 1

        # Si la cantidad de elementos más pequeños es k, elem es el k más pequeño
        return lower_elements_count == k

    for item in l:
        if _is_k_lowest(item):
            return item


def brute_force_1liner(l, k):
    """
    La misma implementación del brute force pero hecho en una linea
    simplemente porque se puede.
    """
    return next(i for i in l if sum(1 for x in l if x < i) == k)
