#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from max_flow import Flow


class FlowPathTest(unittest.TestCase):

    def test_flow_path_returns_correct_path_for_initial_flow(self):
        g = Flow(4)
        g.add_edge(0, 1, 10)
        g.add_edge(1, 2, 0)
        g.add_edge(1, 3, 10)

        f = g.get_empty_flow()
        self.assertEqual([e.dst for e in g.flow_path(0, 3, f)], [1, 3])
        self.assertIsNone(g.flow_path(0, 2, f))


class MaxFlow(unittest.TestCase):

    def test_simple_max_flow(self):
        f = Flow(3)
        f.add_edge(0, 1, 10)
        f.add_edge(1, 2, 20)

        flow = f.get_max_flow(0, 2)
        self.assertEqual(max(flow.values()), 10)


def main():
    return unittest.main()


if __name__ == '__main__':
    main()
