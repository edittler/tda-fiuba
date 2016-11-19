# -*- coding: utf-8 -*-

from graph import Graph


class FlowEdge(object):

    def __init__(self, src, dst, capacity=0, is_backwards=False):
        self.src = src
        self.dst = dst
        self.capacity = capacity
        self.is_backwards = is_backwards
        self.reciproca = None

class Flow(Graph):

    def add_edge(g, u, v, capacity=0):
        """
        Añade una arista  y su equivalente residual al flujo.
        Devuelve la arista agregada.
        """
        e = FlowEdge(u, v, capacity)
        r = FlowEdge(v, u, is_backwards=True)
        e.reciproca = r
        r.reciproca = e

        g._i[u].append(e)
        g._i[v].append(r)

        g._a[u].append(v)
        return e

    def e_transitable(g, e, flow):
        return (e.is_backwards and e.capacity > 0) or ((not e.is_backwards) and flow[e] < e.capacity)

    # Búsqueda de Camino por DFS
    def flow_path(g, source, target, flow):
        visited = set([source])
        parents = {}

        if g._flow_path_rec(source, target, flow, visited, parents):
            path = []
            v = target
            while(v != source):
                path.append(parents[v])
                v = parents[v].src
                path.reverse()
            return path
        else:
            return None

    def _flow_path_rec(g, source, target, flow, visited, parents):
        if source == target:
            return True
        for edge in g.adj_e(source):
            if g.e_transitable(edge, flow) and not edge.dst in visited:
                visited.add(edge.dst)
                parents[edge.dst] = edge
                if g._flow_path_rec(edge.dst, target, flow, visited, parents):
                    return True
        return False

    def bottleneck(g, path, flow):
        return min((e.capacity - flow[e]) for e in path)

    def get_empty_flow(g):
        return {e: 0 for e in g.iter_edges()}

    def get_max_flow(g, source, target):
        flow = g.get_empty_flow()
        path = g.flow_path(source, target, flow)

        while path != None:
            b = g.bottleneck(path, flow)
            for edge in path:
                if edge.is_backwards:
                    edge.capacity -= b
                else:
                    edge.reciproca.capacity += b
                    flow[edge] += b
            path = g.flow_path(source, target, flow)

        return flow

    # Reachable from s.
    def get_min_cut(g, source, flow):
        visited = set([source])
        g.visit(source, flow, visited)
        return visited

    def visit(g, src, flow, visited):
        visited.add(src)
        for e in g.adj_e(src):
            if g.e_transitable(e, flow) and not e.dst in visited:
                visited.add(e.dst)
                g.visit(e.dst, flow, visited)

    def repr_max_flow(g, source, target):
        flow = g.get_max_flow(source, target)
        edges = sorted(flow.keys(), key=lambda x: (x.src, x.dst))
        res = ''
        for e in edges:
            if not e.is_backwards:
                res += str(e.src) + ' -> ' + str(e.dst) + ': ' + str(flow[e]) + '\n'
        return res
