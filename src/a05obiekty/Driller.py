from .Tool import *


class Driller(Tool):
    def __init__(self) -> None:
        super().__init__()

    def can_drill(self):
        return True
