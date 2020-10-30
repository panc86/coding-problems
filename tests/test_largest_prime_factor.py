import unittest
from problems import largest_prime_factor as func


class TestLargestPrimeFactor(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(func.solution(600851475143) == 6857)
