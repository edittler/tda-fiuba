#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph import Graph
from tsp_data import tsp_data
from tsp_parser import tsp_parser


def travelling_salesman_path(graph):
    """
    Recibe el grafo sobre el cual se desea resolver problema del viajante de
    comercio.
    Retorna una lista con el orden de ciudades que minimiza el costo del viaje.
    """

    if not isinstance(graph, Graph):
        print("El parámetro no es de tipo Graph")
        return

    # Busca el camino óptimo (incluye el origen como fin)
    path = [0]

    # Incluye el inicio como origen
    path.append(0)

    return opt, list(reversed(path)), len(costs)


def main(args):
    M = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
    data = tsp_data("FULL_MATRIX", M)
    graph = data.graph(True)
    print("\nPrimer ejemplo")
    # print(travelling_salesman_path(graph))
    tree = graph.minimum_spanning_tree()
    print(tree)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
