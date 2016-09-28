# -*- coding: utf-8 -*-

def order_and_select(l, k):
	"""
	Se ordena el conjunto dado y se devuelve el k-esimo valor
	"""
	# TODO: No ser ladri e implementar un algoritmo de ordenamiento (ahora es tarde)
	list.sort(l)
	return l[k]

def test_order_and_select():
	l = [5,2,9,7,1,90,123,8,3]
	assert order_and_select(l,3) == 5
	l = [5,2,9,7,1,90,123,8,3]
	assert order_and_select(l,0) == 1
	l = [5,2,9,7,1,90,123,8,3]
	assert order_and_select(l,len(l) - 1) == 123
