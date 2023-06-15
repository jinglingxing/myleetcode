# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root]
        res = []
        if not root:
            return []

        while q:
            level = len(q)
            level_list = []
            while level:
                node = q.pop(0)
                level -= 1
                level_list.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_list)
        return res[::-1]