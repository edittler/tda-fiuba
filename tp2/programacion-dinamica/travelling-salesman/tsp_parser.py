#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tsp_data import tsp_data


class tsp_parser(object):

    @classmethod
    def parse_tsp_file(cls, filename):
        edge_weight_format = "FULL_MATRIX"
        edge_weight_section = False
        matrix_strings = []
        matrix = []

        file = open(filename, 'r')
        for line in file:
            key_value = line.split(':')

            if len(key_value) == 2:
                key = key_value[0]
                if key.strip() == "EDGE_WEIGHT_FORMAT":
                    edge_weight_format = key_value[1].strip()

            if len(key_value) == 1:
                key = key_value[0].strip()
                if key == "EDGE_WEIGHT_SECTION":
                    edge_weight_section = True
                    continue
                if key == "TOUR_SECTION" or key == "EOF":
                    edge_weight_section = False
                    continue

            if edge_weight_section:
                matrix_strings.append(line)
                continue

        if edge_weight_format == "FULL_MATRIX":
            for line in matrix_strings:
                values = line.strip().split(' ')
                row = [int(float(i)) for i in values if i != '']
                matrix.append(row)

        if edge_weight_format == "LOWER_DIAG_ROW":
            row = []
            for line in matrix_strings:
                value = int(float(line.strip()))
                row.append(value)
                if value == 0:
                    matrix.append(row)
                    row = []

        return tsp_data(edge_weight_format, matrix)

    @classmethod
    def parse_matrix_file(cls, filename):
        edge_weight_format = "FULL_MATRIX"
        matrix = []

        file = open(filename, 'r')
        for line in file:
            values = line.strip().split(' ')
            row = [int(float(i)) for i in values if i != '']
            matrix.append(row)

        return tsp_data(edge_weight_format, matrix)
