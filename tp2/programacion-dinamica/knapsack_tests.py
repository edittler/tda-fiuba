#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from knapsack_file_parser import Parser
from knapsack import knapsack_bottom_up, knapsack_top_down

class KnapsackTest(unittest.TestCase):

    # Se realizan los tests con el archivo basico para probar correctitud
    # que se encuentra en ./test_files/small_coef/knapPI_1_50_1000.csv

    def setUp(self):
        self.problems = Parser.parse_file('test_files/small_coef/knapPI_1_50_1000.csv')
        
    def test_knapsack_bottom_up(self):
        for problem in self.problems:
            print(str(problem.id) + ") ", end = "", flush = True)
            bu_optimum_value = knapsack_bottom_up(problem.values, problem.weights, problem.knapsack_weight)
            self.assertEqual(bu_optimum_value, problem.value_found)

    def test_knapsack_top_down(self):
        for problem in self.problems:
            print(str(problem.id) + ") ", end = "", flush = True)
            td_optimum_value = knapsack_top_down(problem.values, problem.weights, problem.knapsack_weight)
            self.assertEqual(td_optimum_value, problem.value_found)

def main():
    return unittest.main()

if __name__ == '__main__':
    main()
