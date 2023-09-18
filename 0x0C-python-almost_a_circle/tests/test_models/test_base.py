#!/usr/bin/python3
import unittest
from models.base import Base
"""Test=Base"""


class test_Base(unittest.TestCase):
    """unittest"""

    def test_init(self):
        a = Base()
        self.assertEqual(a.id, 1)

        a1 = Base()
        self.assertEqual(a1.id, 2)

        a2 = Base(10)
        self.assertEqual(a2.id, 10)
