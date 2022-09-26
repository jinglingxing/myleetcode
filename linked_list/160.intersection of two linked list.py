#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:28:40 2020

@author: jinlingxing
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dicA = {}  
        #The linked lists must retain their original structure after the function returns
        A = headA 
        while A:
            dicA[A] = A.val
            A = A.next
          
        B = headB
        while B:
            if B in dicA:
                return B
            B = B.next
        return None

