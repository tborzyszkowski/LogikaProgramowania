class Tool:
    def __init__(self) -> None:
        super().__init__()

    def can_drill(self):
        return False

    def can_cut(self):
        return False

    def can_sweep(self):
        return False

    def can_fly(self):
        return False

    def capability(self):
        result = {
            "drill": self.can_drill(),
            "cut": self.can_cut(),
            "sweep": self.can_sweep(),
            "fly": self.can_fly()
        }
        return result