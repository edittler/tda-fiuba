#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ProblemContainer(object):

    def __init__(self, identificator, name, cant_items, knapsack_weight, value_found, time, items_value, max_value, items_weight, items_included):
        self.id = identificator
        self.name = name
        self.cant_items = cant_items
        self.knapsack_weight = knapsack_weight
        self.value_found = value_found
        self.time = time
        self.values = items_value
        self.max_value = max_value
        self.weights = items_weight
        self.solution_items = []
        for i in range(1, cant_items + 1):
            if items_included[i - 1]:
                self.solution_items.append(i)

    def __lt__(self, other):
        # Ordeno por peso
        return self.knapsack_weight < other.knapsack_weight
