import unittest
from problems import multiples_of_3_and_5 as func


class TestMultiplesOf3And5(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(func.solution(1000) == 233168)
