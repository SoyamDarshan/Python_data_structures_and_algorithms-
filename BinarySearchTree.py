# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 21:48:58 2019

@author: soyam
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

    def find_position(self, data):
        curr = self.root
        while curr:
            prev = curr
            if data <= curr.data:
                if curr.left is None:
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    break
                curr = curr.right
        return curr, prev

    def add_node(self, data):
        new_node = self.Node(data)
        if self.is_root_empty():
            self.root = new_node
        else:
            curr, prev = self.find_position(data)
            curr = new_node
            if(data <= prev.data):
                prev.left = curr
            else:
                prev.right = curr

    def print_preorder(self, root):
        if root:
            print(root.data)
            self.print_preorder(root.left)
            self.print_preorder(root.right)

    def preorder(self):
        print("preorder")
        self.print_preorder(self.root)

    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print(root.data)
            self.print_inorder(root.right)

    def inorder(self):
        print("inorder")
        self.print_inorder(self.root)

    def print_postorder(self, root):
        if root:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            print(root.data)

    def postorder(self):
        print("postorder")
        self.print_postorder(self.root)

    def print_leaf_nodes(self, root):
        if root:
            self.print_leaf_nodes(root.left)
            self.print_leaf_nodes(root.right)
            if root.left is None and root.right is None:
                print(root.data)

    def print_leaf(self):
        print("leaf nodes")
        self.print_leaf_nodes(self.root)


if __name__ == '__main__':
    name = BinarySearchTree()
    name.add_node(16)
    name.add_node(5)
    name.add_node(11)
    name.add_node(17)
    name.add_node(19)
    name.add_node(31)
    name.add_node(12)
    name.add_node(17)
    name.add_node(21)
    name.preorder()
    name.inorder()
    name.postorder()
    name.print_leaf()
