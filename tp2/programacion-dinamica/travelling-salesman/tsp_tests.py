#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from tsp_data import tsp_data
from tsp_parser import tsp_parser
from travelling_salesman_path import travelling_salesman_path


class TSPTest(unittest.TestCase):

    def test_4_cities(self):
        M = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
        sol = [1, 3, 4, 2, 1]
        data = tsp_data("FULL_MATRIX", M, sol)
        path = travelling_salesman_path(data)
        path = [(i + 1) for i in path[1]]
        self.assertEqual(data.solution, path)

    def test_4_cities_from_file(self):
        data = tsp_parser.parse_tsp_file("test_files/ex04.tsp")
        path = travelling_salesman_path(data)
        path = [(i + 1) for i in path[1]]
        self.assertEqual(data.solution, path)

    def test_15_cities(self):
        data = tsp_parser.parse_tsp_file("test_files/p01.tsp")
        path = travelling_salesman_path(data)
        path = [(i + 1) for i in path[1]]
        self.assertEqual(data.solution, path)


def main(args):
    return unittest.main()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
