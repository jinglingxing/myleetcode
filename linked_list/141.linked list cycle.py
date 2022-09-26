#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:58:23 2020

@author: jinlingxing
"""



#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        if not head: #head -> []
            return False
        
        while True: #always true 
            if not head.next: #no cycle at the end
                return False
            if head in dic: 
                return True
            else:
                dic[head] = head.val #kye: listnode, value: head.val
            head = head.next

sol = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
sol.hasCycle(head)