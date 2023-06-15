"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        q = [root]
        res = []
        while q:
            level = len(q)
            level_list = []
            while level:
                node = q.pop(0)

                level -= 1
                level_list.append(node.val)
                for child in node.children:
                    q.append(child)

            res.append(level_list)
        return res
