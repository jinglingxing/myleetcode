"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node: Optional[TreeNode], reminder: int):
            if not node:
                return False

            if not node.left and not node.right and node.val == reminder:
                val = node.val
                return True

            return dfs(node.left, reminder - node.val) or dfs(node.right, reminder - node.val)

        return dfs(root, targetSum)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.right = TreeNode(2)
    sol.hasPathSum(root, 15)