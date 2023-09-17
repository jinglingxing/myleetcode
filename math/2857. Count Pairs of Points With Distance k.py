"""
You are given a 2D integer array coordinates and an integer k, where coordinates[i] = [xi, yi] are the coordinates of the ith point in a 2D plane.

We define the distance between two points (x1, y1) and (x2, y2) as (x1 XOR x2) + (y1 XOR y2) where XOR is the bitwise XOR operation.

Return the number of pairs (i, j) such that i < j and the distance between points i and j is equal to k.



Example 1:

Input: coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5
Output: 2
Explanation: We can choose the following pairs:
- (0,1): Because we have (1 XOR 4) + (2 XOR 2) = 5.
- (2,3): Because we have (1 XOR 5) + (3 XOR 2) = 5.

"""


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        # math
        # x1^x2 = xDistance
        # x1^x2+y1^y2=k; y1^y2 = k-x1^x2; y1^y2 = k-xDistance; y2 = (k-xDistance)^y1
        # k distance from (x1, y1) is the count of points (x1^xDistance, (k-xDistance)^y1)
        # [[1,3],[1,3],[1,3],[1,3],[1,3]], k=5
        counter = Counter()
        res = 0

        for x, y in coordinates:
            for xDistance in range(k + 1):
                d_x = x ^ xDistance
                d_y = (k - xDistance) ^ y
                res += counter[(d_x, d_y)]
            counter[(x, y)] += 1
        return res


