# -*- coding: utf-8 -*-

from graph import Graph


class FlowEdge(object):

    def __init__(self, src, dst, capacity=0, is_residual=False):
        self.src = src
        self.dst = dst
        self.capacity = capacity
        self.is_residual = is_residual


class Flow(Graph):

    def add_edge(g, u, v, capacity=0):
        """
        Añade una arista  y su equivalente residual al flujo.
        Devuelve la arista agregada.
        """
        e = FlowEdge(u, v, capacity)
        r = FlowEdge(v, u, is_residual=True)
        g._i[u].append(e)
        g._a[u].append(v)
        g._i[v].append(r)
        return e

    def flow_path(g, source, target, flow):
        return g._flow_path_rec(source, target, flow, [])

    def _flow_path_rec(g, source, target, flow, path):
        if source == target:
            return path
        for edge in g.adj_e(source):
            residual = edge.capacity - flow[edge]
            if not edge.is_residual and residual > 0:
                path.append(edge)
                result = g._flow_path_rec(edge.dst, target, flow, path)
                if result is not None:
                    return result

    def bottleneck(g, path, flow):
        return min((e.capacity - flow[e]) for e in path)

    def get_empty_flow(g):
        return {e: 0 for e in g.iter_edges()}

    def get_max_flow(g, source, target):
        """ """
        flow = g.get_empty_flow()

        while True:
            path = g.flow_path(source, target, flow)
            if path is None:
                return flow

            b = g.bottleneck(path, flow)

            for edge in path:
                flow[edge] -= b if edge.is_residual else -b

    def repr_max_flow(g, source, target):
        flow = g.get_max_flow(source, target)
        edges = sorted(flow.keys(), key=lambda x: (x.src, x.dst))
        res = ''
        for e in edges:
            if not e.is_residual:
                res += str(e.src) + ' -> ' + str(e.dst) + ': ' + str(flow[e]) + '\n'
        return res
