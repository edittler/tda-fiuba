# -*- coding: utf-8 -*-


def brute_force(l, k):
    """
    Estadístico de orden k por fuerza bruta. l es el conjunto de elementos, k
    es el orden del elemento más chico.
    """

    # función interna que verifica si un elemento es el k más chico
    def _is_k_lowest(elem):
        # Uso un set para guardar todos los elementos menores a elem. Set inserta
        # solo elementos nuevos, ignorando los duplicados. La inserción en un
        # set es O(1) amortizada (https://wiki.python.org/moin/TimeComplexity)
        lower_than_elem = set()

        for item in l:
            if item < elem:
                lower_than_elem.add(item)
        # Si la cantidad de elementos guardados es k - 1, elem es el k más pequeño
        return len(lower_than_elem) == k - 1

    for item in l:
        if _is_k_lowest(item):
            return item


def brute_force_1liner(l, k):
    """
    La misma implementación del brute force pero hecho en una linea simplemente
    porque se puede.
    """
    return next(i for i in l if len({x for x in l if x < i}) == k - 1)
