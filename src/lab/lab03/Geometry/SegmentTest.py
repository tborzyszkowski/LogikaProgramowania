import math
import unittest
from Segment import Segment
from Point import Point

class SegmentTest(unittest.TestCase):
    def test_lenght_0(self):
        segment = Segment(
            Point(1, 1),
            Point(1, 1)
        )
        len = segment.lenght()
        self.assertEqual(0, len)

    def test_lenght_1(self):
        segment = Segment(
            Point(1, 1),
            Point(1, 2)
        )
        len = segment.lenght()
        self.assertEqual(1, len)

    def test_lenght_sqrt2(self):
        segment = Segment(
            Point(1, 1),
            Point(2, 2)
        )
        len = segment.lenght()
        self.assertAlmostEqual(1.41421, len, 4)

if __name__ == '__main__':
    unittest.main()
