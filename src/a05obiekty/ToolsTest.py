import unittest

from .Knife import *

class MyTestCase(unittest.TestCase):
    def test_knife_can_cut(self):
        knife = Knife()
        can_cut = knife.capability()["cut"]
        self.assertTrue(can_cut)

    def test_knife_cannnot_sweep(self):
        knife = Knife()
        can_cut = knife.capability()["sweep"]
        self.assertFalse(can_cut)


if __name__ == '__main__':
    unittest.main()
