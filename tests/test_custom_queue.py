import unittest
from utils.custom_queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertIsNone(queue.tail.next_node)

    def test_enqueue_empty_queue(self):
        queue = Queue()
        queue.enqueue('data')

        self.assertEqual(queue.head.data, 'data')
        self.assertEqual(queue.tail.data, 'data')

    def test_enqueue_one_element_queue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')

        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data2')
        self.assertIsNone(queue.tail.next_node)


if __name__ == '__main__':
    unittest.main()
