# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:20:29 2016

@author: adamjaku
"""
class Node:
 
    def __init__(self, data):
        self.data = data#nalezy dodac potemdodatkowe pole
        self.next = None
        self.prev = None
 
    def __str__(self):
        return str(self.data)
 
class TwoWayList:
 
    def __init__(self):
        self.head = None
        self.size = 0
 
    def addLast(self, data):    #dodaje element na koncu listy
        if not self.head:
            n = Node(data)
            self.head = n
        else:
            n = self.head
            while n.next != None:
                n = n.next
            new_node = Node(data)
            n.next = new_node;
            
    def addFirst(self, data):
        
    def addMiddle(self, data):
        
    def removelast(self):
        
    def removeFirst(self):
        
    def removeMiddle(self):
        
 
    def printList(self):
        n = self.head
        while n:
            print (n)
            n = n.next
 
ll = TwoWayList()
ll.addLast(14)
ll.addLast("test")
ll.addLast(2.34)
ll.addLast(True)
 
ll.printList()