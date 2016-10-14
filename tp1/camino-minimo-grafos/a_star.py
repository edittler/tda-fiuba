# -*- coding: utf-8 -*-

from path import CommonPath
import math
from minPQ import MinPQ

class A_Star(CommonPath):
    """
    Realiza una búsqueda teniendo en cuenta tanto el peso de las aristas
    como la heurística.
    """

    # Función de evaluación. Será la prioridad para la frontera.
    def f(self, v):
        return self.distance[v] + self.heuristic(v, self.v)

    def search(self):
        # distancias a cada nodo.
        self.distance = {}
        self.visitado = {}
        frontera = MinPQ()

        # Inicializo todos los vertices con distancia infinita
        for v in self.g:
            self.distance[v] = math.inf
            self.visitado[v] = False;

        # Inicializo nodo origen y lo agrego a la PQ
        self.distance[self.u] = 0
        frontera.push(0, self.u)

        # Voy procesando tomando los vertices con menor distancia desde origen
        while not frontera.empty():
            (f, u) = frontera.pop()

            # Condicion de corte -> El nodo a visitar es el destino.
            if u == self.v:
                self._visited[self.v] = True
                return

            if not self.visited(u):
                self._visited[u] = True
                # Verifico todas las aristas salientes para computar distancias
                for edge in self.g.adj_e(u):
                    v = edge.dst
                    if not self.visited(v):
                        current_distance = self.distance[u] + edge.weight
                        if (current_distance < self.distance[v]):
                            self.distance[v] = current_distance
                            self.parents[v] = u
                            frontera.push(self.f(v), v)
