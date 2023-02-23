import unittest

from utils.main import Node, Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')

    def test_node(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n2.next_node, n1)


if __name__ == '__main__':
    unittest.main()
