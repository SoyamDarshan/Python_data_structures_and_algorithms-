# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:33:20 2019

@author: ThinkPad
"""


class Node:

        def __init__(self, element, next=None):
            self.element = element
            self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.pos = None

    def addNode(self, e):
        new_node = Node(e)
        if self.head is None:
            self.head = new_node
            self.pos = self.head
        else:
            self.pos.next = new_node
            self.pos = new_node
        

    def printNode(self):
        curr = self.head
        while curr:
            print (curr.element)
            curr = curr.next

if __name__ == '__main__':
    myList = LinkedList()
    print("Inserting")
    print(myList.addNode(5))
    print(myList.addNode(15))
    print(myList.addNode(25))
    print("Printing")
    myList.printNode()
