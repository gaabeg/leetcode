#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        outs = []
        nums.sort()
        print(nums)
        i = 0
        while i<len(nums)-3:
            if i>0 and nums[i]==nums[i-1]:
                i += 1
                continue
            j = i+1
            while j<len(nums)-2:
                if j > i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                k,l = j+1, len(nums)-1
                while k<l:
                    val = nums[i]+nums[j]+nums[k]+nums[l]
                    if val == target:
                        outs.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=nums[j+1:].count(nums[k])
                        l-= nums[j+1:].count(nums[l])
                    elif val > target:
                        l-=1
                    else:
                        k+=1
                j+=1
            i+=1
        return outs

# @lc code=end

