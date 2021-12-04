import unittest

from .Knife import *
from .Broom import *
from .Driller import *


class ToolTestCase(unittest.TestCase):
    def test_knife_can_cut(self):
        knife = Knife()
        can_cut = knife.capability()["cut"]
        self.assertTrue(can_cut)

    def test_knife_cannot_sweep(self):
        knife = Knife()
        can_sweep = knife.capability()["sweep"]
        self.assertFalse(can_sweep)

    def test_broom_can_fly(self):
        broom = Broom()
        can_fly = broom.capability()["fly"]
        self.assertTrue(can_fly)

    def test_driller_cannot_fly(self):
        driller = Driller()
        can_fly = driller.capability()["fly"]
        self.assertFalse(can_fly)


if __name__ == '__main__':
    unittest.main()
