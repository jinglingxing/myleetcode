"""
Given two integer arrays preorder and inorder
where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if not preorder:
                return
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = dfs(preorder[1:mid+1], inorder[:mid])
            root.right = dfs(preorder[mid+1:], inorder[mid+1:])
            return root

        return dfs(preorder, inorder)