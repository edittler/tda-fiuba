#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from problem_container import ProblemContainer

class Parser(object):

    #def __init__(self, filename):

    @classmethod
    def parse_file(cls, filename):

        parsed_problems = []

        with open(filename, "r+") as file_handler:

            while True:

                # Primer linea: Nombre del archivo
                name = file_handler.readline()
                if not name:
                    # Llegue al final del archivo
                    return parsed_problems
                print("El nombre de la instancia es " + name)

                # Segunda linea: Cantidad de items
                cant_items = int(file_handler.readline().rstrip().split(' ')[1])
                values = [0 for x in range(cant_items)]
                weights = [0 for x in range(cant_items)]
                included = [0 for x in range(cant_items)]

                # Tercera linea: Capacidad de la mochila
                knapsack_weight = int(file_handler.readline().rstrip().split(' ')[1])

                # Cuarta linea: Solucion optima encontrada por el autor del ejemplo
                value_found = int(file_handler.readline().rstrip().split(' ')[1])

                # Quinta fila: Tiempo que tardo el autor del ejemplo en encontrar solucion
                time = file_handler.readline()

                # Desde aquí, cant_items lineas con la descripcion de cada item (Formato CSV)
                i = 0
                for line in file_handler:

                    # El ejemplo termina con estos guiones
                    if "-----" in line:
                        break

                    separated_line = line.split(',')
                    # Primer campo: Numero de item

                    # Segundo campo: Valor del item
                    values[i] = int(separated_line[1])

                    # Tercer campo: Peso del item                
                    weights[i] = int(separated_line[2])

                    # Cuarto campo: Si pertenece a solucion optima
                    included[i] = int(separated_line[3])
                    i += 1

                parsed_problems.append(ProblemContainer(name, cant_items, knapsack_weight, value_found, time, values, weights, included))

                blank_line = file_handler.readline()
                if not blank_line:
                    # Llegue al final del archivo
                    return parsed_problems
