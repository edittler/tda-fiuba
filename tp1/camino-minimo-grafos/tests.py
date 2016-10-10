#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from graph import Graph
from bfs import BFS
from dijkstra import Dijkstra

class GraphTest(unittest.TestCase):

    def setUp(self):
        self.g = Graph(5)

    def test_add_edges_to_graph(self):
        self.g.add_edge(0, 1)
        self.g.add_edge(1, 2)
        self.g.add_edge(3, 4)
        self.assertEqual(self.g.E(), 3)
        self.assertListEqual(list(self.g.adj(0)), [1])
        self.assertListEqual(list(self.g.adj(1)), [2])
        self.assertListEqual(list(self.g.adj(3)), [4])
        self.assertListEqual(list(self.g.adj(2)), [])

    def test_add_multiple_edges(self):
        a1 = self.g.add_edge(0, 1)
        a2 = self.g.add_edge(0, 2)
        a3 = self.g.add_edge(0, 3)
        self.assertListEqual(list(self.g.adj(0)), [1, 2, 3])
        self.assertListEqual(list(self.g.adj_e(0)), [a1, a2, a3])

    def test_from_dict(self):
        g = Graph.from_dict({0: [1, 2], 1: [2], 2: [1]})
        self.assertListEqual(list(g.adj(0)), [1, 2])
        self.assertListEqual(list(g.adj(1)), [2])
        self.assertListEqual(list(g.adj(2)), [1])


class PathTest(object):

    path = None

    def test_path_to(self):
        g = Graph.from_dict({0: [1, 2], 1: [4], 2: [3], 3: [5], 4: [5, 6]})
        self.create_path(g, 0, 6)
        self.assertListEqual(self.path.path_to(1), [0, 1])
        self.assertListEqual(self.path.path_to(2), [0, 2])
        self.assertListEqual(self.path.path_to(3), [0, 2, 3])
        self.assertListEqual(self.path.path_to(4), [0, 1, 4])
        self.assertListEqual(self.path.path_to(5), [0, 2, 3, 5])

    def test_partial_path(self):
        g = Graph.from_dict({0: [1, 2], 1: [4], 2: [3], 3: [5], 4: [5, 6]})
        self.create_path(g, 0, 3)
        self.assertListEqual(self.path.path_to(1), [0, 1])
        self.assertListEqual(self.path.path_to(2), [0, 2])
        self.assertListEqual(self.path.path_to(3), [0, 2, 3])
        self.assertIsNone(self.path.path_to(4))
        self.assertIsNone(self.path.path_to(5))

class BFSTest(PathTest, unittest.TestCase):
    def create_path(self, g, u, v):
        self.path = BFS(g, u, v)

class DijkstraTest(PathTest, unittest.TestCase):
    def create_path(self, g, u, v):
        self.path = Dijkstra(g, u, v)

    def test_path_to_with_weigth(self):
        g = Graph.from_dict_with_weigth({0: [(1,5), (2,10)], 1: [(4,5)], 2: [(3,1)], 3: [(5,6)], 4: [(5,5), (6,10)], 5: [(6,2)]})
        self.create_path(g, 0, 6)
        self.assertListEqual(self.path.path_to(1), [0, 1])
        self.assertListEqual(self.path.path_to(2), [0, 2])
        self.assertListEqual(self.path.path_to(3), [0, 2, 3])
        self.assertListEqual(self.path.path_to(4), [0, 1, 4])
        self.assertListEqual(self.path.path_to(5), [0, 1, 4, 5])

    def test_partial_path_with_weigth(self):
        g = Graph.from_dict_with_weigth({0: [(1,5), (2,1)], 1: [(4,5)], 2: [(3,21)], 3: [(5,6)], 4: [(5,5), (6,10)], 5: [(3,1)]})
        self.create_path(g, 0, 3)
        self.assertListEqual(self.path.path_to(1), [0, 1])
        self.assertListEqual(self.path.path_to(2), [0, 2])
        self.assertListEqual(self.path.path_to(3), [0, 1, 4, 5, 3])

def main():
    # test_brute_force()
    return unittest.main()


if __name__ == '__main__':
    main()
