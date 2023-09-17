import unittest
from Point import Point

class PointTest(unittest.TestCase):
    def test_set_x_positive(self):
        point = Point()
        point.x = 10
        self.assertEqual(10, point.x)

    def test_set_x_negative(self):
        point = Point()
        point.x = -10
        self.assertEqual(10, point.x)

    def test_dist_the_same(self):
        point1 = Point()
        point2 = Point()
        result = point1.distance(point2)
        self.assertEqual(0, result)

    def test_dist_result_1(self):
        point1 = Point(1, 1)
        point2 = Point(1, 2)
        result = point1.distance(point2)
        self.assertEqual(1, result)



if __name__ == '__main__':
    unittest.main()
