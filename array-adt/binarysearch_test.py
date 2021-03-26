#!/usr/bin/env python3

import unittest
from binarysearch import BinarySearch

class TestArraysBinarySearchRecursively(unittest.TestCase):
    def setUp(self):
        self.bs = BinarySearch()
    
    def test_value_is_first_middle_element(self):
        actual = self.bs.get_index_recursively([1, 2, 3], 2)
        self.assertEqual(actual, 1)
    
    def test_value_is_right_of_middle(self):
        actual = self.bs.get_index_recursively([1, 2, 3, 4, 5, 6], 5)
        self.assertEqual(actual, 4)

    def test_value_is_left_of_middle(self):
        actual = self.bs.get_index_recursively([1, 2, 3, 4, 5, 6], 2)
        self.assertEqual(actual, 1)

    def test_value_is_not_in_list(self):
        actual = self.bs.get_index_recursively([1, 2, 3, 4], 5)
        self.assertEqual(actual, -1)
    
    def test_value_is_only_element(self):
        actual = self.bs.get_index_recursively([1], 1)
        self.assertEqual(actual, 0)
    
    def test_list_is_empty(self):
        actual = self.bs.get_index_recursively([], 1)
        self.assertEqual(actual, -1)

class TestArraysBinarySearchIteratively(unittest.TestCase):
    def setUp(self):
        self.bs = BinarySearch()
    
    def test_value_is_only_element_in_list(self):
        actual = self.bs.get_index_iteratively([1], 1)
        self.assertEqual(actual, 0)
    
    def test_list_is_empty(self):
        actual = self.bs.get_index_iteratively([], 1)
        self.assertEqual(actual, -1)
    
    def test_value_not_in_list(self):
        actual = self.bs.get_index_iteratively([1, 2, 3], 4)
        self.assertEqual(actual, -1)
    
    def test_value_to_rightside(self):
        actual = self.bs.get_index_iteratively([1, 2, 3, 4, 5, 6], 5)
        self.assertEqual(actual, 4)
    
    def test_value_to_leftside(self):
        actual = self.bs.get_index_iteratively([1, 2, 3, 4, 5, 6], 2)
        self.assertEqual(actual, 1)