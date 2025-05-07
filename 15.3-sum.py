#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[tuple[int]]:
        triplets = set()
        negs = []
        zeros = []
        pos = []
        for x in nums:
            if x>0: pos.append(x)
            elif x<0: negs.append(x)
            else: zeros.append(x)
        p_set = set(pos)
        n_set = set(negs)

        if len(zeros)>= 3:
            triplets.add((0,0,0))
        if len(zeros)>0:
            for i in n_set:
                if (-1*i) in p_set:
                    triplets.add((0, i, -1*i))
        for i in range(len(negs)):
            for j in range(i+1, len(negs)):
                check = -(negs[i]+negs[j])
                if check in p_set:
                    triplets.add(tuple(sorted([negs[i],negs[j],check])))
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                check = -(pos[i]+pos[j])
                if check in n_set:
                    triplets.add(tuple(sorted([pos[i],pos[j],check])))
        return list(triplets)
# @lc code=end

