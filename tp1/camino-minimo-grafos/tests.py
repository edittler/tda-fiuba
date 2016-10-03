#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from graph import Graph


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


def main(args):
    # test_brute_force()
    return unittest.main()
