#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:19:36 2020

@author: jinlingxing
"""
'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pt_a = dummyoddhead = ListNode(-1)
        pt_b = dummyevenhead = ListNode(-1)  
        
        while head and head.next :
            pt_a.next = head
            pt_b.next = head.next
            pt_a = pt_a.next
            pt_b = pt_b.next
            head = head.next.next
        
        pt_b.next = None
        
        if head:
            pt_a.next = head 
            pt_a = pt_a.next
                
        pt_a.next = dummyevenhead.next
            
        return dummyoddhead.next