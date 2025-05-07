#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math

        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))
# @lc code=end

