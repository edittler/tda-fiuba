# -*- coding: utf-8 -*-


class Graph(object):
    """Grafo no dirigido con un número fijo de vértices.

    Los vértices son siempre números enteros no negativos. El primer vértice
    es 0.

    El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
    creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
    nuevas aristas.
    """

    def __init__(g, V):
        """ Construye un grafo sin aristas de V vértices. """
        g._a = [[] for _ in range(V)]  # _a es la matriz de adyacencias
        g._i = [[] for _ in range(V)]  # _i es la matriz de incidencias

    def V(g):
        """ Número de vértices en el grafo. """
        return len(g._a)

    def E(g):
        """ Número de aristas en el grafo. """
        return sum(len(x) for x in g._i)

    def adj_e(g, v):
        """ Itera sobre los aristas incidentes desde v. """
        return iter(g._i[v])

    def adj(g, v):
        """ Itera sobre los vértices adyacentes a v. """
        return iter(g._a[v])

    def add_edge(g, u, v, weight=0):
        """ Añade una arista al grafo. Devuelve la arista agregada """
        a = Edge(u, v, weight)
        g._i[u].append(a)
        g._a[u].append(v)
        return a

    def __iter__(g):
        """Itera de 0 a V."""
        return iter(range(g.V()))

    def iter_edges(g):
        """Itera sobre todas las aristas del grafo.

        Las aristas devueltas tienen los siguientes atributos de solo lectura:
            - e.src
            - e.dst
            - e.weight
        """
        return iter(edge for edges in g._i for edge in edges)

    def has_node(g, v):
        return v < len(g._a)

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

    def copy(g):
        g_copy = Graph(len(g._a))
        g_copy._a = g._a.copy()
        g_copy._i = g._i.copy()
        return g_copy


class Edge(object):
    """ Arista de un grafo. """

    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight
