\newpage

# Código

Aclaración: en este documento solo aparece el código que refleja las consignas
del trabajo práctico. En nuestro repositorio de código se pueden encontrar tests,
ejemplos, benchmarks de algoritmos y más:
[github.com/ezeperez26/tda-fiuba](https://github.com/ezeperez26/tda-fiuba)

## Algoritmos de aproximación

### El problema de la mochila

#### Función que setea el ambiente para llamar al algoritmo de aproximación

```python
def knapsack_bottom_up_aproximado(items_value, max_value, items_weight, knapsack_weight, 
precision_e):

    cant_items = len(items_value)

    # Seteo el factor 'b' y normalizo
    print("Precision: " + str(precision_e) + ". Cantidad Items: " + str(cant_items) + 
    ". Max Value: " + str(max_value))
    b = (precision_e / cant_items) * max_value
    print("b: " + str(b))
    rounded_items_value = [ ceil(value/b) for value in items_value ]
    rounded_max_value = ceil(max_value/b)

    # Inicializo mi matriz de resultados
    matrix_value_range = (rounded_max_value * cant_items)
    results = [[float("inf") for x in range(matrix_value_range + 1)] for y in range(cant_items + 1)]
    for i in range(0, cant_items):
        results[i][0] = 0

    # Corro el algoritmo en si, midiendo el tiempo
    knapsack_bottom_up_aproximado_core(rounded_items_value, matrix_value_range, 
                                        items_weight, knapsack_weight, results)

    return int(int(knapsack_get_optimum_value_aproximado(results, cant_items, 
                    matrix_value_range, knapsack_weight)) * b)
```

#### Implementación del algoritmo de aproximación

```python
def knapsack_bottom_up_aproximado_core(items_value, max_value, items_weight, 
knapsack_weight, results):

    value_sum = 0
    value_accum = 0
    for i in range(1, len(items_value) + 1):

        value_accum += items_value[i - 1]
        if i > 1:
            value_sum += items_value[i - 2]

        for v in range(1, value_accum + 1):

            if v > value_sum:
                results[i][v] = items_weight[i - 1] + 
                                results[i - 1][max(0, v - items_value[i - 1])]
            else:
                results[i][v] = min(results[i - 1][v], items_weight[i - 1] + 
                                results[i - 1][max(0, v - items_value[i - 1])])
```

#### Función que obtiene el valor óptimo aproximado de la matriz solución

```python
def knapsack_get_optimum_value_aproximado(results, cant_items, matrix_value_range, knapsack_weight):

    # Recorro la matriz viendo desde el mayor valor V posible
    # Si encuentro que se puede llegar con un W menor a la capacidad de la
    # mochila, ese es mi V optimo
    for v in range(matrix_value_range, 0, -1):

        for i in range(cant_items, -1, -1):

            if results[i][v] <= knapsack_weight:

                return v
```

### El problema del viajante de comercio

#### Función que calcula el camino y costo mínimo

```python
def travelling_salesman_aprox_path(graph):
    """
    Recibe el grafo sobre el cual se desea resolver problema del viajante de
    comercio.
    Retorna una lista con el orden de ciudades que minimiza el costo del viaje.
    """

    if not isinstance(graph, Graph):
        print("El parámetro no es de tipo Graph")
        return

    # Obtengo el árbol recubridor mínimo
    tree_graph = graph.minimum_spanning_tree()

    # Busca el camino óptimo
    path = []

    def dfs(start):
        path.append(start)
        for next in tree_graph.adj(start):
            if next not in path:
                dfs(next)
    dfs(0)

    # Calculo el costo del tour
    opt = 0
    current = -1
    for next in path:
        if current < 0:
            current = 0
            continue
        edge = graph.edge(current, next)
        opt += edge.weight
        current = next

    # Agrego el costo al origen
    opt += graph.edge(current, 0).weight
    path.append(0)

    return opt, list(path)
```

#### Método de la clase Graph que genera el árbol recubridor mínimo

```python
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

        # Algoritmo de Kruskal: ordena las aristas por peso y las agrega a la
        # estructura de conjuntos disjuntos hasta que no queden conjuntos disjuntos.
        edges = [e for e in self.iter_edges()]
        edges.sort(key=lambda e: e.weight)
        subtrees = UnionFind()
        tree = []
        for e in edges:
            if subtrees[e.src] != subtrees[e.dst]:
                tree.append(e)
                tree.append(Edge(e.dst, e.src, e.weight))
                subtrees.union(e.src, e.dst)

        tree_graph = Graph(self.V())

        for e in tree:
            tree_graph.add_edge(e.src, e.dst, e.weight)

        return tree_graph
```

#### Clase UnionFind

```python
class UnionFind(object):
    """Estructura de datos de Union-buscar"""

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
```

\newpage


# Referencias
