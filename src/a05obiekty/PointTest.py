import unittest

from .Point import *
from math import sqrt

class PointTestCase(unittest.TestCase):

    def test_set_x_positive(self):
        point = Point()
        point.x = 10
        self.assertEqual(10, point.x)

    def test_set_x_negative(self):
        point = Point()
        point.x = -10
        self.assertEqual(10, point.x)

    def test_distance_to_self(self):
        point = Point(10, 10, 10)
        distance = point.distance(point)
        self.assertEqual(0, distance)

    def test_distance_to_other(self):
        point1 = Point(1, 1, 0)
        point2 = Point(2, 2, 0)
        distance = point1.distance(point2)
        self.assertEqual(sqrt(2), distance)

    def test_distance_to_other_in_3d(self):
        point1 = Point(1, 1, 1)
        point2 = Point(2, 2, 2)
        distance = point1.distance(point2)
        self.assertEqual(sqrt(3), distance)


if __name__ == '__main__':
    unittest.main()
