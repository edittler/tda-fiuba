#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import itertools


def travelling_salesman_path(matrix):
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
    costs = {}

    for k in range(1, n):
        costs[(1 << k, k)] = (matrix[0][k], 0)

    print(costs)

    for subset_size in range(2, n):
        subsets = itertools.combinations(range(1, n), subset_size)
        for subset in subsets:
            # Seteo los bits de todos los nodos del subconjunto
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Busco el menor costo para llegar a ese subconjunto
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((costs[(prev, m)][0] + matrix[m][k], m))
                costs[(bits, k)] = min(res)
                # print(costs)

    bits = (2**n - 1) - 1

    # Calcular el costo óptimo
    res = []
    for k in range(1, n):
        res.append((costs[(bits, k)][0] + matrix[k][0], k))
    opt, parent = min(res)

    # Busca el camino óptimo (incluye el origen como fin)
    path = [0]
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = costs[(bits, parent)]
        bits = new_bits

    # Incluye el inicio como origen
    path.append(0)

    return opt, list(reversed(path))


def main(args):
    # M = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12], [10, 4, 8, 0]]
    M = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
    print("Resultado")
    print(travelling_salesman_path(M))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
