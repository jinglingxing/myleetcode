#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 12:02:05 2020

@author: jinlingxing
"""
'''
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
 

Constraints:

2n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000

'''
from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cityA = 0
        cityB = 0
        countA = len(costs)//2
        countB = len(costs)//2
        cost_diff = []
        #calculate the cost difference between two cities
        for person_cost in costs:
            #cost_diff is a list like [index of a person's cost in cost, cost difference between two cities]
            cost_diff.append([costs.index(person_cost), abs(person_cost[0]-person_cost[1])])
        #sort the cost difference
        cost_diff.sort(key=lambda x: x[1])
        while countA!=0 or countB!=0:
            #get the max cost difference
            curr_max = cost_diff.pop(-1)
            #city a > city b
            if costs[curr_max[0]][0] >= costs[curr_max[0]][1] and countB!=0:
                #add the cost to city B, curr_max[0] is the index of the person's cost in costs
                cityB+=costs[curr_max[0]][1]
                countB-=1
            elif countA != 0:
                cityA+=costs[curr_max[0]][0]
                countA-=1
            #when one city is full, add the rest element in another city
            if countA == 0:
                for i in range(0,len(cost_diff)):
                    cityB += costs[cost_diff[i][0]][1]
                return cityA+cityB
            if countB == 0:
                for i in range(0,len(cost_diff)):
                    cityA += costs[cost_diff[i][0]][0]  
                return cityA+cityB
                
        return cityA+cityB
    
sol = Solution()
costs = [[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]
sol.twoCitySchedCost(costs)