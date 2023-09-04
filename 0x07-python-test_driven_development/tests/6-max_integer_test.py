#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
class test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_integer([1, 3, 5, 10]), 10)
        self.assertEqual(max_integer([1, 3, 20, 10]), 20)
        self.assertEqual(max_integer([1, 30, 5, 10]), 30)
        self.assertEqual(max_integer([40, 3, 5, 10]), 40)
        self.assertEqual(max_integer([1, 50, 60, 10]), 60)