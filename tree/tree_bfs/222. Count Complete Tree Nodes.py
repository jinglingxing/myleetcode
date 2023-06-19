# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0
        q = [root]
        count = 1
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
                count += 1
            if node.right:
                q.append(node.right)
                count += 1
        return count

        # DFS
        # if not root:
        #     return 0
        # left = self.countNodes(root.left)
        # right = self.countNodes(root.right)
        # return left + right + 1
