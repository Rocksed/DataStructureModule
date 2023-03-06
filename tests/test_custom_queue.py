import unittest
from utils.custom_queue import Queue


class TestQueue(unittest.TestCase):

    def test_dequeue_empty_queue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())

    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertIsNone(queue.dequeue())

    def test_enqueue_dequeue_single_element(self):
        queue = Queue()
        queue.enqueue('data1')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertIsNone(queue.dequeue())


if __name__ == '__main__':
    unittest.main()
