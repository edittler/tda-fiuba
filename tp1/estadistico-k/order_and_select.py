#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def k_min(elements, k):
    return order_and_select(elements.copy(), k)


def order_and_select(l, k):
	"""
	Se ordena el conjunto dado y se devuelve el k-esimo valor
	"""

	list.sort(l)
	return l[k]
