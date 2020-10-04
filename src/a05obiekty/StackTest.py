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


if __name__ == '__main__':
    unittest.main()
