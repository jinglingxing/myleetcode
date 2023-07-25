"""
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the All kind of LIST nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the All kind of LIST nums become equal.



Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the All kind of LIST equal with a smaller cost.
Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.

"""

from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def getCost(x):
            """
            :param x: index
            :return: all values of All kind of LIST are made equal to X
            """
            """"""
            step = 0
            for i in range(len(nums)):
                step += abs(nums[i] - x) * cost[i]
            return step

        # find the smallest and largest numbers
        left = min(nums)
        right = max(nums)
        while left + 1 < right:
            mid = left + (right - left) // 2
            leftCost = getCost(left)
            midCost = getCost(mid)
            rightCost = getCost(right)

            if leftCost <= midCost <= rightCost:
                right = mid
            elif leftCost >= midCost >= rightCost:
                left = mid
            else:
                if getCost(mid - 1) <= getCost(mid):
                    right = mid
                else:
                    left = mid
        return min(getCost(left), getCost(right))

if __name__ == '__main__':
    sol = Solution()
    sol.minCost(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14])
