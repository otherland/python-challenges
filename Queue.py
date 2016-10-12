"""
Implement a Queue data structure
"""

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def peek(self):
        return getattr(self.head, 'data', None)

    def add(self, data):
        node = Node(data)
        if self.tail != None:
            self.tail.next = node
        self.tail = node

        if self.head == None:
            self.head = node

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return data

Q = Queue()
assert Q.is_empty() == True
assert Q.peek() == None

Q.add(23)
assert Q.peek() == 23

Q.add(99)
assert Q.peek() == 23
assert Q.head != Q.head.next

Q.remove()
assert Q.peek() == 99

