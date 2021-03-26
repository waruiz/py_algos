#!/usr/bin/env python3

import unittest
from sorted import Sorted

class TestSorted(unittest.TestCase):
    def setUp(self):
        self.sut = Sorted()
    
    def test_value_insert_in_sorted_position(self):
        actual = self.sut.insert([1, 3, 4, None], 2)
        self.assertEqual(actual, [1, 2, 3, 4])
    
    def test_big_value_insert_small_list(self):
        actual = self.sut.insert([0, None], 3)
        self.assertEqual(actual, [0, 3])
    
    def test_small_value_insert_small_list(self):
        actual = self.sut.insert([2, None], 0)
        self.assertEqual(actual, [0, 2])

    def test_sorted_list_returns_True(self):
        actual = self.sut.is_sorted([1, 3, 5, 8, 19])
        self.assertEqual(actual, True)

    def test_unsorted_list_returns_False(self):
        actual = self.sut.is_sorted([5, 2, 4, 2, 1])
        self.assertEqual(actual, False)