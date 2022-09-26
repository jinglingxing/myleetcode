#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:31:38 2020

@author: jinlingxing
"""

'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
'''


from typing import List
import heapq
# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         dic = {}
#         for i in range(0,len(points)):
#             key = points[i][0]*points[i][0] + points[i][1]*points[i][1]
#             if key not in dic:
#                 dic[key] = [points[i][0],points[i][1]]
#             else:
#                 dic[key] += [points[i][0],points[i][1]]
#         print("dic: " + str(dic))
#         return [[0,0]]
#         dic_items = dic.items()
#         sorted_items = sorted(dic_items)
#         nearest_points = sorted_items[0:K]
#         res = [row[1] for row in nearest_points]
# #        print("dic values limited by k is: " + str(res))
  
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points)<K:
            return points
        heap = []
        for x,y in points:
            heapq.heappush(heap, [-(y**2 + x**2), [x,y]])
            if len(heap)>K:
                heapq.heappop(heap)
        return [x[1] for x in heap]
              
sol = Solution()        
points = [[3,3],[5,-1],[-2,4],[-3,-3]]
K=2
sol.kClosest(points, K)