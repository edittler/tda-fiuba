# -*- coding: utf-8 -*-

from path import CommonPath
import math
import heapq

class _PriorityQueueNode():
        def __init__(self, distance, node):
            self.distance = distance
            self.node = node

        def __lt__(self, other):
            return self.distance <= other.distance

class Dijkstra(CommonPath):
    """
    Implementacion del algoritmo de Dijkstra para encontrar camino minimo
    usando priority queue
    """

    def search(self):

        distance = {}
        priority_queue = []

        # Inicializo todos los vertices con distancia infinita
        for v in self.g:
            distance[v] = math.inf

        # Inicializo nodo origen y lo agrego a la PQ
        distance[self.u] = 0
        heapq.heappush(priority_queue, _PriorityQueueNode(distance[self.u], self.u))

        # Voy procesando tomando los vertices con menor distancia desde origen
        while priority_queue:
            u = heapq.heappop(priority_queue)

            # Corroboro que el nodo no haya sido visitado
            # (Puede que se haya insertado dos veces en la PQ por haber
            # encontrado otro camino minimo que el primero encontrado)
            if u.node not in self._visited:

                # Condicion de corte -> Mi nodo actual es el destino
                if u.node == self.v:
                    self._visited.add(u.node)
                    return

                # Verifico todas las aristas salientes para computar distancias
                for edge in self.g.adj_e(u.node):
                    current_distance = u.distance + edge.weight
                    if (current_distance < distance[edge.dst]):
                        distance[edge.dst] = current_distance
                        self.parents[edge.dst] = u.node

                        # Actualizo la distancia minima hacia este vertice en la PQ
                        to_insert_node = _PriorityQueueNode(current_distance, edge.dst)
                        heapq.heappush(priority_queue, to_insert_node)

                self._visited.add(u.node)
