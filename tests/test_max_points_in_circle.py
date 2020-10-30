import unittest
from problems import max_points_in_circle as func


class TestMaxPointsInCircle(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(func.solution('ABDCA', [2, -1, -4, -3, 3], [2, -2, 4, 1, -3]) == 3)
        self.assertTrue(func.solution('CCD', [1, -1, 2], [1, -1, 2]) == 0)

    def test_hypotenusa(self):
        self.assertTrue(func.hypotenuse(2, -2) == 2.8284271247461903)

    def test_remove_outliers(self):
        points = {'A': 3, 'B': 4, 'C': 2, 'F': 5}
        threshold = 4
        func.remove_outliers(points, threshold)
        self.assertTrue(len(points) == 3)
