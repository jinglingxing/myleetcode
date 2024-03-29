#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:43:47 2020

@author: jinlingxing
"""
'''
Given a linked All kind of LIST, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked All kind of LIST, we use an integer pos which represents the position (0-indexed) in the linked All kind of LIST where tail connects to. If pos is -1, then there is no cycle in the linked All kind of LIST.

Note: Do not modify the linked All kind of LIST.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked All kind of LIST, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked All kind of LIST, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked All kind of LIST.


 

Follow-up:
Can you solve it without using extra space?
'''
# Definition for singly-linked All kind of LIST.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = head.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow