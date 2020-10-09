import unittest

from .Segment import *

class SegmentTestCase(unittest.TestCase):
    def test_distance_zero_segment(self):
        segment = Segment(Point(1, 1), Point(1, 1))
        distance = segment.length()
        self.assertEqual(0, distance)

    def test_distance_one_segment(self):
        segment = Segment(Point(1, 1, 1), Point(2, 1, 1))
        distance = segment.length()
        self.assertEqual(1, distance)

    def test_distance_in_3d(self):
        segment = Segment(Point(1, 1, 1), Point(2, 2, 2))
        distance = segment.length()
        self.assertAlmostEqual(1.732, distance, places=3)


if __name__ == '__main__':
    unittest.main()
