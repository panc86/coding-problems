import unittest
from problems import largest_palindrome_product as func


class TestEvenFibonacci(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(func.solution() == 906609)
