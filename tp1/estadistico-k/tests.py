#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import brute_force
import order_and_select
import k_selections
import k_heapsort
import heap_select
import quick_select

one = [5, 2, 9, 7, 1, 90, 123, 8, 3]


class CommonKminTest(object):
    module = None

    def setUp(self):
        super(CommonKminTest, self).setUp()
        self.elements = [5, 2, 9, 7, 1, 90, 123, 8, 3]

    def _call_algorithm(self, *args):
        # Esta es una forma rápida que encontré de llamar un algoritmo
        # dinámicamente.
        return self.module.__dict__['k_min'](*args)

    def test_k_is_zero(self):
        self.assertEqual(self._call_algorithm(self.elements, 0), 1)

    def test_k_is_3(self):
        self.assertEqual(self._call_algorithm(self.elements, 3), 5)

    def test_k_is_elements_length(self):
        self.assertEqual(self._call_algorithm(self.elements, len(self.elements) - 1), 123)

    def test_algorithm_does_not_change_the_list(self):
        elems = self.elements.copy()
        self._call_algorithm(self.elements, len(self.elements) - 1)
        self.assertListEqual(elems, self.elements)

    def test_algorithm_on_set_with_duplicated_elements(self):
        elems = [5, 2, 9, 7, 1, 2, 90, 123, 2, 8, 3]
        self.assertEqual(self._call_algorithm(elems, 1), 2)
        self.assertEqual(self._call_algorithm(elems, 2), 2)
        self.assertEqual(self._call_algorithm(elems, 3), 2)
        self.assertEqual(self._call_algorithm(elems, 4), 3)


class BruteForceTest(CommonKminTest, unittest.TestCase):
    module = brute_force


class OrderAndSelectTest(CommonKminTest, unittest.TestCase):
    module = order_and_select


class KSelectionsTest(CommonKminTest, unittest.TestCase):
    module = k_selections


class KHeapsortTest(CommonKminTest, unittest.TestCase):
    module = k_heapsort


class HeapSelectTest(CommonKminTest, unittest.TestCase):
    module = heap_select


class QuickSelectTest(CommonKminTest, unittest.TestCase):
    module = quick_select


def main(args):
	# test_brute_force()
	return unittest.main()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
