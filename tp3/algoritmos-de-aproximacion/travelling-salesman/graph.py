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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        def edge_text(e):
            return "(" + str(e.dst) + ", " + str(e.weight) + ")"

        text = ""
        for v in self:
            text += str(v) + " -> "
            adj_str = ", ".join([edge_text(e) for e in self.adj_e(v)]) + "\n"
            text += adj_str
        return text

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

    def edge(self, u, v):
        """Retorna la arista que se dirije desde u a v."""
        for e in self._i[u]:
            if e.dst == v:
                return e
        return None

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
        return iter(edge for edges in self._i for edge in edges)

    def has_node(self, v):
        return v < len(self._a)

    def is_undirected(self):
        """Comprueba si el gráfico es simple no dirigido."""
        for v in self:
            if v in self._a[v]:
                return False
            for w in self.adj(v):
                if v not in self._a[w]:
                    return False
        return True

    def minimum_spanning_tree(self):
        """
        Retorna el árbol recubridod mínimo del grafo no dirigido G.
        El árbol retornado es una lista de aristas.
        """
        if not self.is_undirected():
            raise ValueError("MinimumSpanningTree: input is not undirected")
        for u in self:
            for v in self.adj(u):
                if self.edge(u, v).weight != self.edge(v, u).weight:
                    raise ValueError("MinimumSpanningTree: asymmetric weights")

        # Kruskal's algorithm: sort edges by weight, and add them one at a time.
        # We use Kruskal's algorithm, first because it is very simple to
        # implement once UnionFind exists, and second, because the only slow
        # part (the sort) is sped up by being built in to Python.
        edges = [e for e in self.iter_edges()]
        edges.sort(key=lambda e: e.weight)
        subtrees = UnionFind()
        tree = []
        for e in edges:
            if subtrees[e.src] != subtrees[e.dst]:
                tree.append(e)
                subtrees.union(e.src, e.dst)
                print(subtrees.parents)
        return tree

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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        text = "(src: " + str(self.src)
        text += ", dst: " + str(self.dst)
        text += ", weight: " + str(self.weight) + ")"
        return text


class UnionFind(object):
    """Estructura de datos de Union-buscar

    Cada instancia X mantiene una familia de conjuntos disjuntos de objetos,
    soportando los siguientes métodos siguientes:

    - X[item] devuelve un nombre del conjunto que contiene el elemento dado.
      Si el elemento aún no forma parte de un conjunto en X, se crea un nuevo
      conjunto de singleton para él.

    - X.union(item1, item2, ...) junta los conjuntos que contienen cada elemento
      en un solo conjunto más grande. Si algún elemento aún no forma parte de
      un conjunto en X, se agrega a X como uno de los miembros del conjunto
      combinado.
    """

    def __init__(self):
        """Crea una estructura vacía de Union-buscar."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Busca y retorna el nombte del conjunto que contiene el objeto."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        """Iterar a través de todos los items encontrados por la estructura."""
        return iter(self.parents)

    def union(self, *objects):
        """Encuentra los conjuntos que contienen los objetos y une."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest
