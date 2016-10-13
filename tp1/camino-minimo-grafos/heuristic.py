# -*- coding: utf-8 -*-

import heapq
from path import CommonPath


class Heuristic(CommonPath):
    """
    Realiza una búsqueda con heurística.
    """

    def search(self):
        queue = []
        heapq.heappush(queue, (0, self.u))

        while queue:
            u = heapq.heappop(queue)[1]
            nodes = [(self.heuristic(v, self.v), v) for v in self.g.adj(u)]
            for tuple in nodes:
                v = tuple[1]
                if v not in self.parents:
                    self.parents[v] = u
                    heapq.heappush(queue, tuple)
                if v == self.v:
                    return
