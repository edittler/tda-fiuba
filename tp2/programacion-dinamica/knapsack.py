#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from knapsack_file_parser import Parser

def knapsack_bottom_up(items_value, items_weight, knapsack_weight):

    # Inicializo mi matriz de resultados
    cant_items = len(items_value)
    results = [[0 for x in range(knapsack_weight + 1)] for y in range(cant_items + 1)]

    # Corro el algoritmo en si, midiendo el tiempo    
    start_time = time.time()
    knapsack_bottom_up_core(items_value, items_weight, knapsack_weight, results)
    total_time = time.time() - start_time
    print("Bottom Up: " + str(total_time))

    return results[cant_items][knapsack_weight]

def knapsack_bottom_up_core(items_value, items_weight, knapsack_weight, results):
    for i in range(1, len(items_value) + 1):
        for w in range(1, knapsack_weight + 1):

            if (w < items_weight[i - 1]):
                results[i][w] = results[i - 1][w]
            else:
                results[i][w] = max(results[i - 1][w], items_value[i - 1] + results[i - 1][w - items_weight[i - 1]])

def knapsack_top_down(items_value, items_weight, knapsack_weight):

    # Inicializo mis variables (se hacen globales para no pasarlas siempre en la recursividad)
    cant_items = len(items_value)
    global td_results
    td_results = [[None for x in range(knapsack_weight + 1)] for y in range(cant_items + 1)]
    global td_items_value
    td_items_value = items_value
    global td_items_weight
    td_items_weight = items_weight
    global td_knapsack_weight
    td_knapsack_weight = knapsack_weight

    # Corro el algoritmo top-down midiendo el tiempo
    start_time = time.time()
    knapsack_top_down_core(cant_items, knapsack_weight)
    total_time = time.time() - start_time
    print("Top Down: " + str(total_time))

    return td_results[cant_items][knapsack_weight]

def knapsack_top_down_core(cant_items, knapsack_weight):

    if ((cant_items <= 0) or (knapsack_weight <= 0)):
        return 0

    if (td_results[cant_items][knapsack_weight] is not None):
        return td_results[cant_items][knapsack_weight]
    elif (td_items_weight[cant_items - 1] > knapsack_weight):
        td_results[cant_items][knapsack_weight] = knapsack_top_down_core(cant_items - 1, knapsack_weight)
        return td_results[cant_items][knapsack_weight]
    else:
        td_results[cant_items][knapsack_weight] = max(knapsack_top_down_core(cant_items - 1, knapsack_weight), td_items_value[cant_items - 1] + knapsack_top_down_core(cant_items - 1, knapsack_weight - td_items_weight[cant_items - 1]))
        return td_results[cant_items][knapsack_weight]
