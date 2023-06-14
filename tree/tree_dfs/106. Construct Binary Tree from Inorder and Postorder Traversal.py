# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(inorder, postorder):
            if not inorder:
                return

            root_val = postorder.pop()
            root = TreeNode(root_val)

            mid = inorder.index(root_val)

            root.left = dfs(inorder[:mid], postorder[:mid])
            root.right = dfs(inorder[mid + 1:], postorder[mid:])
            return root

        return dfs(inorder, postorder)