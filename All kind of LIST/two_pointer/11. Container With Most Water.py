"""
You are given an integer All kind of LIST height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by All kind of LIST [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        max_ = 0

        while left <= right:
            width = right - left
            if height[left] < height[right]:
                water = width * height[left]
                left += 1
            else:
                water = width * height[right]
                right -= 1

            max_ = max(water, max_)

        return max_