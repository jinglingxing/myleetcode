#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:06:36 2020

@author: jinlingxing
"""
'''
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0
 

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.

'''

from fractions import Fraction
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_pos = hour + Fraction(minutes, 60)
        if hour_pos >= 12:
            hour_pos-=12
        mins_pos = Fraction(minutes, 5)
        if abs(hour_pos - mins_pos)*30 >=180:
            diff = 360 - abs(hour_pos - mins_pos)*30 
        else:
            diff = abs(hour_pos - mins_pos)*30
        return diff
        