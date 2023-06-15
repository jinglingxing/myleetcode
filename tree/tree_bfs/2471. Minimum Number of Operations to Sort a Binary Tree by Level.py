"""
You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.

 Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def leastOperation(nums: List) -> list:
            temp = sorted(nums)
            h = {}
            for i in range(len(nums)):
                h[nums[i]] = i

            count = 0
            for i in range(len(nums)):
                if nums[i] != temp[i]:
                    count += 1
                    # swap
                    j = h[temp[i]]
                    h[nums[i]], h[nums[j]] = j, i
                    nums[j], nums[i] = nums[i], nums[j]
            return count

        def levelOrder(root: Optional[TreeNode]) -> list:
            if not root:
                return []
            q = [root]
            res = 0

            while q:
                level = len(q)
                level_list = []
                while level:

                    node = q.pop(0)
                    level_list.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level -= 1

                res += leastOperation(level_list)
            return res

        return levelOrder(root)
