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
        return distance[v] + heuristic(v, self.v)

    def search(self):
        # distancias a cada nodo.
        distance = {}
        frontera = MinPQ()

        # Inicializo todos los vertices con distancia infinita
        for v in self.g:
            distance[v] = math.inf

        # Inicializo nodo origen y lo agrego a la PQ
        distance[self.u] = 0
        frontera.push(0, self.u)

        # Voy procesando tomando los vertices con menor distancia desde origen
        while priority_queue:
            (f, u) = frontera.pop()

            # Condicion de corte -> El nodo a visitar es el destino.
            if u == self.v:
                return

            if not visited(u):
                # Verifico todas las aristas salientes para computar distancias
                for edge in self.g.adj_e(u):
                    v = edge.dst
                    current_distance = distance[u] + edge.weight
                    if (current_distance < distance[v]):
                        distance[v] = current_distance
                        self.parents[v] = u
                        if not visited(v):
                            frontera.push(f(v), v)
