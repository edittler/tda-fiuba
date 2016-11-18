#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class tsp_data(object):

    def __init__(self, edge_weight_format, matrix, solution=[]):
        self.edge_weight_format = edge_weight_format
        self.matrix = matrix
        self.solution = solution

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        text = "EDGE_WEIGHT_FORMAT: " + self.edge_weight_format + "\n"
        for row in self.matrix:
            str_row = " ".join([str(i) for i in row]) + "\n"
            text += str_row
        return text

    def dimension(self):
        return len(self.matrix)

    def cost(self, from_city, to_city):
        if self.edge_weight_format == "LOWER_DIAG_ROW" and from_city < to_city:
            return self.matrix[to_city][from_city]
        return self.matrix[from_city][to_city]
