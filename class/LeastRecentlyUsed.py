#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:47:34 2020

@author: jinlingxing
"""

'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictN = {}
        self.head = DLNode(None,None,None,None)
        self.tail = DLNode(self.head,None,None,None)
        self.head.nextN = self.tail
        

    def get(self, key: int) -> int:

        if key not in self.dictN:
            return -1
        else:
            Node = self.dictN[key]
            self.backtohead(Node)
            return Node.value

    def put(self, key: int, value: int) -> None:

        if key in self.dictN:
            Node = self.dictN[key]
            self.backtohead(Node)
            Node.value = value
        else:
            if(len(self.dictN)<self.capacity):
                Node = DLNode(self.head,self.head.nextN,key,value)
                # Put our node right after the head
                self.head.nextN.prevN = Node
                self.head.nextN = Node
                # Put our node in the dictionary
                self.dictN[key] = Node
            else:
                # Delete the last node
                Node_to_delete = self.tail.prevN
                self.tail.prevN = Node_to_delete.prevN
                Node_to_delete.prevN.nextN = self.tail
                del(self.dictN[Node_to_delete.key])
                # Add new node to the head
                Node = DLNode(self.head,self.head.nextN,key,value)
                # Put our node right after the head
                self.head.nextN.prevN = Node
                self.head.nextN = Node
                # Put our node in the dictionary
                self.dictN[key] = Node
                
                
    
    def backtohead(self, Node):
        # DELETE NODE OF DLL
        # link previous node to the next one and next node to the previous one
        Node.prevN.nextN = Node.nextN
        Node.nextN.prevN = Node.prevN
        # ADD NODE AFTER HEAD OF DLL
        Head = self.head
        Node.nextN = Head.nextN
        Head.nextN.prevN = Node
        Node.prevN = Head
        Head.nextN = Node

class DLNode:
    def __init__(self,prevN,nextN,key,value):
        self.prevN = prevN
        self.nextN = nextN
        self.key = key
        self.value = value
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)