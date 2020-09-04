import unittest
from problems import even_fibonacci


class TestStringMethods(unittest.TestCase):

    def test_result(self):
        self.assertTrue(even_fibonacci.solution() == 4613732)
