#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_vol = (j-i)*min(height[i],height[j])
        max_l = height[i]
        max_r = height[j]
        stable = False
        while (not stable):
            if i==j:
                stable = True
                break
            if height[i]<height[j]:
                i=i+1
                if height[i]>max_l:
                    max_vol = max(max_vol, (j-i)*min(height[i],height[j]))
                    max_l = height[i]
            else:
                j=j-1
                if height[j]>max_r:
                    max_vol = max(max_vol, (j-i)*min(height[i],height[j]))
                    max_r = height[j]
        return max_vol




# @lc code=end

