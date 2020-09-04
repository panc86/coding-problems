import unittest
from problems import min_window_substring


class TestStringMethods(unittest.TestCase):

    def test_result1(self):
        res = min_window_substring.solution("aaffhkksemckelloe", "fhea")
        self.assertTrue(res == "affhkkse")

    def test_result2(self):
        res = min_window_substring.solution("ahffaksfajeeubsne", "jefaa")
        self.assertTrue(res == "aksfaje")
