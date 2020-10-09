class Stack:

    def __init__(self) -> None:
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def size(self):
        return len(self.elements)

    def pop(self):
        result = self.elements[self.size()-1]
        self.elements = self.elements[:self.size()-1]
        return result

    def peek(self):
        result = self.elements[self.size()-1]
        return result