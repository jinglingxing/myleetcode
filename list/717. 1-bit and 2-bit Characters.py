"""
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary list bits that ends with 0, return true if the last character must be a one-bit character.



Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

"""


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0

        while i < len(bits):
            if bits[i] == 0:
                i += 1
                flag = True
            else:
                i += 2
                flag = False
        return flag

