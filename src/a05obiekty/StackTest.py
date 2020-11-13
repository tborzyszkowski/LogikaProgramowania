import unittest

from .Stack import Stack


class StackTestCase(unittest.TestCase):
    def test_push_pop_the_same(self):
        stack = Stack()
        stack.push(10)
        result = stack.pop()
        self.assertEqual(10, result)

    def test_push2_pop_the_same(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        result = stack.pop()
        self.assertEqual(20, result)

    def test_push2_pop2_the_same(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.pop()
        result = stack.pop()
        self.assertEqual(10, result)

    def test_push_pop_size(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        size_after_push = stack.size()
        stack.pop()
        self.assertEqual(size_after_push - 1, stack.size())

    def test_push_peek_element(self):
        stack = Stack()
        stack.push(10)
        result = stack.peek()
        self.assertEqual(10, result)

    def test_push_peek_size(self):
        stack = Stack()
        stack.push(10)
        stack.peek()
        self.assertEqual(1, stack.size())


if __name__ == '__main__':
    unittest.main()
