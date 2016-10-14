# -*- coding: utf-8 -*-


class CommonPath(object):
    """
    Abstracción de búsqueda de caminos para todos los algoritmos.

    Los algoritmos deberán ser subclase de CommonPath y definir el método
    search, que se va a llamar en el constructor.
    La idea (inicial) es que se llene el diccionario parents con vertices como
    claves y valores. Ese diccionario luego se va a usar para reproducir los
    caminos y calcular las distancias.
    """

    def __init__(self, g, u, v, heuristic=None):
        """
        g es el grafo a trabajar, u es el nodo origen, v es el nodo destino
        """
        self.g, self.u, self.v = g, u, v
        self.heuristic = heuristic
        self.parents = {}
        self.search()

    def search(self):
        """ Este método deberá ser redefinido en subclases. """
        pass

    def visited(self, v):
        return v in self.parents

    def distance(self, v):
        return len(self.path_to(v))

    def path_to(self, v):
        """
        Devuelve la lista con el camino hasta el nodo pasado a partir del
        diccionario parents. Si el nodo no fue visitado, devuelve None.
        """
        if self.visited(v):
            path = [v]
            while path[-1] != self.u:
                path.append(self.parents[path[-1]])
            path.reverse()
            return path

