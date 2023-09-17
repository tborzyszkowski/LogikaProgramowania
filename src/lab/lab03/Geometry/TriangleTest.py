import unittest
from Triangle import Triangle
from Point import Point


class TriangleTest(unittest.TestCase):
    def test_proper_triangle_points(self):
        point_1 = Point(1, 1)
        point_2 = Point(1, 2)
        point_3 = Point(2, 1)
        triangle = Triangle(point_1, point_2, point_3)
        self.assertIsNotNone(triangle, "Points are OK")

    def test_wrong_triangle_points(self):
        point_1 = Point(1, 1)
        point_2 = Point(2, 2)
        point_3 = Point(3, 3)

        with self.assertRaises(AttributeError):
            triangle = Triangle(point_1, point_2, point_3)


if __name__ == '__main__':
    unittest.main()
