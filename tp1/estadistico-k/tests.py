#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

import brute_force
import order_and_select
import k_selections
import heap_select
import quick_select
import k_heapsort


one = [5, 2, 9, 7, 1, 90, 123, 8, 3]


def test_brute_force():
    l = copy.copy(one)
    assert brute_force.k_min(l, 3) == 5
    l = copy.copy(one)
    assert brute_force.k_min(l, 0) == 1
    l = copy.copy(one)
    assert brute_force.k_min(l, len(l) - 1) == 123


def test_order_and_select():
    l = copy.copy(one)
    assert order_and_select.k_min(l, 3) == 5
    l = copy.copy(one)
    assert order_and_select.k_min(l, 0) == 1
    l = copy.copy(one)
    assert order_and_select.k_min(l, len(l) - 1) == 123


def test_k_selections():
    l = copy.copy(one)
    assert k_selections.k_min(l, 3) == 5
    l = copy.copy(one)
    assert k_selections.k_min(l, 0) == 1
    l = copy.copy(one)
    assert k_selections.k_min(l, len(l) - 1) == 123


def test_k_heapsort():
    l = copy.copy(one)
    assert k_heapsort.k_min(l, 3) == 5
    l = copy.copy(one)
    assert k_heapsort.k_min(l, 0) == 1
    l = copy.copy(one)
    assert k_heapsort.k_min(l, len(l) - 1) == 123


def test_heap_select():
    l = copy.copy(one)
    assert heap_select.k_min(l, 3) == 5
    l = copy.copy(one)
    assert heap_select.k_min(l, 0) == 1
    l = copy.copy(one)
    assert heap_select.k_min(l, len(l) - 1) == 123


def test_quick_select():
	l = copy.copy(one)
	assert quick_select.k_min(l, 3) == 5
	l = copy.copy(one)
	assert quick_select.k_min(l, 0) == 1
	l = copy.copy(one)
	assert quick_select.k_min(l, len(l) - 1) == 123


def main(args):
	# test_brute_force()
	test_order_and_select()
	test_k_selections()
	test_heap_select()
	test_quick_select()
	return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
