#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = n < 0
        n = abs(n)
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        conq = self.myPow(x, n//2)
        res = conq*conq
        if n % 2 == 1:
            res = res*x
        
        return (1/res if neg else res)
        
# @lc code=end

