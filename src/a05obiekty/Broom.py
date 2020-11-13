from .Tool import *


class Broom(Tool):
    def __init__(self) -> None:
        super().__init__()

    def can_sweep(self):
        return True

    def can_fly(self):
        return True
