# -*- coding: utf-8 -*-


class Graph(object):
    """Grafo no dirigido con un número fijo de vértices.

    Los vértices son siempre números enteros no negativos. El primer vértice
    es 0.

    El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
    creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
    nuevas aristas.
    """

    def __init__(self, V):
        """ Construye un grafo sin aristas de V vértices. """
        self._a = [[] for _ in range(V)]  # _a es la matriz de adyacencias
        self._i = [[] for _ in range(V)]  # _i es la matriz de incidencias

    def V(self):
        """ Número de vértices en el grafo. """
        return len(self._a)

    def E(self):
        """ Número de aristas en el grafo. """
        return sum(len(x) for x in self._i)

    def adj_e(self, v):
        """ Itera sobre los aristas incidentes desde v. """
        return iter(self._i[v])

    def adj(self, v):
        """ Itera sobre los vértices adyacentes a v. """
        return iter(self._a[v])

    def add_edge(self, u, v, weight=0):
        """ Añade una arista al grafo. Devuelve la arista agregada """
        a = Edge(u, v, weight)
        self._i[u].append(a)
        self._a[u].append(v)
        return a

    def __iter__(self):
        """Itera de 0 a V."""
        return iter(range(self.V()))

    def iter_edges(self):
        """Itera sobre todas las aristas del grafo.

        Las aristas devueltas tienen los siguientes atributos de solo lectura:
            - e.src
            - e.dst
            - e.weight
        """
        return iter(edge for edges in self._a for edge in edges)

    def has_node(self, v):
        return v < len(self._a)

    @classmethod
    def from_dict(cls, d):
        """ Toma un diccionario, compuesto de la siguiente manera:
            {
                nodo: [nodo_adjacente, nodo_adjacente2],
                nodo2: [...]
            }
            Por ejemplo:
            {
                1: [2, 3, 4, 5]
                2: [3],
                4: [5]
            }

            El listado de nodos adyacentes tambien puede ser una tupla, donde
            el primer elemento es el nodo y el segundo es el peso de la arista.
        """
        max_ady = max(v[0] if isinstance(v, tuple) else v
                      for values in d.values() for v in values)
        max_node = max(max(d.keys()), max_ady)
        g = cls(max_node + 1)
        for src, v in d.items():
            for dst in v:
                weight = 1
                if isinstance(dst, tuple):
                    weight = dst[1]
                    dst = dst[0]
                if g.has_node(dst):
                    g.add_edge(src, dst, weight)
        return g

    @classmethod
    def from_dict_with_weigth(cls, d):
        """ Toma un diccionario, compuesto de la siguiente manera:
            {
                nodo: [(nodo_adjacente, peso), (nodo_adjacente2, peso)],
                nodo2: [...]
            }
            Por ejemplo:
            {
                1: [(2,5), (3,2), (4,1), (5,19)]
                2: [(3,20)],
                4: [(5,100)]
            }
        """
        max_node = max(max(d.keys()), max(v[0] for values in d.values() for v in values))
        g = cls(max_node + 1)
        for src, v in d.items():
            for dst in v:
                if g.has_node(dst[0]):
                    g.add_edge(src, dst[0], dst[1])
        return g


class Edge(object):
    """ Arista de un grafo. """

    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight
