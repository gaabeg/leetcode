#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        par = [None]*(n+1)
        par[1] = {"()"}
        for i in range(2, n+1):
            par[i] = set()
            for j in range(1, i):
                if j == i-1:
                    par[i].update(["(" + prev + ")" for prev in par[j]])
                par[i].update([p1 + p2 for p1 in par[j] for p2 in par[i-j]])
        return list(par[n])
# @lc code=end

