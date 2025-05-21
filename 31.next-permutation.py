#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start

from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums)
        l = r-2
        while l>=0 and nums[l]>= nums[l+1]:
            l-=1
        
        if l == -1:
            nums.reverse()
            return
        piv = nums[l]
        min_ind = l+1
        for i in range(r-1, l+1, -1):
            if (nums[i]>piv):
                min_ind = i
                break
        
        nums[l] = nums[min_ind]
        nums[min_ind] = piv

        nums[l+1:] = reversed(nums[l+1:])


        
# @lc code=end
