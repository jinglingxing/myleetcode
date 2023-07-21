"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = None

    def dfs(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        if not node:
            return False

        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        if self.res is not None:
            return True

        if left and right:
            self.res = node
            return True

        if left or right:
            if node in [p, q]:
                self.res = node
            return True
        return node.val in [p.val, q.val]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.res


if __name__ == '__main__':
    # [3,5,1,6]
    #     3
    #    / \
    #   5   1
    #  /
    # 6
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    p = TreeNode(1)
    q = TreeNode(6)
    sol = Solution()
    res = sol.lowestCommonAncestor(root, p, q)
    print(res)

