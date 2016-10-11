# -*- coding: utf-8 -*-

from path import CommonPath


class Heuristic(CommonPath):
    """
    Realiza una búsqueda con heurística.
    """

    def search(self):
        q = [self.u]

        while q:
            u = q.pop()
            nodes = [(self.heuristic(v, self.v), v) for v in self.g.adj(u)]
            sorted_nodes = sorted(nodes, key=lambda t: t[0], reverse=True)
            for t in sorted_nodes:
                v = t[1]
                if v not in self.parents:
                    self.parents[v] = u
                    q.append(v)
                if v == self.v:
                    return
