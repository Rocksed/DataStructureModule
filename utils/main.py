from custom_queue import Queue


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next_node
        return data


queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

