# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode], low: int, high: int) -> bool:
            if not root:
                return True

            if not low < root.val < high:
                return False

            left = dfs(root.left, low, root.val)
            right = dfs(root.right, root.val, high)

            return left and right

        return dfs(root, float('-inf'), float('inf'))



if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    sol.isValidBST(root)