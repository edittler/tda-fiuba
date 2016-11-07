#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Parser(object):

    def __init__(self, filename):
        self.filename = filename

    def parse_first_example(self):

        with open(self.filename) as file_handler:
            filename = file_handler.readline()
            #print(str(file_handler.readline().rstrip()))
            cant_items = int(file_handler.readline().rstrip().split(' ')[1])
            self.values = [0 for x in range(cant_items)]
            self.weights = [0 for x in range(cant_items)]
            self.included = [0 for x in range(cant_items)]
            self.knapsack_weight = int(file_handler.readline().rstrip().split(' ')[1])
            self.value_found = int(file_handler.readline().rstrip().split(' ')[1])
            time = file_handler.readline()

            i = 0
            for line in file_handler:

                if "-----" in line:
                    break

                separated_line = line.split(',')
                self.values[i] = int(separated_line[1])
                self.weights[i] = int(separated_line[2])
                self.included[i] = int(separated_line[3])
                i += 1
