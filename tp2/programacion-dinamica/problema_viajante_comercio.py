#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import itertools


def camino_viajante_comercio(matrix):
    """
    Recibe una matriz de costos de todos los destinos y el vertice de inicio.
    Retorna una lista con el orden de ciudades que minimiza el costo del viaje.
    """

    matrix_shape = numpy.shape(matrix)
    if len(matrix_shape) != 2:
        print("La matriz no es de dimension 2")
        return []
    elif matrix_shape[0] != matrix_shape[1]:
        print("La matriz no es cuadrada")
        return []

    n = matrix_shape[0]
    costos_parciales = {}

    for k in range(1, n):
        costos_parciales[(1 << k, k)] = (matrix[0][k], 0)

    print(costos_parciales)

    for tamanio_subconjuntos in range(2, n):
        subconjuntos = itertools.combinations(range(1, n), tamanio_subconjuntos)
        for subconjunto in subconjuntos:
            # Seteo los bits de todos los nodos del subconjunto
            bits = 0
            for bit in subconjunto:
                bits |= 1 << bit

            # Busco el menor costo para llegar a ese subconjunto
            for k in subconjunto:
                prev = bits & ~(1 << k)

                res = []
                for m in subconjunto:
                    if m == 0 or m == k:
                        continue
                    res.append((costos_parciales[(prev, m)][0] + matrix[m][k], m))
                costos_parciales[(bits, k)] = min(res)
                # print(costos_parciales)

    bits = (2**n - 1) - 1

    # Calcular el costo óptimo
    res = []
    for k in range(1, n):
        res.append((costos_parciales[(bits, k)][0] + matrix[k][0], k))
    opt, padre = min(res)

    # Busca el camino óptimo (incluye el origen como fin)
    camino = [0]
    for i in range(n - 1):
        camino.append(padre)
        new_bits = bits & ~(1 << padre)
        _, padre = costos_parciales[(bits, padre)]
        bits = new_bits

    # Incluye el inicio como origen
    camino.append(0)

    return opt, list(reversed(camino))


def main(args):
    # M = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10, 4, 8, 0]]
    M = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
    print("Resultado")
    print(camino_viajante_comercio(M))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
