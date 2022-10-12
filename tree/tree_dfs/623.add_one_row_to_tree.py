from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], cur_depth: int):
            if node:
                if cur_depth == depth - 1:
                    # create two tree nodes
                    old_node_left = node.left
                    node.left = TreeNode(val)
                    node.left.left = old_node_left

                    old_node_right = node.right
                    node.right = TreeNode(val)
                    node.right.right = old_node_right

                dfs(node.left, cur_depth + 1)
                dfs(node.right, cur_depth + 1)

        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        dfs(root, 1)
        return root


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    sol.addOneRow(root, 1, 3)