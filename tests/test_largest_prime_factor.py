import unittest
from problems import largest_prime_factor


class TestStringMethods(unittest.TestCase):

    def test_result(self):
        self.assertTrue(largest_prime_factor.solution(600851475143) == 6857)
