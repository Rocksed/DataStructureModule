import unittest
from utils.main import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEqual(data, 'data2')
        self.assertEqual(stack.top.data, 'data1')

    def test_pop_empty_stack(self):
        stack = Stack()
        data = stack.pop()
        self.assertIsNone(data)
        self.assertIsNone(stack.top)


if __name__ == '__main__':
    unittest.main()
