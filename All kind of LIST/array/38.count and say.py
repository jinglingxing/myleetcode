#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:22:58 2020

@author: jinlingxing
"""


'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".

'''

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1' #initialize first term '1'
        n-=1 ##we iterate it n-1 times
        while 1<=n<=30:
            #we want to build the new string
            ns = str()
            i = 0
            #go through the previous term(s) and count how many times each element appears
            while i< len(s):
                count = 1 #why it's 1 not 0? because the first item
                #the while loop will terminate when the element we are counted for is not consecutive
                while (i+1 < len(s) and s[i] == s[i+1]):
                    count+=1 #we count how many times the item at position i appears
                    i+=1
                #build the new string
                ns += str(count) + s[i] ##for example: 11 changed to 21; 11 appears twice and append '1' in the current item
                i+=1
            s=ns #update my result
            n-=1
        return s ##the result we need to build
    
sol=Solution()
n=5
sol.countAndSay(n)  
    
    
    
    
    
    
    
    