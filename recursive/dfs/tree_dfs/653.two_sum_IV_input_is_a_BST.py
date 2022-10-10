# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []
        def dfs(node):
            if node:
                l.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)

        return any(k-num in l for num in l if num != k-num)

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = self.searchAllNode(root)

        for i in range(0, len(res)):
            for j in range(0, len(res)):
                if i != j and res[i] + res[j] == k:
                    return True
        return False

    def searchAllNode(self, root, res=None):
        if res is None:
            res = []
        if root:
            res.append(root.val)
            self.searchAllNode(root.left, res)
            self.searchAllNode(root.right, res)
            return res
        else:
            return res




