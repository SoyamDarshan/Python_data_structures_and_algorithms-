# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:16:09 2019

@author: ThinkPad
"""


class BinarySearchTree:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def is_root_empty(self):
        return self.root is None

    def find_position(self, data, pos):
        curr = pos
        prev = curr
        while curr is not None:
            print(curr.data, data)
            print(curr.left)
            print(curr.right)
            if data <= curr.data:
                if curr.left is None:
                    return curr.left, prev
                curr = curr.left
            elif data > curr.data:
                if curr.right is None:
                    return curr.right, prev
                curr = curr.right
        return curr

    def add_node(self, data):
        new_node = self.Node(data)
        curr = self.root
        if self.is_root_empty():
            self.root = new_node
        else:
            curr, prev = self.find_position(data, self.root)
            curr = new_node
            print(prev.data, curr.data)

    def preorder_traversal(self, root):
        if root is not None:
            curr = root
            print(curr.data)
            self.preorder_traversal(curr.left)
            self.preorder_traversal(curr.right)

    def preorder(self):
        self.preorder_traversal(self.root)


if __name__ == '__main__':

    name = BinarySearchTree()
    print(name.add_node(15))
    print(name.add_node(9))
    print(name.add_node(10))
#    print(name.add_node(50))
#    print(name.add_node(30))
#    print(name.preorder())
