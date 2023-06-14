"""

Given the root of a binary tree, return the postorder traversal of its nodes' values.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        res = []
        dfs(root)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    sol = Solution()
    sol.postorderTraversal(root)
