#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph import Graph
from tsp_parser import tsp_parser


def travelling_salesman_path(graph):
    """
    Recibe el grafo sobre el cual se desea resolver problema del viajante de
    comercio.
    Retorna una lista con el orden de ciudades que minimiza el costo del viaje.
    """

    if not isinstance(graph, Graph):
        print("Los datos no son del tipo tsp_data")
        return

    # Busca el camino óptimo (incluye el origen como fin)
    path = [0]

    # Incluye el inicio como origen
    path.append(0)

    return opt, list(reversed(path)), len(costs)


def main(args):

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
