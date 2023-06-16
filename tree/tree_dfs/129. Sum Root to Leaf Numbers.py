# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode], path_sum: int) -> int:
            if not root:
                return 0

            path_sum = path_sum * 10 + root.val

            if not root.left and not root.right:
                return path_sum

            return dfs(root.left, path_sum) + dfs(root.right, path_sum)

        return dfs(root, 0)
