import unittest
from problems import min_window_substring as func


class TestMinWindowSubstring(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(func.solution("aaffhkksemckelloe", "fhea") == "affhkkse")
        self.assertTrue(func.solution("ahffaksfajeeubsne", "jefaa") == "aksfaje")
