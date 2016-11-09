#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from max_flow import Flow


class ProjectSelection(object):
    """
    Esta es la clase que va a resolver el problema de ganancias por proyecto.
    En el Kleinberg-Tardos aparece bajo ese nombre.

    Necesita un archivo que tenga el siguiente formato:

        N
        M
        c1
        c2
        ...
        g1 r11 r12
        g2 r21 r22
        ...

    Donde N es la cantidad de capacidades, M es la cantidad de proyectos,
    c1 es el nombre de la capacidad 1, g1 es la ganancia de proyecto uno, y
    r11..r1k son las capacidades requeridas del proyecto 1.
    """

    def __init__(self, filename):
        self.capacities = []
        self.proyects = []

        with open(filename) as f:
            self.n = int(f.readline().strip())
            self.m = int(f.readline().strip())
            for _ in range(self.n):
                self.capacities.append(f.readline().strip())
            for _ in range(self.m):
                self.proyects.append(f.readline().strip().split(' '))

    def solve(self):
        pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Por favor, pase un archivo!')
    else:
        ProjectSelection(sys.argv[1]).solve()
