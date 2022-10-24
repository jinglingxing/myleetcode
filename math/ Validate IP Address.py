#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:21:32 2020

@author: jinlingxing
"""

'''
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

 

Example 1:

Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
 

Constraints:

IP consists only of English letters, digits and the characters "." and ":".
'''


# class Solution:
#     def validIPAddress(self, IP: str) -> str:
#         if '.' in IP:
#             IP_split = IP.split('.')
#             # to avoid cases like : "1.1.1.1."
#             if len(IP_split) > 4 or len(IP_split) < 4:
#                 return 'Neither'
            
    
#             for i in IP_split:
#                 # if there are letters in string
#                 for j in i :
#                     if not j.isdigit():
#                         return 'Neither'
                    
#                 # when no letters in string, check if the ip is correct
#                 if  0 <= int(i) <= 255:
#                     if len(i) > 1 and i[0] == '0':
#                         return 'Neither'
#                 else:
#                     return 'Neither'
#             return 'IPv4'
        
#         if ':' in IP:
#             IP_split = IP.split(':')
#             if len(IP_split) == 8:
#                 for i in IP_split:
#                     if  0 < len(i) < 4 and i[0] != 0:
#                         continue
#                     if len(i) == 4 and i[0] == 0:
#                         continue
#                     if len(i) > 4:
#                         return 'Neither' 
#                 return 'IPv6'
#             else:
#                 return 'Neither'


class Solution:
    def validate_IPv4(self, IP: str) -> str:
        nums = IP.split('.')
        for x in nums:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            # 3. only digits are allowed
            # 4. less than 255
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"
    
    def validate_IPv6(self, IP: str) -> str:
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"
        
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validate_IPv4(IP)
        elif IP.count(':') == 7:
            return self.validate_IPv6(IP)
        else:
            return "Neither"
        
sol = Solution()
IP = '1.1.1.'
sol.validIPAddress(IP)






