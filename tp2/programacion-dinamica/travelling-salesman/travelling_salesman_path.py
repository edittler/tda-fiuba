#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
from tsp_data import tsp_data
from tsp_parser import tsp_parser


def travelling_salesman_path(data):
    """
    Recibe los datos del problema del viajante de comercio.
    Retorna una lista con el orden de ciudades que minimiza el costo del viaje.
    """

    if not isinstance(data, tsp_data):
        print("Los datos no son del tipo tsp_data")
        return

    n = data.dimension()
    # print("Cities: " + str(n))
    costs = {}

    for k in range(1, n):
        costs[(1 << k, k)] = (data.cost(0, k), 0)

    # print(costs)

    for subset_size in range(2, n):
        subsets = itertools.combinations(range(1, n), subset_size)
        # subset_size_text = "(subset size: " + str(subset_size) + ")"
        # progress_text = "Progress " + str(int(float(subset_size / n * 100))) + "%"
        # print(progress_text + " " + subset_size_text)
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
                    res.append((costs[(prev, m)][0] + data.cost(m, k), m))
                costs[(bits, k)] = min(res)
                # print(costs)

    bits = (2**n - 1) - 1

    # Calcular el costo óptimo
    res = []
    for k in range(1, n):
        res.append((costs[(bits, k)][0] + data.cost(k, 0), k))
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

    return opt, list(reversed(path)), len(costs)


def main(args):
    M = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
    data = tsp_data("FULL_MATRIX", M)
    print("\nPrimer ejemplo")
    print(travelling_salesman_path(data))

    data = tsp_parser.parse_tsp_file("test_files/p01.tsp")
    print("\nSegundo ejemplo")
    print(travelling_salesman_path(data))

    data = tsp_parser.parse_tsp_file("test_files/fri26.tsp")
    print("\nTercer ejemplo")
    print(travelling_salesman_path(data))

    data = tsp_parser.parse_matrix_file("test_files/att48_d.txt")
    print("\nCuarto ejemplo")
    # print(travelling_salesman_path(data))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
