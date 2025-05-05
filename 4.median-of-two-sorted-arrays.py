
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = (len(nums1) + len(nums2)) // 2 
        even = (len(nums1) + len(nums2)) % 2 == 0
        found = []
        i = j = tot = 0
        while (tot <= mid):
            if (j >= len(nums2) or (i < len(nums1) and nums1[i] < nums2[j])):
                found.append(nums1[i])
                i += 1
                tot += 1
            else:
                found.append(nums2[j])
                j += 1
                tot += 1
        if (even):
            return (found[tot-1] + found[tot-2]) / 2
        return found[tot-1]
        

# @lc code=end

