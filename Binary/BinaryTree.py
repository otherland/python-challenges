"""
Implement a binary tree

"""

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


"""
Check if the binary search tree is valid

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/forum


Method

Does the tree meet the requirements of a binary search tree?

Left < Parent < Root
Right > Parent > Root

"""

def checkBST(root, xmin, xmax):
    # Recursion base cases
    if root is None:
        print('Root is none', root)
        return True
    if root.data < xmin or root.data > xmax:
        print('{} < {} or > {}'.format(root.data, xmin, xmax))
        return False
    left = checkBST(root.left, xmin, root.data - 1)
    right = checkBST(root.right, root.data + 1, xmax)
    print(left, right)
    return left and right

root = Node(4)
root.insert(2)
root.insert(1)
root.insert(7)
root.insert(6)
root.insert(3)
root.insert(5)
# root.print_in_order()

checkBST(root, -99999, 99999)

