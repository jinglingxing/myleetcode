"""
You are given an integer list nums. You are initially positioned at the list's first index, and each element in the list represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_good_position = len(nums)-1
        for i in range(last_good_position, -1, -1):
            if nums[i]+i >= last_good_position:
                last_good_position = i

        return last_good_position == 0