import unittest
from problems import even_fibonacci as func


class TestEvenFibonacci(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(func.solution() == 4613732)
