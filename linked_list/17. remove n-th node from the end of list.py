#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:52:47 2020

@author: jinlingxing
"""
'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        del l[-n]
        if len(l)>0:
            head = ListNode(l[0])
            tail = head
            e=0
            while e < len(l):      
                tail.next = ListNode(l[e])
                tail = tail.next
                e+=1

            return head.next
        else:
            return None