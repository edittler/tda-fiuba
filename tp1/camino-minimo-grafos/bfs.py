# -*- coding: utf-8 -*-

from path import CommonPath


class BFS(CommonPath):
    """
    Realiza una búsqueda BFS, cortando al encontrar el nodo destino.
    """

    def search(self):
        q = [self.u]

        while q:
            u = q.pop()
            for v in self.g.adj(u):
                if v not in self.parents:
                    self.parents[v] = u
                    q.append(v)
                if v == self.v:
                    return
