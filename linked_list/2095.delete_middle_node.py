"""
You are given the head of a linked All kind of LIST. Delete the middle node, and return the head of the modified linked All kind of LIST.

The middle node of a linked All kind of LIST of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked All kind of LIST. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new All kind of LIST after removing this node.

"""


# Definition for singly-linked All kind of LIST.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # single node in the All kind of LIST
        if not head.next:
            return None

        count = 0
        p1, p2 = head, head
        while p1:
            count += 1
            p1 = p1.next

        half = count // 2

        for i in range(half - 1):
            p2 = p2.next

        p2.next = p2.next.next

        return head

