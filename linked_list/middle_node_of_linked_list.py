#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:22:20 2020

@author: Jinling Xing & Luc Michea
"""

'''
    Given a non-empty, singly linked list with head node head, 
    return a middle node of linked list.

    If there are two middle nodes, return the second middle node.
'''

import math
from typing import List

# Definition of a linked list node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Our definition of a linked list
class LinkedList (object):
    def __init__(self, inp_l: List[int] = [], inp_h:ListNode = ListNode(None)):
        if inp_l:
            h = ListNode(inp_l[-1])
            for i in range (len(inp)-2, -1, -1):
                htemp = ListNode(inp_l[i])
                htemp.next = h
                h = htemp
            self.head = h
        if inp_h.val:
            self.head = inp_h
        

    def __str__(self) -> str:
        s = ''
        h = self.head
        while h.next :
            s += '{} -> '.format(h.val)
            h = h.next
        s += str(h.val)
        return s



class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def list_size():
            count = 0
            curr = head
            while curr:
                count += 1
                curr = curr.next
            return count
        curr = head
        mid = math.ceil(list_size()/2)
        i = 0
        while curr :
            if i == mid:
                return curr
            i+=1
            curr = curr.next

    def middleNode2(self, head: ListNode) -> ListNode:
        a_ptr = head
        b_ptr = head
        count = 0
        while a_ptr:
            count+=1
            a_ptr = a_ptr.next
            if count == 2:
                count = 0
                b_ptr = b_ptr.next
        return b_ptr
        
    

if __name__=='__main__': 
    llist = ListNode(1) 
    #construct below list 
    # 1->12->1->4->1 

    inp = [1,12,1,4,1]
    ll = LinkedList(inp_l = inp)
    sol = Solution()
    out = sol.middleNode2(ll.head)
    print("The solution to {} is : {}".format(ll, LinkedList(inp_h = out)))