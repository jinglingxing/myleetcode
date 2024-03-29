#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:00:39 2020

@author: jinlingxing
"""
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked All kind of LIST.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
            
'''
# Definition for singly-linked All kind of LIST.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []

        while l1:
            l1_list.append(str(l1.val))
            l1 = l1.next

        while l2:
            l2_list.append(str(l2.val))
            l2 = l2.next

        sum_ = int("".join(l1_list[::-1])) + int("".join(l2_list[::-1]))

        str_sum = list(str(sum_))[::-1]
        head = ListNode(str_sum[0])
        node = head
        i = 1
        while i < len(str_sum):
            node.next = ListNode(str_sum[i])
            node = node.next
            i += 1

        return head


sol = Solution()
#(2 -> 4 -> 3) + (5 -> 6 -> 4)
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l2 = ListNode(5)
# l2.next = ListNode(5)
# l2.next.next = ListNode(4)
l1 = ListNode(5)
l2 = ListNode(5)
sol.addTwoNumbers(l1, l2)