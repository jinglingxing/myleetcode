"""
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5,
 the linked list should become 4 -> 1 -> 9 after calling your function.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # next_node: 1
        next_node = node.next

        # update the deleted node to the next node(1)'s value
        node.val = node.next.val

        # node(5).next -> node(9)
        node.next = next_node.next



