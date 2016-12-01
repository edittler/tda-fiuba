#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from math import ceil

from knapsack_file_parser import Parser

def knapsack_bottom_up_aproximado(items_value, max_value, items_weight, knapsack_weight, precision_e):

    cant_items = len(items_value)

    # Seteo el factor 'b' y normalizo
    print("Precision: " + str(precision_e) + ". Cantidad Items: " + str(cant_items) + ". Max Value: " + str(max_value))
    b = (precision_e / cant_items) * max_value
    print("b: " + str(b))
    rounded_items_value = [ ceil(value/b) for value in items_value ]
    rounded_max_value = ceil(max_value/b)

    # Inicializo mi matriz de resultados
    matrix_value_range = (rounded_max_value * cant_items)
    results = [[float("inf") for x in range(matrix_value_range + 1)] for y in range(cant_items + 1)]
    for i in range(0, cant_items):
        results[i][0] = 0

    # Corro el algoritmo en si, midiendo el tiempo
    knapsack_bottom_up_aproximado_core(rounded_items_value, matrix_value_range, items_weight, knapsack_weight, results)

    #return KnapsackSolution(results[cant_items][knapsack_weight], knapsack_get_solution(cant_items, knapsack_weight, items_value, items_weight, results))
    return int(int(knapsack_get_optimum_value_aproximado(results, cant_items, matrix_value_range, knapsack_weight)) * b)

def knapsack_bottom_up_aproximado_core(items_value, max_value, items_weight, knapsack_weight, results):

    value_sum = 0
    value_accum = 0
    for i in range(1, len(items_value) + 1):

        value_accum += items_value[i - 1]
        if i > 1:
            value_sum += items_value[i - 2]

        for v in range(1, value_accum + 1):

            #if (items_weight[i - 1] > knapsack_weight or v > value_sum):
            if v > value_sum:
                results[i][v] = items_weight[i - 1] + results[i - 1][max(0, v - items_value[i - 1])]
            else:
                results[i][v] = min(results[i - 1][v], items_weight[i - 1] + results[i - 1][max(0, v - items_value[i - 1])])

def knapsack_get_optimum_value_aproximado(results, cant_items, matrix_value_range, knapsack_weight):

    # Recorro la matriz viendo desde el mayor valor V posible
    # Si encuentro que se puede llegar con un W menor a la capacidad de la
    # mochila, ese es mi V optimo
    for v in range(matrix_value_range, 0, -1):

        for i in range(cant_items, -1, -1):

            if results[i][v] <= knapsack_weight:

                return v
