import unittest

from utils.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 1})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.head.next_node.data, {'id': 1})

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 1})
        ll.insert_at_end({'id': 2})
        self.assertEqual(ll.tail.data, {'id': 2})
        self.assertEqual(ll.head.next_node.data, {'id': 2})

    def test_print_ll(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})


if __name__ == '__main__':
    unittest.main()
