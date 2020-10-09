class Calculator:
    def __init__(self) -> None:
        self.state = 0
        self.error_state = 0

    def add(self, number):
        self.state += number

    def mult(self, number):
        self.state *= number

    def div(self, number):
        if number != 0:
            self.state = self.state / number
        else:
            self.state = 0
            self.error_state = 1

    def factorial(self):
        pass