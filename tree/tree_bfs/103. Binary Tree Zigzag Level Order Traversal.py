# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        res = []

        while q:
            level = len(q)
            level_list = []
            while level:
                node = q.pop(0)
                level_list.append(node.val)
                level -= 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_list)

        result = []

        for i in range(len(res)):
            if i % 2 == 0:
                result.append(res[i])
            else:
                result.append(res[i][::-1])
        return result
