"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 In this case, 6 units of rain water (blue section) are being trapped.
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # i=0, j=11
        i, j = 0, len(height) - 1

        # lmax = 0, rmax = 1
        lmax = height[0]
        rmax = height[-1]
        ans = 0

        # i=0, j=11, height[0]=0, height[11]=1
        # i=1, j=11, height[1]=1, height[11]=1
        # i=2, j=11, height[2]=0, height[11]=1
        # i=3, j=11, height[3]=2, height[11]=1
        # i=3, j=10, height[3]=2, height[10]=2
        # i=4, j=10, height[4]=1, height[10]=2
        # i=5, j=10, height[5]=0, height[10]=2
        # i=6, j=10, height[6]=1, height[10]=2
        # i=7, j=10, height[7]=3, height[10]=2
        # i=7, j=9,  height[7]=3, height[9]=1
        # i=7, j=8,  height[7]=3, height[8]=2
        # i=7, j=7,  height[7]=3
        while i <= j:
            # lmax=height[1]=1
            # lmax=height[3]=2
            # lmax=height[7]=3

            if height[i] > lmax:
                lmax = height[i]

            # rmax=height[10]=2
            # height[j]=3>2, rmax=3
            if height[j] > rmax:
                rmax = height[j]

            # i=1, j=11
            # ans=1-1=0, i=2
            # ans=1-0=1, i=3
            # ans=1, i=3, j=10
            # ans=1+(2-2)=1, i=4
            # ans=1+(2-1)=2, i=5
            # ans=2+(2-0)=4, i=6
            # ans=4+(2-1)=5, i=7
            # ans=5+(2-2)=5, i=7, j=9
            # ans=5+(2-1)=6, i=7, j=8
            # ans=6+(2-2)=6, i=7, j=7
            # ans=6+(3-3)=6
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
            else:
                ans += rmax - height[j]
                j -= 1

        return ans