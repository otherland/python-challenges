class Node:
    def __init__(self, data: int, *args, **kwargs):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, value: int) -> None:
        if value <= self.data:
            if self.left == None:
                self.left = Node(data=value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(data=value)
            else:
                self.right.insert(value)

    def contains(self, value: int) -> bool:
        if value == self.data:
            return True
        elif value < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)

        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)

    def print_in_order(self) -> None:
        """
        In order traversal, smallest to largest.
        """
        if self.left != None:
            self.left.print_in_order()
        print(self.data)
        if self.right != None:
            self.right.print_in_order()


Node()