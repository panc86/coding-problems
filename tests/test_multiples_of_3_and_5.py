import unittest
from problems import multiples_of_3_and_5


class TestStringMethods(unittest.TestCase):

    def test_result(self):
        self.assertTrue(multiples_of_3_and_5.solution(1000) == 233168)
