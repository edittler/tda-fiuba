#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ProblemContainer(object):

    def __init__(self, name, cant_items, knapsack_weight, value_found, time, items_value, items_weight, items_included):
        self.name = name
        self.cant_items = cant_items
        self.knapsack_weight = knapsack_weight
        self.value_found = value_found
        self.time = time
        self.values = items_value
        self.weights = items_weight
        self.items_included = items_included
