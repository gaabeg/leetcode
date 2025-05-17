#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = sum(nums[:3])

        if len(nums) == 3:
            return ret
        
        if ret >= target:
            return ret
        
        if sum(nums[-3:]) <= target:
            return sum(nums[-3:])
        

        i = 0
        while i<len(nums)-2:
            if i>0 and nums[i]==nums[i-1]:
                i += 1
                continue
            j,k = i+1, len(nums)-1
            while j<k:
                val = nums[i]+nums[j]+nums[k]

                if val == target:
                    return val
                elif val > target:
                    k -= 1
                else:
                    j += 1
                
                if abs(ret-target)>abs(val-target):
                    ret = val
            i+=1
        return ret
                




# @lc code=end

