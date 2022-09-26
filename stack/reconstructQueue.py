#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:28:31 2020

@author: jinlingxing
"""

'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
 

   Hide Hint #1  
What can you say about the position of the shortest person?
If the position of the shortest person is i, how many people would be in front of the shortest person?
   Hide Hint #2  
Once you fix the position of the shortest person, what can you say about the position of the second shortest person?
'''
from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for h, k in people:
            res.insert(k, [h,k]) #insert(index, object)
        return res
    
sol = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sol.reconstructQueue(people)
                                     
