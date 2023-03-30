import unittest

from utils.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.ll.insert_beginning(1)
        self.ll.insert_beginning(2)
        self.assertEqual(self.ll.to_list(), [2, 1])

    def test_insert_at_end(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.assertEqual(self.ll.to_list(), [1, 2])

    def test_get_data_by_id(self):
        self.ll.insert_beginning({'id': 0, 'username': 'user1'})
        self.ll.insert_beginning({'id': 1, 'username': 'user2'})
        self.ll.insert_beginning({'id': 2, 'username': 'user3'})
        self.ll.insert_beginning({'id': 3, 'username': 'user4'})

        self.assertEqual(self.ll.get_data_by_id(1), {'id': 1, 'username': 'user2'})
        self.assertIsNone(self.ll.get_data_by_id(4))

    def test_get_data_by_id_with_wrong_data_format(self):
        self.ll.insert_beginning({'id': 0, 'username': 'user1'})
        self.ll.insert_beginning([1, 2, 3])
        self.ll.insert_beginning({'id': 2, 'username': 'user3'})
        self.ll.insert_beginning({'id': 3, 'username': 'user4'})


if __name__ == '__main__':
    unittest.main()
