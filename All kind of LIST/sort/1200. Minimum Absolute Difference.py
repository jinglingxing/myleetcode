"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr


Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # [4,2,1,3] -> [1,2,3,4]
        arr.sort()
        n = len(arr)
        # diff = [1,1,1]
        diff = [arr[i] - arr[i - 1] for i in range(1, n)]
        min_diff = min(diff)

        res = []
        for i, d in enumerate(diff):
            if d == min_diff:
                res.append([arr[i], arr[i + 1]])
        return res

#         Time Limit Exceeded
#         arr.sort()
#         n = len(arr)
#         min_abs_diff = float('inf')

#         for i in range(1, n):
#             abs_diff = abs(arr[i] - arr[i-1])
#             if abs_diff < min_abs_diff:
#                 min_abs_diff = abs_diff

#         res = []
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if arr[j]-arr[i] == min_abs_diff:
#                     if arr[i] < arr[j]:
#                         pair = [arr[i], arr[j]]
#                     else:
#                         pair = [arr[j], arr[i]]
#                     res.append(pair)

#         return res