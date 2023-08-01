"""
You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].



Example 1:

Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation:
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
"""


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # nums = [5,4,0,3,1,6,2]
        visited = [False] * len(nums)
        res = 1

        def dfs(num, depth):
            # num=5, depth=1, res=1
            # num=6, depth=2, res=2
            # num=2, depth=3, res=3
            # num=0, depth=4, res=4
            # [True, False, True, False, False, True, True]
            nonlocal res
            if visited[num]:
                return
            visited[num] = True
            res = max(res, depth)
            dfs(nums[num], depth + 1)

        for num in nums:
            if not visited[num]:
                dfs(num, 1)

        print(visited)
        return res