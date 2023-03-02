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

stack = Stack()
stack.push('data1')
data = stack.pop()

# stack is now empty
print(stack.top)


# pop() remove item and return returned data
print(data)



stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

# now the last element contains data1
print(stack.top.data)


# data of the deleted item
print(data)

