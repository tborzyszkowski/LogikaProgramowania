import unittest

from .Point import *

class PointTestCase(unittest.TestCase):

    def test_set_x_positive(self):
        point = Point()
        point.x = 10
        self.assertEqual(10, point.x)

    def test_set_x_negative(self):
        point = Point()
        point.x = -10
        self.assertEqual(10, point.x)



if __name__ == '__main__':
    unittest.main()
