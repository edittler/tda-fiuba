# -*- coding: utf-8 -*-
from math import sqrt
from graph import Graph
from heuristic import Heuristic
from a_star import A_Star

""" Ejemplo 1: grafo en grilla con heurística Manhattan """

g = Graph.from_dict({0: [1,14], 1: [2], 2:[3], 3:[4], 4:[5], 5:[6], 6:[7], 7:[8], 8:[9], 9:[10],
                    10: [11], 11:[12], 12:[13], 14:[15], 15:[16], 16:[17], 17:[18], 18:[19], 19:[13] })

points = {
    0: (0, 0),
    1: (0, 1),
    2: (0, 2),
    3: (0, 3),
    4: (1, 3),
    5: (1, 2),
    6: (2, 2),
    7: (2, 3),
    8: (2, 4),
    9: (2, 5),
    10: (1, 5),
    11: (1, 4),
    12: (0, 4),
    13: (0, 5),
    14: (-1, 0),
    15: (-1, 1),
    16: (-1, 2),
    17: (-1, 3),
    18: (-1, 4),
    19: (-1, 5)
}

# Heurística manhattan
def h(points):
    return lambda u, v: abs(points[v][0] - points[u][0])  + abs(points[v][1] - points[u][1])

path = Heuristic(g,0,13,h(points))
print("Camino con búsqueda por heurísticas: ")
print(path.path_to(13))

path2 = A_Star(g,0,13,h(points))
print("Camino con A*: ")
print(path2.path_to(13))

print("----.----")

""" Otro ejemplo: Grafo Triangular con heurística Manhattan. """

g = Graph(4)
g.add_edge(0,1,1)
g.add_edge(1,3,15)
g.add_edge(0,2,11)
g.add_edge(2,3,9)

points = {
    0: (0, 0),
    1: (0, -1),
    2: (0, 11),
    3: (9, 11),
}

def manhattan(points):
    return lambda u, v: abs(points[v][0] - points[u][0])  + abs(points[v][1] - points[u][1])

def euclidea(points):
    return lambda u,v: sqrt( (points[v][0] - points[u][0])**2 + (points[v][1] - points[u][1])**2 )

path = A_Star(g,0,3,manhattan(points))
print("Camino de A* con Heurística Manhattan")
print(path.path_to(3))

path2 = A_Star(g,0,3,euclidea(points))
print("Camino de A* con Heurística Euclídea")
print(path2.path_to(3))
