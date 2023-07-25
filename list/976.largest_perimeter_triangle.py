"""
Given an integer list nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.



Example 1:

Input: nums = [2,1,2]
Output: 5
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)-1

        while i >= 2:
            if (nums[i] < nums[i-1]+nums[i-2]) and (nums[i]-nums[i-2] < nums[i-1]):
                return (nums[i]+nums[i-1]+nums[i-2])
            i-=1
        return 0