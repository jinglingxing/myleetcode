#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:22:13 2020

@author: jinlingxing
"""

'''
Merge two sorted linked lists and return it as a new list. The new list should be made by
 splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1
        
        if l1.val <= l2.val:
            l3 = ListNode(l1.val) #set the head of listNode l3
            l1 = l1.next #the move the head of l1
        else:
            l3 = ListNode(l2.val) #set the head of listNode l3
            l2 = l2.next #the move the head of l2
        head = l3
        
        while (l1 is not None) or (l2 is not None): #when l1 and l2 are not reached None
    
            if l1 is None:  #but if l1 reached None
                l3.next = l2.next #add the rest of l2 to l3
                break 
            if l2 is None:  #but if l2 reached None
                l3.next = l1.next  #add the rest of l1 to l3
                break
            
            if l1.val <= l2.val: 
                l3.next = ListNode(l1.val) #add listnode(l1.val) to l3.next
                l1 = l1.next #move l1
                l3 = l3.next #move l3, 
                #otherwise the listnode(l1.val) will always add at the end of the head of l3
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next
        
        return head #return the head of l3
            
                

#[1,2,4]
#[1,3,4] 
if __name__ == "__main__":
    sol = Solution()
    
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(5)
    
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    sol.mergeTwoLists(l1,l2)
    head =  sol.mergeTwoLists(l1,l2)