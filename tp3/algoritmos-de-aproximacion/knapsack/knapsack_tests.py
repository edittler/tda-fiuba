#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from knapsack_file_parser import Parser
from knapsack import knapsack_bottom_up_aproximado, knapsack_top_down

class KnapsackTest(unittest.TestCase):

    # Se realizan los tests con el archivo basico para probar correctitud
    # que se encuentra en ./test_files/small_coef/knapPI_1_50_1000.csv

    def setUp(self):
        self.problems = Parser.parse_file('test_files/small_coef/knapPI_1_50_1000.csv')
        
    def test_knapsack_bottom_up(self):
        for problem in self.problems:
            print(str(problem.id) + ")")
            knapsack_solution = knapsack_bottom_up_aproximado(problem.values, problem.max_value, problem.weights, problem.knapsack_weight, 0.1)
            print("Mi solucion: " + str(knapsack_solution) + " VS Solucion Optima: " + str(problem.value_found))

    #def test_knapsack_top_down(self):
    #    return
    #    for problem in self.problems:
    #        print(str(problem.id) + ")")
    #        td_optimum_value = knapsack_top_down(problem.values, problem.weights, problem.knapsack_weight)
    #        self.assertEqual(td_optimum_value, problem.value_found)

def main():
    return unittest.main()

if __name__ == '__main__':
    main()
