"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            neg = True
        if dividend < 0 and divisor < 0:
            neg = False
    
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
        
        # dividend=1 !> 3, break
        while dividend >= divisor:
            # x=3, y=1
            x = divisor
            y = 1
   
            while dividend >= x + x:
                # x=6, y=2
                x += x
                y += y
                print('ss', x, y)

            # dividend=4, res=2
            # dividend=1, res=3
            dividend -= x
            res += y
            print('dividend', dividend, 'res', res)
            
        if neg:
            res = -res
            
        return min(max(-2147483648, res), 2147483647)


"""
Time Limit Exceeded
-2147483648
-1
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        count = 0
        neg = False
        if dividend < 0 and divisor > 0: 
            dividend = -dividend
            neg = True
            
        if dividend > 0 and divisor < 0: 
            divisor = -divisor
            neg = True
            
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
            neg = False
        
        while dividend >= divisor:
            dividend = dividend-divisor
            count += 1
            
        return -count if neg else count
"""

        