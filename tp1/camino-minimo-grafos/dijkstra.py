# -*- coding: utf-8 -*-

from path import CommonPath
import math
import heapq

class _PriorityQueueNode():
        def __init__(self, distance, node):
            self.distance = distance
            self.node = node
            self.removed = False

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
        priority_queue_node_finder = {}

        # Inicializo todos los vertices con distancia infinita
        for v in self.g:
            distance[v] = math.inf

        # Inicializo nodo origen y lo agrego a la PQ
        distance[self.u] = 0
        heapq.heappush(priority_queue, _PriorityQueueNode(distance[self.u], self.u))

        # Voy procesando tomando los vertices con menor distancia desde origen
        while priority_queue:
            u = heapq.heappop(priority_queue)

            # Corroboro que el nodo no fue eliminado anteriormente
            # (es mas facil chequear un tag que eliminar de la PQ)
            if not u.removed:

                # Condicion de corte -> Mi nodo actual es el destino
                if u.node == self.v:
                    return

                # Verifico todas las aristas salientes para computar distancias
                for edge in self.g.adj_e(u.node):
                    current_distance = u.distance + edge.weight
                    if (current_distance < distance[edge.dst]):
                        distance[edge.dst] = current_distance
                        self.parents[edge.dst] = u.node

                        try:
                            # Si consigo una menor distancia, "elimino" el nodo
                            # que representa este vertice de la PQ
                            to_remove_node = priority_queue_node_finder[edge.dst]
                            to_remove_node.removed = True
                        except KeyError:
                            # Es la primera vez que se inserta el nodo en la PQ
                            pass

                        # Actualizo la distancia minima hacia este vertice en la PQ
                        to_insert_node = _PriorityQueueNode(current_distance, edge.dst)
                        heapq.heappush(priority_queue, to_insert_node)
                        priority_queue_node_finder[edge.dst] = to_insert_node
