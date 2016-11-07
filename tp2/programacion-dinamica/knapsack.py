#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def knapsack_bottom_up(items_value, items_weight, knapsack_weight):
    # Inicializo mi matriz de resultados
    cant_items = len(items_value)
    results = [[0 for x in range(knapsack_weight + 1)] for y in range(cant_items + 1)]
    print(str(results))
    knapsack(items_value, items_weight, knapsack_weight, results)
    print(str(results))
    return results[cant_items][knapsack_weight]

def knapsack(items_value, items_weight, knapsack_weight, results):
    for i in range(1, len(items_value) + 1):
        for w in range(1, knapsack_weight + 1):

            if (w < items_weight[i - 1]):
                results[i][w] = results[i - 1][w]
            else:
                results[i][w] = max(results[i - 1][w], items_value[i - 1] + results[i - 1][w - items_weight[i - 1]])

if __name__ == "__main__":
    # Testeo del algoritmo
    values = [1, 1, 1]
    weights = [2, 2, 3]
    optimum_value = knapsack_bottom_up(values, weights, 6)
    print(str(optimum_value))
