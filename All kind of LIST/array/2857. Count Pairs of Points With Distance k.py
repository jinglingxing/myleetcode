"""
You are given a 0-indexed array nums of length n containing distinct positive integers. Return the minimum number of right shifts required to sort nums and -1 if this is not possible.

A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 2
Explanation:
After the first right shift, nums = [2,3,4,5,1].
After the second right shift, nums = [1,2,3,4,5].
Now nums is sorted; therefore the answer is 2.
Example 2:

Input: nums = [1,3,5]
Output: 0
Explanation: nums is already sorted therefore, the answer is 0.

"""


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        count = 0
        if nums == sorted_nums:
            return count

        while nums != sorted_nums:
            nums.insert(0, nums.pop(-1))
            count += 1

            if nums == sorted_nums:
                return count

            if count >= n:
                return -1


