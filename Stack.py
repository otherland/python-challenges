"""
Implement a stack data structure
"""

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.top = None

    def is_empty():
        return self.top == None

    def peek():
        return getattr(self.top, 'data', None)

    def push(data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop():
        data = self.peek()
        self.top = self.top.next
        return data