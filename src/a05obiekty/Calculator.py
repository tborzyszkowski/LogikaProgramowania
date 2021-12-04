class Calculator:
    def __init__(self) -> None:
        self.state = 0
        self.error_state = False

    def add(self, number):
        self.state += number

    def mult(self, number):
        self.state *= number

    def div(self, number):
        if number != 0:
            self.state = self.state / number
        else:
            self.state = 0
            self.error_state = True

    def factorial(self):
        def fact(n):
            if n < 2:
                return 1
            else:
                return fact(n-1) * n
        self.state = fact(self.state)

    def sqrt(self):
        if self.state > 0:
            result = -1
            begin = 0
            end = int(self.state)
            while begin < end and result < 0:
                pol = int((begin + end) / 2)
                if pol * pol <= int(self.state) < (pol+1)*(pol+1):
                    result = pol
                else:
                    if pol * pol < int(self.state):
                        begin = pol
                    else:
                        end = pol
            self.state = pol
        else:
            self.state = 0