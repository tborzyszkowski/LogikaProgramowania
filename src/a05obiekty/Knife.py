from .Tool import *


class Knife(Tool):
    def __init__(self) -> None:
        super().__init__()

    def can_cut(self):
        return True
