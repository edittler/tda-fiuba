#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor
import random

def k_min(elements, k):
    #return quick_select_algorithm(elements.copy(), k, 0, len(elements) - 1)
    return quick_select_algorithm_recursive(elements.copy(), k, 0, len(elements) - 1)

def quick_select_algorithm(l, k, first_index, last_index):
    """
    Mismo 'paradigma' que quicksort. Se elige pivote, se ordena el pivote
    y se chequea numero de indice. Dependiendo del mismo (y de k) se elige
    que lado procesar
    """

    # Funcion auxiliar que me ordena el pivote en la lista
    def order_pivot(l, first_index, last_index, pivot_index):
        pivot_value = l[pivot_index]
        l[pivot_index], l[last_index] = l[last_index], l[pivot_index]
        final_pivot_index = first_index

        for index in range(first_index, last_index):
            if l[index] < pivot_value:
                l[index], l[final_pivot_index] = l[final_pivot_index], l[index]
                final_pivot_index += 1

        l[last_index], l[final_pivot_index] = l[final_pivot_index], l[last_index]

        return final_pivot_index


    #for index in range(first_index, last_index):
    while(True):
        if first_index == last_index:
            return l[first_index]

        # Elijo el pivote arbitrariamente y opero
        pivot_index = floor((first_index + last_index) / 2)
        pivot_index = order_pivot(l, first_index, last_index, pivot_index)

        if k == pivot_index:
            return l[k]
        elif k < pivot_index:
            last_index = pivot_index - 1
        else:
            first_index = pivot_index + 1

def quick_select_algorithm_recursive(l, k, first_index, last_index):

    def partition(l, p, r):
        x = l[r]
        f = p - 1
        for j in range(p,r):
            if l[j] < x:
                f += 1
                l[f], l[j] = l[j], l[f]
        f += 1
        l[f], l[r] = l[r], l[f]
        return f
       
    def random_partition(l, p, r):
        h = random.randrange(p, r)
        l[r], l[h] = l[h], l[r]
        return partition(l, p, r)
        
    if first_index == last_index:
        return l[first_index]

    q = random_partition(l, first_index, last_index)

    i = q - first_index 

    if k == i:
        return l[q]
    elif k < i:
        return quick_select_algorithm_recursive(l, k, first_index, q - 1)
    else:
        return quick_select_algorithm_recursive(l, k - i, q + 1, last_index)
