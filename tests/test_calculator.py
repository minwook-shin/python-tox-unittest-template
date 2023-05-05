"""Docstring."""
import unittest

from src import Calculator


class TestCalculator(unittest.TestCase):
    """Tests Calculator class"""

    def test_add(self):
        """Tests run add"""
        main = Calculator()
        self.assertEqual(main.add(1, 1), 2)

    def test_sub(self):
        """Tests run sub"""
        main = Calculator()
        self.assertEqual(main.sub(1, 1), 0)
